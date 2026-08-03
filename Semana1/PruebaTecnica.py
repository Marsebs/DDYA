import math
def p1(posi):

    if posi > 0:
        print(f"El numero {posi} es positivo")
    elif posi < 0:
        print(f"El numero {posi} es negativo")
    else:
        print(f"El numero {posi} es 0")

def p2(par):

    if par % 2 == 0:
        print(f"El numero {par} es par")
    else:
        print(f"El numero {par} es impar")

def p3(fibonazi):
    z = math.sqrt((5 * fibonazi ** 2) + 4)
    y = math.sqrt((5 * fibonazi ** 2) - 4)

    if z == int(z) or y == int(y):
        print(f"El numero {fibonazi} esta en la serie Fibonacci")
    else:
        print(f"El numero {fibonazi} no esta en la serie Fibonacci")

def p4(primo):
    x = 2
    cont = 0

    if primo < 2:
        print(f"El numero {primo} no es primo")
        return

    while x < primo:
        if primo % x == 0:
            cont += 1
        x += 1

    if cont == 0:
        print(f"El numero {primo} es primo")
    else:
        print(f"El numero {primo} no es primo")

def p5(valor1, valor2):
    suma = int()

    for x in range(valor1+1, valor2):
        suma+=x
    print(f"La suma de los numeros entre los 2 valores ingresados en un total de {suma}")

def p6(impar):

    if impar % 2 == 0:
        print(f"El numero al cubo es {impar ** 3}")
    else:
        print(f"El numero al cuadrado es {impar ** 2}")

def p7():
    carnet = int(input("Ingrese su carnet de la universidad\n"))
    p1(carnet)
    p2(carnet)
    p3(carnet)
    p4(carnet)
    p6(carnet)
    numeros = str(carnet)
    valor11 = int(numeros[0])
    valor22 = int(numeros[-1])
    suma = 0

    for x in range(min(valor11, valor22) + 1, max(valor11, valor22)):
        suma += x

    print(f"La suma de los numeros entre los extremos es {suma}")
    print(f"El primer extremo es {valor11} y el ultimo es {valor22}")

def p8():
    naci = input("Ingrese su fecha, ejemplo: 7octubre20000100032300\n")
    pala = ""

    for x in naci:
        if x.isalpha():
            pala += x

    print(f"El mes de su nacimiento es {pala}")
    return pala

def p9(pala):
    vocal = 0
    conso = 0

    for x in pala:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            vocal += 1
        else:
            conso += 1

    print(f"El mes de su nacimiento tiene {vocal} vocales y {conso} consonantes")

def p10(pala):
    abece = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]

    for x in pala:
        for z in range(len(abece)):
            if x == abece[z]:
                print(f"La letra {x} esta en la posicion {z + 1} del abecedario")
def main():
    opc = 1
    while opc != 0:
        opc = int(input("Seleccione el punto que va a ejecutar\n1. Positivo, negativo o cero\n2. Par o impar\n3. Serie Fibonacci\n4. Número primo\n5. Sumar números intermedios\n6. Cuadrado o cubo\n7. Proceso con código estudiantil\n8. Obtener mes de nacimiento\n9. Vocales y consonantes del mes\n10. Posición de las letras del mes\n0. Salir\n"))

        if opc == 1:
            posi = int(input("Ingrese un numero: "))
            p1(posi)
        elif opc == 2:
            par = int(input("Ingrese un numero: "))
            p2(par)
        elif opc == 3:
            fibonazi = int(input("Ingrese un numero: "))
            p3(fibonazi)
        elif opc == 4:
            primo = int(input("Ingrese un numero: "))
            p4(primo)
        elif opc == 5:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
            p5(valor1, valor2)
        elif opc == 6:
            impar = int(input("Ingrese un numero: "))
            p6(impar)
        elif opc == 7:
            p7()
        elif opc == 8:
            p8()
        elif opc == 9:
            pala = p8()
            p9(pala)
        elif opc == 10:
            pala = p8()
            p10(pala)
        elif opc == 0:
            print("Gracias por usar el programa")
        else:
            print("Opcion no valida")
main()
