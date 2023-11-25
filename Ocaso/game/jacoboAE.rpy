label jacoboLine:
    scene small_town with fade
    "Prefieres la seguridad y aceptas ir con Jacobo. Caminan de regreso al pueblo, charlando y riendo."
    show basic_j at left with moveinbottom
    show isa_bite at right with moveinbottom

    "Te encuentras disfrutando de la compañía de Jacobo, su humor tranquilo es un cambio bienvenido respecto de los misterios que rodean a Eduardo."
    "Y no puedes negar que detrás de esa peluca, digo, cabello completamente real, hay un chico muy atractivo."

    jump wolf


label wolf:
    scene house with fade
    "A medida que las semanas se convierten en meses, tú y Jacobo estan muy enamorados."
    show basic_j at left with moveinbottom
    show isa_basic at right with moveinbottom
    
    scene wolf_land with fade
    "Un día, el secreto de Jacobo se revela de forma dramática."
    show wolf_transform with fade
    "Finalmente descubres que es un hombre lobo." 
    hide wolf_transform
    show wolf_wait with moveinbottom
    "La revelación es menos impactante y más un momento de 'Aa, eso explica muchas cosas'."

    jacobo "Isabella, tengo que decirte algo. No soy como los demás tipos. Quiero decir, literalmente, me convierto en un lobo"
    isabella "a"
    
    "Ahora, tienes que tomar una decisión."
    "Quédate con Jacobo, a pesar de sus dominantes tendencias de hombre lobo, o haz lo sensato y abandona una relación potencialmente, no, DEFINITIVAMENTE peligrosa."

    menu:
        "Quédate con Jacobo": 
            "Supongo que cada relación tiene sus peculiaridades."
            hide wolf_wait with moveoutbottom
            show happy_j with moveinbottom
            jump jacoboEnding

        "Deja a Jacobo": 
            isabella "Eres genial, Jacobo, pero creo que prefiero que mis novios no se conviertan en lobos."
            hide wolf_wait
            show wolf_sad
            isabella "No eres tú, soy yo … bueno si eres tú. Adiós."
            hide wolf_sad
            show wolf_angry
            "Haces lo sensato y dejas a Jacobo, pero las cosas no salen muy bien."
            "En un ataque de ira, Jacobo se enfurece, y te hace pedacitos. Es un final trágico."
            return

label jacoboEnding:
    "Por alguna razón te quedaste con Jacobo."
    scene close_door with fade
    "Ustedes llevan juntos una vida extraña pero feliz."
    "Jacobo permanece sin camisa la mayor parte del tiempo, es raro, pero no te quejas."

    if TeamEduardo >= 2:
        "Envejecen juntos, y cuando Jacobo fallece como un viejo hombre lobo, Eduardo aparece en la puerta, el mismo vampiro por siempre joven."
        show open_door with fade
        menu:
            "Salir con Eduardo":
                "Bueno, ya has esperado bastante. Démosle pues."
                return  

            "Cierra la puerta":
                hide open_door
                "Hmmm no."
                return 
    else:
        "Felicidades por completar el juego, y bienvenid@ a #TeamJacobo ¡Buen trabajo!"
        return  

