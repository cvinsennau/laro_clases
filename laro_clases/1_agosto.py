#Clase (Class)
#A class is considered as a blueprint of objects. We can think of the class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House is the object. Since many houses can be made from the same description, we can create many objects from a class.

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        
    def study(self):
        print("... estudiando")
    
    def hello(self):
        print (f"Hola! Soy {self.name}") 
    
class Profession(Student):
    def __init__(self, name, age, city, profession):
        super().__init__(name, age, city)
        self.profession = profession
        
    def hello(self):
        print (f"Hola! Soy {self.name} + y soy {self.profession}") 
    # En general, cuando importamos frameworks, no podemos modificar la clase "PADRE". Entonces, pisamos el metodo en la clase "HIJO".


juan = Student("Juan",30,"NY")

print(juan)
# <__main__.Student object at 0x000002C10466E890>
# Representación del objeto de la clase Student y la dirección de memoria donde se encuentra almacenado ese objeto.

juan.study()
juan.hello()


# Ejercicio 1
# Crea la clase Coche que contenga las siguientes propiedades:
# matrícula (string)
# marca (string)
# kilometros_recorridos (float)
# gasolina (float)
# La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. 
# El método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0'1. 
# La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable gasolina. Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario repostar para recorrer la cantidad indicada de kilómetros".
# Ejemplo:
# avanzar(50) # gasolina = 50
# avanzar(100) # kilometros_recorridos = 100, gasolina = 40
# avanzar(40) # kilometros_recorridos = 140, gasolina = 36
# avanzar(180) # kilometros_recorridos = 320, gasolina = 18

class Coche:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina): #propiedades
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina
        
    def avanzar(self, kilometros_restantes):
        
        consumo = self.gasolina - (kilometros_restantes * 0.1)
        
        if consumo <=0:
            print("Es necesario repostar para recorrer la cantidad indicada de kilómetros")
        else:
            self.kilometros_recorridos += kilometros_restantes
            self.gasolina -= (kilometros_restantes * 0.1)
            print(f"Quedan {self.gasolina}km de nafta")
            
    def repostar(self, litros):
        self.gasolina += litros    
            
    

auto = Coche("ABC123", "BMW", 0, 100)

auto.avanzar(1000)


