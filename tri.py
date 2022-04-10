import os
import time
import math

# funcion para calcular el area del triangulo según sus lados
def calcular(lado1, lado2, lado3):
    semiper = (lado1 + lado2 + lado3) / 2
    area = ((semiper) * (semiper - lado1) * (semiper - lado2) * (semiper - lado3)) ** 0.5
    return area

#funcion para calcular con base y altura
def calcular2(base,altura):
    area = (base * altura)/2
    return area

def calcular3(ang1, ang2, ang3):
    print('SI SE PUEDE')

def calcular4(lado1, lado2, ang):
    area = (lado1 * lado2 * math.sin(ang)) / 2
    return area

def calcular5(lado, ang1, ang2):
    area = ( ((lado)**2) * math.sin(ang1) * math.sin(ang2) ) / (2 * math.sin(ang1 + ang2))
    return area

# función para contar los lados iguales del triangulo
def conocertipo(lad1, lad2, lad3):
    iguales = 0
    if(lad1 == lad2):
        iguales +=1
    if (lad1 == lad3):
        iguales += 1
    if (lad2 == lad3):
        iguales += 1
    
    #ahora devolvemos el nombre del tipo de triangulo

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
    print('1. Cálculo por medio de 3 lados')
    print('2. Cálculo por medio de base y altura')
    print('3. Cálculo por medio de 2 lados y un ángulo')
    print('4. Cálculo por medio de 2 ángulos y un lado')
    op = int(input('Respuesta: '))
    return op


def main():
    print('---Programa para calcular el área de un triángulo---')
    print()

    resp = menu()
    os.system ("cls")

    if (resp == 1):
        # ingreso del valor del lado 1 y control de este
        lado1 = float(input('Ingrese el valor del lado 1: '))
        while(lado1 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado1 = float(input('Ingrese el valor del lado 1: '))

        # ingreso del valor del lado 2 y control de este
        lado2 = float(input('Ingrese el valor del lado 2: '))
        while(lado2 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado2 = float(input('Ingrese el valor del lado 2: '))

        # ingreso del valor del lado 3 y control de este
        lado3 = float(input('Ingrese el valor del lado 3: '))
        while(lado3 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado3 = float(input('Ingrese el valor del lado 3: '))

        print()

        print("El triangulo se identifica como uno de tipo ", conocertipo(lado1, lado2, lado3))
        print("Su área es de: ", round(calcular(lado1, lado2, lado3), 3))

        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opcion: ')
        if(op == '1'):
            os.system ("cls")
            main()
        else:
            print()
            os.system ("cls")
            print('Gracias por usar el sistema :)')
    
    elif(resp == 2):
        # ingreso del valor de la base y control de este
        base = float(input('Ingrese el valor de la base: '))
        while(base <= 0):
            print('El valor de la base debe ser superior a 0')
            base = float(input('Ingrese el valor de la base: '))

        # ingreso del valor de la altura y control de este
        altura = float(input('Ingrese el valor de la altura: '))
        while(altura <= 0):
            print('El valor de la altura debe ser superior a 0')
            altura = float(input('Ingrese el valor de la altura: '))

        print("El triangulo se identifica como uno de tipo RECTÁNGULO")
        print('El area es: ', calcular2(base,altura))

        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opcion: ')
        if(op == '1'):
            os.system ("cls")
            main()
        else:
            print()
            os.system ("cls")
            print('Gracias por usar el sistema :)')
    
    elif(resp == 3):
        # ingreso del valor del lado 1 y control de este
        lado1 = float(input('Ingrese el valor del lado 1: '))
        while(lado1 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado1 = float(input('Ingrese el valor del lado 1: '))

        # ingreso del valor del lado 2 y control de este
        lado2 = float(input('Ingrese el valor del lado 2: '))
        while(lado2 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado2 = float(input('Ingrese el valor del lado 2: '))
        
        ang1 = float(input('Ingrese el valor del ángulo: '))
        while(ang1<= 0):
            print('Un ángulo no puede tomar el valor de ', ang1)
            print('Intente de nuevo...')
            ang1 = float(input('Ingrese el valor del ángulo: '))
        
        lado3 = ((lado1*2) + (lado22) - (2 * lado1 * lado2 * math.cos(ang1)))*0.5

        print("El triangulo se identifica como uno de tipo ", conocertipo(lado1, lado2, lado3))
        print('El area es: ', round(calcular(lado1, lado2, lado3),3))

        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opcion: ')
        if(op == '1'):
            os.system ("cls")
            main()
        else:
            print()
            os.system ("cls")
            print('Gracias por usar el sistema :)')
    
    elif(resp == 4):
        lado1 = float(input('Ingrese el valor del lado 1: '))
        while(lado1 <= 0):
            print('El valor de un lado debe ser superior a 0')
            lado1 = float(input('Ingrese el valor del lado 1: '))
        
        ang1 = float(input('Ingrese el valor del ángulo 1: '))

        ang2 = float(input('Ingrese el valor del ángulo 2: '))

        print('El area es: ', calcular5(lado1, ang1, ang2))

        print()
        input('Presione ENTER para continuar')
        print()
        print('Volver a intentar:')
        print('1. Si')
        print('2. No')
        op = input('Opcion: ')
        if(op == '1'):
            os.system ("cls")
            main()
        else:
            print()
            os.system ("cls")
            print('Gracias por usar el sistema :)')
        
    else:
        print('Esta opción no está disponible en el menu')
        print('Intente de nuevo... ')
        print()
        input('Presione ENTER para continuar')
        os.system ("cls")
        main()

os.system ("cls")
main()