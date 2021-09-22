import sys
from Empleado import *
from Estudiante import *
from VehiculoAereo import *
from VehiculoTerrestre import *
menu = '''
TALLER #4 - POO EN PYTHON
Integrantes
> Sindy Paola Devoz Perez
> Freddy Manuel Barrios Del rio
> Luis Guillermo Castro
Ejecutar programa

================================================================
1. Implemente la clase Empleado, con los atributos de identificacion, tipo de identificacion, cargo, sueldo, email, telefono, 
   empresa y los respectivos metodos get/set para cada atributo. Construya la Clase Principal que haga uso de la Clase Empleado.

2. Implemente la clase Estudiante, con los atributos de identificacion, tipo de identificacion, nombres, programa academico, 
   semestre, institucion y los respectivos metodos get/set para cada atributo. Construya la Clase Principal que haga uso de la Clase Estudiante

3. Implemente mediante el uso de herencia, la Clase Vehiculo(padre) y las subclases Vehiculo Terrestre, Vehiculo Aereo. 
    De la subclase Vehiculo Aereo heredan las clases Avion, Helicoptero, Dron. 
    De la Clase Vehiculo Terrestre heredan las Clases Auto, Motocicleta y Bicicleta.

4. Salir
================================================================

'''
options = ['1', '2', '3','4']
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
        
def mostrarEmpleado():
    print("================================================================")
    print("Creando Empleado")
    emple = Empleado("1143354429","CC","Desarrollador",300000,"jose@gmial.com","311245879","SoftProgramer")
    print("El empleado es Identififacion: {} tipo: {}  cargo: {} sueldo: {} Email: {} Telefono: {} Empresa: {}"
    .format(emple.identificacion,emple.tipo_identificacion,emple.cargo,emple.sueldo,emple.email,emple.telefono,emple.empresa))
    print("Modificando el Empleado")
    emple.sueldo=5000000
    emple.empresa="Desarrollo LTDA"
    print("El empleado es Identififacion: {} tipo: {}  cargo: {} sueldo: {} Email: {} Telefono: {} Empresa: {}"
    .format(emple.identificacion,emple.tipo_identificacion,emple.cargo,emple.sueldo,emple.email,emple.telefono,emple.empresa))
    print("================================================================")
    
def mostrarEstudiante():
    print("================================================================")
    print("Creando Estudiante")
    estu = Estudiante("1143354429","CC","JOSE MAURICIO","INGENIERIA DE SISTEMAS","VIII","SINU")
    print("El estudiante es ---> Identififacion: {} tipo: {} nombre: {} Programa: {} semestre: {} institucion: {} "
    .format(estu.identificacion,estu.tipo_identificacion,estu.nombres,estu.programa,estu.semestre,estu.institucion))
    print("Modificando el Estudiante")
    estu.semestre="X"
    estu.institucion="Tecnologico Comfenalco"
    print("El estudiante es ---> Identififacion: {} tipo: {} nombre: {} Programa: {} semestre: {} institucion: {} "
    .format(estu.identificacion,estu.tipo_identificacion,estu.nombres,estu.programa,estu.semestre,estu.institucion))
    print("================================================================")

def mostrarHerencia():   
   print("Creando AUTO")
   print("================================================================")  
   vehic= Auto("PLC",6)   
   print("================================================================")
   print("Creando MOTO")
   print("================================================================")  
   vehic= Motocicleta("CMP-54F",2)
   print("================================================================")
   print("Creando BICILETA")
   print("================================================================")  
   vehic= Bicicleta("RR-34T",2)
   print("================================================================")
   print("Creando AVION")
   print("================================================================")  
   vehic= Avion("XA-WEC",8)   
   print("================================================================")
   print("Creando HELICOPTERO")
   print("================================================================")  
   vehic= Motocicleta("XC-RSD",5)
   print("================================================================")
   print("Creando DRON")
   print("================================================================")  
   vehic= Dron("DR-3T",1)
   print("================================================================")
        

def process(program):
    if program == '1':
        mostrarEmpleado()
    if program == '2':
        mostrarEstudiante()
    if program == '3':
        mostrarHerencia()
    elif program == '4':
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