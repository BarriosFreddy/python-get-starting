from Vehiculo import *
class VehiculoAereo(Vehiculo):       
    
    def __init__(self,placa,nroturbinas):
        Vehiculo.__init__(self,placa)
        nroturbinas = nroturbinas
        print("Soy un Vehiculo Aereo")
    
    def nroturbinas(self):
        return self.nroturbinas  
    
    def nroturbinas(self,nroturbinas):
        self.nroturbinas = nroturbinas
    
class Avion(VehiculoAereo):
    def __init__(self,placa,nroturbinas):
        VehiculoAereo.__init__(self,placa,nroturbinas)
        print ("Avion creado con placa: {} turbinas: {}".format(placa,nroturbinas))

class Helicoptero(VehiculoAereo):
    def __init__(self,placa,nroturbinas):
        VehiculoAereo.__init__(self,placa,nroturbinas)
        print ("Helicoptero creado con placa: {} turbinas: {}".format(placa,nroturbinas))

class Dron(VehiculoAereo):
    def __init__(self,placa,nroturbinas):
        VehiculoAereo.__init__(self,placa,nroturbinas)
        print ("Dron creado con placa: {} turbinas: {}".format(placa,nroturbinas))
    
    

