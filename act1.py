#Ejercicio de sumar 
a = float(8)
b = float(17.7)
res = a + b

print ("el resultado de tu suma es:", res)

#Ejercicio de IMC
peso = float(input ("Agrega el valor tu peso: "))
estatura = float(input ("Agrega el valor tu estatura: "))

imc = round (peso / (estatura ** 2), 2)

print("Tu indice de masa corporal es: ", imc) 

#Calculadora
print("Selecciona una operación")
def sumar (a, b): return a + b
def restar (a, b): return a - b
def multiplicar (a, b): return a * b
def dividir (a, b):
    if b == 0:
        return "Error división por cero"
    return a / b

print ("Selecciona la opración: ")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")

opcion = input("Ingrese opción 1 / 2 / 3 / 4")

try:
    num1 = float(input("Ingrese el valor del primero número: "))
    num2 = float(input("Ingrese el valor del segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida")
except ValueError:
    print("Porfavor ingrese números válidos")