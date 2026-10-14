# Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

person1 = Person("Bob", 28)
#print(person1.introduce()) # Output: My name is Bob and I am 28 years old

class Gato:
    def __init__(self, nombre, edad, raza, sexo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
    
    def maullar(self):
        return print(self.nombre, "está maullando")
    
    def presentarse(self):
        return print("Hola, soy  " , self.nombre, "y tengo" , self.edad , "años")

gato1 = Gato("Michi", 2, "Siames", "Macho")
gato1.maullar() # Output: Michi está maullando

#herencia
gato2 = Gato("Nina", 1, "Persa", "Hembra")
gato2.presentarse() # Output: Nina está maullando


#polimorfismo
class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

    def mePresento(self):
        print("Hola, soy: " , self.especie, ' de color ' , self.color, ' y tengo ' , self.edad, ' años')

    def cumplirAnios(self):
        self.edad += 1
        
a1 = Animal("Perro", 5, "Negro")
a2 = Animal("Gato", 3, "Blanco")

a1.mePresento()
a2.mePresento()

a1.cumplirAnios()
a2.cumplirAnios()

a1.mePresento()
a2.mePresento()


""" 
a- Abstracción

Es cuando separamos los datos de un objeto para luego generar un molde,
 (una clase), cuando creamos la clase gato, realizamos la abstracción de 
 sus atributos como son el nombre, edad , raza y sexo, como también en el método presentar, 
 luego, a partir de esta entidad llamada clase, pudimos crear objetos ya con características
  definidas en cada uno de estos atributos.

b- Encapsulamiento

Se utiliza cuando es necesario que ciertos métodos o propiedades sean inviolables
 o inalterables. Se refiere a la ocultación de los detalles internos de una clase 
 para proteger los datos y comportamientos de esa clase de accesos no autorizados o
  modificaciones accidentales.

El encapsulamiento es como un cofre con una cerradura. Los datos y comportamientos de
 una clase se almacenan dentro del "cofre" y solo se pueden acceder a ellos a través 
 de métodos públicos autorizados, como si tuvieras la "llave" para abrir el cofre. 
 Esto ayuda a prevenir la modificación accidental o no autorizada de los datos y comportamientos de la clase.

c- Herencia

Permite crear nuevas clases a partir de otras. Al tener la clase Gato, pudimos crear 
el objeto gato1, con los atributos que ya vimos, podemos crear gato2, que va también 
a tomar propiedades y métodos de la clase Gato. Esto nos da una jerarquía de padre e hijo.

d- Polimorfismo

Proviene de poli = muchas, morfismo = formas. Se utiliza para crear métodos con el
 mismo nombre pero con diferente comportamiento. 
 """