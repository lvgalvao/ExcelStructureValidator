# Arquivo existem_colunas_a_menos.py

from typing import Tuple

from pandas import DataFrame


def validar_se_existem_colunas_a_menos(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """
    Verifica se o arquivo recebido tem colunas a menos em relação ao modelo.
    """
    colunas_a_mais = set(excel_modelo.columns) - set(arquivo.columns)
    return len(colunas_a_mais) == 0, list(colunas_a_mais)
