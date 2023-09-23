# Arquivo quantidade_de_linhas.py

from typing import Tuple

from pandas import DataFrame


def validar_quantidade_de_linhas(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """
    Verifica se o arquivo recebido tem o mesmo número de linhas em relação ao modelo.
    """
    num_linhas_df1 = len(excel_modelo)
    num_linhas_df2 = len(arquivo)
    return num_linhas_df1 == num_linhas_df2, num_linhas_df2 - num_linhas_df1
