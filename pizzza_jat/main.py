from menu import mostrar_menu
from personalizacion import seleccionar_masa, seleccionar_salsa, modificar_ingredientes, mostrar_ingredientes_actuales
from estimacion import estimar_tiempo_y_confirmar

def main():
    masa = ""
    salsa = ""
    ingredientes_actuales = []
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            masa = seleccionar_masa()
            print(f"Masa seleccionada: {masa}")
        
        elif opcion == 2:
            salsa = seleccionar_salsa()
            print(f"Salsa seleccionada: {salsa}")
        
        elif opcion == 3:
            ingredientes_actuales = modificar_ingredientes(ingredientes_actuales)
        
        elif opcion == 4:
            mostrar_ingredientes_actuales(ingredientes_actuales)
        
        elif opcion == 5:
            estimar_tiempo_y_confirmar(ingredientes_actuales)
        
        elif opcion == 6:
            print("Gracias por usar el sistema de pedidos de Pizza JAT. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
