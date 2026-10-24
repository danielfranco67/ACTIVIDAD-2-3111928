print("\n★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT HECHO POR Daniel Franco")

# Aquí el usuario es texto, no lo convertimos
usuario = "_danielfranco_"
print(f"\nTu usuario de Instagram/TikTok: @{usuario}")

# int() convierte a número entero para poder hacer cuentas
seguidores = int(461)
print(f"¿Cuántos seguidores tienes? {seguidores}")
likes = int(109)
print(f"¿Cuántos likes tuvo tu último post? {likes}")
comentarios = int(7)
print(f"¿Cuántos comentarios tuvo? {comentarios}")

# Sumamos todas las interacciones: interacciones = 109 + 7
# Ahora interacciones vale 116
interacciones = likes + comentarios

# Calculamos el engagement: qué porcentaje de mis seguidores interactuó
# Los paréntesis hacen que la división se haga ANTES de multiplicar por 100
# Esta fórmula dice: engagement = (116 / 461) * 100
engagement = (interacciones / seguidores) * 100
# Ahora engagement vale 25.16...

print(f"\n★★★★★★★★★★★★★★★★★★★★ RESULTADOS DE @{usuario} ★★★★★★★★★★★★★★★★★★★★")
print(f"Interacciones totales: {interacciones}")
# El :.2f muestra 2 decimales, así que se ve 25.16%
print(f"Engagement: {engagement:.2f}%")
print("\nDato: en redes, un engagement arriba de 3% ya se considera bueno")
print("\n★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")