from Vehiculo import *
class VehiculoTerrestre(Vehiculo):       
    
    def __init__(self,placa,nrollantas):
        Vehiculo.__init__(self,placa)
        nrollantas = nrollantas
        print("Soy un Vehiculo terrestre")
        
    
    def nrollantas(self):
        return self.nrollantas  
    
    def nrollantas(self,nrollantas):
        self.nrollantas = nrollantas
    
class Auto(VehiculoTerrestre):
    def __init__(self,placa,nrollantas):
        VehiculoTerrestre.__init__(self,placa,nrollantas)
        print ("Auto creado con placa: {} llantas: {}".format(placa,nrollantas))
        

class Motocicleta(VehiculoTerrestre):
    def __init__(self,placa,nrollantas):
        VehiculoTerrestre.__init__(self,placa,nrollantas)
        print ("Motocicleta creado con placa: {} llantas: {}".format(placa,nrollantas))
      
        

class Bicicleta(VehiculoTerrestre):
    def __init__(self,placa,nrollantas):
        VehiculoTerrestre.__init__(self,placa,nrollantas)
        print ("Bicicleta creada con placa: {} llantas: {}".format(placa,nrollantas))
        

