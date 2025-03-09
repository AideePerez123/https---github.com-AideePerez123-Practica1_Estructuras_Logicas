from menu import mostrar_menu 

def evaluar_variable(variables, operacion):
    if operacion == 'conjuncion':
        if variables[0] == 1 and variables[1] == 1:
            return True
        else:
            return False
    elif operacion == 'disyuncion':
        if variables[0] == 0 and variables[1] == 0:
            return False
        else:
            return True
    elif operacion == 'disyuncion excluyente':
        if (variables[0] == 1 and varables[1] == 0) or (variables[0] == 0 and variables[1] == 1):
            return True
        else:
            return False
    elif operacion == 'condicional':
        if variables[0] == 1 and varables[1] == 0:
            return False
        else:
            return True
    else:
        return None 
        print('la operacion que ingreso no es valida')

def imprimir_tabla(tabla, encabezados):
    for encabezado in encabezados:
        print(encabezado, end=" | ")
    print()

    for fila in tabla:
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def generar_tabla_verdad():
    print("Ingrese las variables, pueden ser maximo 3(separadas por comas):")
    variables = input()  
    variable_lista = []
    
    #aqui se dividen las variables una por una
    i = 0
    while i < len(variables):
        var = ""
        while i < len(variables) and variables[i] != ',':
            var += variables[i]
            i = i + 1
        variable_lista.append(var.strip()) 
        i = i + 1  

#aqui se comprueba el numero de las variables
    if len(variable_lista) < 1 or len(variable_lista) > 3:
        print("error no se permiten mas variables, solo pueden ser tres")
        return 

    print("Ingrese hasta 3 expresiones lógicas (separadas por comas):")
    expresion = input()  
    operacion_list = []
    
    #aqui se dividen manualmente las expreciones
    i = 0
    while i < len(expresion):
        operacion = ""
        while i < len(expresion) and expresion[i] != ',':
            operacion = operacion + expresion[i]
            i = i + 1
        operacion_list.append(operacion.strip()) 
        i = i + 1  

    #aqui se analiza que la operacion sea la que esta en la lista
    for operacion in operacion_list:
        if operacion not in ['conjuncion', 'disyuncion', 'disyuncion excluyente', 'condicional', 'bicondicional']:
            print(f"Error: La operación '{operacion}' no es válida.")
            return

    # Generar la tabla de verdad
    filas = 2 ** len(variable_lista)
    tabla = []

    for i in range(filas):
        valores = [(i >> (len(variable_lista) - j - 1)) & 1 for j in range(len(variable_lista))]
        filas = []

        for operacion in operacion_list:
            if len(variable_lista) >= 2:
                resultado = evaluar_variable(valores[:2], operacion)
                filas.append(int(resultado))

        tabla.append(valores + filas)

    print("----------TABLA---------------")
    imprimir_tabla(tabla, variable_lista + operacion_list)

def main():
    while True:
        option = mostrar_menu()

        if option == '1':
            generar_tabla_verdad()
        elif option == '2':
            print("Programa finalizado")
            break
        else:
            print("Esa opcion no es valida")

if __name__ == "__main__":
    main()