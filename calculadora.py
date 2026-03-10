from funciones import *

print("Bienvenido a la Calculadora Python")

# Pedir los números por primera vez
numero1,numero2=cambiar_numeros()
        
while True:
    mostrar_menu()
    operacion = input("Selecciona una opción: ")
    if operacion == "1":
        print("Resultado:", sumar(numero1, numero2))
    elif operacion == "2":
        print("Resultado:", restar(numero1, numero2))
    elif operacion == "3":
        print("Resultado:", multiplicar(numero1, numero2))
    elif operacion == "4":
        resultado = dividir(numero1, numero2)
        print("Resultado:", resultado)
    elif operacion == "5":
     numero1,numero2= cambiar_numeros()
    elif operacion == "0":
        print("Gracias por usar la calculadora")
        break
    else:
        print("Opción no válida")