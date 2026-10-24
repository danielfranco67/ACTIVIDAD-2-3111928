
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Ejercicio 7: Subir de nivel")
print("FORTNITE - SUBIR DE NIVEL")

# Damos de alta las variables
xp_actual = 1500
xp_siguiente_nivel = 2500
xp_por_partida = 175

print(f"\nTengo {xp_actual} de XP y necesito {xp_siguiente_nivel} para subir de nivel")
print(f"En cada partida gano {xp_por_partida} de XP")

# Calculamos cuánta XP me falta
xp_faltante = xp_siguiente_nivel - xp_actual
print(f"Me faltan {xp_faltante} de XP")

# Calculamos cuántas partidas completas necesito
partidas = xp_faltante // xp_por_partida
print(f"Con {partidas} partidas llego casi al nivel")

# Calculamos cuánta XP sobra
xp_sobrante = xp_faltante % xp_por_partida
print(f"Después de esas partidas, todavía me faltan {xp_sobrante} de XP")

# Sumamos una partida más si es necesario
if xp_sobrante > 0:
    partidas_totales = partidas + 1
else:
    partidas_totales = partidas

print(f"\nEn total necesito jugar {partidas_totales} partidas para subir de nivel")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")


