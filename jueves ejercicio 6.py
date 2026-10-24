
print("\n================================================")
print("Ejercicio 6: Vidas y daño")
print("================ BATALLA =======================")

# Damos de alta las variables
personaje = "Mario"
vida = 100

print(f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")

# Primer golpe: Goomba
vida = vida - 25
print(f"Me dio un golpe un Goomba, ahora tengo vida: {vida}")

# Segundo golpe: Koopa
vida = vida - 40
print(f"Me dio un golpe un Koopa, ahora tengo vida: {vida}")

# Tercer golpe: Bowser
vida = vida - 15
print(f"Me dio un golpe Bowser, ahora tengo vida: {vida}")

# Mario toma una poción
vida = vida + 30
print(f"Tomé una poción... mi vida: {vida}")

print(f"\n{personaje} terminó la batalla con {vida} HP\n")
print("================================================")
