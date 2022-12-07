class Persona:
    nombre        = str
    edad          = int
    CentroEstudio = str
    def __init__(self,nombre,edad, CentroEstudio):
        self.nombre        = nombre 
        self.edad          = edad
        self.CentroEstudio = CentroEstudio
        
    def conversar (self,otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre} tengo 18 años, estudio en el {self.CentroEstudio}'  
    
if __name__== "__main__" :
    Persona1 = Persona("Isaac", 18, "Instituto YAVIRAC y estoy en el segundo semestre de la carrera Desarrollo de Software")
    Persona2 = Persona("Vanessa", 18, "U.Central") 
    
    print(Persona1.conversar(Persona2))  
    