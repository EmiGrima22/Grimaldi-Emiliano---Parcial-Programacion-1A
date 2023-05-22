# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter en la cadena


def reemplazarCaracteres(cadena:str, primer_caracter:str, segundo_caracter:str)->int:
    """Reemplaza un caracter por otro en una cadena

    Args:
        cadena (str): La cadena a evaluar
        primer_caracter (str): El caracter a reemplazar en la cadena
        segundo_caracter (str): El caracter nuevo

    Returns:
        int: La cantidad de veces que se reemplazo el caracter
    """
    
    cantidad_veces = 0
    cadena_cambiada = ""
    
    for caracter in cadena:
        if caracter == primer_caracter:
            caracter = segundo_caracter
            cantidad_veces += 1
            
        cadena_cambiada += caracter
        
    return cantidad_veces
