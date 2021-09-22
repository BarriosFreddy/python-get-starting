class Estudiante:       
    
    def __init__(self,identificacion="",tipo_identificacion="",nombres="",programa=0,semestre="",institucion=""):
        self.identificacion = identificacion
        self.tipo_identificacion = tipo_identificacion
        self.nombres = nombres
        self.programa = programa
        self.semestre = semestre
        self.institucion = institucion
    
    def identificacion(self):
        return self.identificacion
    
    def tipo_identificacion(self):
        return self.tipo_identificacion
    
    def nombres(self):
        return self.nombres
    
    def programa(self):
        return self.programa

    def semestre(self):
        return self.semestre
    
    def institucion(self):
        return self.institucion
    

    
    def identificacion(self,identificacion):
        self.identificacion = identificacion
    
    def tipo_identificacion(self,tipo_identificacion):
        self.tipo_identificacion = tipo_identificacion

    def nombres(self,nombres):
        self.nombres = nombres
    
    def programa(self,programa):
        self.programa = programa
        
    def semestre(self,semestre):
        self.semestre = semestre

    def institucion(self,institucion):
        self.institucion = institucion


