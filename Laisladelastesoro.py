


print("Inicio")
print("Bienvenido a la isla. Tu misión será encontrar el tesoro.")
print("Camina al horizonte a buscar una pista")
print("Ves algo")
decision = input("¿Lo agarras?")
if(decision == "si"):
    print("Es un mapa")
    print("Lo revisas")
    print("Encuentras muchos acertijos, para llegar al tesoro debes desbloquear unos accesorios")
    print("Debes elegir un camino")
    camino = input("¿Derecha o izquierda?")
    if(camino == "izquierda"):
        print("Ves el mar")
        print("Caminas hacia el mar")
        print("Revisas el mapa")
        print("Entras al mar para desbloquear un puente que conecta dos montañas, las cuales son un atajajo")
        print("Ves a lo lejos una isla con una calavera")
        print("Volteas y ves un tubiron nodriza")
        Nadar = input ("¿Nadas hacia la isla?")
        if Nadar == ("si"):
            print("Te ataca una tribu - GAME OVER")
        else:
            print("Ves que el tiburon pasa de largo") 
            print("Desbloqueas el nivel confianza y ya tienes el puente")
            print("Sales del mar")
            print("revisas el mapa")
            print("Te dirijes hacia las montañas")
            print("Usas el puente para pasar")
            print("Bajas la montaña")
            print("Ves que se acerca un jaguar")
            elegir = input("¿Buscas un arma para defenderte?")
            if elegir == ("si"):
                print("Lo asustaste, te ataco - GAME OVER")
            else:
                print("Te acercas")
                print("Lo acaricias")
                print("Desbloqueas el nivel Cree en tì, Ganas un machete")
                print("revisas el mapa")
                print("Estas cerca del tesoro")
                print("Debes atravesar una siembra")
                print("Caminas hacia ella")
                print("Usas el machete para abrirte paso ")
                print("Ves una casa que tiene cuatro puertas")
                print("Escoge la puerta correcta para encontrar el tesoro puede ser Amarilla, verde, rojo o azul")
                puerta = input("¿Que puerta eliges?")
                if puerta == ("azul"):
                   print("Devorado por bestias - GAME OVER")
                if puerta == ("verde"):
                   print("Asfixiado por gas venenoso - GAME OVER")
                if puerta == ("amarilla"):
                   print("Haz conseguido el tesoro - CONGRATULATIONS")
                if puerta == ("rojo"):
                   print("Devorado por bestias - GAME OVER")

                





    else:
        print("Caiste en el agujero - GAME OVER")


else:
    print("Mueres por una trampa")







