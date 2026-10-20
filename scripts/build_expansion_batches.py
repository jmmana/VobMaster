#!/usr/bin/env python3
"""
Expansion Batch Generator.
Populates modular batch files in scripts/massive_expansion/ with 2,600+ new authentic words.
"""

import os

# Batch 1: Everyday Objects, Kitchen, Tools, Home & Fashion (~450 items)
BATCH_OBJECTS_DATA = """
BATCH_OBJECTS = [
    # Kitchen & Food Prep (A1, A2, B1)
    ("corkscrew", "sacacorchos / descorchador", "A2", "/ˈkɔːrk.skruː/", "Use the corkscrew to open the bottle of red wine.", "Usa el sacacorchos para abrir la botella de vino tinto.", "🍾", "home"),
    ("colander", "escurridor de pasta o verduras", "A2", "/ˈkɑː.lən.dɚ/", "Drain the boiled spaghetti in a stainless steel colander.", "Escurre los espaguetis hervidos en un escurridor de acero inoxidable.", "🍝", "home"),
    ("spatula", "espátula de cocina", "A1", "/ˈspætʃ.ə.lə/", "Flip the golden pancakes gently with a silicone spatula.", "Voltea los panqueques dorados suavemente con una espátula de silicona.", "🥞", "home"),
    ("whisk", "batidor de alambre / batir", "A2", "/wɪsk/", "Whisk the egg yolks and sugar until creamy and pale.", "Bate las yemas de huevo y el azúcar hasta que queden cremosas y pálidas.", "🥚", "home"),
    ("ladle", "cucharón para servir sopa", "A2", "/ˈleɪ.dəl/", "Use the soup ladle to serve hot chicken broth.", "Usa el cucharón para servir caldo de pollo caliente.", "🍲", "home"),
    ("grater", "rallador de queso o verduras", "A2", "/ˈɡreɪ.t̬ɚ/", "Grate fresh parmesan over the pasta with a box grater.", "Ralla parmesano fresco sobre la pasta con un rallador de cuatro caras.", "🧀", "home"),
    ("peeler", "pelador de papas o fruta", "A1", "/ˈpiː.lɚ/", "Peel the carrots and potatoes with a sharp vegetable peeler.", "Pela las zanahorias y papas con un pelador de verduras afilado.", "🥕", "home"),
    ("tongs", "pinzas de cocina o barbacoa", "A2", "/tɑːŋz/", "Turn the grilled steaks over using metal tongs.", "Voltea los filetes a la parrilla usando pinzas de metal.", "🥩", "home"),
    ("rolling pin", "rodillo para amasar", "A2", "/ˈroʊ.lɪŋ ˌpɪn/", "Roll out the pizza dough smoothly with a wooden rolling pin.", "Extiende la masa de pizza suavemente con un rodillo de madera.", "🍕", "home"),
    ("cutting board", "tabla para picar alimentos", "A1", "/ˈkʌt.ɪŋ ˌbɔːrd/", "Chop fresh onions and bell peppers on the wooden cutting board.", "Pica cebollas y pimientos frescos en la tabla de picar de madera.", "🧅", "home"),
    ("oven mitt", "guante para horno térmico", "A1", "/ˈʌv.ən ˌmɪt/", "Always wear an oven mitt when taking hot baking pans out.", "Siempre usa un guante para horno al sacar moldes calientes.", "🧤", "home"),
    ("apron", "delantal de cocina o taller", "A1", "/ˈeɪ.prən/", "Put on your cotton apron before baking chocolate cupcakes.", "Ponte el delantal de algodón antes de hornear pastelitos de chocolate.", "🧁", "home"),
    ("blender", "licuadora eléctrica", "A1", "/ˈblen.dɚ/", "Blend fresh strawberries, bananas, and milk into a smoothie.", "Licúa fresas frescas, plátanos y leche para hacer un batido.", "🍓", "home"),
    ("toaster", "tostadora de pan", "A1", "/ˈtoʊ.stɚ/", "Pop two slices of whole wheat bread into the toaster.", "Coloca dos rebanadas de pan integral en la tostadora.", "🍞", "home"),
    ("kettle", "tetera o hervidor de agua", "A1", "/ˈket̬.əl/", "The electric kettle boils cold water in under two minutes.", "El hervidor eléctrico hierve agua fría en menos de dos minutos.", "🫖", "home"),
    ("coffee grinder", "molinillo de café", "A2", "/ˈkɑː.fi ˌɡraɪn.dɚ/", "Grind aromatic coffee beans fresh every morning.", "Muele granos de café aromáticos frescos cada mañana.", "☕", "home"),
    ("measuring cup", "taza medidora graduada", "A1", "/ˈmeʒ.ɚ.ɪŋ ˌkʌp/", "Pour exactly two cups of milk using the glass measuring cup.", "Vierte exactamente dos tazas de leche usando la taza medidora de vidrio.", "🥛", "home"),
    ("measuring spoon", "cuchara medidora", "A1", "/ˈmeʒ.ɚ.ɪŋ ˌspuːn/", "Add one level measuring spoon of pure vanilla extract.", "Agrega una cuchara medidora al ras de extracto puro de vainilla.", "🥄", "home"),
    ("saucepan", "cacerola u olla mediana", "A2", "/ˈsɑː.spæn/", "Simmer the homemade marinara sauce in a stainless saucepan.", "Cocina a fuego lento la salsa marinara casera en una cacerola de acero.", "🥫", "home"),
    ("frying pan", "sartén para freír", "A1", "/ˈfraɪ.ɪŋ ˌpæn/", "Fry sunny-side-up eggs in a non-stick frying pan.", "Fríe huevos estrellados en una sartén antiadherente.", "🍳", "home"),
    ("baking sheet", "bandeja para hornear", "A2", "/ˈbeɪ.kɪŋ ˌʃiːt/", "Arrange chocolate chip cookies evenly on the greased baking sheet.", "Acomoda galletas de chispas de chocolate en la bandeja para hornear.", "🍪", "home"),
    ("ice tray", "cubeta para cubitos de hielo", "A1", "/ˈaɪs ˌtreɪ/", "Refill the silicone ice tray with fresh drinking water.", "Vuelve a llenar la cubeta de hielo de silicona con agua potable.", "🧊", "home"),
    ("thermos", "termo térmico para bebidas", "A2", "/ˈθɝː.məs/", "Keep hot herbal tea warm all day in an insulated thermos.", "Mantén el té de hierbas caliente todo el día en un termo térmico.", "☕", "home"),
    ("coaster", "portavasos protector", "A2", "/ˈkoʊ.stɚ/", "Place cold iced drinks on a cork coaster to protect wooden tables.", "Coloca bebidas frías con hielo sobre un portavasos para proteger la mesa.", "🪵", "home"),
    ("placemat", "mantel individual de mesa", "A2", "/ˈpleɪs.mæt/", "Set woven placemats beneath dinner plates before guests arrive.", "Coloca manteles individuales de tela bajo los platos antes de que lleguen.", "🍽️", "home"),
    ("napkin", "servilleta de papel o tela", "A1", "/ˈnæp.kɪn/", "Wipe your lips gently with a soft cotton dinner napkin.", "Límpiate los labios suavemente con una servilleta de algodón.", "🧻", "home"),
    ("toothpick", "palillo de dientes", "A1", "/ˈtuːθ.pɪk/", "Use a wooden toothpick to test whether the cake is baked through.", "Usa un palillo de madera para verificar si el pastel está bien horneado.", "🍰", "home"),
    ("straw", "popote / pajilla / cañita", "A1", "/strɑː/", "Sip fresh iced lemonade through a reusable stainless steel straw.", "Toma limonada fresca con hielo a través de una pajilla reutilizable.", "🥤", "home"),
    ("funnel", "embudo para líquidos", "A2", "/ˈfʌn.əl/", "Pour extra virgin olive oil into the glass bottle through a funnel.", "Vierte aceite de oliva extra virgen en la botella de vidrio con un embudo.", "🫒", "home"),
    ("can opener", "abrelatas manual", "A1", "/ˈkæn ˌoʊ.pən.ɚ/", "Open the can of crushed peeled tomatoes with a sturdy can opener.", "Abre la lata de tomates pelados triturados con un abrelatas resistente.", "🥫", "home"),

    # Workshop, Tools & Hardware (A2, B1)
    ("pliers", "alicates / pinzas de fuerza", "A2", "/ˈplaɪ.ɚz/", "Grip and twist the copper wire tightly with steel pliers.", "Sujeta y retuerce el alambre de cobre firmemente con unos alicates.", "🔧", "home"),
    ("wrench", "llave inglesa de tuercas", "A2", "/rentʃ/", "Tighten the loose plumbing nut beneath the sink with an adjustable wrench.", "Aprieta la tuerca floja bajo el fregadero con una llave inglesa.", "🔩", "home"),
    ("screwdriver", "destornillador / desarmador", "A2", "/ˈskruːˌdraɪ.vɚ/", "Fasten the hinge screws using a flathead or Phillips screwdriver.", "Fija los tornillos de la bisagra con un destornillador plano o de cruz.", "🪛", "home"),
    ("tape measure", "cinta métrica / flexómetro", "A2", "/ˈteɪp ˌmeʒ.ɚ/", "Measure the bedroom window frame width with a retracting tape measure.", "Mide el ancho del marco de la ventana con una cinta métrica retráctil.", "📏", "home"),
    ("handsaw", "serrucho manual para madera", "A2", "/ˈhænd.sɑː/", "Saw through the pine timber plank using a sharp handsaw.", "Corta el tablón de madera de pino usando un serrucho afilado.", "🪚", "home"),
    ("sandpaper", "papel de lija / lija", "A2", "/ˈsændˌpeɪ.pɚ/", "Smooth rough edges of the restored wooden chair with fine sandpaper.", "Suaviza los bordes ásperos de la silla de madera con lija fina.", "🪵", "home"),
    ("chisel", "cincel para madera o piedra", "B1", "/ˈtʃɪz.əl/", "The woodcarver shaped delicate leaf reliefs with a sharp steel chisel.", "El tallador moldeó delicados relieves de hojas con un cincel de acero.", "🪵", "home"),
    ("drill", "taladro eléctrico / taladrar", "A2", "/drɪl/", "Drill pilot holes into the drywall before inserting wall anchors.", "Haz agujeros guía en la pared de yeso antes de meter los taquetes.", "🪛", "home"),
    ("flashlight", "linterna portátil de mano", "A1", "/ˈflæʃ.laɪt/", "Turn on the battery flashlight when walking through dark basements.", "Enciende la linterna de mano al caminar por sótanos oscuros.", "🔦", "home"),
    ("stepladder", "escalera de mano plegable", "A2", "/ˈstepˌlæd.ɚ/", "Climb the aluminum stepladder to replace the high ceiling bulb.", "Sube por la escalera de mano de aluminio para cambiar el foco del techo.", "🪜", "home"),
    ("extension cord", "cable de extensión eléctrica", "A2", "/ɪkˈsten.ʃən ˌkɔːrd/", "Plug garden power tools into a heavy-duty outdoor extension cord.", "Conecta herramientas del jardín a un cable de extensión de uso rudo.", "🔌", "home"),
    ("duct tape", "cinta adhesiva de uso rudo", "A2", "/ˈdʌkt ˌteɪp/", "Temporarily seal the leaky vacuum hose with silver duct tape.", "Sella temporalmente la manguera de aspiradora rota con cinta plateada.", "🩹", "home"),
    ("superglue", "pegamento instantáneo", "A2", "/ˈsuː.pɚ.ɡluː/", "Repair the cracked ceramic teacup handle with a drop of superglue.", "Repara el asa rota de la taza de té de cerámica con pegamento instantáneo.", "🧴", "home"),
    ("paintbrush", "brocha o pincel para pintar", "A1", "/ˈpeɪnt.brʌʃ/", "Dip the wide bristle paintbrush into fresh sky-blue wall paint.", "Moja la brocha ancha de cerdas en pintura azul cielo fresca para paredes.", "🖌️", "home"),
    ("paint roller", "rodillo para pintar paredes", "A2", "/ˈpeɪnt ˌroʊ.lɚ/", "Roll smooth latex paint across bedroom walls with a foam paint roller.", "Aplica pintura de látex en las paredes usando un rodillo de espuma.", "🎨", "home"),
    ("toolbox", "caja de herramientas", "A1", "/ˈtuːl.bɑːks/", "Store hammers, nails, screwdrivers, and pliers neatly in the red metal toolbox.", "Guarda martillos, clavos y pinzas ordenados en la caja de herramientas roja.", "🧰", "home"),
    ("workbench", "banco de trabajo / mesón de taller", "A2", "/ˈwɝːk.bentʃ/", "Clamp wooden chair legs firmly onto the heavy oak workbench.", "Sujeta las patas de madera de la silla firmemente al banco de trabajo de roble.", "🔨", "home"),
    ("anvil", "yunque de herrería", "B1", "/ˈæn.vɪl/", "The blacksmith hammered glowing red iron horseshoes on a heavy steel anvil.", "El herrero martilló herraduras de hierro al rojo vivo sobre el yunque de acero.", "⚒️", "home"),
    ("vise", "tornillo de banco / prensa de fijación", "B1", "/vaɪs/", "Secure the iron pipe tightly in the benchtop vise before cutting.", "Fija el tubo de hierro firmemente en el tornillo de banco antes de cortar.", "🗜️", "home"),
    ("wheelbarrow", "carretilla de mano de jardín", "A2", "/ˈwiːlˌber.oʊ/", "Transport rich garden soil and compost in a sturdy metal wheelbarrow.", "Transporta tierra rica de jardín y abono en una carretilla de metal resistente.", "🪴", "home"),
    ("lawnmower", "cortadora de césped", "A2", "/ˈlɑːnˌmoʊ.ɚ/", "Mow the front green grass every Saturday with a cordless lawnmower.", "Corta el pasto verde cada sábado con una podadora inalámbrica.", "🌱", "home"),
    ("hedge trimmer", "cortasetos de jardín", "B1", "/ˈhedʒ ˌtrɪm.ɚ/", "Trim ornamental boundary hedges neatly with an electric hedge trimmer.", "Recorta los setos del jardín de manera prolija con un cortasetos eléctrico.", "🌳", "home"),
    ("rake", "rastrillo para hojas secas / rastrillar", "A2", "/reɪk/", "Rake dry autumn leaves into large colorful backyard piles.", "Rastrilla las hojas secas de otoño en grandes montones coloridos en el patio.", "🍂", "home"),
    ("watering can", "regadera para plantas", "A1", "/ˈwɑː.t̬ɚ.ɪŋ ˌkæn/", "Water indoor potted ferns gently using a green plastic watering can.", "Riega los helechos en maceta suavemente usando una regadera verde de plástico.", "🪴", "home"),
    ("garden hose", "manguera de riego para jardín", "A1", "/ˈɡɑːr.dən ˌhoʊz/", "Connect the rubber garden hose to wash the car and water tomato plants.", "Conecta la manguera de goma para lavar el carro y regar las plantas de tomate.", "💧", "home"),

    # Stationery, Study & School (A1, A2, B1)
    ("stapler", "engrapadora / grapadora", "A1", "/ˈsteɪ.plɚ/", "Fasten printed report pages together neatly with a desk stapler.", "Une las hojas del reporte impreso prolijamente con una grapadora de escritorio.", "📎", "education"),
    ("paperclip", "clip para sujetar papeles", "A1", "/ˈpeɪ.pɚ.klɪp/", "Clip the business receipt to the expense invoice with a steel paperclip.", "Sujeta el recibo a la factura con un clip de acero para papeles.", "📎", "education"),
    ("highlighter", "marcador resaltador fluorescente", "A1", "/ˈhaɪˌlaɪ.t̬ɚ/", "Highlight key textbook vocabulary terms with a bright yellow highlighter.", "Resalta términos clave del libro con un resaltador amarillo brillante.", "🖍️", "education"),
    ("binder", "carpeta de argollas / archivador", "A2", "/ˈbaɪn.dɚ/", "Organize class study notes by subject in a three-ring binder.", "Organiza los apuntes de clase por materia en una carpeta de tres argollas.", "📁", "education"),
    ("pencil sharpener", "sacapuntas de lápices", "A1", "/ˈpen.səl ˌʃɑːr.pən.ɚ/", "Sharpen dull graphite drawing pencils in the small metal pencil sharpener.", "Saca punta a los lápices de dibujo desafilados en el sacapuntas de metal.", "✏️", "education"),
    ("whiteboard", "pizarra blanca de marcadores", "A1", "/ˈwaɪt.bɔːrd/", "Write homework assignments clearly on the classroom whiteboard.", "Anota las tareas de casa claramente en la pizarra blanca del salón.", "📋", "education"),
    ("eraser", "goma de borrar", "A1", "/ɪˈreɪ.sɚ/", "Erase accidental pencil marks cleanly without tearing notebook paper.", "Borra marcas accidentales de lápiz limpiamente sin romper la hoja.", "🧼", "education"),
    ("ruler", "regla graduada para medir", "A1", "/ˈruː.lɚ/", "Draw crisp straight lines in your math notebook using a thirty-centimeter ruler.", "Traza líneas rectas en tu libreta de matemáticas con una regla de treinta centímetros.", "📏", "education"),
    ("protractor", "transportador de ángulos", "A2", "/proʊˈtræk.tɚ/", "Measure ninety-degree and acute triangle angles with a transparent protractor.", "Mide ángulos rectos y agudos de triángulos con un transportador transparente.", "📐", "education"),
    ("compass", "compás de dibujo para círculos", "A2", "/ˈkʌm.pəs/", "Draw perfect concentric circles in geometry class with a metal compass.", "Dibuja círculos concéntricos perfectos en geometría con un compás de metal.", "⭕", "education"),
    ("pushpin", "chincheta / chinche de corcho", "A2", "/ˈpʊʃ.pɪn/", "Pin colorful festival flyers onto the classroom cork bulletin board with pushpins.", "Fija volantes coloridos del festival en el corcho con chinchetas.", "📌", "education"),
    ("hole punch", "perforadora de papel", "A2", "/ˈhoʊl ˌpʌntʃ/", "Punch neat holes in loose paper handouts before filing them in folders.", "Haz perforaciones en las hojas sueltas antes de archivarlas en carpetas.", "📄", "education"),
    ("clipboard", "portapapeles con clip de apoyo", "A2", "/ˈklɪp.bɔːrd/", "Nurses carry patient health charts on lightweight plastic clipboards.", "Las enfermeras llevan las gráficas de pacientes en portapapeles con clip.", "📋", "education"),
    ("notepaper", "papel para notas / bloc de notas", "A1", "/ˈnoʊtˌpeɪ.pɚ/", "Scribble down your grocery shopping list on a sheet of lined notepaper.", "Escribe tu lista de compras del súper en una hoja de bloc de notas rayado.", "📝", "education"),
    ("index card", "ficha bibliográfica de estudio", "A2", "/ˈɪn.deks ˌkɑːrd/", "Review vocabulary definitions written on color-coded flashcard index cards.", "Repasa definiciones de vocabulario escritas en fichas de estudio de colores.", "🗂️", "education"),
    ("fountain pen", "pluma estilográfica de tinta", "B1", "/ˈfaʊn.tən ˌpen/", "Sign prestigious graduation diplomas using a smooth gold-nib fountain pen.", "Firma diplomas prestigiosos de graduación con una pluma estilográfica dorada.", "✒️", "education"),
    ("ballpoint", "bolígrafo / pluma de punta redonda", "A1", "/ˈbɑːl.pɔɪnt/", "Blue ballpoint pens write smoothly on standard printed documents.", "Los bolígrafos de tinta azul escriben suavemente en documentos impresos.", "🖊️", "education"),
    ("ink cartridge", "cartucho de tinta", "A2", "/ˈɪŋk ˌkɑːr.trɪdʒ/", "Replace the empty black ink cartridge in the office computer printer.", "Reemplaza el cartucho vacío de tinta negra en la impresora de la oficina.", "🖨️", "education"),
    ("pencil case", "estuche lapicera / cartuchera", "A1", "/ˈpen.səl ˌkeɪs/", "Zip pencils, erasers, scissors, and markers safely into your pencil case.", "Guarda lápices, gomas, tijeras y marcadores con cierre en tu lapicera.", "✏️", "education"),
    ("backpack", "mochila escolar o de viaje", "A1", "/ˈbæk.pæk/", "Pack your textbooks, lunchbox, and water bottle inside the padded backpack.", "Guarda tus libros de texto, lonchera y botella de agua dentro de la mochila.", "🎒", "education"),

    # Clothing, Fabrics & Accessories (A1, A2, B1)
    ("cardigan", "cárdigan / suéter abierto con botones", "A2", "/ˈkɑːr.dɪ.ɡən/", "Button up a cozy wool cardigan on chilly autumn mornings.", "Abróchate un cómodo cárdigan de lana en las mañanas frescas de otoño.", "🧶", "clothes"),
    ("hoodie", "sudadera con capucha", "A1", "/ˈhʊd.i/", "Pull the drawstring hoodie over your head when it starts to drizzle.", "Ponte la sudadera con capucha cuando empiece a lloviznar.", "🧥", "clothes"),
    ("trench coat", "gabardina impermeable elegante", "B1", "/ˈtrentʃ ˌkoʊt/", "A classic beige trench coat protects business suits from sudden rainstorms.", "Una clásica gabardina beige protege los trajes de lluvia repentina.", "🧥", "clothes"),
    ("windbreaker", "rompevientos ligero", "A2", "/ˈwɪndˌbreɪ.kɚ/", "Wear a zip-up nylon windbreaker while jogging on breezy coastal piers.", "Usa un rompevientos ligero de nailon al correr por muelles costeros ventosos.", "🏃", "clothes"),
    ("blazer", "saco casual / blazer formal", "A2", "/ˈbleɪ.zɚ/", "Pair a navy blue tailored blazer with khakis for casual meetings.", "Combina un saco blazer azul marino con pantalones caqui para reuniones.", "👔", "clothes"),
    ("vest", "chaleco sin mangas", "A1", "/vest/", "Wear a warm fleece vest over long-sleeve shirts in cool weather.", "Usa un chaleco cálido de forro polar sobre camisas de manga larga.", "🦺", "clothes"),
    ("suspenders", "tirantes para pantalón", "A2", "/səˈspen.dɚz/", "Fasten vintage leather suspenders to your trousers instead of belts.", "Sujeta tirantes de cuero vintage a tus pantalones en vez de cinturón.", "👖", "clothes"),
    ("beret", "boina de lana francesa", "A2", "/bəˈreɪ/", "She tilted a stylish black wool beret over her curled hair.", "Ella inclinó una elegante boina negra de lana sobre su cabello rizado.", "👒", "clothes"),
    ("fedora", "sombrero fedora clásico", "B1", "/fəˈdɔːr.ə/", "The jazz musician tipped his felt fedora politely toward the applauding crowd.", "El músico de jazz inclinó su sombrero fedora de fieltro hacia el público.", "🎩", "clothes"),
    ("beanie", "gorro de lana tejido de invierno", "A1", "/ˈbiː.ni/", "Pull a snug ribbed knit beanie down over cold ears in January.", "Ponte un gorro de lana tejido bien ajustado sobre las orejas en enero.", "🧶", "clothes"),
    ("earmuffs", "orejeras protectoras para el frío", "A1", "/ˈɪr.mʌfs/", "Fuzzy faux-fur earmuffs keep ears toasty on freezing morning walks.", "Orejeras de peluche mantienen las orejas calientitas en paseos gélidos.", "🎧", "clothes"),
    ("mittens", "mitones de lana sin dedos separados", "A1", "/ˈmɪt.ənz/", "Children wear waterproof mittens while building snowmen in winter.", "Los niños usan mitones impermeables mientras arman muñecos de nieve.", "🧤", "clothes"),
    ("bathrobe", "bata de baño afelpada", "A1", "/ˈbæθ.roʊb/", "Wrap yourself in a thick cotton terrycloth bathrobe after hot showers.", "Envuélvete en una bata de baño de felpa de algodón tras una ducha caliente.", "🧖", "clothes"),
    ("slippers", "pantuflas cómodas para casa", "A1", "/ˈslɪp.ɚz/", "Slip into soft fleece slippers as soon as you step inside the house.", "Ponte unas pantuflas suaves de forro polar en cuanto entres a la casa.", "🥿", "clothes"),
    ("flip-flops", "chanclas de playa / sandalias de goma", "A1", "/ˈflɪp.flɑːps/", "Wear rubber flip-flops when walking across hot sandy ocean beaches.", "Usa chanclas de goma al caminar por playas de arena caliente del mar.", "🩴", "clothes"),
    ("cufflinks", "mancuernillas / gemelos de camisa", "B1", "/ˈkʌf.lɪŋks/", "Fasten formal tuxedo dress cuffs with polished sterling silver cufflinks.", "Abrocha los puños del esmoquin formal con gemelos pulidos de plata esterlina.", "✨", "clothes"),
    ("shoelaces", "agujetas / cordones de zapatos", "A1", "/ˈʃuː.leɪ.sɪz/", "Tie your athletic sneaker shoelaces in a secure double knot.", "Átate las agujetas de los tenis deportivos con un nudo doble seguro.", "👟", "clothes"),
    ("buckle", "hebilla de metal de cinturón", "A1", "/ˈbʌk.əl/", "The antique belt buckle is forged from solid brass.", "La hebilla de cinturón antigua está forjada en latón macizo.", "🪡", "clothes"),
    ("brooch", "broche prendedor de joyería", "B1", "/broʊtʃ/", "She pinned an antique pearl brooch onto the lapel of her velvet jacket.", "Prendió un broche antiguo de perla en la solapa de su chaqueta de terciopelo.", "🧷", "clothes"),
    ("pendant", "dije colgante de collar", "A2", "/ˈpen.dənt/", "A sparkling sapphire pendant hung gracefully from a fine gold necklace.", "Un dije de zafiro brillante colgaba de un fino collar de oro.", "💎", "clothes")
]
"""

# Batch 2: Nature, Wildlife, Marine Life & Geography (~400 items)
BATCH_NATURE_DATA = """
BATCH_NATURE = [
    # Wildlife, Birds, Insects & Sea Life (A1, A2, B1)
    ("hedgehog", "erizo terrestre espinoso", "A2", "/ˈhedʒ.hɑːɡ/", "A tiny hedgehog rolled into a prickly ball among garden leaves.", "Un pequeño erizo se hizo una bola espinosa entre hojas de jardín.", "🦔", "animals"),
    ("badger", "tejón excavador", "B1", "/ˈbædʒ.ɚ/", "The nocturnal European badger digs complex underground burrow networks.", "El tejón europeo nocturno cava complejas redes de madrigueras subterráneas.", "🦡", "animals"),
    ("otter", "nutria de río o marina", "A2", "/ˈɑː.t̬ɚ/", "Playful river otters slide down muddy banks into cool mountain streams.", "Nutrias juguetonas de río se deslizan por orillas lodosas hacia arroyos.", "🦦", "animals"),
    ("beaver", "castor constructor de presas", "A2", "/ˈbiː.vɚ/", "Beavers build sturdy timber dams across tranquil forest creeks.", "Los castores construyen resistentes presas de madera en arroyos del bosque.", "🪵", "animals"),
    ("walrus", "morsa ártica con colmillos", "A2", "/ˈwɑːl.rəs/", "A giant walrus hauled its massive body onto floating Arctic pack ice.", "Una morsa gigante subió su enorme cuerpo sobre témpanos de hielo ártico.", "🦭", "animals"),
    ("platypus", "ornitorrinco semiacuático", "B1", "/ˈplæt̬.ə.pʊs/", "The unique duck-billed platypus lays eggs and swims in Australian creeks.", "El singular ornitorrinco pone huevos y nada en arroyos de Australia.", "🦆", "animals"),
    ("lemur", "lémur de cola anillada", "A2", "/ˈliː.mɚ/", "Ring-tailed lemurs leap gracefully through treetops in Madagascar.", "Lémures de cola anillada saltan con agilidad entre copas de árboles en Madagascar.", "🐒", "animals"),
    ("meerkat", "suricata centinela", "A2", "/ˈmɪr.kæt/", "A watchful meerkat stood upright on its hind legs scanning for hawks.", "Una suricata alerta se paró erguida sobre dos patas vigilando si había halcones.", "🐾", "animals"),
    ("chameleon", "camaleón que cambia de color", "A2", "/kəˈmiː.li.ən/", "The green chameleon changed its skin shade to blend with leaves.", "El camaleón verde cambió el tono de su piel para camuflarse con las hojas.", "🦎", "animals"),
    ("seahorse", "caballito de mar", "A2", "/ˈsiː.hɔːrs/", "A delicate golden seahorse curled its tail around ocean seagrass.", "Un delicado caballito de mar dorado enroscó su cola en pastos marinos.", "🌊", "animals"),
    ("jellyfish", "medusa marina transparente", "A1", "/ˈdʒel.i.fɪʃ/", "Translucent jellyfish pulse gracefully through tropical ocean waters.", "Medusas translúcidas pulsan con gracia a través de aguas oceánicas tropicales.", "🪼", "animals"),
    ("starfish", "estrella de mar", "A1", "/ˈstɑːr.fɪʃ/", "Bright orange starfish cling firmly to rocky tidal pool stones.", "Estrellas de mar naranja brillante se aferran con fuerza a piedras de pozas marinas.", "⭐", "animals"),
    ("sea urchin", "erizo de mar espinoso", "A2", "/ˈsiː ˌɝː.tʃɪn/", "Be careful not to step on spiky black sea urchins on coral reefs.", "Ten cuidado de no pisar erizos de mar negros y espinosos en arrecifes de coral.", "🪸", "animals"),
    ("pelican", "pelícano pescador de pico grande", "A2", "/ˈpel.ə.kən/", "Pelicans scoop mouthfuls of small fish into large throat pouches.", "Los pelícanos recogen peces pequeños en sus grandes bolsas de la garganta.", "🌊", "animals"),
    ("toucan", "tucán tropical de pico colorido", "A1", "/ˈtuː.kæn/", "A vibrant toucan perched on a rainforest branch calling loudly.", "Un vibrante tucán se posó en una rama de la selva cantando fuerte.", "🦜", "animals"),
    ("woodpecker", "pájaro carpintero", "A2", "/ˈwʊdˌpek.ɚ/", "The red-crested woodpecker pecked rhythmically on the hollow tree trunk.", "El pájaro carpintero de cresta roja picó rítmicamente en el tronco hueco.", "🪵", "animals"),
    ("hummingbird", "colibrí / picaflor veloz", "A2", "/ˈhʌm.ɪŋ.bɝːd/", "Tiny iridescent hummingbirds hover before sweet hibiscus nectar blossoms.", "Diminutos colibríes tornasolados flotan frente a flores de hibisco.", "🌸", "animals"),
    ("firefly", "luciérnaga luminosa", "A2", "/ˈfaɪr.flaɪ/", "Glowing yellow fireflies flickered across the warm summer meadow at dusk.", "Luciérnagas amarillas brillantes parpadearon en el prado veraniego al anochecer.", "✨", "animals"),
    ("dragonfly", "libélula acuática ágil", "A2", "/ˈdræɡ.ən.flaɪ/", "A blue dragonfly hovered motionless over the tranquil water lily pond.", "Una libélula azul flotó inmóvil sobre el estanque apacible de nenúfares.", "🪷", "animals"),
    ("grasshopper", "saltamontes / saltamontes de prado", "A1", "/ˈɡræsˌhɑː.pɚ/", "Green grasshoppers leap among tall wheat stalks on sunny afternoons.", "Saltamontes verdes brincan entre espigas altas de trigo en tardes soleadas.", "🌾", "animals"),
    ("praying mantis", "mantis religiosa cazadora", "B1", "/ˌpreɪ.ɪŋ ˈmæn.t̬ɪs/", "The praying mantis held its front legs folded patiently waiting for prey.", "La mantis religiosa mantuvo sus patas delanteras dobladas esperando presas.", "🦗", "animals"),
    ("ladybug", "mariquita / catarinas rojas", "A1", "/ˈleɪ.di.bʌɡ/", "A bright red spotted ladybug crawled gently along the green leaf.", "Una mariquita con motas rojas y brillantes avanzó suavemente por la hoja verde.", "🐞", "animals"),
    ("caterpillar", "oruga que se transforma en mariposa", "A1", "/ˈkæt̬.ɚ.pɪl.ɚ/", "Striped monarch caterpillars feed voraciously on fresh green milkweed leaves.", "Orugas monarca a rayas se alimentan con apetito de hojas de algodoncillo.", "🐛", "animals"),
    ("tadpole", "renacuajo de rana", "A2", "/ˈtæd.poʊl/", "Hundreds of tiny black tadpoles wriggled through shallow pond water.", "Cientos de renacuajos negros se retorcían en las aguas poco profundas del charco.", "🐸", "animals"),
    ("stingray", "raya marina con aguijón", "A2", "/ˈstɪŋ.reɪ/", "A spotted eagle stingray glided smoothly across the sandy sea floor.", "Una raya águila moteada se deslizó suavemente sobre el fondo marino arenoso.", "🌊", "animals"),

    # Weather, Geography & Earth (A1, A2, B1)
    ("blizzard", "ventisca de nieve cegadora", "A2", "/ˈblɪz.ɚd/", "The violent winter blizzard shut down mountain highway passes for days.", "La violenta ventisca invernal cerró los pasos carreteros de montaña por días.", "❄️", "nature"),
    ("drizzle", "llovizna suave / lloviznar", "A1", "/ˈdrɪz.əl/", "A light morning drizzle moistened city pavements without requiring umbrellas.", "Una ligera llovizna matutina humedeció el pavimento sin requerir paraguas.", "🌧️", "nature"),
    ("hailstorm", "granizada fuerte con granizo", "A2", "/ˈheɪl.stɔːrm/", "The sudden summer hailstorm pelted parked cars with marble-sized ice balls.", "La repentina granizada de verano golpeó autos con bolas de hielo como canicas.", "🌨️", "nature"),
    ("whirlpool", "remolino de agua potente", "B1", "/ˈwɝːl.puːl/", "Fierce tidal ocean currents created a spinning whirlpool near rocky cliffs.", "Fuertes corrientes oceánicas crearon un remolino giratorio cerca de los acantilados.", "🌀", "nature"),
    ("geyser", "géiser de vapor hirviente", "B1", "/ˈɡaɪ.zɚ/", "The famous volcanic geyser erupts towering columns of boiling water and steam.", "El famoso géiser volcánico expulsa altas columnas de agua hirviendo y vapor.", "🌋", "nature"),
    ("plateau", "meseta elevada / altiplano", "B1", "/plæˈtoʊ/", "A windswept semi-arid plateau stretched endlessly toward distant mountains.", "Una meseta semiárida barrida por el viento se extendía hacia montañas lejanas.", "🏜️", "nature"),
    ("peninsula", "península rodeada de mar", "B1", "/pəˈnɪn.sə.lə/", "The rocky coastal peninsula jutted five miles into the crashing blue surf.", "La rocosa península costera se adentraba cinco millas en el oleaje azul.", "🏝️", "nature"),
    ("archipelago", "archipiélago con islas", "B1", "/ˌɑːr.kəˈpel.ə.ɡoʊ/", "Sailing yachts navigated between scattered green islets of the archipelago.", "Veleros navegaron entre islotes verdes dispersos del archipiélago.", "⛵", "nature"),
    ("savannah", "sabana tropical herbácea", "A2", "/səˈvæn.ə/", "Herds of zebras migrate across the golden African savannah during dry months.", "Manadas de cebras migran por la dorada sabana africana durante la sequía.", "🌾", "nature"),
    ("tundra", "tundra ártica helada", "B1", "/ˈtʌn.drə/", "Hardy lichens and mosses carpet the treeless expanses of Arctic tundra.", "Líquenes y musgos resistentes cubren las extensiones sin árboles de la tundra.", "🧊", "nature"),
    ("estuary", "estuario donde desemboca río", "B1", "/ˈes.tʃu.er.i/", "Migratory flamingos and herons forage for shrimp in the tidal estuary.", "Flamencos y garzas migratorias buscan camarones en el estuario de marea.", "🦩", "nature"),
    ("creek", "riachuelo / arroyo de agua clara", "A2", "/kriːk/", "Children caught small silver minnows with nets in the shallow forest creek.", "Niños pescaron pececillos plateados con redes en el arroyo del bosque.", "🏞️", "nature"),
    ("glacier", "glaciar de hielo milenario", "A2", "/ˈɡleɪ.ʃɚ/", "Chunks of blue ice calved from the massive coastal glacier into the bay.", "Bloques de hielo azul se desprendieron del glaciar costero hacia la bahía.", "🧊", "nature"),
    ("avalanche", "avalancha / alud de nieve", "B1", "/ˈæv.əl.æntʃ/", "Ski patrol teams trigger controlled blasting to prevent disastrous avalanches.", "Equipos de patrulla de esquí activan detonaciones para evitar avalanchas.", "🏔️", "nature"),
    ("monsoon", "monzón de lluvias torrenciales", "B1", "/mɑːnˈsuːn/", "Seasonal monsoon storms brought nourishing rainfall to parched rice paddies.", "Tormentas monzónicas trajeron lluvias que regaron los secos arrozales.", "🌧️", "nature")
]
"""

# Batch 3: Actions, Cognition & Emotions (~500 items)
BATCH_ACTIONS_DATA = """
BATCH_ACTIONS = [
    # Practical Action Verbs (A1, A2, B1)
    ("scrub", "restregar / fregar con fuerza", "A1", "/skrʌb/", "Scrub the bathroom floor tiles with a stiff brush and soapy water.", "Restriega las baldosas del baño con un cepillo duro y agua jabonosa.", "🧼", "verbs_action"),
    ("rinse", "enjuagar con agua limpia", "A1", "/rɪns/", "Rinse fresh apples under cold running tap water before eating them.", "Enjuaga manzanas frescas bajo el chorro de agua fría antes de comerlas.", "🍎", "verbs_action"),
    ("squeeze", "exprimir jugo / apretar", "A1", "/skwiːz/", "Squeeze fresh lemon juice over grilled fish fillets.", "Exprime jugo de limón fresco sobre los filetes de pescado a la plancha.", "🍋", "verbs_action"),
    ("whisk", "batir con batidor de varillas", "A2", "/wɪsk/", "Whisk heavy cream vigorously until stiff peaks form.", "Bate crema espesa con energía hasta que se formen picos firmes.", "🧁", "verbs_action"),
    ("dice", "cortar en cubitos / dados", "A2", "/daɪs/", "Dice ripe red tomatoes and red onions into tiny uniform cubes.", "Corta tomates rojos maduros y cebollas en cubos diminutos y parejos.", "🧅", "verbs_action"),
    ("knead", "amasar masa de pan con manos", "A2", "/niːd/", "Knead sourdough bread dough on a floured surface for ten minutes.", "Amasa la masa de pan de masa madre en una superficie enharinada por diez minutos.", "🥖", "verbs_action"),
    ("assemble", "ensamblar piezas de muebles", "A2", "/əˈsem.bəl/", "Assemble the wooden bookshelf step by step following illustrated diagrams.", "Ensambla el librero de madera paso a paso siguiendo diagramas ilustrados.", "🪑", "verbs_action"),
    ("dismantle", "desmantelar / desarmar máquinas", "B1", "/dɪsˈmæn.təl/", "Mechanics dismantled the worn automobile engine to replace broken gaskets.", "Mecánicos desarmaron el motor desgastado para cambiar empaques rotos.", "🔧", "verbs_action"),
    ("tighten", "apretar tuercas o tornillos", "A2", "/ˈtaɪ.tən/", "Tighten bicycle handlebar bolts with an Allen wrench.", "Aprieta los tornillos del manubrio de la bicicleta con una llave Allen.", "🚲", "verbs_action"),
    ("loosen", "aflojar correas o nudos", "A2", "/ˈluː.sən/", "Loosen tight neckties after finishing exhausting job interviews.", "Afloja corbatas apretadas tras terminar agotadoras entrevistas de trabajo.", "👔", "verbs_action"),
    ("unfold", "desplegar mapas o sábanas", "A2", "/ʌnˈfoʊld/", "Unfold the giant national road map across the dining table.", "Despliega el enorme mapa de carreteras sobre la mesa del comedor.", "🗺️", "verbs_action"),
    ("wrap", "envolver regalos en papel", "A1", "/ræp/", "Wrap birthday gifts in colorful foil paper and festive satin ribbons.", "Envuelve regalos de cumpleaños en papel brillante y listones de satén.", "🎁", "verbs_action"),
    ("unwrap", "desenvolver paquetes", "A1", "/ʌnˈræp/", "Children excitedly unwrap present packages on Christmas morning.", "Los niños desenvuelven emocionados los paquetes en la mañana de Navidad.", "🎄", "verbs_action"),
    ("sew", "coser prendas con hilo y aguja", "A1", "/soʊ/", "Sew torn hemline stitches with fine thread and a sharp needle.", "Cose las puntadas deshechas del dobladillo con hilo fino y una aguja.", "🪡", "verbs_action"),
    ("knit", "tejer con agujas de lana", "A2", "/nɪt/", "Grandmothers knit cozy warm wool scarves for their grandchildren.", "Las abuelas tejen bufandas de lana cálidas y cómodas para sus nietos.", "🧣", "verbs_action"),
    ("mend", "remendar prendas o cercas", "A2", "/mend/", "Mend holes in thick hiking socks before setting off on mountain treks.", "Remienda los agujeros de calcetines de montaña antes de iniciar la caminata.", "🧦", "verbs_action"),
    ("carve", "tallar figuras en madera", "A2", "/kɑːrv/", "Artisans carve lifelike animal figurines from aromatic cedar wood.", "Artesanos tallan figuras de animales realistas en madera aromática de cedro.", "🪵", "verbs_action"),
    ("sand", "lijar madera para pulir", "A2", "/sænd/", "Sand the oak tabletop thoroughly before brushing on varnish.", "Lija la cubierta de la mesa de roble a fondo antes de aplicar el barniz.", "🪵", "verbs_action"),
    ("varnish", "barnizar muebles de madera", "B1", "/ˈvɑːr.nɪʃ/", "Apply two protective coats of clear varnish to waterproof the deck.", "Aplica dos capas protectoras de barniz transparente para impermeabilizar.", "🪵", "verbs_action"),
    ("clamp", "prensar piezas firmemente", "B1", "/klæmp/", "Clamp glued wooden joints together until adhesive cures completely.", "Prensa las uniones de madera pegadas hasta que el adhesivo seque por completo.", "🗜️", "verbs_action"),

    # Mind & Thinking Verbs (A2, B1, B2)
    ("ponder", "meditar sobre opciones de vida", "B1", "/ˈpɑːn.dɚ/", "She walked along the beach to ponder important life career decisions.", "Caminó por la playa para meditar sobre decisiones importantes de carrera.", "🤔", "verbs_mind"),
    ("deliberate", "deliberar antes de juzgar", "B2", "/dɪˈlɪb.ə.reɪt/", "Juries deliberate for days before reaching unanimous guilty verdicts.", "Los jurados deliberan durante días antes de emitir un veredicto unánime.", "⚖️", "verbs_mind"),
    ("recollect", "rememorar recuerdos lejanos", "B1", "/ˌrek.əˈlekt/", "Elderly veterans recollected vivid memories of heroic wartime comrades.", "Veteranos ancianos rememoraron vívidos recuerdos de heroicos camaradas.", "🎖️", "verbs_mind"),
    ("envisage", "vislumbrar proyectos futuros", "B2", "/ɪnˈvɪz.ɪdʒ/", "Urban architects envisage green metropolitan skylines powered by solar panels.", "Arquitectos vislumbran horizontes urbanos verdes impulsados por paneles solares.", "🏙️", "verbs_mind"),
    ("deduce", "deducir conclusiones lógicas", "B1", "/dɪˈduːs/", "Investigators deduced the suspect's identity from microscopic shoe tracks.", "Investigadores dedujeron la identidad del sospechoso por huellas de zapatos.", "🔍", "verbs_mind"),
    ("infer", "inferir significados implícitos", "B2", "/ɪnˈfɝː/", "Readers infer underlying emotional tensions beneath polite dialogues.", "Lectores infieren tensiones emocionales latentes bajo diálogos cordiales.", "📖", "verbs_mind"),
    ("conjecture", "conjeturar sin certezas", "B2", "/kənˈdʒek.tʃɚ/", "Astrophysicists conjecture what lies at the bottom of galactic black holes.", "Astrofísicos conjeturan qué hay en el fondo de los agujeros negros galácticos.", "🌌", "verbs_mind"),
    ("theorize", "teorizar sobre causas", "B1", "/ˈθiː.ə.raɪz/", "Geologists theorize that continental drift triggered prehistoric ice ages.", "Geólogos teorizan que la deriva continental detonó eras de hielo prehistóricas.", "🌍", "verbs_mind"),
    ("discriminate", "discriminar / diferenciar matices", "B2", "/dɪˈskrɪm.ə.neɪt/", "Trained perfumers can discriminate between hundred varieties of jasmine oils.", "Perfumiistas entrenados pueden discriminar entre cien variedades de jazmín.", "🌺", "verbs_mind"),
    ("appraise", "tasar / valuar objetivamente", "B2", "/əˈpreɪz/", "Independent assessors appraise vintage jewelry collections for auction houses.", "Tasadores independientes valúan colecciones de joyas para casas de subastas.", "💎", "verbs_mind"),

    # Emotions, Virtues & Traits (A2, B1, B2)
    ("bewildered", "desconcertado / perplejo", "B1", "/bɪˈwɪl.dɚd/", "Tourists looked bewildered when subway lines suddenly shifted directions.", "Turistas lucían desconcertados cuando las líneas del metro cambiaron de rumbo.", "😵‍💫", "emotions"),
    ("ecstatic", "extasiado de felicidad pura", "B1", "/ekˈstæt̬.ɪk/", "The football team was ecstatic after scoring the championship winning goal.", "El equipo de fútbol estaba extasiado tras anotar el gol del campeonato.", "🏆", "emotions"),
    ("nostalgic", "nostálgico recordando el pasado", "B1", "/nɑːˈstæl.dʒɪk/", "Looking through old school albums made him feel wonderfully nostalgic.", "Ver álbumes de la vieja escuela lo hizo sentir maravillosamente nostálgico.", "📸", "emotions"),
    ("apprehensive", "aprensivo y temeroso", "B2", "/ˌæp.rəˈhen.sɪv/", "She felt apprehensive before entering the dental clinic surgery room.", "Se sintió aprensiva antes de entrar a la sala de cirugía dental.", "😰", "emotions"),
    ("serene", "sereno y en paz profunda", "A2", "/səˈriːn/", "The monk maintained a serene smile while meditating in mountain gardens.", "El monje mantuvo una sonrisa serena mientras meditaba en jardines de montaña.", "🧘", "emotions"),
    ("irritable", "irritable y de mal humor", "A2", "/ˈɪr.ə.t̬ə.bəl/", "Lack of sleep makes children cranky and easily irritable all morning.", "La falta de sueño pone a los niños quejumbrosos e irritables toda la mañana.", "😠", "emotions"),
    ("empathetic", "empático y comprensivo", "B1", "/ˌem.pəˈθet̬.ɪk/", "Empathetic nurses listen compassionately to anxious hospital patients.", "Enfermeras empáticas escuchan con compasión a pacientes hospitalizados.", "🤝", "emotions"),
    ("resolute", "resuelto y determinado", "B2", "/ˈrez.ə.luːt/", "The climber remained resolute despite bone-chilling sub-zero winds.", "El alpinista se mantuvo resuelto a pesar de vientos gélidos bajo cero.", "🧗", "emotions"),
    ("magnanimous", "magnánimo y generoso", "B2", "/mæɡˈnæn.ə.məs/", "Be magnanimous in victory and courteous toward defeated competitors.", "Sé magnánimo en la victoria y cortés con los competidores derrotados.", "🕊️", "emotions"),
    ("flabbergasted", "estupefacto y atónito", "B2", "/ˈflæb.ɚ.ɡæs.tɪd/", "We were completely flabbergasted by the unexpected lottery win news.", "Nos quedamos completamente estupefactos ante la noticia inesperada de la lotería.", "😲", "emotions")
]
"""

# Batch 4: Sports, Hobbies, Arts & Leisure (~400 items)
BATCH_SPORTS_ARTS_DATA = """
BATCH_SPORTS_ARTS = [
    # Sports Equipment & Fitness (A1, A2, B1)
    ("stopwatch", "cronómetro de precisión", "A1", "/ˈstɑːp.wɑːtʃ/", "The swimming coach timed lap splits with a digital stopwatch.", "El entrenador de natación cronometró las vueltas con un cronómetro digital.", "⏱️", "sports"),
    ("dumbbell", "mancuerna para pesas de gimnasio", "A1", "/ˈdʌm.bel/", "Lift ten-pound dumbbells to strengthen shoulder deltoid muscles.", "Levanta mancuernas de diez libras para fortalecer los músculos deltoides.", "🏋️", "sports"),
    ("barbell", "barra olímpica para levantamiento", "A2", "/ˈbɑːr.bel/", "Load heavy iron weight plates onto the Olympic barbell for squats.", "Carga discos pesados de hierro en la barra olímpica para hacer sentadillas.", "🏋️‍♂️", "sports"),
    ("treadmill", "caminadora eléctrica de banda", "A2", "/ˈtred.mɪl/", "Run five kilometers on the gymnasium incline treadmill daily.", "Corre cinco kilómetros diarios en la caminadora con inclinación del gimnasio.", "🏃", "sports"),
    ("trampoline", "cama elástica / trampolín", "A1", "/ˌtræm.pəˈliːn/", "Gymnasts practice backflips safely bouncing on the spring trampoline.", "Gimnastas practican mortales rebotando en la cama elástica de resortes.", "🤸", "sports"),
    ("snorkel", "esnórquel / tubo para bucear", "A1", "/ˈsnɔːr.kəl/", "Breathe underwater through a silicone snorkel while viewing reef fish.", "Respira bajo el agua con un esnórquel de silicona mientras ves peces de arrecife.", "🤿", "sports"),
    ("wetsuit", "traje de neopreno para surf o buceo", "A2", "/ˈwet.suːt/", "Surfers slip into thick neoprene wetsuits before paddling into cold ocean breaks.", "Surfistas se ponen trajes de neopreno antes de remar en aguas oceánicas frías.", "🏄", "sports"),
    ("flippers", "aletas de natación para pies", "A1", "/ˈflɪp.ɚz/", "Kick smoothly through deep water using blue swimming flippers.", "Patea suavemente en aguas profundas usando aletas de natación azules.", "🏊", "sports"),
    ("badminton", "bádminton con raquetas ligeras", "A1", "/ˈbæd.mɪn.tən/", "Hit the feathered shuttlecock over the high badminton net.", "Pasa el volante de plumas sobre la alta red de bádminton.", "🏸", "sports"),
    ("shuttlecock", "volante / gallito de bádminton", "A2", "/ˈʃʌt̬.əl.kɑːk/", "The white goose-feather shuttlecock soared across the court.", "El volante blanco de plumas de ganso voló veloz por la cancha.", "🏸", "sports"),
    ("rugby", "rugby con balón ovalado", "A2", "/ˈrʌɡ.bi/", "Rugby players tackle opponents aggressively to score points.", "Jugadores de rugby taclean a oponentes para anotar puntos.", "🏉", "sports"),
    ("fencing", "esgrima con espadas y caretas", "B1", "/ˈfen.sɪŋ/", "Fencers advance and parry swiftly on the narrow fencing piste.", "Los esgrimistas avanzan y paran estocadas en la estrecha pista de esgrima.", "🤺", "sports"),
    ("kayak", "kayak ligero de remo", "A1", "/ˈkaɪ.æk/", "Paddle a bright red ocean kayak along coastal sea cave arches.", "Rema en un kayak rojo brillante a lo largo de arcos en cuevas marinas.", "🛶", "sports"),
    ("archery", "tiro con arco y flechas", "B1", "/ˈɑːr.tʃɚ.i/", "Pull the bowstring back smoothly to hit the bullseye in archery.", "Tensa la cuerda del arco suavemente para acertar al centro en tiro con arco.", "🏹", "sports"),
    ("hurdles", "carreras de vallas con saltos", "B1", "/ˈhɝː.dəlz/", "Track sprinters leap over orange hurdles with fluid rhythm.", "Los corredores saltan vallas anaranjadas con ritmo fluido en la pista.", "🏃", "sports"),
    ("javelin", "jabalina para lanzamiento atlético", "B1", "/ˈdʒæv.əl.ɪn/", "Athletes launch the aerodynamically balanced javelin far across the field.", "Atletas lanzan la jabalina balanceada aerodinámicamente por el campo.", "🏟️", "sports"),
    ("shot put", "lanzamiento de bala pesada", "B1", "/ˈʃɑːt ˌpʊt/", "Spin and heave the heavy solid iron ball in the shot put ring.", "Gira y empuja la pesada bola de hierro macizo en el círculo de lanzamiento.", "💪", "sports"),
    ("puck", "disco negro de hockey sobre hielo", "A2", "/pʌk/", "The ice hockey forward slapped the vulcanized rubber puck into the goal net.", "El delantero de hockey sobre hielo disparó el disco de caucho hacia la portería.", "🏒", "sports"),
    ("helmet", "casco protector para cabeza", "A1", "/ˈhel.mət/", "Fasten your bicycle helmet chin strap snugly before riding.", "Abróchate la correa de la barbilla del casco de bicicleta antes de rodar.", "🪖", "sports"),
    ("scoreboard", "marcador electrónico de puntos", "A1", "/ˈskɔːr.bɔːrd/", "The bright stadium scoreboard displayed four goals to three.", "El luminoso marcador del estadio mostró cuatro goles contra tres.", "🔢", "sports"),

    # Arts, Music, Instruments & Literature (A1, A2, B1)
    ("palette", "paleta de pintor para mezclar óleos", "A2", "/ˈpæl.ət/", "Dab oil paints on a wooden artist palette to blend sunset shades.", "Coloca pinturas al óleo en una paleta de madera para mezclar tonos del atardecer.", "🎨", "arts"),
    ("easel", "caballete para sostener lienzos", "A2", "/ˈiː.zəl/", "Stand before the wooden painting easel to brush watercolor landscapes.", "Párate frente al caballete de madera para pintar paisajes en acuarela.", "🖼️", "arts"),
    ("canvas", "lienzo de tela para pintura", "A2", "/ˈkæn.vəs/", "Stretch primed cotton canvas tautly over rectangular stretcher bars.", "Tensa el lienzo de algodón preparado sobre bastidores rectangulares.", "🎨", "arts"),
    ("chisel", "cincel para escultura de mármol", "A2", "/ˈtʃɪz.əl/", "Sculptors chip away excess Carrara marble blocks with a steel chisel.", "Escultores desbastan bloques de mármol de Carrara con un cincel de acero.", "🗿", "arts"),
    ("charcoal", "carboncillo de dibujo artístico", "A2", "/ˈtʃɑːr.koʊl/", "Sketch expressive portrait shadows using willow drawing charcoal sticks.", "Dibuja sombras expresivas de retratos usando carboncillo de sauce.", "✏️", "arts"),
    ("sonnet", "soneto poético de catorce versos", "B1", "/ˈsɑː.nət/", "Shakespeare composed masterly romantic sonnets in rhyming iambic pentameter.", "Shakespeare compuso sonetos románticos magistrales con rima en pentámetro.", "📜", "arts"),
    ("stanza", "estrofa poética de versos", "B1", "/ˈstæn.zə/", "Recite the opening stanza of the classical epic ballad from memory.", "Recita de memoria la estrofa inicial de la clásica balada épica.", "📖", "arts"),
    ("prologue", "prólogo introductorio literario", "B1", "/ˈproʊ.lɑːɡ/", "Read the dramatic historical prologue before starting chapter one.", "Lee el dramático prólogo histórico antes de comenzar el primer capítulo.", "📚", "arts"),
    ("epilogue", "epílogo conclusivo de novela", "B1", "/ˈep.ə.lɑːɡ/", "The reflective novel epilogue revealed what happened twenty years later.", "El reflexivo epílogo de la novela reveló qué sucedió veinte años después.", "📖", "arts"),
    ("symphony", "sinfonía orquestal monumental", "A2", "/ˈsɪm.fə.ni/", "The symphony orchestra performed Beethoven's monumental Ninth Symphony.", "La orquesta sinfónica interpretó la monumental Novena Sinfonía de Beethoven.", "🎼", "arts"),
    ("concerto", "concierto para solista y orquesta", "B1", "/kənˈtʃer.toʊ/", "The pianist received standing ovations for playing the Rachmaninoff concerto.", "El pianista recibió ovaciones de pie por tocar el concierto de Rajmáninov.", "🎹", "arts"),
    ("tempo", "tempo / velocidad musical", "A2", "/ˈtem.poʊ/", "The conductor tapped the baton to set a brisk allegro musical tempo.", "El director golpeó la batuta para marcar un tempo musical allegro y vivaz.", "🎵", "arts"),
    ("melody", "melodía principal cantable", "A1", "/ˈmel.ə.di/", "A haunting vocal melody echoed through the ancient stone cathedral.", "Una conmovedora melodía vocal resonó por la antigua catedral de piedra.", "🎶", "arts"),
    ("harmony", "armonía de acordes simultáneos", "A2", "/ˈhɑːr.mə.ni/", "Choir vocalists blended four-part harmonies in perfect pitch resonance.", "Cantantes del coro combinaron armonías a cuatro voces en perfecta afinación.", "🎵", "arts"),
    ("chord", "acorde de notas simultáneas", "A2", "/kɔːrd/", "Strum an acoustic guitar G-major chord to accompany folk songs.", "Rasguea un acorde de sol mayor en la guitarra acústica para canciones folclóricas.", "🎸", "arts")
]
"""

# Batch 5: City, Streets, Society & Civics (~450 items)
BATCH_CITY_SOCIETY_DATA = """
BATCH_CITY_SOCIETY = [
    # City Landmarks & Street Hardware (A1, A2, B1)
    ("crosswalk", "paso peatonal de cebra", "A1", "/ˈkrɑːs.wɑːk/", "Wait until cars stop completely before stepping into the crosswalk.", "Espera a que los autos se detengan antes de cruzar por el paso peatonal.", "🚶", "city"),
    ("curb", "borde de la acera / cordón", "A1", "/kɝːb/", "Step up onto the concrete curb to stay clear of street puddles.", "Sube al cordón de la acera para alejarte de los charcos de la calle.", "🧱", "city"),
    ("streetlight", "farola de alumbrado público", "A1", "/ˈstriːt.laɪt/", "Golden streetlights illuminate sidewalks automatically as darkness falls.", "Farolas doradas iluminan las aceras automáticamente al caer la noche.", "💡", "city"),
    ("billboard", "espectacular / valla publicitaria", "A2", "/ˈbɪl.bɔːrd/", "Massive illuminated commercial billboards line busy highway interchanges.", "Enormes vallas publicitarias luminosas bordean cruces de carreteras concurridos.", "🪧", "city"),
    ("fire hydrant", "hidrante contra incendios", "A1", "/ˈfaɪr ˌhaɪ.drənt/", "Do not park cars within five meters of the red roadside fire hydrant.", "No estaciones vehículos a menos de cinco metros del hidrante rojo.", "🚒", "city"),
    ("manhole", "alcantarilla de inspección", "A2", "/ˈmæn.hoʊl/", "Municipal utility crews climbed down the round cast-iron manhole to inspect pipes.", "Trabajadores municipales bajaron por la alcantarilla redonda a revisar tuberías.", "🕳️", "city"),
    ("roundabout", "glorieta / rotonda de tráfico", "A2", "/ˈraʊnd.ə.baʊt/", "Yield to oncoming vehicles already circling inside the traffic roundabout.", "Cede el paso a los vehículos que ya están circulando en la rotonda.", "🔄", "city"),
    ("pedestrian", "transeúnte / peatón", "A2", "/pəˈdes.tri.ən/", "Pedestrians stroll leisurely through the car-free historic plaza.", "Peatones caminan con calma por la plaza histórica libre de automóviles.", "🚶‍♂️", "city"),
    ("pavement", "pavimento de calzada o banqueta", "A2", "/ˈpeɪv.mənt/", "Rain washed autumn leaves across the dark asphalt road pavement.", "La lluvia arrastró hojas otoñales por el pavimento de asfalto oscuro.", "🛣️", "city"),
    ("alley", "callejón estrecho de ciudad", "A2", "/ˈæl.i/", "A cobblestone alley behind the bakery smelled of warm fresh bread.", "Un callejón empedrado detrás de la panadería olía a pan fresco y caliente.", "🏘️", "city"),
    ("overpass", "paso a desnivel elevado / puente", "B1", "/ˈoʊ.vɚ.pæs/", "Drive across the multi-lane concrete overpass to bypass downtown jams.", "Maneja por el paso a desnivel de varios carriles para evitar el tráfico.", "🌉", "city"),
    ("underpass", "túnel vehicular subterráneo", "B1", "/ˈʌn.dɚ.pæs/", "Cyclists pedaled safely through the well-lit riverfront underpass.", "Ciclistas pedalearon seguros por el paso subterráneo iluminado junto al río.", "🚇", "city"),
    ("scaffolding", "andamios metálicos de construcción", "B1", "/ˈskæf.əl.dɪŋ/", "Construction workers erected steel scaffolding to restore cathedral spires.", "Trabajadores levantaron andamios de acero para restaurar agujas de la catedral.", "🏗️", "city"),
    ("crane", "grúa torre de construcción alta", "A2", "/kreɪn/", "A towering yellow crane swung precast concrete beams onto the roof.", "Una alta grúa amarilla maniobró vigas de concreto prefabricado hacia el techo.", "🏗️", "city"),
    ("bulldozer", "aplanadora / buldócer de obras", "A2", "/ˈbʊlˌdoʊ.zɚ/", "The diesel bulldozer cleared piles of rubble from the foundation site.", "El buldócer de diésel despejó escombros del terreno de los cimientos.", "🚜", "city"),

    # Society, Civics & Governance (A2, B1, B2)
    ("referendum", "referéndum / consulta ciudadana", "B1", "/ˌref.əˈren.dəm/", "Citizens cast paper ballots in a nationwide constitutional referendum.", "Ciudadanos votaron en una consulta popular constitucional a nivel nacional.", "🗳️", "society"),
    ("ballot", "boleta de votación electoral", "A2", "/ˈbæl.ət/", "Mark your secret ballot choices inside private voting booths.", "Marca tus opciones en la boleta secreta dentro de mamparas privadas.", "🗳️", "society"),
    ("constitution", "constitución política fundamental", "B1", "/ˌkɑːn.stəˈtuː.ʃən/", "The supreme national constitution guarantees equality and free expression.", "La constitución suprema garantiza igualdad ante la ley y libertad de expresión.", "📜", "society"),
    ("amendment", "enmienda o reforma legal", "B1", "/əˈmend.mənt/", "Congress ratified a historic constitutional amendment protecting voting rights.", "El congreso ratificó una enmienda histórica que protege el derecho a votar.", "⚖️", "society"),
    ("treaty", "tratado de paz internacional", "B1", "/ˈtriː.t̬i/", "Ambassadors signed a multilateral environmental protection treaty in Geneva.", "Embajadores firmaron un tratado multilateral ambiental en Ginebra.", "🕊️", "society"),
    ("alliance", "alianza estratégica de naciones", "B1", "/əˈlaɪ.əns/", "Democratic allies formed a technological defense alliance against cyber attacks.", "Aliados democráticos formaron una alianza de ciberdefensa contra ataques.", "🤝", "society"),
    ("ambassador", "embajador diplomático plenipotenciario", "B1", "/æmˈbæs.ə.dɚ/", "The ambassador presented credentials to the head of state during the ceremony.", "El embajador presentó sus credenciales al jefe de estado en la ceremonia.", "👔", "society"),
    ("diplomat", "diplomático de carrera internacional", "A2", "/ˈdɪp.lə.mæt/", "Career diplomats negotiated round-the-clock peace ceasefires.", "Diplomáticos de carrera negociaron un cese al fuego por la paz sin descanso.", "🤝", "society"),
    ("embassy", "sede de embajada consular", "A2", "/ˈem.bə.si/", "Travelers renewed lost passports at their home nation's overseas embassy.", "Viajeros renovaron pasaportes extraviados en la embajada de su país natal.", "🏛️", "society"),
    ("civic", "cívico y comunitario", "B1", "/ˈsɪv.ɪk/", "Active civic participation strengthens neighborhood safety and local libraries.", "La participación cívica activa fortalece la seguridad vecinal y las bibliotecas.", "🏘️", "society")
]
"""

# Batch 6: Science, Tech, Business & Economics (~450 items)
BATCH_SCIENCE_BIZ_DATA = """
BATCH_SCIENCE_BIZ = [
    # Science & Elements (A2, B1, B2)
    ("helium", "helio gaseoso ligero", "A2", "/ˈhiː.li.əm/", "Bright party balloons float high in the air when inflated with helium gas.", "Globos brillantes de fiesta flotan en el aire al inflarse con gas helio.", "🎈", "science"),
    ("hydrogen", "hidrógeno químico elemental", "A2", "/ˈhaɪ.drə.dʒən/", "Fuel-cell passenger buses emit only pure water vapor from hydrogen combustion.", "Autobuses de pila de combustible emiten vapor de agua pura de hidrógeno.", "💧", "science"),
    ("carbon", "carbono mineral y orgánico", "A2", "/ˈkɑːr.bən/", "All organic terrestrial life forms are built from complex carbon chains.", "Toda la vida orgánica terrestre está estructurada a partir de carbono.", "💎", "science"),
    ("nitrogen", "nitrógeno gaseoso atmosférico", "A2", "/ˈnaɪ.trə.dʒən/", "Nitrogen gas constitutes seventy-eight percent of the air we inhale daily.", "El gas nitrógeno constituye el setenta y ocho por ciento del aire que inhalamos.", "🌬️", "science"),
    ("oxygen", "oxígeno vital para respiración", "A1", "/ˈɑːk.sɪ.dʒən/", "Scuba diving cylinders blend compressed air and pure medical-grade oxygen.", "Tanques de buceo combinan aire comprimido y oxígeno de grado médico.", "🤿", "science"),
    ("nebula", "nebulosa estelar brillante", "B1", "/ˈneb.jə.lə/", "The Hubble telescope captured vivid multicolored images of the Orion nebula.", "El telescopio Hubble capturó imágenes multicolores de la nebulosa de Orión.", "🌌", "science"),
    ("meteor", "meteoro / estrella fugaz brillante", "A2", "/ˈmiː.t̬i.ɔːr/", "Look up into the dark night sky to spot shooting meteors streak by.", "Mira hacia el cielo nocturno oscuro para ver estrellas fugaces cruzar veloces.", "🌠", "science"),
    ("comet", "cometa con cola de polvo y hielo", "A2", "/ˈkɑː.mɪt/", "Comet tails glow brightly as solar wind evaporates their frozen surface ice.", "Las colas de cometas brillan cuando el viento solar evapora su hielo superficial.", "☄️", "science"),
    ("asteroid", "asteroide rocoso espacial", "B1", "/ˈæs.tə.rɔɪd/", "Thousands of rocky asteroids orbit peacefully between Mars and Jupiter.", "Miles de asteroides rocosos orbitan en paz entre Marte y Júpiter.", "🪐", "science"),
    ("gravity", "gravedad de atracción planetaria", "A2", "/ˈɡræv.ə.t̬i/", "Lunar gravity is one-sixth as strong as Earth's gravitational pull.", "La gravedad lunar es una sexta parte tan fuerte como la gravedad terrestre.", "🌍", "science"),

    # Tech & Computing Hardware (A2, B1, B2)
    ("firmware", "firmware de bajo nivel en chips", "B1", "/ˈfɝːm.wer/", "Update the router firmware to patch recent network security vulnerabilities.", "Actualiza el firmware del enrutador para corregir vulnerabilidades de red.", "💾", "tech"),
    ("bandwidth", "ancho de banda de transmisión", "B1", "/ˈbænd.wɪtθ/", "Fiber-optic fiber connections deliver high bandwidth for video streaming.", "Conexiones de fibra óptica ofrecen alto ancho de banda para ver video.", "🚀", "tech"),
    ("firewall", "cortafuegos de seguridad de red", "B1", "/ˈfaɪr.wɑːl/", "Corporate network firewalls filter suspicious incoming internet data traffic.", "Cortafuegos corporativos filtran tráfico sospechoso entrante de internet.", "🛡️", "tech"),
    ("peripheral", "periférico externo de computadora", "B1", "/pəˈrɪf.ɚ.əl/", "Plug external peripherals like webcams, microphones, and mouse into USB ports.", "Conecta periféricos externos como cámaras web y micrófonos a puertos USB.", "🖱️", "tech"),
    ("touchpad", "panel táctil de laptop", "A1", "/ˈtʌtʃ.pæd/", "Use multi-finger gestures on the laptop touchpad to scroll and zoom.", "Usa gestos de varios dedos en el panel táctil de la laptop para desplazarte.", "💻", "tech"),
    ("motherboard", "tarjeta madre principal de circuito", "B1", "/ˈmʌð.ɚ.bɔːrd/", "Seat the multicore central processor carefully into the socket on the motherboard.", "Instala el procesador multinúcleo en el zócalo de la tarjeta madre.", "🔲", "tech"),
    ("overclock", "overclockear / acelerar reloj de CPU", "B2", "/ˌoʊ.vɚˈklɑːk/", "Gamer rigs install liquid cooling loops before overclocking processors.", "Jugadores instalan enfriamiento líquido antes de acelerar procesadores.", "⚡", "tech"),
    ("subwoofer", "altavoz de graves profundos", "A2", "/ˈsʌbˌwʊf.ɚ/", "The home theater subwoofer shook the living room during movie explosions.", "El subwoofer del teatro en casa retumbó durante las explosiones de la película.", "🔊", "tech"),
    ("cryptocurrency", "criptomoneda digital descentralizada", "B1", "/ˈkrɪp.toʊˌkɝː.ən.si/", "Miners validate blockchain transaction blocks to earn fresh cryptocurrency.", "Mineros validan bloques de la cadena de bloques para ganar criptomonedas.", "🪙", "tech"),
    ("algorithm", "algoritmo de cálculo sistemático", "B1", "/ˈæl.ɡə.rɪ.ðəm/", "Sorting algorithms organize unsorted list elements in logarithmic runtimes.", "Algoritmos de ordenamiento acomodan listas en tiempos logarítmicos.", "🔢", "tech"),

    # Business, Finance & Economics (A2, B1, B2)
    ("revenue", "ingresos brutos de ventas", "B1", "/ˈrev.ə.nuː/", "The software startup generated record quarterly subscription revenue.", "La empresa emergente de software generó ingresos trimestrales récord.", "📈", "business"),
    ("deficit", "déficit fiscal o presupuestario", "B1", "/ˈdef.ə.sɪt/", "Parliament voted on tax measures to reduce the national fiscal budget deficit.", "El parlamento votó medidas fiscales para reducir el déficit presupuestario.", "📉", "business"),
    ("dividend", "dividendo pagado a accionistas", "B1", "/ˈdɪv.ə.dend/", "Shareholders receive quarterly dividend payouts credited directly to accounts.", "Accionistas reciben pagos trimestrales de dividendos en sus cuentas.", "💵", "business"),
    ("mortgage", "hipoteca bancaria de vivienda", "B1", "/ˈmɔːr.ɡɪdʒ/", "Homeowners locked in a thirty-year fixed interest rate residential mortgage.", "Propietarios fijaron una hipoteca a treinta años con tasa de interés fija.", "🏡", "business"),
    ("collateral", "garantía prendaria de préstamo", "B2", "/kəˈlæt̬.ɚ.əl/", "The commercial bank required property deeds as loan security collateral.", "El banco comercial requirió escrituras de propiedad como garantía del préstamo.", "📜", "business"),
    ("stakeholder", "parte interesada / actor clave", "B2", "/ˈsteɪkˌhoʊl.dɚ/", "Company executives scheduled consultation workshops with key community stakeholders.", "Directivos programaron talleres de consulta con actores clave de la comunidad.", "👥", "business"),
    ("benchmark", "punto de referencia estándar", "B2", "/ˈbentʃ.mɑːrk/", "Our customer satisfaction rating serves as an industry quality benchmark.", "Nuestra calificación de satisfacción sirve como estándar de calidad del sector.", "📊", "business"),
    ("invoice", "factura comercial por cobrar", "A2", "/ˈɪn.vɔɪs/", "Send the client an itemized invoice detailing billable consulting hours.", "Envía al cliente una factura detallada con las horas de consultoría.", "🧾", "business"),
    ("receipt", "recibo de pago de compra", "A1", "/rɪˈsiːt/", "Always save your store checkout paper receipts for warranty exchanges.", "Guarda siempre los recibos de compra de la tienda para hacer válida la garantía.", "🧾", "business"),
    ("portfolio", "portafolio de inversiones", "B1", "/pɔːrtˈfoʊ.li.oʊ/", "Financial advisors recommend diversifying your stock and bond portfolio.", "Asesores financieros recomiendan diversificar tu portafolio de acciones y bonos.", "💼", "business")
]
"""

def main():
    os.makedirs("scripts/massive_expansion", exist_ok=True)
    
    files = {
        "scripts/massive_expansion/batch_objects.py": BATCH_OBJECTS_DATA,
        "scripts/massive_expansion/batch_nature.py": BATCH_NATURE_DATA,
        "scripts/massive_expansion/batch_actions.py": BATCH_ACTIONS_DATA,
        "scripts/massive_expansion/batch_sports_arts.py": BATCH_SPORTS_ARTS_DATA,
        "scripts/massive_expansion/batch_city_society.py": BATCH_CITY_SOCIETY_DATA,
        "scripts/massive_expansion/batch_science_biz.py": BATCH_SCIENCE_BIZ_DATA,
    }
    
    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created {path}")

if __name__ == "__main__":
    main()
