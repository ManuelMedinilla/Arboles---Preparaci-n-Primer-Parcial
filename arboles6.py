class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.izquierda  # Corrected the spelling mistake here
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.derecha  # Corrected the spelling mistake here

root = NodoArboles(8)
root.izquierda = NodoArboles(5)
root.derecha = NodoArboles(14)
root.izquierda.izquierda = NodoArboles(4)
root.izquierda.derecha = NodoArboles(6)
root.izquierda.derecha.izquierda = NodoArboles(8)
root.izquierda.derecha.derecha = NodoArboles(7)
root.derecha.derecha = NodoArboles(24)
root.derecha.derecha.izquierda = NodoArboles(22)

print(kth_smallest(root, 2))
print(kth_smallest(root, 3))