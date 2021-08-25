import sys
menu = '''
TALLER #2 - CONDICIONALES, ITERACIONES Y FUNCIONES
Integrantes
> Sindy Paola Devoz Perez
> Freddy Manuel Barrios Del rio

Ejecutar programa

a. que imprima todos los números pares entre dos números que ingrese el 
   usuario. Valide que los valores ingresados sean numéricos.
b. que reciba un número n e imprima los primeros n números triangulares 
   junto con su índice. Los números triangulares se obtienen mediante la suma de los números 
   naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
   * Desarrolle una versión mediante el diseño de una función. 
1 --> 1
2 --> 3
3 --> 6
4 --> 10
5 --> 15
c. que mediante una función, calcule el costo de las llamadas realizadas 
   en un teléfono móvil y la duración en segundos, recibiendo como entrada la tarifa por segundo, 
   el numero de comunicaciones realizadas y la duración de cada llamada expresada en horas, minutos y segundos.
d. que mediante funciones, convierte una cantidad ingresada en pesos colombianos 
   a dólares americanos, euros y bitcoins. 
e. que, mediante una función, organize de forma ascendente, tres valores numéricos ingresados por el usuario.
f. Salir

'''

options = ['a', 'b', 'c', 'd', 'e', 'f']
numberPI = 3.1416
running = True

def main():
    print(menu)
    program = input('Ingresa la letra correspondiente al programa que quieres ejecutar: ')
    options.index(program)
    print("================================================================")
    process(program)
    print("================================================================")
    return program


def continueProgram():
    wantContinue = input('Deseas continuar? Ingresa YES or NO: ')
    return wantContinue == 'YES' or wantContinue == 'yes' or wantContinue == 'y'
        
def printPairs():
    print('''que imprima todos los números pares entre dos números que ingrese el 
    usuario. Valide que los valores ingresados sean numéricos.''')
    pairs = []
    
    firstNumber = input('Ingresa el primer número: ')
    secondNumber = input('Ingresa el segundo número: ')
    if firstNumber.isnumeric() and secondNumber.isnumeric():
        firstNumber = int(firstNumber)
        secondNumber = int(secondNumber)
        if secondNumber < firstNumber:
            print('El segundo número debe ser mayor')
        else:
            evaluatedNumber = firstNumber
            while evaluatedNumber <= secondNumber:
                if evaluatedNumber % 2 == 0:
                    pairs.append(evaluatedNumber)
                evaluatedNumber = evaluatedNumber + 1
            print('Los números pares que se encuentran entre {} y {} son: {} '.format(firstNumber, secondNumber, pairs))
    else:
        print('Los valores no son númericos')


def process(program):
    if program == 'a':
        printPairs()
    elif program == 'f':
        print('Good bye! ')
        global running
        running = False

while running:
    #try:
        selectedProgram = main()
        if selectedProgram != 'f' and continueProgram():
            continue
        else:
            break
    #except:
    #    print('Por favor, ingresa una opción válida')
    #    continue



