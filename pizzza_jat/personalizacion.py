def seleccionar_masa():
    masas = ["Tradicional", "Delgada", "Con Bordes de Queso"]
    print("\nTipos de Masa:")
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    eleccion = int(input("Seleccione el tipo de masa: "))
    return masas[eleccion - 1]

def seleccionar_salsa():
    salsas = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    print("\nTipos de Salsa:")
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    eleccion = int(input("Seleccione el tipo de salsa: "))
    return salsas[eleccion - 1]

def modificar_ingredientes(ingredientes_actuales):
    ingredientes = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    print("\nIngredientes Disponibles:")
    for i, ing in enumerate(ingredientes, 1):
        print(f"{i}. {ing}")
    accion = input("¿Desea agregar (A) o eliminar (E) un ingrediente? ").lower()
    if accion == 'a':
        eleccion = int(input("Seleccione el ingrediente a agregar: "))
        if ingredientes[eleccion - 1] not in ingredientes_actuales:
            ingredientes_actuales.append(ingredientes[eleccion - 1])
    elif accion == 'e':
        eleccion = int(input("Seleccione el ingrediente a eliminar: "))
        if ingredientes[eleccion - 1] in ingredientes_actuales:
            ingredientes_actuales.remove(ingredientes[eleccion - 1])
    return ingredientes_actuales

def mostrar_ingredientes_actuales(ingredientes_actuales):
    print("\nIngredientes Actuales en la Pizza:")
    for ing in ingredientes_actuales:
        print(f"- {ing}")
