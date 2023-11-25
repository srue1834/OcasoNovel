label eduardoLine:
    scene forest2 with fade
    "Siguiendo tus instintos, curiosidad y falta de sentido común, finalmente alcanzas a Eduardo"
    show isa_bite with moveinbottom 
    "La luz se filtra entre los árboles, proyectando un brillo etéreo."
    hide isa_bite with fade
    show angry_e with moveinbottom
    "Eduardo te voltea a ver, su expresión es una mezcla de frustración y resignación."
    eduardo "¿Por qué me sigues, Isabella? ¿No te das cuenta de lo peligroso que soy?"

    "Se acerca a un rayo de sol y su piel brilla de forma poco natural." 
    hide angry_e with moveoutbottom
    show shinny_e with moveinbottom 
    "Desconcertada por la visión surrealista, sabes que tiene que decir algo." 
    "Todas las señales son claras, ha estado en el mismo grado por 10 años, su apariencia no ha cambiado, tiene ojos raros y su piel es demasiado pálida."

    menu:
        "Aceptarlo":
            isabella "Sé lo que eres."
            eduardo "Dilo, en voz alta. ¡Dilo!"
            jump vampiro


label vampiro:
    menu:
        "Vampiro":
            $ TeamEduardo += 1
            
            isabella "Un vampiro. Y, sinceramente, eso es genial. ¿Brillas todo el tiempo o sólo bajo la luz del sol?"
            eduardo "Sí, soy un vampiro. Y esta ..." 
            eduardo "... esta es la piel de un asesino"
            jump secondChance

        "Hmmm no no nop corre":
            isabella "¿Sabes qué? Esto es demasiado extraño para mí. No me gusta salir con criaturas míticas potencialmente peligrosas. Debería irme"
            eduardo "Entiendo. Probablemente sea lo mejor. Ten cuidado, Isabella"

        "Anemia":
            isabella "Tienes anemia. No juzgo, yo también."
            show ferridoce at right with moveinbottom
            isabella "De hecho, ten. Esto te servirá más a ti que a mí"
            eduardo "No, Isabella, no soy anímico. Soy un vampiro. Y esta ..."
            hide ferridoce with moveoutbottom
            eduardo "... esta es la piel de un asesino"

            jump secondChance

label secondChance:
    menu:
        "Aceptar que es un vampiro, tu puedes arreglarlo <3":
            $ TeamEduardo += 1
            isabella "Aaa okay, esto puede funcionar para mí."
            hide shinny_e with moveoutbottom
            # ed carga a bella
            show running with moveinright
            "Eduardo te carga y pasan por el bosque de una manera como nunca habías experimentado."
            "Estás aterrada y a la vez emocionada de ver qué más puede hacer tu novio vampiro."

            jump eduardoEnding
            
        "Última oportunidad, tienes que irte":
            isabella "¿Sabes qué? Esto es demasiado extraño para mí. No me gusta salir con criaturas míticas potencialmente peligrosas. Debería irme"
            eduardo "Entiendo. Probablemente sea lo mejor. Ten cuidado, Isabella"

            "Al darte cuenta del peligro potencial y lo absurdo de la situación, decides alejarte."
            show house with fade
            "Regresas a la seguridad de tu casa, con tu mente echando punta con las extrañas revelaciones del día."
            jump finalChoice


label eduardoEnding:
    "A medida que profundizas tu relación con Eduardo, tu vida se convierte en una absurda telenovela." 
    "De esas que tienen 50 efectos de sonidos por cada escena, varias tomas en cámara lenta y editada con los ojos cerrados."  
    scene wedding_venue with fade
    show married with moveinbottom
    "Después de mucho involucrando vampiros locos y hombres lobo, finalmente, Eduardo y tú se casan y tienen una hermosa boda." 
    hide married with moveoutbottom
    "Poco después de su luna de miel, y sí literalmente como 3 días desde su luna de miel, quedaste embarazada de un bebé medio vampiro que te está comiendo por dentro."
    scene forest3 with fade
    show pregnant at right with moveinbottom
    "Después de 2 semanas embarazada, el bebe demonio decide destruirte y salir a aterrorizar a todo quien lo vea."
    show demon with moveinleft
    "Eduardo no puede vivir sin ti y decide convertirte en vampiro."
    hide pregnant with moveoutbottom
    show vampire at right with moveinbottom
    "Después de ver al engendro del mal que pariste reconsideras tus decisiones pero ya no hay vuelta atrás y no tienes más opción que vivir como un monstruo chupa sangre."
    "Porque tu y Eduardo son malos padres, deciden nombrar al bebé Renesme, una combinación entre Renata, tu mamá, y Esmeralda, la mamá de Eduardo."
    
    "Ah, y Jacobo se imprimo sobre ella."
    "Así es, tal cual como leíste."
    
    "Al final, contemplas tu inmortalidad, llena de vampiros brillantes, hombres lobo con amores no correspondidos y esa cosa que llamas hija."
    "Felicidades por completar el juego, y bienvenid@ a #TeamEduardo ¡Buen trabajo!"

    return

label finalChoice:
    show isa_basic with moveinbottom
    isabella "¡Wow! Vaya que día, por fin en casa."
    
    if TeamJacobo == 1:
        "Parece que has mostrado un interés especial en Jacobo. ¿Quieres seguir explorando esta posibilidad?"
        menu:
            "Sí, quiero ver dónde lleva esto con Jacobo":
                jump jacoboLine
            "Hmmm paso, ya me cansé":
                "En un giro del destino, decides que una vida llena de vampiros brillantes y hombres lobo enamorados no es lo quieres. Haces tus maletas y te despides de Dorks."
                "Felicidades por completar el juego, y bienvenid@ a #TeamSentidoComún ¡Buen trabajo!"
                return

    else:
        "En un giro del destino, decides que una vida llena de vampiros brillantes y hombres lobo enamorados no es lo quieres. Haces tus maletas y te despides de Dorks."
        isabella "Sabes, tal vez ser 'no como otras chicas' no se trata de salir con criaturas sobrenaturales."
        isabella "Tal vez se trata de elegir una vida que no implique ser parte de un monstruoso y muy tóxico triángulo amoroso."
        
        "Felicidades por completar el juego, y bienvenid@ a #TeamSentidoComún ¡Buen trabajo!"
        return