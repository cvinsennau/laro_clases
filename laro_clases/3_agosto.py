#Encapsulamiento (propiedades)
    # 1. Public (se puede acceder FUERA de la clase) 
    # 2. Protected (se puede acceder DENTRO de la clase y las clases hijas) 
    # 3. Private (se accede unicamente DENTRO de la clase que la definiste). Suelen usar getter y setter para cambiar diferentes variables PRIVADAS

#Getter / Setter
#Decorators


def decorator(hello):
    def before_hello():
        print("Ehhh gato")
        hello()
    return before_hello

@decorator #Agrega la funcion antes de una funcion
def hello():
    print("Hello")
    
hello()




class Person:
    def __init__(self, name=None, surname = None):
        self.name = name
        self.surname = surname

    def hello(self):
        print ("Hola!") 
    
    @property #hace tu funcion un getter
    def fullname(self):
        return self.name + " " + self.surname

    @fullname.setter #nombre de la variable + setter
    def fullname(self, new_name):
        self.name, self.surname = new_name.split()

    
person = Person("Cande", "Vinsennau")
print(person.fullname) 

person.fullname = "Mirta Lorenzi"
print(person.fullname)