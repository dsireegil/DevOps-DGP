#Cuestionario de Hobies

print("Bienvenido")
nombre = str(input("Nombre: "))
edad = int(input("Edad: "))
color_favorito = str(input("Color favorito: "))
comida_favorita = str(input("Comida favorita: "))

datos =[nombre, edad, color_favorito, comida_favorita]
print ("Datos: ", datos)

hobbies = []
print ("Inserta tus hobbies")

h = int(input("¿Cuántos hobbies te gustarían añadir? "))

for i in range(h):
    hobbie = input(f"Introduce tu hobbie {i+1}: ")
    hobbies.append(hobbie)

print("\nLista de hobbies")
for indice, valor in enumerate(hobbies, 1):
    print(f"{indice}. {valor}")
