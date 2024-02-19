class Animal:
    def __init__(self,nombre,raza): 
        self.nombre = nombre
        self.raza = raza
    def pasear(self):
        pass
    def alimentar(self):
        pass
    def dar_info(self):
        return self.nombre + " de raza: " + self.raza
class Gato(Animal):
    def pasear(self):
        print("Paseando al gato " + self.dar_info())
    def alimentar(self):
        print("Alimentando al gato " + self.dar_info())

class Lagarto(Animal):
    def pasear(self):
        print("Paseando al lagarto "+ self.dar_info())
    def alimentar(self):
        print("Alimentando al lagarto "+ self.dar_info())

class Perro(Animal):
    def pasear(self):
        print("Paseando al perro " + self.dar_info())
    
    def alimentar(self):
        print("Alimentando al perro " + self.dar_info())

if __name__ =='__main__':
    mascotas=[Perro("neron","buldog"), Gato("fifi","naranja"),Lagarto("Rayo mcqueen","verde")]
    
    for m in mascotas:
        m.pasear()
        m.alimentar()
        
#super()