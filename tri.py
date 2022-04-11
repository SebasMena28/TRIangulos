import os
import time
import math

# funcion para calcular el area del triangulo según sus lados


def calcular(lado1, lado2, lado3):
    semiper = (lado1 + lado2 + lado3) / 2
    area = ((semiper) * (semiper - lado1) *
            (semiper - lado2) * (semiper - lado3)) ** 0.5
    return area

# funcion para calcular con base y altura


def calcular2(base, altura):
    area = (base * altura)/2
    return area


def calcular3(ang1, ang2, ang3):
    print('SI SE PUEDE')


def calcular4(lado1, lado2, ang):
    angulo = math.radians(ang)
    area = (lado1 * lado2 * math.sin(angulo)) / 2
    return area


def calcular5(lado, ang1, ang2):
    angulo1 = math.radians(ang1)
    angulo2 = math.radians(ang2)
    area = (((lado)**2) * math.sin(angulo1) * math.sin(angulo2)) / \
        (2 * math.sin(angulo1 + angulo2))
    return area


def esnumero():
    while True:
        entrada = input()
        try:
            entrada = float(entrada)
            while(entrada <= 0 or entrada >= 200):
                print()
                print('El valor ingresado es muy pequeño o demasiado grande')
                entrada = input('Ingrese de nuevo: ')
                entrada = float(entrada)
            return entrada
        except ValueError:
            print()
            print("Error! Los textos no pueden ser ingresados.")
            print("Intente de nuevo:")


# función para contar los lados iguales del triangulo
def conocertipo(lad1, lad2, lad3):
    iguales = 0
    if(lad1 == lad2):
        iguales += 1
    if (lad1 == lad3):
        iguales += 1
    if (lad2 == lad3):
        iguales += 1

    # ahora devolvemos el nombre del tipo de triangulo

    if(iguales == 3):
        tipo = 'EQUILÁTERO'
    elif(iguales == 1):
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'

    return tipo


def menu():
    print('Ingrese una de las siguientes opciones: ')
    print()
    print('1. Cálculo del área conociendo los 3 lados')
    print('2. Cálculo del área conociendo su base y altura')
    print('3. Cálculo del área conociendo 2 lados y un ángulo')
    print('4. Cálculo del área conociendo 2 ángulos y un lado')
    print('5. Salir')
    op = (input('Respuesta: '))
    return op


def main():
    print('---Programa para calcular el área de un triángulo---')
    print()

    resp = menu()
    os.system("cls")

    if (resp == '1'):
        # ingreso del valor del lado 1 y control de este
        print('Ingrese el valor del lado 1: ')
        lado1 = esnumero()

        print()
        print('Ingrese el valor del lado 2: ')
        lado2 = esnumero()

        print()
        print('Ingrese el valor del lado 3: ')
        lado3 = esnumero()

        print()

        print("El triángulo se identifica como uno de tipo ",
              conocertipo(lado1, lado2, lado3))

        resultado = calcular(lado1, lado2, lado3)
        print("El area es: ", '{0:.2f}'.format(resultado))

        time.sleep(2)
        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opción: ')
        if(op == '1'):
            os.system("cls")
            main()
        else:
            print()
            os.system("cls")
            print('Gracias por usar el sistema :)')

    elif(resp == '2'):

        print('Ingrese el valor de la base: ')
        base = esnumero()

        print('Ingrese el valor de la altura: ')
        altura = esnumero()

        print("El triangulo se identifica como uno de tipo TRIÁNGULO RECTÁNGULO")

        resultado = calcular2(base, altura)
        print("El area es: ", '{0:.2f}'.format(resultado))

        time.sleep(2)
        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opción: ')
        if(op == '1'):
            os.system("cls")
            main()
        else:
            print()
            os.system("cls")
            print('Gracias por usar el sistema ')

    elif(resp == '3'):

        print('Ingrese el valor del lado 1: ')
        lado1 = esnumero()

        print('Ingrese el valor del lado 2: ')
        lado2 = esnumero()

        print('Ingrese el valor del ángulo: ')
        ang1 = esnumero()

        while(ang1 >= 180):
            print('El valor del ángulo es inválido. Intente de nuevo: ')
            ang1 = esnumero()

        lado3 = ((lado1**2) + (lado2**2) -
                 (2 * lado1 * lado2 * math.cos(ang1)))*0.5

        if(lado1 == lado2 and ang1 == 60):
            print("El triángulo se identifica como uno de tipo EQUILÁTERO")
        else:
            print("El triángulo se identifica como uno de tipo ",
                  conocertipo(lado1, lado2, lado3))

        resultado = calcular4(lado1, lado2, ang1)
        print("El area es: ", '{0:.2f}'.format(resultado))

        time.sleep(2)
        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opción: ')
        if(op == '1'):
            os.system("cls")
            main()
        else:
            print()
            os.system("cls")
            print('Gracias por usar el sistema ')

    elif(resp == '4'):

        print('Ingrese el valor del lado 1: ')
        lado1 = esnumero()

        print('Ingrese el valor del ángulo 1: ')
        ang1 = esnumero()

        print('Ingrese el valor del ángulo 2: ')
        ang2 = esnumero()

        while (ang1+ang2 >= 180):
            print('El valor de los ángulos es inválido')
            print('Intente de nuevo:')
            print()
            print('Ingrese el valor del ángulo 1: ')
            ang1 = esnumero()

            print('Ingrese el valor del ángulo 2: ')
            ang2 = esnumero()

        resultado = calcular5(lado1, ang1, ang2)
        print("El area es: ", '{0:.2f}'.format(resultado))

        time.sleep(2)
        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opción: ')
        if(op == '1'):
            os.system("cls")
            main()
        else:
            print()
            os.system("cls")
            print('Gracias por usar el sistema :)')

    elif(resp == '5'):
        os.system("cls")
        print('Gracias por usar el sistema :)')

    else:
        print('Esta opción no está disponible en el menú')
        print('Intente de nuevo... ')
        print()
        input('Presione ENTER para continuar')
        os.system("cls")
        main()


os.system("cls")
main()
