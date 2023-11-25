
label scene1:
    scene dorks with fade
    "Tu nombre es Isabella Cisne. Acabas de mudarte al pequeño pueblo de Dorks, para vivir con tu padre, Carlos Cisne, el alguacil local."
    "Tu madre, Renata, decidió viajar con su nuevo marido, un jugador de béisbol de ligas menores, y tú elegiste venir aquí para darles algo de espacio."
    "Dorks parece ser tranquilo. Lo cual es muy conveniente, porque eres un poco introvertida y te sientes más cómoda con un libro en la mano que en un espacio lleno de gente."
    scene house with fade
    "Conoces a tu padre, Carlos, quien está feliz pero incómodo por tu llegada."
    carlos "¡Isabella, qué alegría verte! Ven, te mostraré tu habitación."
    scene isa_room with fade
    "Te muestra tu antigua habitación, que ha conservado tal como la dejaste durante tus anteriores visitas."
    jump scene2
    
label scene2:
    scene highschool with fade
    "Al día siguiente, comienzas en Dorks High."
    show isa_basic at center with moveinbottom
    "Todo el mundo parece saber acerca de la chica nueva y te sientes observada."
    jump scene3

label scene3:
    scene cafeteria with fade
    # cafeteria 
    "Es la hora del almuerzo en Dorks High."
    show cafeteria_c with fade

    "Entras a la bulliciosa cafetería y es entonces cuando los ves: un grupo de estudiantes increíblemente atractivos."
    "Son pálidos, todos con ojos amarillos y con una expresion de querer matarte."

    "Entre ellos, un chico en particular te llama la atención. Tiene el cabello oscuro, despeinado y parece estar sumido en sus pensamientos."
    "No se parece a nadie que hayas visto."
    
    menu:
        "Pregúntale a una compañera sobre ellos. Sobre todo el guapito que te está viendo raro":
            $ TeamEduardo += 1

            isabella "¿Quiénes son? Parecen... diferentes"
            show basic_jess at left with moveinbottom

            jessica "Ellos son los Cuéllar. Son los hijos adoptivos del Dr. Cuéllar."
            jessica "No conviven con nadie fuera de su círculo. Literalmente. Solo salen entre ellos. Es raro. Y aparte llevan como 10 años en el último año."
            isabella "¿Y quién es él?"
            jessica "Él es Eduardo Cuéllar. Ni lo pienses, se cree mejor que todos. No tienes ni la menor oportunidad con él."

        "Admira desde lejos":
            $ TeamEduardo += 1
            isabella "Parecen sacados de una revista de moda"
            show basic_jess at left with moveinbottom

            jessica "Así es, pero no te recomiendo acercarte a ellos. De hecho ni siquiera sé si es posible hacer algo distinto que admirarlos."
            jessica "Sobre todo Eduardo Cuéllar, no te dará ni la hora."

        "¿Te importa? No.":
            isabella "Debería mantener la distancia. Parecen fuera de mi alcance"

    jump scene4
    
label scene4:
    scene science_lab with fade
    "Más tarde, en la clase de ciencias, eres asignada como compañera del chico hermoso de la cafetería."
    show stinky with fade
    "Cuando te acercas, notas su repentino malestar. Se tapa la nariz y mira hacia otro lado, su expresión es una mezcla de disgusto y pánico."
    "¿Se te olvidó ponerte desodorante hoy? ¿O tal vez sea el sándwich de atún con cebolla que comiste en el almuerzo?"

    menu:
        "Confrontalo, te respetas y sabes que nadie te pueda tratar asi":
            isabella "Oye, ¿pasa algo? ¿Hice algo para ofenderte?"
            eduardo "..."

        "Vergüenza silenciosa":
            isabella "Me sentaré aquí y fingiré que no me di cuenta. Tal vez no se trate de mí."

    hide stinky with fade 

    "A pesar del comienzo incómodo, intentas concentrarte en la clase. Él, sin embargo, mantiene la distancia y se va rápidamente cuando suena el timbre, dejándote con más preguntas que respuestas."

    show isa_basic with fade
    isabella "¿Cuál será su problema?"
    hide isa_basic 
    show isa_bite
    "Aún así no puedes evitar sentirte intrigada."

    jump scene5
    
label scene5:
    scene window with fade
    "Una tarde, encuentra a tu papá afuera de la casa con Guillermo Blanco y su hijo, Jacobo." 
    show house with fade
    show happy_j at right with moveinbottom
    "Jacobo, que tiene más o menos tu edad, sonríe ampliamente cuando te acercas."
    "Jacobo tiene un encanto dificil de explicar."
    "Tiene el cabello largo, parece una peluca, pero no es, y está muy marcado para tener 15 años."
    jacobo "¡Hola, Isabella! Esta belleza es toda tuya. No es la más rápida, pero tiene buen carácter. ¡Y yo mismo la arreglé!"
    show truck at left with moveinleft

    menu:
        "Coquetea con Jacobo, esta bien guapo":
            $ TeamJacobo += 1
            isabella "Vaya, ¿un tipo que puede arreglar autos? Eso es bastante impresionante. ¡Gracias, Jacobo!"
        
            jacobo "Entonces, eres nueva en la ciudad, ¿verdad? Si necesitas un guía turístico, aquí estoy. Dorks tiene algunos lugares interesantes si sabes dónde buscar"
            isabella  "¿Un guía turístico personal? Suena como una cita. Estoy dentro"

        "Friendzonealo, no te gusta su peluca":
            isabella "Es muy amable de tu parte, Jacobo. Será fantástico para moverse. Eres un buen amigo"
            hide happy_j
            show basic_j at right

            jacobo "Entonces, eres nueva en la ciudad, ¿verdad? Si necesitas un guía turístico, aquí estoy. Dorks tiene algunos lugares interesantes si sabes dónde buscar"
            isabella "¡Claro, un recorrido amistoso, de amigos, muy amigos, mejores amigos, suena divertido!"
    
label scene6:
    scene parkinglot with fade
    "Es una mañana típica en Dorks High. Estás saliendo de tu camión, escuchando música y distraída, cuando de repente un auto se dirige descontroladamente hacia ti."
    show carscrash with fade
    "De la nada, el misterioso chico de tu clase de ciencias, Eduardo Cuéllar, entra corriendo y detiene el auto con sus propias manos."
    hide carscrash
    show ed_save with fade
    "Eduardo te mira con ojos intensos ..."

    menu:
        "Agradécele sin cuestionarlo":
            $ TeamEduardo += 1

            isabella "Okay, hmm wow ¿Cómo hiciste eso? Debes ejercitarte mucho, ¿eh? ¡Muchas gracias!"
            eduardo "Estaba en el lugar correcto en el momento correcto. Deberías tener más cuidado. Tengo que irme"
            hide ed_save

        "Razonablemente, te quedas sin palabras y en shock":
            hide ed_save
            show isa_shock with fade
            "lo miras fijamente con incredulidad, incapaz de formar palabras. Cuando él comienza a alejarse, todavía estás tratando de procesar lo que acaba de suceder."
            "Eduardo duda por un momento, parece preocupado, pero luego se da vuelta y se aleja rápidamente."
            hide isa_shock with fade

        "Cuestionalo":
            isabella "¡Espera un minuto! Nadie puede hacer lo que tú acabas de hacer. ¿Qué eres?"
            eduardo "No me creerías si te lo dijera. Por favor, olvida que esto pasó"
            "Luego se da vuelta y desaparece entre la multitud."
            hide ed_save

    show isa_basic with moveinbottom
    "Después del encuentro, te quedas con más preguntas que respuestas. Por alguna razón, sientes una necesidad de saber más sobre Eduardo."
    jump scene7

label scene7:
    scene forest with fade
    "Impulsada por la curiosidad, decides seguirlo al finalizar las clases. Lo ves caminando hacia el denso bosque que rodea Dorks."
    show isa_basic with moveinbottom
    "Manteniendo la distancia, lo sigues al bosque con la esperanza de descubrir algunas pistas sobre sus misteriosas habilidades."
    
    "Mientras sigues sigilosamente a Eduardo a través del bosque, con los sonidos de la naturaleza a su alrededor, de repente escuchas una voz familiar."
    "Es Jacobo, llamándote con una mezcla de preocupación y curiosidad."

    hide isa_basic with fade
    show happy_j with moveinbottom
    jacobo "¡Isabella! ¿Dónde diablos has estado loca?"

    hide happy_j
    show angry_j 
    jacobo "Oye, así deberás, ¿qué estás haciendo aquí sola? No es seguro deambular por este bosque, especialmente con... bueno, ya sabes, vida silvestre alrededor"

    "Isabella está sorprendida y un poco molesta por haber sido interrumpida ... "
    "pero también se da cuenta que seguir a Eduardo tal vez no es la mejor idea. De hecho es muy estúpido."

    menu:
        "Deja a Jacobo atrás":
            
            isabella "Solo estoy... explorando. No te preocupes por mí, Jacobo. Creo que vi algo interesante más adelante."
            isabella "Necesito comprobarlo sola. Y ya no me sigas, es raro"

            jacobo "¿Estás segura? Es fácil perderse aquí. Y hay... historias sobre estos bosques"
            jump eduardoLine

        "Quédate con Jacobo":
            $ TeamJacobo += 1
            isabella "Sabes qué, tienes razón. Probablemente no sea nada."
            isabella "¿Quieres tomar un café o algo así? Es bueno tener compañía."

            hide angry_j
            show happy_j 
            jacobo "¡Claro, eso suena genial! Hay un pequeño café cerca. Vayamos hacia allí. ¡Es más seguro y el chocolate caliente es increíble!"
            jump jacoboLine