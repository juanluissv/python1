#herencia
class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color
        
    def hablar(self):
        #metodo vacio
        pass

    def moverse(self):
        pass

    def describeme(self):
        print('soy un animal del tipo: ' , type(self).__name__)

#perro hereda de animal
class Perro(Animal):
    pass

mi_perro = Perro("Firulais", 5, "Blanco")
mi_perro.describeme()

class Perro(Animal):
    def hablar(self):
        print("Guau")

    def moverse(self):
        print("El perro camina sobre sus patas")

class Vaca(Animal):
    def hablar(self):
        print("Muu")
    
    def moverse(self):
        print("La vaca camina sobre sus patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz")
    def moverse(self):
        print("La abeja vuela en el aire")
    
    #nuevo metodo 
    def picar(self):
        print("La abeja picó a un humano")

mi_perro = Perro("Firulais", 5, "Blanco")
mi_vaca = Vaca("Lola", 3, "Blanca")
mi_abeja = Abeja("Berta", 1, "Negra")

mi_perro.hablar()
mi_vaca.hablar()
mi_abeja.hablar()

mi_abeja.describeme()
mi_abeja.picar()


#super
class Perro(Animal):
    def __init__(self, especie, edad, color, dueño):
        super().__init__(especie, edad, color)
        self.dueño = dueño

nuevo_perro = Perro("Firulais", 5, "Blanco", "Juan")
print(nuevo_perro.dueño)