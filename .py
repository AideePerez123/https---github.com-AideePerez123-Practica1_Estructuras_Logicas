from menu import mostrar_menu

def evaluar_expresion(p, q, operacion):
    if operacion == 'p^q':  
        return p and q
    elif operacion == 'pvq':  
        return p or q
    elif operacion == 'p v q':  
        return p or q
    elif operacion == 'p≠q':  
        return p != q
    elif operacion == 'p→q':  
        return not p or q
    elif operacion == 'p↔q':  
        return p == q
    else:
        raise ValueError("Operación no reconocida")

    