class NodoArbol(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def array_a_bst(nums):
    if not nums:
        return None
    medio = len(nums) // 2
    nodo = NodoArbol(nums[medio])
    nodo.izquierda = array_a_bst(nums[:medio])
    nodo.derecha = array_a_bst(nums[medio+1:])
    return nodo

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda)
    preOrder(node.derecha)

# Ejemplo de uso
resultado = array_a_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(resultado)
