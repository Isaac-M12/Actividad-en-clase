class Persona:
    nombre        = str
    edad          = int
    centroEstudio = str
    def __init__(self,nombre,edad, centroEstudio):
        self.nombre        = nombre 
        self.edad          = edad
        self.centroEstudio = centroEstudio
        
    def conversar (self,otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}, y estudio en la  {self.centroEstudio} '  
    
if __name__== "__main__" :
    Persona1 = Persona("Isaac", 18, "ISTYAVIRAC")
    Persona2 = Persona("Vanessa", 18, "U.Central") 
    
    print(Persona1.conversar(Persona2))  
    