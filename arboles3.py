class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def is_BST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.izquierda
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.derecha

    return True  
root = NodoArboles(2)
root.izquierda = NodoArboles(1)
root.derecha = NodoArboles(3)

result = is_BST(root)
print(result)
root = NodoArboles(1)
root.izquierda = NodoArboles(2)
root.derecha = NodoArboles(3)

result = is_BST(root)
print(result)
