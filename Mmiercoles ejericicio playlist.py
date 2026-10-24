
print("\n++++++++++")
print("Ejercicio 5 realizado por Daniel Franco\n")
print("Ejercicio 5: ¿Cuánto dura mi playlist?")

# Duración de cada canción en segundos
cancion1 = 215  # ROA
cancion2 = 187  # ANUEL
cancion3 = 240  # BAD BUNNY
cancion4 = 198  # JHAYCO
cancion5 = 225  # ALVARO DIAZ

# Sumamos todo
total_segundos = cancion1 + cancion2 + cancion3 + cancion4 + cancion5

# Calculamos los minutos completos
minutos = total_segundos // 60

# Calculamos los segundos que sobran
segundos = total_segundos % 60

print("\nResultados")
print(f"Total en segundos: {total_segundos}")
print(f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print("\n++++++++++")
