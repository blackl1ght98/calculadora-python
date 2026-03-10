def sumar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado
def restar(numero1,numero2):
    resultado = numero1 - numero2
    return resultado
def multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    return resultado
def dividir(numero1,numero2):
    if numero2 == 0:
        print("No es posible dividir entre 0")
    else: 
        resultado = numero1 / numero2
        return resultado
def cambiar_numeros():
    while True:
        try:
            numero1 = int(input("Introduce el primer numero: "))
            numero2 = int(input("Introduce el segundo numero: "))
            return numero1, numero2
        except ValueError:
            print("Por favor, introduce números válidos.")
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Cambiar números")
    print("0. Salir")