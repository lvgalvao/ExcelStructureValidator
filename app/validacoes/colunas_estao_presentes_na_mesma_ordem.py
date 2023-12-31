# Arquivo colunas_estao_presentes_na_mesma_ordem.py

from typing import Tuple

from pandas import DataFrame


def validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """
    Verifica se as colunas do modelo estão na mesma ordem em relação ao arquivo recebido.
    """
    if excel_modelo.columns.equals(arquivo.columns):
        return True, 'As colunas estão na mesma ordem.'
    else:
        return False, 'As colunas não estão na mesma ordem.'
