
print("\n♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")
print("Ejercicio realizado por Daniel Franco\n")
print("Ejercicio 4: ¿Cuánto tardo en terminar una serie?")

# Damos de alta las variables
serie = "Breaking Bad"
temporadas = 5
episodios_por_temporada = 12.4
minutos_por_episodio = 47
horas_al_dia = 3

# Total de episodios
total_episodios = 62

# Total de minutos y horas
total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60

# ¿Cuántos días necesito?
dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"{serie} tiene {total_episodios} episodios")
print(f"Son {total_minutos} minutos en total")
print(f"Equivale a {total_horas:.1f} horas")
print(f"Viendo {horas_al_dia} horas diarias, la terminas en {dias_necesarios:.1f} días")
print("\n♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")
