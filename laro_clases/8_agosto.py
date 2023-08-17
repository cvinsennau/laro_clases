# Parte 1
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular #privada = No se puede editar
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular #para que no loopee
    
    @property
    def cantidad(self):
        return self.__cantidad
        
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:" + self.cantidad
    
    def ingresar(self, cantidad):
        if cantidad < 0:
            print("Hubo un error en la transacción")
        else:
            self.__cantidad += cantidad
            print(f"Hay ${self.cantidad} en tu cuenta")
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        print(f"Hay ${self.cantidad} en tu cuenta")
        


cuenta = Cuenta("Cande Vinsennau", 20.1)
print(cuenta.mostrar()) 

cuenta.ingresar(200)
print(cuenta.mostrar())

# Parte 2
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.

class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0, bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
