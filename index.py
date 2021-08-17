import sys
menu = '''
TALLER #1 - INICIANDO CON PYTHON
Ejecutar programa

a. que pregunte al usuario: Su nombre y luego lo salude
b. que solicite dos números y luego muestre el producto.
c. que calcule el perímetro y el área de un rectángulo dada su base y su altura.
d. que calcule el perímetro y el área de un circulo dado su radio.
e. que calcule el volumen de una esfera dado su radio.
f. que dado dos números, se muestre la suma, resta, división y multiplicación de ambos.
g. que dado un numero N, imprimir su factorial.
h. que permita convertir una cifra en pesos colombianos a dólares americanos, euros y bitcoins.
i. que calcule el Índice de Masa Corporal(IMC) a partir de los datos del peso y la estatura de una persona.
j. que dada una temperatura en grados Celsius, la convierta a grados Fahrenheit y Kelvin.
k. Salir

'''

options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
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
        
def greeting():
    print('que pregunte al usuario: Su nombre y luego lo salude')
    name = input('Cual es tu nombre?\n')
    print('Hola, ', name)

def multiplication():
    print('que solicite dos números y luego muestre el producto.')
    firstNumber = input('Ingresa el primer número(multiplicando): ')
    secondNumber = input('Ingresa el segundo número(multiplicador): ')
    if firstNumber.isnumeric() and secondNumber.isnumeric():
        result = int(firstNumber) * int(secondNumber)
        print('{} por {} es: {} '.format(firstNumber, secondNumber, result))
    else:
        print('Los valores no son númericos')

def calculateRectanglePerimeter():
    print('que calcule el perímetro y el área de un rectángulo dada su base y su altura.')
    length = input('Ingresa la altura: ')
    width = input('Ingresa el base: ')
    if length.isnumeric() and width.isnumeric():
        perimeter = 2 * (int(length) + int(width))
        print('Altura: {}, base: {}, el perímetro del rectangulo es: {:.2f} '.format(length, width, perimeter)) 
    else:
        print('Los valores no son númericos')

def calculateCirclePerimeter():
    print('que calcule el perímetro y el área de un circulo dado su radio.')
    ratio = input('Ingresa el radio del circulo: ')
    if ratio.isnumeric():
        result = numberPI * int(ratio) * 2 
        print('El perímetro del circulo con radio {} es: {:.2f} '.format(ratio, result))    
    else:
        print('Los valores no son númericos')

def calculateSphereVolume():
    print('que calcule el volumen de una esfera dado su radio.')
    ratio = input('Ingresa el radio del circulo: ')
    if ratio.isnumeric():
        result = (4/3) * numberPI * (int(ratio) ** 3)
        print('El volumen de la esfera con radio {} es: {:.2f} '.format(ratio, result)) 
    else:
        print('Los valores no son númericos')

def calculateBasicOperations():
    print('que dado dos números, se muestre la suma, resta, división y multiplicación de ambos.')
    firstNumber = input('Ingresa el primer número: ')
    secondNumber = input('Ingresa el segundo número: ')

    if firstNumber.isnumeric() and secondNumber.isnumeric():
        firstNumber = int(firstNumber)
        secondNumber = int(secondNumber)
        multiplication = firstNumber * secondNumber
        division = firstNumber / secondNumber
        addition = firstNumber + secondNumber
        substraction = firstNumber - secondNumber
        print('{} por {} es: {} '.format(firstNumber, secondNumber, multiplication))
        print('{} divido por {} es: {:.2f} '.format(firstNumber, secondNumber, division))
        print('{} más {} es: {} '.format(firstNumber, secondNumber, addition))
        print('{} menos {} es: {} '.format(firstNumber, secondNumber, substraction))
    else:
        print('Los valores no son númericos')

def calculateFactorial():
    print('que dado un numero N, imprimir su factorial.')
    number = input('Ingresa el número: ')
    if number.isnumeric():
        number = int(number)
        accumulator = 1
        for i in range(number):
            accumulator *= i + 1
        print('El factorial de {} es: {} '.format(number, accumulator))
    else:
        print('Los valores no son númericos')


def convertCoins():
    print('que permita convertir una cifra en pesos colombianos a dólares americanos, euros y bitcoins.')
    amount = input('Ingresa la cantidad a convertir: ')
    if amount.isnumeric():
        amount = float(amount)
        dollars = amount / 3845
        euros = amount / 4528
        bitcoins = amount / 178640917

        print('{} pesos colombianos son: {:.2f} en dolares '.format(amount, dollars))
        print('{} pesos colombianos son: {:.2f} en euros '.format(amount, euros))
        print('{} pesos colombianos son: {:.2f} en bitcoins '.format(amount, bitcoins))
    else:
        print('Los valores no son númericos')


def calculateIMC():
    print('que calcule el Índice de Masa Corporal(IMC) a partir de los datos del peso y la estatura de una persona.')
    weight = input('Ingresa tu peso en kilogramos: ')
    height = input('Ingresa tu altura en centimetros: ')
    if weight.isnumeric() and height.isnumeric():
        result = int(weight) / (int(height) / 100) ** 2
        print('Peso {}; Altura; {}, El indice de masa corporal es: {:.2f}'.format(weight, height,  result))
    else:
        print('Los valores no son númericos')


def convertTemperature():
    print('que dada una temperatura en grados Celsius, la convierta a grados Fahrenheit y Kelvin.')
    temperaturaCelsius = input('Ingresa la temperatura en celsius: ')
    if temperaturaCelsius.isnumeric():
        temperaturaCelsius = int(temperaturaCelsius)
        temperaturaFahrenheit = temperaturaCelsius * (9/5) + 32
        temperatureKevin = temperaturaCelsius + 273.15
        print('{} grados celsius son: {:.2f} farenheint '.format(temperaturaCelsius, temperaturaFahrenheit))
        print('{} grados celsius son: {:.2f} kelvin '.format(temperaturaCelsius, temperatureKevin))
    else:
        print('Los valores no son númericos')

def process(program):
    if program == 'a':
        greeting()
    elif program == 'b':
        multiplication()
    elif program == 'c':
        calculateRectanglePerimeter()
    elif program == 'd':
        calculateCirclePerimeter()
    elif program == 'e':
        calculateSphereVolume()
    elif program == 'f':
        calculateBasicOperations()
    elif program == 'g':
        calculateFactorial()
    elif program == 'h':
        convertCoins()
    elif program == 'i':
        calculateIMC()
    elif program == 'j':
        convertTemperature()
    elif program == 'k':
        print('Good bye! ')
        global running
        running = False

while running:
    try:
        selectedProgram = main()
        if selectedProgram is not 'k' and continueProgram():
            continue
        else:
            break
    except:
        print('Por favor, ingresa una opción válida')
        continue



