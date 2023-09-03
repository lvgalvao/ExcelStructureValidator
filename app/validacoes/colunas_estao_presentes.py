from typing import Tuple

from pandas import DataFrame



def validar_se_todas_as_colunas_estao_presentes(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """
    Verifica se todas as colunas do modelo estão presentes no arquivo recebido."
    """
    if set(excel_modelo.columns) == set(arquivo.columns):
        return True, "Todas as colunas estão presentes."
    else:
        return False, "Algumas colunas não estão presentes."
