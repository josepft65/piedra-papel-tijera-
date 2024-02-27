import random

def jugar():
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    opciones = ['piedra', 'papel', 'tijeras']
    computadora = random.choice(opciones)
    print(f"El oponente elige: {computadora}")

    if usuario not in opciones:
        print("!porfavor elige una opcion correcta!")
        return

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == 'piedra' and computadora == 'tijeras') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijeras' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

while True:
    jugar()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        break

