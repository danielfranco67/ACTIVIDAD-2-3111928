
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ejercicio 9: Tienda de mascotas interactiva")
print("TIENDA DE MASCOTAS DE Daniel Franco")

# Datos del cliente (ya vienen escritos en el código)
mascota = "PERRO"
print(f"\n¿Qué mascota quieres adoptar? {mascota}")

# float() sirve para precios con decimales
precio_mascota = float(500)
print(f"¿Cuánto cuesta el {mascota}? ${precio_mascota:.0f}")

precio_croquetas = float(50)
print(f"¿Cuánto cuesta un mes de croquetas? ${precio_croquetas:.0f}")

# int() sirve para números enteros, porque los meses no llevan decimales
meses = int(5)
print(f"¿Para cuántos meses quieres croquetas? {meses}")

# Calculamos cuánto gasto en croquetas: 50.0 * 5
costo_croquetas = precio_croquetas * meses
# Ahora costo_croquetas vale 250.0

# Calculamos el total: 500.0 + 250.0
total = precio_mascota + costo_croquetas
# Ahora total vale 750.0

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ticket de compra")
# El :.2f muestra 2 decimales, como se ve el dinero
print(f"Mascota: {mascota}  ${precio_mascota:.2f}")
print(f"Croquetas por {meses} meses: ${costo_croquetas:.2f}")
print(f"\nTOTAL A PAGAR: ${total:.2f}\n")
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")





