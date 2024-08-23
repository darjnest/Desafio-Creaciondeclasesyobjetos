from te import Te

# Pedir datos al usuario
sabor = int(
    input("Ingrese el sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): ")
)
formato = int(input("Ingrese el formato del té (300 o 500 gramos): "))

# Obtener datos del té
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Mostrar detalles del pedido
sabores = {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}
print("Detalle del pedido:")
print(f"Sabor: {sabores.get(sabor, 'Sabor no válido')}")
print(f"Formato: {formato} gramos")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
