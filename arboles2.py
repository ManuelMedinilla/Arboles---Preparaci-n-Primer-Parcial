class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

# Función para encontrar el valor más cercano a un objetivo en el árbol
def valor_mas_cercano(root, target):
    # Si el nodo es nulo, devuelve infinito
    if not root:
        return float('inf')
    
    # Valor del nodo actual
    a = root.val
    
    # Determina hacia qué hijo continuar según el valor objetivo
    hijo = root.izquierda if target < a else root.derecha
    
    # Si no hay hijo, devuelve el valor del nodo actual
    if not hijo:
        return a
    
    # Recursivamente busca el valor más cercano en el subárbol
    b = valor_mas_cercano(hijo, target)
    
    # Retorna el valor más cercano entre el nodo actual y el valor del subárbol
    return min((a, b), key=lambda x: abs(target - x))

# Construcción del árbol de ejemplo
root = NodoArboles(8)
root.izquierda = NodoArboles(5)
root.derecha = NodoArboles(14)
root.izquierda.izquierda = NodoArboles(4)
root.izquierda.derecha = NodoArboles(6)
root.izquierda.derecha.izquierda = NodoArboles(7)
root.derecha.derecha = NodoArboles(24)
root.derecha.derecha.izquierda = NodoArboles(22)

# Llamada a la función para encontrar el valor más cercano a 19 en el árbol
resultado = valor_mas_cercano(root, 19)
print(resultado)  # Salida esperada: 22
