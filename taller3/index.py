menu = '''
TALLER #3: GESTION DE CADENAS Y LISTAS
Integrantes
> Sindy Paola Devoz Perez
> Freddy Manuel Barrios Del rio
> Luis Guillermo Castro
Ejecutar programa
a. que mediante una función, permita establecer el número de veces que aparece un carácter en una cadena de texto. Ambos valores, se deben ingresar por el usuario.
b. que cuente cuantas veces aparecen cada una de las vocales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula.
c. que implemente las siguientes funciones en Python:
    a.  Imprima los dos primeros caracteres
    b.  Imprima los tres primeros caracteres
    c.  Imprima la cadena cada dos caracteres
    d.  Imprima la cadena en sentido inverso
d. que dada una lista de datos numéricos con duplicados ingresados por el usuario, permita generar dos listas nuevas: una con los elementos duplicados y otra con los elementos únicos.
e. que dado un numero ingresado por el usuario, se solicite N entradas correspondientes a cadenas de texto. Posteriormente solicite una cadena, la busque en la lista, e indique cuantas veces aparece en la misma.
f. que dada una lista de números ingresados por el usuario, permita realizar las funciones de suma, producto, mayor y menor valor.
g. que permita generar una lista de N cadenas, posteriormente solicite un carácter, que se deberá insertar antes de cada una de las cadenas de la lista original. El resultado debe imprimir ambas listas.
h. que permita mediante funciones, generar la listas de los N números de Fibonacci, los N números primos.
i. que dada una lista de N elementos numéricos, ingresados por el usuario, genere una nueva lista de N elementos, donde cada elemento de esta segunda lista, sea el resultado de tomar cada elemento de la primera lista y sumarle 1(n+1). Ejemplo:  primera lista : [0,1,2,3,4,5]. Segunda lista: [1, 0, 3, 2, 5, 4]
j. que dado dos listas de N y M elementos, permita reemplazar el ultimo elemento de la primera lista, con la segunda lista…ejemplo:
    Primera Lista: [1, 3, 5, 7, 9, 10] . Segunda Lista: [2, 4, 6, 8] .
    Lista solicitada: [1, 3, 5, 7, 9, 2, 4, 6, 8]
k. Salir
'''
options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

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
        

def calculateCharacters():
    texto = input("Ingrese la cadena de texto")
    char = input("Ingrese el caracter a buscar")
    count = texto.count(char)
    print("El caracter -{}- aparece en el texto -{}-, {} veces".format(char, texto, count))
    
def countVowels():
    texto = input("Ingrese la cadena de texto")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for vowel in vowels:
        count = texto.count(vowel)
        print("La vocal -{}- aparece en el texto {} veces".format(vowel, count))

def multiFuncitons():
    texto = input("Ingrese la cadena de texto")
    vowels = ('a', 'e', 'i', 'o', 'u')
    firstTwoChars = texto[:2]
    firstThreeChars = texto[:3]
    eachTwoChars = texto[::2]
    stringInverse = texto[::-1]
    print("Primeros dos caracteres son: {}".format(firstTwoChars))
    print("Primeros tres caracteres son: {}".format(firstThreeChars))
    print("Cadena de texto impresa cada dos caracteres: {}".format(eachTwoChars))
    print("Cadena de texto impresa de manera inversa: {}".format(stringInverse))

def findDuplicatedOnes():
    numItems = input('Ingrese el numero de items a añadir')
    list = []
    uniquesList = []
    duplicatedList = []
    if numItems.isnumeric():
        numItems = int(numItems)
        for i in range(0, numItems):
            item = input("Ingrese el numero de la posicion {}".format(i+1))
            list.append(item)
    
        for item in list:
            try:
                uniquesList.index(item)
                duplicatedList.append(item)
            except:
                uniquesList.append(item)
        print("Items unicos {}".format(uniquesList))
        print("Items duplicados {}".format(duplicatedList))
        
    else:
        print('El numero de items no es un valor numerico')

def findSubstring():
    numItems = input('Ingrese el numero de cadena de textos a añadir')
    list = []
    counter = 0
    if numItems.isnumeric():
        numItems = int(numItems)
        for i in range(0, numItems):
            item = input("Ingrese la cadena de texto # {}".format(i+1))
            list.append(item)
        stringToFind = input('Ingrese la cadena de texto a buscar')
        for stringItem in list:
            try:
                stringItem.index(stringToFind)
                counter += 1
            except:
                pass
        print("La cadena de texto -{}- se encuenta {} veces en la lista ingresada".format(stringToFind, counter))
    else:
        print('El numero de items no es un valor numerico')

def operations():
    numItems = input('Ingrese el numero de items de la lista')
    list = []
    counter = 0
    addition = 0
    multiplication = 1
    isValidList = True
    if numItems.isnumeric():
        numItems = int(numItems)
        for i in range(0, numItems):
            number = input("Ingrese el valor numerico")
            list.append(number)

        for number in list:
            if number.isnumeric() is not True:
                isValidList = False

        if isValidList is False:
            print('Al menos un valor ingresado no es numerico')
        else:
            tempList = []
            for number in list:
                number = int(number)
                addition += number
                multiplication *= number
                tempList.append(number)
            
            numberMin = min(tempList)
            numberMax = max(tempList)
            print("La suma de los numeros es {}".format(addition))
            print("La multiplicacion de los numeros es {}".format(multiplication))
            print("El numero minimo es {}".format(numberMin))
            print("El numero maximo es {}".format(numberMax))

    else:
        print('El numero de items no es un valor numerico')


def listPrefix():
    numItems = input('Ingrese el numero de cadenas de la lista')
    list = []
    listWithPrefix = []
    if numItems.isnumeric():
        numItems = int(numItems)
        for i in range(0, numItems):
            string = input("Ingrese la cadena de texto #{}".format(i+1))
            list.append(string)

        prefix = input('Ingrese la cadena de texto que va como prefijo')
        for string in list:
            listWithPrefix.append("{}{}".format(prefix, string))
        print(list)
        print(listWithPrefix) 
    else:
        print('El numero de items no es un valor numerico')



def process(program):
    if program == 'a':
        calculateCharacters()
    if program == 'b':
        countVowels()
    if program == 'c':
        multiFuncitons()
    if program == 'd':
        findDuplicatedOnes()
    if program == 'e':
        findSubstring()
    if program == 'f':
        operations()
    if program == 'g':
        listPrefix()
    if program == 'h':
        pass
    if program == 'i':
        pass
    if program == 'j':
        pass
    elif program == 'k':
        print('Good bye! ')
        global running
        running = False
while running:
        selectedProgram = main()
        if selectedProgram != 'f' and continueProgram():
            continue
        else:
            break