#3 vs 3
#2 equipos
# Opciones de este programa son: 
#   1. Agregar jugador
#        A que equipo {"Equipo 1" o "Equipo 2"}
#   2. Borrar jugador
#       A que equipo {"Equipo 1" o "Equipo 2"}

#Restricciones:
#   1. Solo se permite un arquero por equipo
#   2. Maximo 3 jugadores por equipo


players = {
    'cande': {"nombre": "cande", "posicion": "Arquero"},
    'juan': {"nombre": "juan", "posicion": "Defensor"},
    'laro': {"nombre": "laro", "posicion": "Delantero"},
    'mirta': {"nombre": "mirta", "posicion": "Defensor"},
    'sofi': {"nombre": "sofi", "posicion": "Arquero"},
    'cati': {"nombre": "cati", "posicion": "Delantero"},
    'nico': {"nombre": "nico", "posicion": "Delantero"},
    'juli': {"nombre": "juli", "posicion": "Defensor"},
    'licha': {"nombre": "licha", "posicion": "Defensor"},
    'ivan': {"nombre": "ivan", "posicion": "Arquero"}
} 

print(players.keys())

#1) Definir los dos equipos
#2) Armar menu
#3) Funcion para agregar jugadores
#4) Funcion para borrar jugadores

river = dict()
velez = dict()

menu = input("Elegir opción:\n 1 - Agregar jugador\n 2 - Quitar jugador \n 3 - Mostrar equipos \n 4- Jugar! \n\n Opción elegida: ")

def addPlayer(teamId, playerName):
    if playerName in players.keys():
        if teamId == 1:
            river[playerName] = players[playerName]
        else:
            velez[playerName] = players[playerName]
    else:
        print("Ups! Este usuario ya fue seleccionado. Elegi otro")
    return
   
def removePlayer(teamId, playerName):
    if playerName in players.keys():
        if teamId == 1:
            river.pop(playerName,None)
        else:
            river.pop(playerName,None)
    else:
        print("Ups! Este usuario ya fue eliminado. Elegi otro") 
    

while True:
    match(menu):
        case "1":
            selectTeam = int(input("Seleccionar equipo: \n\n 1- River \n 2- Velez \n\n Opción elegida: "))
            selectPlayer = input('Nombre del jugador: ' + str(players.keys()) + "\n")
            addPlayer(selectTeam,selectPlayer)
            
        
        case "2":
            
            selectTeam = int(input("Seleccionar equipo: \n\n 1- River \n 2- Velez \n\n Opción elegida: "))
            selectPlayer = input('Nombre del jugador: ' + str(players.keys()) + "\n")
            removePlayer(selectTeam,selectPlayer)
            
        case "3":
            print(river)
            print(velez)
            break



diccionario = dict()
# ​
# # Devuelve el numero de elementos que tiene el diccionario
# len(dict)
# ​
# # Compara el número de elementos distintos que tienen los dos 
# cmp (dict1,dict2)
# ​
# # Devuelve una lista con las claves del diccionario
# dict.keys()
# ​
# # Devuelve una lista con los valores del diccionario
# dict.values()
# ​
# # Devuelve el valor del elemento con clave key. Sino devuelve default
# dict.get(key, default=None)
# ​
# # Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
# dict.setdefault(key, default=None)
# ​
# # Insertamos un elemento en el diccionario con su clave:valor
# dict['key'] = 'value'
# ​
# # Eliminamos el elemento del diccionario con clave key
# dict.pop('key',None)
# ​
# # Devuleve la copia de un diccionario dict2 = dict.copy()
# dict.copy()
# ​
# # Elimina todos los elementos de un diccionario
# dict.clear()
# ​
# # Crea un nuevo diccionario poniendo como claves las que hay en la lista y los valores por defecto si se les pasa
# dict.fromkeys(list, defaultValue)
# ​
# # Devuelve true si existe la clave. Sino devuelve false
# dict.has_key(key)
# ​
# # devuelve un lista de tuplas formadas por los pares clave:valor
# dict.items()
# ​
# # Añade los elementos de un diccionario a otro
# dict.update(dict2)
#   '''


#1) Definir los dos equipos
#2) Armar menu
#3) Funcion para agregar jugadores
#4) Funcion para borrar jugadores

class Team:
    def __init__(self, team):
        self.team = team
    
    def show(self):
        print(f"{self.team}")


class Player(Team):
    def __init__(self, team, name, position):
        super().__init__(team, name, position)
        self.name = name
        self.position = position

while True:
    match(menu):
        case "1":
            selectTeam = int(input("Seleccionar equipo: \n\n 1- River \n 2- Velez \n\n Opción elegida: "))
            selectPlayer = input('Nombre del jugador: ' + str(players.keys()) + "\n")
            addPlayer(selectTeam,selectPlayer)
            
            
        case "2":
            
            selectTeam = int(input("Seleccionar equipo: \n\n 1- River \n 2- Velez \n\n Opción elegida: "))
            selectPlayer = input('Nombre del jugador: ' + str(players.keys()) + "\n")
            removePlayer(selectTeam,selectPlayer)
            
        case "3":
            print(river)
            print(velez)
            break
