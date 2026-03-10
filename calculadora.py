
while  True:
    numero1= int(input("Introduce el primer numero: "))
    numero2= int(input("Introduce el segundo numero: "))
    operacion = input("Intruce la operacion que va a realizar: (sumar, restar, multiplicar,dividir): ")
    if operacion == "sumar":
        resultado = numero1 + numero2
        print("El resultado de la suma es: ", resultado)
    elif operacion == "restar":
        resultado = numero1 - numero2
        print("El resultado de la resta es: ", resultado)
    elif operacion == "multiplicar":
        resultado = numero1 * numero2
        print("El resultado de la multiplicacion es: ", resultado)
    elif operacion == "dividir":
        if numero2 == 0:
            print("No se puede dividir entre 0")
            continue
        else:
            resultado = numero1 / numero2
            print("El resultado de la division es: ", resultado)
    else:
        print("Operacion no valida")
    salir = input("¿Desea salir? (si/no): ")
    if salir == "si":
        break
print("Gracias por usar la calculadora")

