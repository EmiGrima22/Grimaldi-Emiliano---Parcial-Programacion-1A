# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"


def ordenarCaracteres(cadena:str)->str:
    """Ordena cada caracter de una cadena en orden ascendente

    Args:
        cadena (str): La cadena a ordenar

    Returns:
        str: La cadena ordenada
    """
    
    caracteres_ordenados = sorted(cadena)
    cadena_ordenada = "".join(caracteres_ordenados)
    return cadena_ordenada



