def estimar_tiempo_y_confirmar(ingredientes_actuales):
    tiempo_estimado = 20 + (2 * len(ingredientes_actuales))
    print(f"\nEl tiempo estimado para su pizza es de {tiempo_estimado} minutos.")
    confirmacion = input("¿Desea confirmar su orden? (S/N): ").lower()
    if confirmacion == 's':
        print("Su orden ha sido confirmada")
    else:
        print("La orden ha sido cancelada.")