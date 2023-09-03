import os
import shutil
import time

from loguru import logger
import pandas as pd
from .config import INPUT_DIR, MODEL_DIR, OUTPUT_CORRETOS, OUTPUT_REVISAO
from loguru import logger
from .validacoes import (
    validar_quantidade_de_linhas, validar_se_existem_colunas_a_mais,
    validar_se_existem_colunas_a_menos,
    validar_se_todas_as_colunas_estao_presentes,
    validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem,
    validar_tipos_dados)

# Lendo o arquivo modelo
excel_modelo = pd.read_excel(f'{MODEL_DIR}')

# Lista para armazenar os nomes dos arquivos
file_names = []

# Preenche a lista com os nomes dos arquivos no diretório 'input'
for filename in os.listdir(INPUT_DIR):
    if filename.endswith('.xlsx'):
        file_names.append(filename)

# Ordena a lista de nomes de arquivos em ordem alfabética
file_names.sort()

# Lê os arquivos em ordem alfabética e armazena em uma lista
arquivos_recebidos = [
    (filename, pd.read_excel(os.path.join(INPUT_DIR, filename)))
    for filename in file_names
]

# Lista de funções de validação
validacoes = [
    validar_quantidade_de_linhas, validar_se_existem_colunas_a_mais,
    validar_se_existem_colunas_a_menos,
    validar_se_todas_as_colunas_estao_presentes,
    validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem,
    validar_tipos_dados,
]

# Execução das funções de validação
for i, (filename, arquivo) in enumerate(arquivos_recebidos, start=1):
    log_file_name = f'auditoria:{filename[:-5]}-data:{time.strftime("%Y-%m-%d")}.log'

    logger.remove()
    logger.add(
        log_file_name,
        level='INFO',
        format='{time:YYYY-MM-DDTHH} | {level} | {message}',
    )

    logger.info(f"Iniciando o processo de validação do arquivo {filename}.")

    resultados = []
    testes_falhos = []

    for idx, validacao in enumerate(validacoes, start=1):
        resultado, msg = validacao(excel_modelo, arquivo)

        if resultado:
            logger.info(f"Arquivo {filename} - Teste {idx}. {validacao.__name__}: {msg}")
        else:
            logger.error(f"Arquivo {filename} - Teste {idx}. {validacao.__name__}: {msg}")
            testes_falhos.append(idx)

        resultados.append(resultado)

    origem_excel = os.path.join(INPUT_DIR, filename)
    origem_log = log_file_name  # Assume que o log foi criado no diretório atual

    if all(resultados):
        logger.info(f"Arquivo {filename} - Testes finalizados. Todos os testes passaram. Pode subir o {filename} pro Power BI!")

        # Mover arquivos para o diretório OUTPUT_CORRETOS
        destino_excel = os.path.join(OUTPUT_CORRETOS, filename)
        destino_log = os.path.join(OUTPUT_CORRETOS, log_file_name)

        shutil.move(origem_excel, destino_excel)
        shutil.move(origem_log, destino_log)
    else:
        testes_falhos_str = ', '.join(map(str, testes_falhos))
        logger.critical(f"Arquivo {filename} - Testes {testes_falhos_str} falharam. Um ou mais testes não passaram, não subir o {filename} pro Power BI.")

        # Mover arquivos para o diretório OUTPUT_REVISAO
        destino_excel = os.path.join(OUTPUT_REVISAO, filename)
        destino_log = os.path.join(OUTPUT_REVISAO, log_file_name)

        shutil.move(origem_excel, destino_excel)
        shutil.move(origem_log, destino_log)