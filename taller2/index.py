import sys

menu = '''
TALLER #2 - CONDICIONALES, ITERACIONES Y FUNCIONES
Integrantes
> Sindy Paola Devoz Perez
> Freddy Manuel Barrios Del rio
> Luis Guillermo Castro
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
    print('''Imprima todos los números pares entre dos números que ingrese el 
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


def printTriangular():
    print(''' que reciba un número n e imprima los primeros n números triangulares 
   junto con su índice. Los números triangulares se obtienen mediante la suma de los números 
   naturales desde 1 hasta n''')  
    firstNumber = input('Ingresa el número a triangular: ')
    if firstNumber.isnumeric() :
        firstNumber = int(firstNumber)
        numberInital= 1
        numberTriangular=0
        while numberInital <= firstNumber:
            numberTriangular=numberTriangular+numberInital
            print(numberInital,'--->',numberTriangular)
            numberInital=numberInital+1      
    else:
        print('Los valores no son númericos')

def printCalls():
    print('''Calcule el costo de las llamadas realizadas 
   en un teléfono móvil y la duración en segundos, recibiendo como entrada la tarifa por segundo, 
   el numero de comunicaciones realizadas y la duración de cada llamada expresada en horas, minutos y segundos.''')
    secondRate = input('Ingresa la tarifa por segundos: ')
    numbersCalls = input('Ingresa numero de llamadas realizadas: ')
    if secondRate.isnumeric() and numbersCalls.isnumeric():
        secondRate = int(secondRate)
        numbersCalls = int(numbersCalls)
        rate=[]
        cont=1
        totalScond=0
        while cont<=numbersCalls:
            sconds=0
            print('Ingrese los daos de la llamada {}'.format(cont))
            hoursCalls = input('Hora: ')
            minutesCalls = input('Minutos: ')
            secondCalls = input('Segundos: ')
            if hoursCalls.isnumeric() and minutesCalls.isnumeric() and secondCalls.isnumeric():
                hoursCalls = int(hoursCalls)
                sconds = (hoursCalls*60)*60
                minutesCalls = int(minutesCalls)
                secondCalls = int(secondCalls)
                if minutesCalls <=60 and secondCalls<=60:
                    sconds=sconds+(minutesCalls*60)
                    sconds=sconds+secondCalls                    
                    totalScond=totalScond+sconds
                    print('La llamada {} es de {} segundos con un valor de  ${}'.format(cont, sconds,sconds*secondRate))
                    cont=cont+1
                else:
                    print('Los minutos y segundos  solo van hasta 60')
            else:
                print('Los valores no son númericos')
        print("Total de todas las llamdas es de {} segundos con un valor de  ${}".format(totalScond,totalScond*secondRate))
    else:
        print('Los valores no son númericos')

def printConverter():
    print(''' que mediante funciones, convierte una cantidad ingresada en pesos colombianos 
   a dólares americanos, euros y bitcoins.''') 
    dolar= 0.00027
    bitcoin= 5.5e-9
    euro = 0.00022
    valorCurrency = input('Ingresa el valor en pesos colombianos: ')
    if valorCurrency.isnumeric() :
        valorCurrency = int(valorCurrency)
        print("El valor de  ${} Pesos colombiandos en:".format(valorCurrency))
        print("Dolares es de {} USD".format(valorCurrency*dolar))
        print("Euros es de {} EUR".format(valorCurrency*euro))
        print("Bitcon es de {} XBT".format(valorCurrency*bitcoin))
    else:
        print('Los valores no son númericos')

def printOrder():
    print('que, mediante una función, organize de forma ascendente, tres valores numéricos ingresados por el usuario.')      
    numeros=[]    
    for i in range(0,3):
        num=input("Ingrese valor del numero {} : ".format(i+1))
        if num.isnumeric() :
            num = int(num)
            numeros.append(num)
        else:
            print('Los valores no son númericos')
    numeros.sort()
    for n in numeros:
        print(n)


        

def process(program):
    if program == 'a':
        printPairs()
    if program == 'b':
        printTriangular()
    if program == 'c':
        printCalls()
    if program == 'd':
        printConverter()
    if program == 'e':
        printOrder()
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