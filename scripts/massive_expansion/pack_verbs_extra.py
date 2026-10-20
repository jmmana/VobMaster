"""
Extra Verbs: Action & Cognition (~220 words)
Format: (word, translation, level, ipa, example, exampleEs, emoji, categoryId)
"""

EXTRA_VERBS = [
    # Action verbs
    ("smear", "untar / manchar con crema", "B1", "/smɪr/", "Smear strawberry jam generously over toasted bagels.", "Unta mermelada de fresa en abundancia sobre bagels tostados.", "🍓", "verbs_action"),
    ("drizzle", "rociar un chorrito de aceite o miel", "A2", "/ˈdrɪz.əl/", "Drizzle balsamic glaze and virgin olive oil over sliced mozzarella.", "Rocía reducción balsámica y aceite de oliva sobre la mozzarella.", "🫒", "verbs_action"),
    ("sprinkle", "espolvorear queso o canela", "A1", "/ˈsprɪŋ.kəl/", "Sprinkle ground cinnamon over hot morning oatmeal bowls.", "Espolvorea canela en polvo sobre tazones de avena caliente.", "🥣", "verbs_action"),
    ("garnish", "decorar platillos con hierbas", "B1", "/ˈɡɑːr.nɪʃ/", "Garnish grilled salmon fillets with fresh dill sprigs and lemon wedges.", "Decora filetes de salmón a la plancha con eneldo fresco y rodajas de limón.", "🍋", "verbs_action"),
    ("marinate", "marinar carnes en salsa", "A2", "/ˈmer.ə.neɪt/", "Marinate chicken breasts in lime juice, garlic, and cumin overnight.", "Marina pechugas de pollo en jugo de limón, ajo y comino toda la noche.", "🍗", "verbs_action"),
    ("caramelize", "caramelizar cebollas a fuego lento", "B1", "/ˈker.ə.məl.aɪz/", "Caramelize sweet yellow onions slowly in melted butter for soup.", "Carameliza cebollas dulces lentamente en mantequilla para la sopa.", "🧅", "verbs_action"),
    ("deglaze", "desglasar la sartén con vino", "B2", "/ˌdiːˈɡleɪz/", "Deglaze the stainless skillet with dry white wine to make pan sauce.", "Desglasa la sartén de acero con vino blanco seco para hacer salsa.", "🍳", "verbs_action"),
    ("poach", "escalfar huevos en agua caliente", "A2", "/poʊtʃ/", "Poach fresh eggs in simmering salted water for eggs Benedict.", "Escalfa huevos frescos en agua con sal para preparar huevos Benedictinos.", "🥚", "verbs_action"),
    ("braise", "estofar carne en cazuela", "B1", "/breɪz/", "Braise short beef ribs in red wine and rosemary for three hours.", "Estofa costillas de res en vino tinto y romero por tres horas.", "🍲", "verbs_action"),
    ("sauté", "saltear verduras a fuego vivo", "A2", "/sɔːˈteɪ/", "Sauté sliced cremini mushrooms and baby spinach in garlic butter.", "Saltea champiñones rebanados y espinacas tiernas en mantequilla de ajo.", "🍄", "verbs_action"),
    ("sear", "sellar la carne a fuego alto", "B1", "/sɪr/", "Sear the seasoned steak in a smoking-hot cast-iron skillet.", "Sella el filete sazonado en una sartén de hierro fundido muy caliente.", "🥩", "verbs_action"),
    ("broil", "gratinar al horno bajo llama directa", "B1", "/brɔɪl/", "Broil mozzarella-topped garlic bread slices until golden brown.", "Gratina rebanadas de pan con ajo y mozzarella hasta que doren.", "🍞", "verbs_action"),
    ("simmer", "cocinar a fuego lento suave", "A2", "/ˈsɪm.ɚ/", "Simmer the hearty vegetable lentil soup for forty-five minutes.", "Cocina la sopa de lentejas y verduras a fuego lento por cuarenta y cinco minutos.", "🥣", "verbs_action"),
    ("steam", "cocinar al vapor vegetales", "A1", "/stiːm/", "Steam fresh broccoli florets until bright green and tender-crisp.", "Cocina al vapor ramitos de brócoli fresco hasta que queden tiernos.", "🥦", "verbs_action"),
    ("puree", "hacer puré de verduras", "A2", "/pjʊˈreɪ/", "Puree cooked butternut squash with cream and roasted garlic.", "Haz puré de calabaza cocida con crema y ajo asado.", "🥣", "verbs_action"),
    ("strain", "colar caldo o té", "A2", "/streɪn/", "Strain the chicken stock through a fine mesh sieve to remove herbs.", "Cuela el caldo de pollo con un colador fino para retirar las hierbas.", "🍲", "verbs_action"),
    ("infuse", "infusionar hierbas aromáticas", "B1", "/ɪnˈfjuːz/", "Infuse pure honey with dried lavender blossoms and chili flakes.", "Infusiona miel pura con flores secas de lavanda y hojuelas de chile.", "🍯", "verbs_action"),
    ("ferment", "fermentar alimentos naturalmente", "B1", "/fɚˈment/", "Ferment shredded green cabbage with sea salt to prepare homemade sauerkraut.", "Fermenta col rallada con sal de mar para hacer chucrut casero.", "🥬", "verbs_action"),
    ("cure", "curar carnes o pescados con sal", "B2", "/kjʊr/", "Cure fresh salmon fillets in rock salt, brown sugar, and dill.", "Cura filetes de salmón fresco en sal de grano, azúcar y eneldo.", "🐟", "verbs_action"),
    ("smoke", "ahumar cecina o salmón", "A2", "/smoʊk/", "Smoke pork ribs slowly over applewood chips in the outdoor smoker.", "Ahúma costillas de cerdo sobre virutas de madera de manzano.", "🍖", "verbs_action"),

    # Craft & Workshop verbs
    ("bevel", "biselar bordes de madera o vidrio", "B2", "/ˈbev.əl/", "Bevel the sharp edges of the glass mirror for safety and style.", "Bisela los bordes afilados del espejo de vidrio por seguridad y estilo.", "🪞", "verbs_action"),
    ("chamfer", "achaflanar esquinas rectas", "B2", "/ˈtʃæm.fɚ/", "Chamfer corners on the handcrafted pine table legs.", "Achaflana las esquinas de las patas de madera de pino hechas a mano.", "🪵", "verbs_action"),
    ("groove", "hacer ranuras o canales en piezas", "B1", "/ɡruːv/", "Cut a shallow groove down the wooden plank to guide sliding panels.", "Haz una ranura en el tablón de madera para guiar los paneles corredizos.", "🪵", "verbs_action"),
    ("solder", "soldar con estaño circuitos", "B1", "/ˈsɑː.dɚ/", "Solder the copper diode leads onto the miniature circuit board.", "Suelda las terminales de cobre del diodo en la placa de circuitos.", "🔌", "verbs_action"),
    ("weld", "soldar metal con arco eléctrico", "B1", "/weld/", "Weld steel tubular frames to build industrial factory workbenches.", "Suelda tubos de acero para armar mesas de trabajo industriales.", "⚡", "verbs_action"),
    ("rivet", "remachar chapas de metal", "B2", "/ˈrɪv.ɪt/", "Rivet aluminum sheets firmly to the airplane wing structure.", "Remacha láminas de aluminio a la estructura del ala del avión.", "✈️", "verbs_action"),
    ("galvanize", "galvanizar acero con zinc", "B2", "/ˈɡæl.və.naɪz/", "Galvanize steel chain-link fences to prevent rain rusting.", "Galvaniza cercas de malla de acero para evitar que se oxiden con la lluvia.", "⛓️", "verbs_action"),
    ("anodize", "anodizar aluminio para color", "B2", "/ˈæn.ə.daɪz/", "Anodize lightweight bicycle wheel rims in sleek matte black finish.", "Anodiza los rines de bicicleta de aluminio en un elegante acabado negro.", "🚲", "verbs_action"),
    ("upholster", "tapizar sillones con telas", "B2", "/ʌpˈhoʊl.stɚ/", "Upholster antique vintage armchairs in rich royal blue velvet.", "Tapiza sillones antiguos en un suntuoso terciopelo azul rey.", "🛋️", "verbs_action"),
    ("restring", "encordar raquetas o guitarras", "A2", "/ˌriːˈstrɪŋ/", "Restring the classical acoustic guitar with new bronze strings.", "Vuelve a encordar la guitarra acústica clásica con cuerdas de bronce.", "🎸", "verbs_action"),
    ("retune", "reafinar instrumentos musicales", "A2", "/ˌriːˈtuːn/", "Retune the concert grand piano before the evening solo recital.", "Vuelve a afinar el piano de cola de concierto antes del recital.", "🎹", "verbs_action"),
    ("rebinding", "reencuadernar libros antiguos", "B2", "/riːˈbaɪn.dɪŋ/", "Artisan binders restore antique bibles by rebinding frayed leather covers.", "Encuadernadores restauran biblias antiguas renovando cubiertas de piel.", "📚", "verbs_action"),
    ("plaster", "enyesar paredes de cuartos", "A2", "/ˈplæs.tɚ/", "Plaster cracked interior bedroom walls before applying primer paint.", "Enyesa paredes agrietadas de la recámara antes de poner pintura base.", "🧱", "verbs_action"),
    ("trowel", "aplanar mezcla con llana", "B1", "/ˈtraʊ.əl/", "Trowel wet concrete mortar smoothly across the patio walkway.", "Aplana el mortero de concreto húmedo con la llana a lo largo del patio.", "🧱", "verbs_action"),
    ("caulk", "calafatear grietas con silicón", "B1", "/kɑːk/", "Caulk around the bathtub perimeter to stop water leaks into drywall.", "Calafatea con silicón el borde de la tina para evitar fugas de agua.", "🛁", "verbs_action"),

    # Movement, Motion & Physical action
    ("saunter", "pasear relajado sin prisa", "B2", "/ˈsɑːn.t̬ɚ/", "We sauntered along the boulevard admiring the historic architecture.", "Paseamos relajados por el bulevar admirando la arquitectura histórica.", "🚶", "verbs_action"),
    ("meander", "serpentear o deambular sin rumbo", "B2", "/miˈæn.dɚ/", "Rivers meander peacefully through wide emerald green valleys.", "Los ríos serpentean pacíficamente por amplios valles verde esmeralda.", "🏞️", "verbs_action"),
    ("stride", "caminar con zancadas firmes", "B1", "/straɪd/", "The detective strode confidently into the courthouse foyer.", "El detective entró con zancadas firmes al vestíbulo del tribunal.", "🚶‍♂️", "verbs_action"),
    ("tiptoe", "andar de puntitas sin ruido", "A1", "/ˈtɪp.toʊ/", "Tiptoe past the nursery room so you do not wake the sleeping baby.", "Pasa de puntitas junto al cuarto para no despertar al bebé dormido.", "🤫", "verbs_action"),
    ("creep", "moverse sigiloso arrastrándose", "A2", "/kriːp/", "Cats creep silent and low through the tall garden grass when hunting.", "Los gatos se mueven sigilosos y agachados por el pasto al cazar.", "🐈", "verbs_action"),
    ("prowl", "merodear acechando presas", "B1", "/praʊl/", "Tigers prowl quietly through mangrove thickets in the dark.", "Los tigres merodean en silencio entre manglares en la oscuridad.", "🐅", "verbs_action"),
    ("scurry", "escurrirse corriendo a prisa", "A2", "/ˈskɝː.i/", "Mice scurry across the barn floor as soon as overhead lights flip on.", "Los ratones corren a prisa por el granero en cuanto se enciende la luz.", "🐁", "verbs_action"),
    ("dart", "lanzarse veloz como dardo", "A2", "/dɑːrt/", "Hummingbirds dart between colorful flowers with lightning agility.", "Los colibríes se lanzan veloces entre flores con asombrosa agilidad.", "🌸", "verbs_action"),
    ("lunge", "abalanzarse hacia adelante", "B1", "/lʌndʒ/", "Fencers lunge forward with quick arm thrusts to score touches.", "Los esgrimistas se abalanzan hacia adelante con estocadas para tocar.", "🤺", "verbs_action"),
    ("parry", "parar o desviar un golpe", "B2", "/ˈper.i/", "The knight parried the heavy sword blow with a steel round shield.", "El caballero desvió el golpe de espada con un escudo redondo de acero.", "🛡️", "verbs_action"),
    ("dodge", "esquivar un obstáculo o golpe", "A2", "/dɑːdʒ/", "Athletes dodge falling balls swiftly in fast-paced playground games.", "Los atletas esquivan pelotas que caen con rapidez en los juegos.", "🏃", "verbs_action"),
    ("swerve", "dar un volantazo para esquivar", "B1", "/swɝːv/", "Swerve safely around deer crossing the dark country road at night.", "Da un volantazo seguro para esquivar venados que cruzan la carretera.", "🚗", "verbs_action"),
    ("brake", "frenar el automóvil a tiempo", "A1", "/breɪk/", "Brake smoothly at pedestrian crossings to let school children pass.", "Frena suavemente en pasos peatonales para que crucen los escolares.", "🛑", "verbs_action"),
    ("accelerate", "acelerar la velocidad de marcha", "B1", "/əkˈsel.ə.reɪt/", "Electric cars accelerate smoothly and silently on highway on-ramps.", "Los autos eléctricos aceleran suave y silenciosamente en las autopistas.", "⚡", "verbs_action"),
    ("overtake", "rebasar a otro vehículo en ruta", "B1", "/ˌoʊ.vɚˈteɪk/", "Never overtake slower trucks on blind curving mountain roads.", "Nunca rebases a camiones lentos en curvas ciegas de montaña.", "🚛", "verbs_action"),

    # Mind & Thinking verbs
    ("scrutinize", "examinar con lupa y detalle", "B2", "/ˈskruː.tən.aɪz/", "Auditors scrutinize every expense line item before signing off.", "Los auditores examinan con lupa cada partida de gastos antes de firmar.", "🔍", "verbs_mind"),
    ("ascertain", "averiguar con certeza los hechos", "B2", "/ˌæs.ɚˈteɪn/", "Detectives interviewed witnesses to ascertain the exact sequence of events.", "Detectives entrevistaron testigos para averiguar la secuencia exacta de hechos.", "🕵️", "verbs_mind"),
    ("contemplate", "reflexionar sobre el futuro", "B1", "/ˈkɑːn.təm.pleɪt/", "Sit by the calm ocean shore to contemplate major life milestones.", "Siéntate junto al mar en calma para reflexionar sobre etapas de la vida.", "🌊", "verbs_mind"),
    ("ponder", "sopesar pros y contras", "B1", "/ˈpɑːn.dɚ/", "Take time to ponder career job offers before submitting resignations.", "Tómate tu tiempo para sopesar ofertas de trabajo antes de renunciar.", "💼", "verbs_mind"),
    ("rationalize", "justificar con excusas lógicas", "B2", "/ˈræʃ.ən.əl.aɪz/", "He tried to rationalize missing deadlines by blaming computer crashes.", "Intentó justificar retrasos en las entregas culpando a fallas técnicas.", "💻", "verbs_mind"),
    ("conceptualize", "diseñar el concepto base", "B2", "/kənˈsep.tʃu.ə.laɪz/", "The creative team conceptualized an engaging mobile health app.", "El equipo creativo diseñó el concepto de una app de salud atractiva.", "📱", "verbs_mind"),
    ("formulate", "formular planes o hipótesis", "B1", "/ˈfɔːr.mjə.leɪt/", "Scientists formulate testable hypotheses before conducting lab experiments.", "Los científicos formulan hipótesis comprobables antes de hacer experimentos.", "🔬", "verbs_mind"),
    ("hypothesize", "plantear supuestos de trabajo", "B2", "/haɪˈpɑː.θə.saɪz/", "Astronomers hypothesize that subterranean oceans exist beneath Europa's icy crust.", "Astrónomos plantean que existen océanos subterráneos bajo el hielo de Europa.", "🪐", "verbs_mind"),
    ("theorize", "crear teorías explicativas", "B1", "/ˈθiː.ə.raɪz/", "Physicists theorize about parallel universes in string theory.", "Los físicos crean teorías sobre universos paralelos en la teoría de cuerdas.", "🌌", "verbs_mind"),
    ("extrapolate", "proyectar datos hacia el futuro", "B2", "/ɪkˈstræp.ə.leɪt/", "Statisticians extrapolate demographic trends for the next fifty years.", "Estadísticos proyectan tendencias demográficas para los próximos cincuenta años.", "📈", "verbs_mind")
]
