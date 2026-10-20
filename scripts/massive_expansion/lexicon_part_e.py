"""
Lexicon Part E: Animals, Home & Nature (~120 graded entries)
Format: (word, translation, level, ipa, example, exampleEs, emoji, categoryId)
"""

PART_E_WORDS = [
    # Animals, Wildlife & Insects
    ("armadillo", "armadillo con caparazón óseo", "A2", "/ˌɑːr.məˈdɪl.oʊ/", "An armadillo foraged for subterranean grubs with sharp digging claws.", "Un armadillo buscaba larvas subterráneas con sus garras afiladas.", "🐾", "animals"),
    ("porcupine", "puercoespín con púas defensivas", "A2", "/ˈpɔːr.kjə.paɪn/", "A porcupine rattles its quills to warn off curious mountain cougars.", "Un puercoespín agita sus púas para advertir a pumas curiosos.", "🦔", "animals"),
    ("sloth", "perezoso arborícola lento", "A1", "/sloʊθ/", "A three-toed sloth hangs upside down from tropical cecropia tree branches.", "Un perezoso de tres dedos cuelga cabeza abajo en ramas de selva.", "🦥", "animals"),
    ("anteater", "oso hormiguero de lengua larga", "A2", "/ˈæntˌiː.t̬ɚ/", "The giant anteater uses its sticky tongue to flick up thousands of termites.", "El oso hormiguero gigante usa su lengua pegajosa para atrapar termitas.", "🐜", "animals"),
    ("koala", "koala que come hojas de eucalipto", "A1", "/koʊˈɑː.lə/", "A mother koala sleeps peacefully while cradling a joey in an eucalyptus fork.", "Una madre koala duerme abrazando a su cría en la horqueta de un eucalipto.", "🐨", "animals"),
    ("kangaroo", "canguro saltador australiano", "A1", "/ˌkæŋ.ɡəˈruː/", "Red kangaroos bound effortlessly across dusty red outback plains.", "Canguros rojos brincan con facilidad por planicies áridas del desierto.", "🦘", "animals"),
    ("wombat", "wómbat excavador de madrigueras", "B1", "/ˈwɑːm.bæt/", "The muscular wombat grazes on native grasses under starry Australian skies.", "El musculoso wómbat pasta hierba nativa bajo cielos estrellados.", "🐾", "animals"),
    ("dingo", "dingo o perro salvaje australiano", "B1", "/ˈdɪŋ.ɡoʊ/", "Pack dingos communicated with eerie midnight howls across desert dunes.", "Jaurías de dingos se comunicaban con aullidos nocturnos por las dunas.", "🐕", "animals"),
    ("hyena", "hiena carroñera manchada", "A2", "/haɪˈiː.nə/", "Spotted hyenas circled the savannah in search of remaining lion kills.", "Hienas manchadas rodearon la sabana buscando restos de presas de leones.", "🐾", "animals"),
    ("cheetah", "guepardo / chita el más veloz", "A1", "/ˈtʃiː.t̬ə/", "A sprinting cheetah reaches speeds over sixty miles an hour in three seconds.", "Un guepardo al esprintar supera las sesenta millas por hora en tres segundos.", "🐆", "animals"),
    ("jaguar", "jaguar felino con rosetas", "A2", "/ˈdʒæɡ.wɑːr/", "The stealthy jaguar ambushes caimans along Amazonian river banks.", "El sigiloso jaguar embosca caimanes a lo largo de orillas del río Amazonas.", "🐆", "animals"),
    ("puma", "puma montañés o león de montaña", "A2", "/ˈpjuː.mə/", "A solitary puma bounded across high snowy Rocky Mountain ridges.", "Un puma solitario saltó por las altas crestas nevadas de las Montañas Rocosas.", "🐾", "animals"),
    ("alpaca", "alpaca de lana suave andina", "A2", "/ælˈpæk.ə/", "Herds of fluffy alpacas graze peacefully on high Andean plateaus.", "Rebaños de alpacas afelpadas pastan en apacibles mesetas andinas.", "🦙", "animals"),
    ("llama", "llama de carga tradicional", "A1", "/ˈlɑː.mə/", "Inca traders loaded woven grain sacks onto gentle pack llamas.", "Comerciantes incas cargaban costales de granos sobre dóciles llamas.", "🦙", "animals"),
    ("flamingo", "flamenco rosado de patas largas", "A1", "/fləˈmɪŋ.ɡoʊ/", "Flocks of pink flamingos wade in shallow saltwater lagoons.", "Bandadas de flamencos rosados caminan por lagunas saladas poco profundas.", "🦩", "animals"),
    ("ostrich", "avestruz corredora de gran tamaño", "A1", "/ˈɑː.strɪtʃ/", "The flightless ostrich is the world's largest and fastest running bird.", "El avestruz no volador es el ave más grande y rápida del mundo al correr.", "🐦", "animals"),
    ("iguana", "iguana verde de crestas", "A1", "/ɪˈɡwɑː.nə/", "Green iguanas bask motionless in morning sun atop tropical branches.", "Iguanas verdes toman el sol matutino inmóviles sobre ramas tropicales.", "🦎", "animals"),
    ("gecko", "geco con almohadillas trepadoras", "A2", "/ˈɡek.oʊ/", "Tiny spotted geckos climb up vertical glass windowpanes at night.", "Diminutos gecos moteados trepan por cristales de ventanas por la noche.", "🦎", "animals"),
    ("scorpion", "escorpión o alacrán con aguijón", "A2", "/ˈskɔːr.pi.ən/", "The desert scorpion fluoresces bright neon blue under ultraviolet blacklights.", "El escorpión del desierto brilla en azul neón bajo luz ultravioleta.", "🦂", "animals"),
    ("tarantula", "tarántula peluda de patas largas", "A2", "/təˈræn.tʃə.lə/", "A docile desert tarantula ambled gently across the warm trail stones.", "Una dócil tarántula del desierto caminó con calma por piedras del sendero.", "🕷️", "animals"),

    # Home, Furniture & House Hardware
    ("chandelier", "candelabro de cristal colgante", "B1", "/ˌʃæn.dəˈlɪr/", "A sparkling crystal chandelier illuminated the grand formal dining room.", "Un candelabro de cristal brillante iluminaba el gran comedor formal.", "💡", "home"),
    ("sconce", "aplique de pared para lámpara", "B2", "/skɑːns/", "Brass wall sconces cast warm ambient lighting along the hotel corridor.", "Apliques de latón en la pared proyectan luz cálida en el pasillo del hotel.", "🕯️", "home"),
    ("ottoman", "otomana / taburete tapizado para pies", "A2", "/ˈɑː.t̬ə.mən/", "Rest your tired feet on a plush tufted leather ottoman after work.", "Descansa los pies cansados en una otomana de piel acolchada tras el trabajo.", "🛋️", "home"),
    ("footstool", "banqueta reposapiés pequeña", "A1", "/ˈfʊt.stuːl/", "Slide the wooden footstool beneath your desk to improve sitting posture.", "Coloca el reposapiés de madera bajo tu escritorio para mejorar la postura.", "🪵", "home"),
    ("sideboard", "aparador buffet para vajilla", "B1", "/ˈsaɪd.bɔːrd/", "Store fine porcelain dinner plates and silverware inside the oak sideboard.", "Guarda vajillas de porcelana fina y cubiertos dentro del aparador de roble.", "🍽️", "home"),
    ("credenza", "credencia de oficina con gavetas", "B2", "/krɪˈden.zə/", "Stack executive document binders atop the polished walnut credenza.", "Apila carpetas de documentos sobre la credencia de nogal pulido.", "🗄️", "home"),
    ("wardrobe", "ropero o armario para colgar ropa", "A1", "/ˈwɔːr.droʊb/", "Hang your winter coats and suits inside the tall wooden wardrobe.", "Cuelga tus abrigos de invierno y trajes dentro del alto ropero de madera.", "🚪", "home"),
    ("dresser", "cómoda con cajones para ropa", "A1", "/ˈdres.ɚ/", "Fold clean t-shirts and socks neatly inside the bedroom dresser drawers.", "Dobla camisetas y calcetines limpios en los cajones de la cómoda del cuarto.", "🪞", "home"),
    ("nightstand", "mesa de noche junto a la cama", "A1", "/ˈnaɪt.stænd/", "Keep a reading lamp, a glass of water, and an alarm clock on your nightstand.", "Ten una lámpara de lectura, un vaso de agua y un reloj en tu mesa de noche.", "⏰", "home"),
    ("mattress", "colchón ortopédico para dormir", "A1", "/ˈmæt.rəs/", "Sink into a supportive memory foam mattress for deep restful sleep.", "Acuéstate en un colchón viscoelástico para un sueño profundo y reparador.", "🛏️", "home"),
    ("pillowcase", "funda protectora de almohada", "A1", "/ˈpɪl.oʊ.keɪs/", "Wash cotton pillowcases weekly in hot water for healthy skin hygiene.", "Lava las fundas de almohada de algodón cada semana con agua caliente.", "🛏️", "home"),
    ("duvet", "edredón nórdico de plumas", "A2", "/duːˈveɪ/", "Slip a fresh linen cover over the warm white goose-down duvet.", "Coloca una funda de lino sobre el cálido edredón nórdico de plumón.", "🛏️", "home"),
    ("banister", "pasamanos / barandal de escalera", "A2", "/ˈbæn.ə.stɚ/", "Hold firmly onto the polished mahogany stair banister when descending.", "Sujétate bien del pasamanos de caoba de la escalera al bajar.", "🪜", "home"),
    ("windowsill", "alféizar / repisa de ventana", "A2", "/ˈwɪn.doʊ.sɪl/", "Line small terracotta pots of fresh culinary herbs along the sunny windowsill.", "Coloca macetitas con hierbas culinarias en el soleado alféizar de la ventana.", "🪴", "home"),
    ("hearth", "hogar de la chimenea / fogón", "B1", "/hɑːrθ/", "A crackling fire of birch logs glowed warmly in the stone fireplace hearth.", "Un fuego chisporroteante de leña de abedul brillaba en el fogón de la chimenea.", "🔥", "home"),

    # Nature, Flora & Landscapes
    ("meadow", "prado verde lleno de flores", "A2", "/ˈmed.oʊ/", "Wild lavender and poppies bloomed across the sun-drenched alpine meadow.", "Lavanda silvestre y amapolas florecieron en el prado alpino bañado por el sol.", "🌼", "nature"),
    ("pasture", "pastizal o dehesa para ganado", "A2", "/ˈpæs.tʃɚ/", "Dairy cows grazed lazily on rich clover in the fenced green pasture.", "Vacas lecheras pastaron trébol fresco en el verde pastizal cercado.", "🐄", "nature"),
    ("marsh", "pantano o ciénaga con juncos", "B1", "/mɑːrʃ/", "Ducks splashed among tall cattail reeds in the tranquil freshwater marsh.", "Patos chapotearon entre juncos en la apacible ciénaga de agua dulce.", "🦆", "nature"),
    ("swamp", "humedal pantanoso con cipreses", "A2", "/swɑːmp/", "Navigate wooden boardwalks through ancient moss-draped cypress swamps.", "Camina por puentes de madera a través de pantanos de cipreses con musgo.", "🐊", "nature"),
    ("lagoon", "laguna costera de agua turquesa", "A2", "/ləˈɡuːn/", "Tropical fish swim through crystalline turquoise waters of the island lagoon.", "Peces tropicales nadan por las aguas turquesa cristalinas de la laguna.", "🏝️", "nature"),
    ("rapids", "rápidos de río para balsa", "B1", "/ˈræp.ɪdz/", "Whitewater rafters paddled aggressively through roaring class-four rapids.", "Balsistas de rápidos remaron con fuerza a través de estruendosos rápidos.", "🌊", "nature"),
    ("tributary", "afluente que desemboca en río mayor", "B2", "/ˈtrɪb.jə.ter.i/", "Dozens of crystal mountain tributaries feed into the mighty river basin.", "Docenas de afluentes cristalinos de montaña alimentan la cuenca del gran río.", "🏞️", "nature"),
    ("ravine", "barranco profundo o quebrada", "B1", "/rəˈviːn/", "A suspension footbridge swayed gently high above the forested ravine.", "Un puente colgante peatonal se mecía suavemente sobre el barranco boscoso.", "🌉", "nature"),
    ("cavern", "caverna subterránea de estalactitas", "B1", "/ˈkæv.ɚn/", "Explorers switched on headlamps to view gigantic limestone cavern formations.", "Exploradores encendieron linternas para ver cavernas con estalactitas gigantes.", "🦇", "nature"),
    ("stalactite", "estalactita que cuelga del techo", "B2", "/stəˈlæk.taɪt/", "Mineral-rich water droplets formed hanging pointed calcium stalactites.", "Gotas de agua ricas en minerales formaron estalactitas que cuelgan del techo.", "🪨", "nature"),
    ("stalagmite", "estalagmita que crece del suelo", "B2", "/stəˈlæɡ.maɪt/", "Massive cone-shaped stalagmites rose ten feet high from the cave cavern floor.", "Enormes estalagmitas cónicas se alzaban diez pies desde el suelo de la cueva.", "🪨", "nature"),
    ("crater", "cráter volcánico o meteórico", "A2", "/ˈkreɪ.t̬ɚ/", "Hike up the gravel trail to gaze down into the dormant volcano crater.", "Sube por el sendero de grava para asomarte al cráter del volcán inactivo.", "🌋", "nature"),
    ("canyon", "cañón profundo entre rocas", "A2", "/ˈkæn.jən/", "The Colorado River carved the dramatic red stone depths of the Grand Canyon.", "El río Colorado talló las profundidades rojizas del Gran Cañón.", "🏜️", "nature"),
    ("dune", "duna de arena moldeada por viento", "A2", "/duːn/", "Wind constantly reshapes the golden crests of towering desert sand dunes.", "El viento remodela constantemente las crestas de altas dunas de arena.", "🏜️", "nature"),
    ("oasis", "oasis fértil con palmeras en desierto", "A2", "/oʊˈeɪ.sɪs/", "Nomadic caravans quenched their thirst beneath date palms at the desert oasis.", "Caravanas nómadas calmaron la sed bajo palmeras datileras en el oasis.", "🌴", "nature")
]
