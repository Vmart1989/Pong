from pantallas import Partida, Menu


menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == 'jugar':
    juego = Partida()
    juego.bucle_fotograma()

#TAREA CREAR OTRA VENTANA QUE DIGA GANADOR Y EL MARCADOR