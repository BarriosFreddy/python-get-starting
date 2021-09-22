class Vehiculo:       
    
    def __init__(self,matricula):
        self.matricula = matricula
        self.describeme()

    
    def matricula(self):
        return self.matricula  
 

    
    def matricula(self,matricula):
        self.matricula = matricula

    
    def describeme(self):
        print("Soy un Vehiculo del tipo", type(self).__name__)

