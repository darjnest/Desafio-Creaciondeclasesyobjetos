from te import Te

# Crear dos instancias de la clase Te
te1 = Te()
te2 = Te()

# Almacenar el tipo de dato de cada instancia
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrar el tipo de dato
print(f"Tipo de dato de te1: {tipo_te1}")
print(f"Tipo de dato de te2: {tipo_te2}")

# Comparar y mostrar si son del mismo tipo
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
