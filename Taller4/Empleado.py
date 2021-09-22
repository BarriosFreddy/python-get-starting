class Empleado:       
    
    def __init__(self,identificacion="",tipo_identificacion="",cargo="",sueldo=0,email="",telefono="",empresa=""):
        self.identificacion = identificacion
        self.tipo_identificacion = tipo_identificacion
        self.cargo = cargo
        self.sueldo = sueldo
        self.email = email
        self.telefono = telefono
        self.empresa = empresa
    
    def identificacion(self):
        return self.identificacion
    
    def tipo_identificacion(self):
        return self.tipo_identificacion
    
    def cargo(self):
        return self.cargo
    
    def sueldo(self):
        return self.sueldo

    def email(self):
        return self.email
    
    def telefono(self):
        return self.telefono
    
    def empresa(self):
        return self.empresa
    
    def identificacion(self,identificacion):
        self.identificacion = identificacion
    
    def tipo_identificacion(self,tipo_identificacion):
        self.tipo_identificacion = tipo_identificacion

    def cargo(self,cargo):
        self.cargo = cargo
    
    def sueldo(self,sueldo):
        self.sueldo = sueldo
        
    def email(self,email):
        self.email = email

    def telefono(self,telefono):
        self.telefono = telefono

    def empresa(self,empresa):
        self.empresa = empresa
