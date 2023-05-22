
# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio_producto:float)->float:
    """Aplica un aumento a un producto del 5%

    Args:
        precio_producto (float): Precio del producto

    Returns:
        float: El precio con el aumento aplicado
    """
    
    porcentaje = 0.05
    aumento = precio_producto * porcentaje
    precio_aumento = precio_producto + aumento
    
    return precio_aumento
