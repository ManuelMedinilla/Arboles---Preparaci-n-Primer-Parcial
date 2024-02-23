class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def borrar_nodo(root, key):
    if not root:
        return root

    # Encontramos el nodo en el subárbol izquierdo, pero la llave es evaluada y es menor que el valor de root
    if root.val > key:
        root.izquierda = borrar_nodo(root.izquierda, key)
    
    # Encuentra el nodo en el subárbol derecho cuando la key es evaluada y es mayor que root
    elif root.val < key:
        root.derecha = borrar_nodo(root.derecha, key)
    
    # Borra el nodo si root.val == key
    else:
        # Si el hijo derecho es nulo, la nueva raíz será el hijo izquierdo
        if not root.derecha:
            return root.izquierda
        # Si el hijo izquierdo es nulo, la nueva raíz será el hijo derecho
        elif not root.izquierda:
            return root.derecha
        # Si existen hijos izquierdo y derecho en el nodo,
        # reemplace su valor con el valor mínimo en el subárbol derecho.
        # Ahora elimina ese nodo mínimo en el subárbol derecho
        temp_val = encontrar_minimo(root.derecha)
        root.val = temp_val.val
        root.derecha = borrar_nodo(root.derecha, temp_val.val)

    return root

def encontrar_minimo(node):
    while node.izquierda:
        node = node.izquierda
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda)
    preOrder(node.derecha)

root = NodoArboles(5)
root.izquierda = NodoArboles(3)
root.derecha = NodoArboles(6)
root.izquierda.izquierda = NodoArboles(2)
root.izquierda.derecha = NodoArboles(4)
root.izquierda.derecha.izquierda= NodoArboles(7)
print("nodo original")
print(preOrder(root))
result=borrar_nodo(root,4)
print("despues de boorar el nodo superior: ")
print(preOrder(result))