import sys

menu = '''
TALLER #3 - 
Integrantes
> Freddy Manuel Barrios Del rio
> Luis Guillermo Castro
Ejecutar programa
Desarrolle un programa gestionado por Menú en Python, que permita administrar una tupla de elementos,
a - Crear elemento 
b - Consultar de elementos 
c - Consulta longitud de elemento
d - Conaultar Maximo 
e - Consultar Minimo
f - Suma de elementos
g - Ordenacion de elemento
h - salir
'''
options = ['a', 'b', 'c', 'd', 'e', 'f','g','h']
tupla = []
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
        
def Crearelemento():
    element = input('Ingresa el valor a ingresar: ')
    if element.isnumeric() :    
        tupla.insert(0,int(element))
    else:
        print('Los valores no son númericos')
    
def printTupla():
    element = input('Ingresa el valor a buscar: ')
    if element.isnumeric() :
            try:    
                index=tupla.index(int(element))
                print("elemento encontrado en la posicion : {} con valor : {}".format(index,element))
            except ValueError:
                print('Elemento no encontrado')
        
    else:
        print('Los valores no son númericos')

print(tupla)

def consultarLogitud():
   print("La longitud de la tupa es: {} ".format(len(tupla)))
    
def consultarMaximo():
   print("El valor maximo es: {} ".format(max(tupla)))
    
def consultarMinimo():
    print("El valor minimo es: {} ".format(min(tupla)))

def sumaElementos():
    print("La suma de la tupla {} ".format(sum(tupla)))

def ordenarElementos():
    tupla2=tupla.copy()
    tupla2.sort()
    print("Tupla ordenada {} ".format(tupla2))
    


        

def process(program):
    if program == 'a':
        Crearelemento()
    if program == 'b':
        printTupla()
    if program == 'c':
        consultarLogitud()
    if program == 'd':
        consultarMaximo()
    if program == 'e':
        consultarMinimo()
    if program == 'f':
        sumaElementos()
    if program == 'g':
        ordenarElementos()    
    elif program == 'h':
        print('Good bye! ')
        global running
        running = False
while running:
    try:
        selectedProgram = main()
        if selectedProgram != 'h' and continueProgram():
            continue
        else:
            break
    except ValueError:
            print('Elemento no encontrado')  