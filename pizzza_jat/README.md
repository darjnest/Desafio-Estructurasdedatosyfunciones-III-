## Desafío: Pizza JAT - Automatización de Pedidos

### Descripción del Proyecto

Este proyecto tiene como objetivo crear un prototipo básico para automatizar el proceso de pedido de pizzas en Pizza JAT. El programa permitirá al usuario personalizar su pizza seleccionando el tipo de masa, salsa e ingredientes. Además, proporcionará una estimación del tiempo de preparación y permitirá al usuario confirmar su pedido.

### Estructura del Programa

#### 1. Definición de Datos

* **Tipos de masa:** Una lista o conjunto para almacenar los tipos de masa disponibles.
* **Tipos de salsa:** Una lista o conjunto para almacenar los tipos de salsa disponibles.
* **Ingredientes:** Una lista o conjunto para almacenar los ingredientes disponibles.

#### 2. Funciones

* **mostrar_menu():** Presenta las opciones de personalización al usuario.
* **seleccionar_masa():** Permite al usuario elegir el tipo de masa.
* **seleccionar_salsa():** Permite al usuario elegir el tipo de salsa.
* **agregar_ingrediente():** Agrega un ingrediente a la pizza.
* **eliminar_ingrediente():** Elimina un ingrediente de la pizza.
* **mostrar_ingredientes():** Muestra los ingredientes actuales de la pizza.
* **calcular_tiempo():** Calcula el tiempo estimado de preparación.
* **confirmar_pedido():** Permite al usuario confirmar o cancelar el pedido.

#### 3. Flujo Principal

* Inicializar las listas de masa, salsa e ingredientes.
* Crear una lista vacía para almacenar los ingredientes seleccionados.
* Mostrar el menú principal.
* Utilizar un bucle para permitir al usuario realizar múltiples selecciones.
* En cada iteración del bucle:
    * Mostrar las opciones disponibles.
    * Solicitar al usuario su elección.
    * Llamar a la función correspondiente según la elección del usuario.
* Calcular el tiempo de preparación y mostrarlo al usuario.
* Preguntar al usuario si desea confirmar el pedido.

### Ejemplo de Código (Python)

```python
def mostrar_menu():
    # Imprimir las opciones del menú

def seleccionar_masa():
    # Pedir al usuario que seleccione la masa

# ... otras funciones

def main():
    # Inicializar datos
    masas = ["Tradicional", "Delgada", "Bordes de Queso"]
    salsas = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    ingredientes_disponibles = ["Tomate", "Champiñones", ...]
    ingredientes_seleccionados = []

    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        # ... lógica para cada opción

if __name__ == "__main__":
    main()