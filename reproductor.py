from pygame import mixer

mixer.init()
cancion=str(input("selecciona una cancion para empezar"))
mixer.music.load('acá_va_la_cancion.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("pulse p para parar la cancion")
    print("pulse r para reanudar la cancion")
    print("pulse e para elegir otra cancion")
    print("pulse s para salir")

    opcion = input(">>> ")

    if opcion=="p":
        mixer.music.pause()
    elif opcion=="r":
        mixer.music.unpause()
    elif opcion=="s":
        mixer.music.stop()
        break
    elif opcion=="e":
        mixer.music.stop()
        cancion=str(input("seleccione otra cancion para continuar"))
        mixer.music.load('acá_va_la_cancion.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play()
