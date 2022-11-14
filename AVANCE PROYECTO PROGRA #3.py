listaId = list()

#Opcion agregar jugadores (submenu)
def agregarJugadores (agregarJugadores):
    idJugadores = str(input ("Por favor ingrese el Id del jugador: "))
    listaId.append(idJugadores)
    while True:
        print ("Recuerde que el ID de cada jugador debe ser diferente!")
        print ("")
        agregarDenuevo = int( input(" Si desea agregar otro ID de jugador por favor ingrese uno:  \n" "En caso de no quererlo por favor ingrese cero: \n"))
        if agregarDenuevo == 1:
            idJugadores = str(input ("Por favor ingrese el ID del jugador: "))
            listaId.append(idJugadores)
        elif agregarDenuevo == 0:
            print("Se guardaron los ID")
            break
    print("--------------------------------------------------------------------------------------------")

#Opcion enlistar jugadores (submenu)
def enlistarJug (enlistarJug):
    indice = 0
    while indice < len(listaId):
         print(listaId[indice])
         indice += 1
         print("--------------------------------------------------------------------------------------------")

#Opcion eliminar jugadores (submenu)
def eliminarJug (eliminarJug):
    print ("Lista de Jugadores \n")
    indice = 0
    while indice < len(listaId):
         print(listaId[indice])
         indice += 1                  

    idElim = str( input ("Ingrese el ID a eliminar: "))
    listaId.remove(idElim)
    print (" ID del jugador  {} ha sido eliminado" .format (idElim))
    print("-----------------------------------------------------------------------------------------")
    for jugadores in listaId:
        print (jugadores)
        print("--------------------------------------------------------------------------------------------")    
         
    
def submenu (submenu):
    #Submenu - agregarjugadores
        print ("[1] Agregar nuevo jugador")
        print ("[2] Eliminar Jugador")
        print ("[3] Enlistar jugadores activos")
        print ("[4] Volver al menu principal")
        opcion = int (input ("Digite una opcion: ") )
        print("--------------------------------------------------------------------------------------------")

        if opcion == 1:
            agregarJugadores (agregarJugadores)
        elif opcion == 2:
            eliminarJug (eliminarJug)
            
        elif opcion == 3:
            enlistarJug (enlistarJug)
        elif opcion == 4:
             longitudLista = len(listaId)
             if longitudLista < 2:
                print("No hay suficientes jugadores registrados")
                print("--------------------------------------------------------------------------------------------")
             elif longitudLista  >= 2:
                 return submenu(submenu)
           
        else:
            print("Por favor ingrese una opcion valida")
    
         
print("***************************")

def verificarJug (verificarJug):
    #Verificamos que hayan los jugadores necesarios para jugar
    longitudList = len(listaId)
    if longitudList < 2:
        print ("No hay suficientes jugadores registrados")
        return submenu(submenu)
    elif longitudList >=2:
       elegirJug(elegirJug)

def elegirJug (elegirJug):
    #En esta funcion enlistamos los jugadores y proponemos al usuario que elija los que desea usar
    for jugadores in range(len(listaId)):
            print  (jugadores , "-" , listaId [jugadores])
    elegirJug = int ( input ( "Por favor la posicion del ID del jugador del jugador 1: "))
    jugEleg1= print (listaId[elegirJug])
    print ( " Desea ser X (equis) o O (circulo)?")
    simboloElec = str ( input (" Por favor ingrese el simbolo a elegir: "))
    if simboloElec == "X":
        simbolo = "X"
    elif simboloElec == "O":
        simbolo = "O"
    for jugadores in range(len(listaId)):
            print ("Posicion: " , jugadores)
            print("Valor: " , listaId [jugadores])
    elegirJug = int ( input ( "Por favor la posicion del ID del jugador del jugador 2: "))
    jugEleg2 = print (listaId[elegirJug])
    if elegirJug(" ") not in range(len(listaId)):
        print("Por favor ingrese un valor correcto")
        return verificarJug(verificarJug)
    print('')
    print (" Reglas basicas del Juego Gato")
    print ("----------------------------------------------------")
    print ("-El jugador coloca su figura en la casilla de su eleccion")
    print (" -No se puede cambiar la figura de casilla una vez puesta")
    print (" -Gana el jugador que logre ingresar tres figuras en una misma linea (vertical, horizontal o diagonal)")

    

    

def submenuGato(submenuGato):
    print("Bienvenido al Juego Gato")
    print("-------------------------------------------------------")
    print("")
    verificarJug(verificarJug)
    
        
            
        
        
    
    


    
    

           

    
while True:
     #Menu principal antes del juego
    print ("[1] Agregar nuevos jugadores")
    print ("[2] Juego Gato")
    print ("[3] Juego Ahorcado")
    print ("[4] Quiniela mundialista")
    print ("[5] Salir del juego")

    opcion = int (input ("Digite una opcion: ") )
    print("--------------------------------------------------------------------------------------------")

    if opcion == 1:
        submenu (submenu)

    elif opcion == 2:
        submenuGato (submenuGato)

    elif opcion == 3:
        juegoAhorcado (ahorcado)

    elif opcion == 4:
        quinielaMundialista (mundial)
        

    elif opcion == 5:
        print ("Muchas gracias por preferirnos como su medio de entretenimiento")
        break

    else:
        print ("Por favor ingresar una opcion correcta: ")

        
  






    

    
