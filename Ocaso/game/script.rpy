init python:
    # Esta es una sección de inicialización donde puedes definir música y otras variables globales.
    renpy.music.register_channel("background_music")

label start:
    play music "BellasLullaby.mp3" channel "background_music" loop

    call variables
    call scene1
    return

label variables:
    $ TeamJacobo = 0
    $ TeamEduardo = 0
    return



    


    
