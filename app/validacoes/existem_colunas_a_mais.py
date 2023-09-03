from typing import Tuple

from pandas import DataFrame


def validar_se_existem_colunas_a_mais(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """
    Verifica se o arquivo recebido tem colunas a mais em relação ao modelo.
    """
    colunas_a_mais = set(arquivo.columns) - set(excel_modelo.columns)
    return len(colunas_a_mais) == 0, list(colunas_a_mais)