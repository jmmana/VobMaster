# Mega Lexicon Part 4: High-Quality Graded Vocabulary Entries
# Across Categories: education, business, science, arts, society, travel, tech, emotions, verbs_action, verbs_mind, adjectives_quality, adjectives_sensory

PART4_ITEMS = [
    # Education & Academia
    ("syllabus", "programa de estudios / temario", "B1", "/ˈsɪl.ə.bəs/", "The professor handed out the course syllabus on the first day.", "El profesor entregó el temario del curso el primer día.", "📑", "education"),
    ("dissertation", "tesis doctoral / disertación", "B2", "/ˌdɪs.ɚˈteɪ.ʃən/", "She defended her doctoral dissertation before an academic panel.", "Defendió su tesis doctoral ante un jurado académico.", "🎓", "education"),
    ("fellowship", "beca de investigación postdoctoral", "B2", "/ˈfel.oʊ.ʃɪp/", "The researcher won a prestigious medical science research fellowship.", "El investigador ganó una prestigiosa beca de ciencias médicas.", "🔬", "education"),
    ("auditorium", "auditorio universitario", "A2", "/ˌɑː.dəˈtɔːr.i.əm/", "Hundreds of students packed the auditorium for the guest lecture.", "Cientos de estudiantes llenaron el auditorio para la conferencia.", "🏛️", "education"),
    ("tuition", "colegiatura universitaria", "B1", "/tuːˈɪʃ.ən/", "Academic scholarships help students cover semester tuition costs.", "Becas académicas ayudan a cubrir los costos de colegiatura.", "💳", "education"),
    ("transcript", "kardex de calificaciones / expediente", "B1", "/ˈtræn.skrɪpt/", "Submit your official academic transcript when applying for master's.", "Entrega tu expediente académico oficial al postular a la maestría.", "📜", "education"),
    ("valedictorian", "primer lugar de la generación", "B2", "/ˌvæl.ə.dɪkˈtɔːr.i.ən/", "The class valedictorian delivered an inspiring graduation address.", "El primer lugar de la generación dio un discurso de graduación inspirador.", "🎓", "education"),
    ("plagiarism", "plagio académico", "B2", "/ˈpleɪ.dʒɚ.ɪ.zəm/", "Universities employ anti-plagiarism software to scan student essays.", "Universidades usan software antiplagio para revisar ensayos.", "🚫", "education"),
    ("compendium", "compendio o compilación", "B2", "/kəmˈpen.di.əm/", "The medical compendium summarizes known pharmaceutical therapies.", "El compendio médico resume terapias farmacológicas conocidas.", "📚", "education"),
    ("colloquium", "coloquio científico de debate", "C1", "/kəˈloʊ.kwi.əm/", "Physicists debated gravitational wave findings during the colloquium.", "Físicos debatieron hallazgos de ondas gravitacionales en el coloquio.", "🗣️", "education"),

    # Business, Economics & Management
    ("overhead", "gastos fijos operativos", "B2", "/ˈoʊ.vɚ.hed/", "Remote working reduces commercial office lease overhead expenses.", "El trabajo remoto reduce gastos fijos de arrendamiento de oficinas.", "🏢", "business"),
    ("subsidiary", "empresa filial / subsidiaria", "B2", "/səbˈsɪd.i.er.i/", "The multinational tech giant launched a clean energy subsidiary.", "El gigante tecnológico lanzó una filial de energía limpia.", "🌐", "business"),
    ("merger", "fusión empresarial", "B2", "/ˈmɝː.dʒɚ/", "The cross-border merger formed Europe's largest telecommunications provider.", "La fusión transfronteriza formó el mayor proveedor de telecomunicaciones.", "🤝", "business"),
    ("acquisition", "adquisición corporativa", "B2", "/ˌæk.wəˈzɪʃ.ən/", "The enterprise announced the acquisition of a promising AI laboratory.", "La empresa anunció la adquisición de un prometedor laboratorio de IA.", "💼", "business"),
    ("liability", "pasivo financiero / responsabilidad", "B2", "/ˌlaɪ.əˈbɪl.ə.t̬i/", "Accountants list outstanding bank loans under corporate liabilities.", "Contadores registran préstamos bancarios bajo pasivos corporativos.", "📊", "business"),
    ("dividend", "dividendo pagado a accionistas", "B1", "/ˈdɪv.ə.dend/", "Shareholders receive a quarterly cash dividend per share owned.", "Accionistas reciben un dividendo trimestral en efectivo por acción.", "💵", "business"),
    ("franchise", "franquicia comercial", "B1", "/ˈfræn.tʃaɪz/", "The entrepreneur opened three fast-casual restaurant franchises.", "El emprendedor abrió tres franquicias de restaurantes de comida rápida casual.", "🏪", "business"),
    ("logistics", "logística de distribución", "B1", "/ləˈdʒɪs.tɪks/", "Efficient warehouse logistics ensure same-day parcel delivery.", "Una logística eficiente de almacén asegura entregas de paquetes el mismo día.", "📦", "business"),
    ("inventory", "inventario de mercancía", "A2", "/ˈɪn.vən.tɔːr.i/", "Store staff conduct an annual barcode scan of warehouse inventory.", "Personal de tienda hace un escaneo anual del inventario con código de barras.", "📋", "business"),
    ("wholesale", "venta al por mayor / mayoreo", "B1", "/ˈhoʊl.seɪl/", "Retail shops buy handcrafted ceramics at wholesale discount rates.", "Tiendas minoristas compran cerámica artesanal a precios de mayoreo.", "🏬", "business"),

    # Tech, Software & Electronics
    ("firmware", "firmware de microcontrolador", "B2", "/ˈfɝːm.wer/", "Flash the latest security firmware onto your home smart router.", "Instala el firmware más reciente de seguridad en tu enrutador inteligente.", "💾", "tech"),
    ("broadband", "conexión de banda ancha de fibra", "B1", "/ˈbrɑːd.bænd/", "Rural community co-ops installed ultra-fast fiber broadband.", "Cooperativas rurales instalaron banda ancha ultrarrápida de fibra.", "🌐", "tech"),
    ("ethernet", "cable de red ethernet", "A2", "/ˈiː.θɚ.net/", "Plug the blue ethernet patch cable directly into the gaming console.", "Conecta el cable ethernet azul directamente a la consola de videojuegos.", "🔌", "tech"),
    ("dongle", "adaptador usb inalámbrico / dongle", "B1", "/ˈdɑːŋ.ɡəl/", "Insert the compact wireless dongle into the laptop USB-C port.", "Inserta el dongle inalámbrico en el puerto USB-C de la laptop.", "🖱️", "tech"),
    ("webcam", "cámara web de alta definición", "A1", "/ˈweb.kæm/", "Adjust your external webcam angle before the conference call starts.", "Ajusta el ángulo de tu cámara web antes de iniciar la llamada.", "📷", "tech"),
    ("motherboard", "tarjeta madre / placa base", "B1", "/ˈmʌð.ɚ.bɔːrd/", "Mount the dual memory sticks into slots on the computer motherboard.", "Monta las dos memorias en las ranuras de la placa base.", "🖥️", "tech"),
    ("processor", "procesador de silicio de ocho núcleos", "B1", "/ˈprɑː.ses.ɚ/", "The cutting-edge processor stays cool with liquid heat pipes.", "El procesador de vanguardia se mantiene frío con tubos de calor líquido.", "🔲", "tech"),
    ("transistor", "transistor microscópico de silicio", "B2", "/trænˈzɪs.tɚ/", "Billions of microscopic transistors are etched into microchips.", "Miles de millones de transistores microscópicos se graban en microchips.", "⚡", "tech"),
    ("capacitor", "condensador eléctrico / capacitor", "B2", "/kəˈpæs.ə.t̬ɚ/", "Capacitors store and discharge electrical energy in microsecond pulses.", "Capacitores almacenan y descargan energía en pulsos de microsegundos.", "🔋", "tech"),
    ("resistor", "resistencia eléctrica", "B2", "/rɪˈzɪs.tɚ/", "Color bands on the tiny resistor indicate its electrical resistance.", "Bandas de color en la pequeña resistencia indican su valor en ohmios.", "⚡", "tech"),

    # Arts, Cinema & Stage
    ("screenplay", "guion cinematográfico", "B1", "/ˈskriːn.pleɪ/", "The director spent two years revising the original thriller screenplay.", "El director pasó dos años revisando el guion cinematográfico original.", "🎬", "arts"),
    ("soundtrack", "banda sonora de película", "A2", "/ˈsaʊnd.træk/", "The sweeping orchestral film soundtrack won an international Oscar.", "La banda sonora orquestal de la película ganó un Óscar internacional.", "🎵", "arts"),
    ("rehearsal", "ensayo general de teatro", "B1", "/rɪˈhɝː.səl/", "Actors assembled on stage for the final dress rehearsal.", "Los actores se reunieron en el escenario para el ensayo general.", "🎭", "arts"),
    ("understudy", "actor sustituto / suplente", "B2", "/ˈʌn.dɚˌstʌd.i/", "The talented understudy stepped in flawlessly when the lead fell ill.", "La talentosa actriz sustituta entró al escenario con gran solvencia.", "🎭", "arts"),
    ("costume", "vestuario teatral de época", "A2", "/ˈkɑː.stuːm/", "Wardrobe seamstresses tailored elaborate Victorian opera costumes.", "Costureras de vestuario confeccionaron trajes victorianos de ópera.", "👗", "arts"),
    ("prop", "objeto de utilería teatral", "A2", "/prɑːp/", "The stage manager placed the vintage telephone prop on the desk.", "El utilero colocó el teléfono antiguo de utilería sobre el escritorio.", "☎️", "arts"),
    ("choreography", "coreografía de danza moderna", "B1", "/ˌkɔːr.iˈɑː.ɡrə.fi/", "Dancers synchronized their leaps in breathtaking contemporary choreography.", "Bailarines sincronizaron sus saltos en una coreografía contemporánea.", "🩰", "arts"),
    ("intermission", "intermedio en el teatro", "B1", "/ˌɪn.t̬ɚˈmɪʃ.ən/", "Patrons sip champagne in the grand foyer during the twenty-minute intermission.", "Los asistentes toman champaña en el vestíbulo durante el intermedio.", "🥂", "arts"),
    ("ovation", "ovación de pie con aplausos", "B2", "/oʊˈveɪ.ʃən/", "The virtuoso pianist received a resounding five-minute standing ovation.", "El pianista virtuoso recibió una resonante ovación de pie de cinco minutos.", "👏", "arts"),
    ("encore", "repetición a petición del público / encore", "B1", "/ˈɑːŋ.kɔːr/", "The rock band returned to stage to play two encore songs.", "La banda de rock regresó al escenario a tocar dos canciones de encore.", "🎸", "arts"),

    # Society, Family & Customs
    ("lineage", "linaje familiar ancestral", "B2", "/ˈlɪn.i.ɪdʒ/", "Historians traced the royal lineage back to eleventh-century Normandy.", "Historiadores rastrearon el linaje real hasta la Normandía del siglo once.", "👑", "society"),
    ("patriarch", "patriarca de la familia", "B2", "/ˈpeɪ.tri.ɑːrk/", "The ninety-year-old patriarch smiled proudly at his grandchildren.", "El patriarca de noventa años sonrió con orgullo a sus nietos.", "👴", "society"),
    ("matriarch", "matriarca respetada", "B2", "/ˈmeɪ.tri.ɑːrk/", "The wise family matriarch organized the festive holiday reunion.", "La sabia matriarca de la familia organizó la reunión festiva.", "👵", "society"),
    ("godparent", "padrino o madrina de bautizo", "A2", "/ˈɡɑːdˌper.ənt/", "Godparents promise to provide caring spiritual mentorship.", "Padrinos prometen brindar un afectuoso acompañamiento espiritual.", "👨‍👩‍👧", "society"),
    ("heirloom", "reliquia familiar transmitida", "B1", "/ˈer.luːm/", "The emerald ring is a cherished antique family heirloom.", "El anillo de esmeralda es una preciada reliquia familiar antigua.", "💍", "society"),
    ("neighbor", "vecino de al lado", "A1", "/ˈneɪ.bɚ/", "Our friendly neighbor watered our garden tomatoes while we traveled.", "Nuestro amable vecino regó los jitomates del jardín mientras viajábamos.", "🏡", "society"),
    ("acquaintance", "conocido casual / no amigo íntimo", "B1", "/əˈkweɪn.təns/", "She waved warmly to an office acquaintance in the coffee shop.", "Saludó con afecto a un conocido de la oficina en la cafetería.", "👋", "society"),
    ("civic", "cívico y ciudadano", "B1", "/ˈsɪv.ɪk/", "Voting in local municipal elections is an essential civic duty.", "Votar en elecciones municipales locales es un deber cívico esencial.", "🗳️", "society"),
    ("philanthropist", "filántropo benefactor", "B2", "/fɪˈlæn.θrə.pɪst/", "The philanthropist donated twenty million dollars to public libraries.", "El filántropo donó veinte millones de dólares a bibliotecas públicas.", "❤️", "society"),
    ("volunteer", "voluntario comunitario", "A2", "/ˌvɑː.lənˈtɪr/", "Volunteers package boxes of nutritious food at the city food bank.", "Voluntarios empacan cajas de alimentos nutritivos en el banco de comida.", "📦", "society"),

    # Travel & Places
    ("turnpike", "autopista de cuota / peaje", "B1", "/ˈtɝːn.paɪk/", "Pay tolls smoothly with automatic transponders on the turnpike.", "Paga casetas con transpondedores automáticos en la autopista de cuota.", "🛣️", "travel"),
    ("junction", "empalme de carreteras / cruce", "A2", "/ˈdʒʌŋk.ʃən/", "Take the eastern fork at the highway motorway junction.", "Toma la bifurcación este en el entronque de la autopista.", "🔀", "travel"),
    ("overpass", "paso a desnivel vehicular", "B1", "/ˈoʊ.vɚ.pæs/", "Traffic glided smoothly beneath the newly opened concrete overpass.", "El tránsito fluyó suave debajo del nuevo paso a desnivel de concreto.", "🌉", "travel"),
    ("underpass", "paso subterráneo", "A2", "/ˈʌn.dɚ.pæs/", "Pedestrians walk safely under the busy boulevard through the underpass.", "Peatones cruzan el bulevar con seguridad por el paso subterráneo.", "🚶", "travel"),
    ("cul-de-sac", "calle cerrada sin salida", "B2", "/ˈkʌl.də.sæk/", "Children ride bicycles freely in the quiet suburban cul-de-sac.", "Niños andan en bicicleta con libertad en la calle cerrada suburbana.", "🏘️", "travel"),
    ("crossroads", "encrucijada de caminos / cruce de caminos", "B1", "/ˈkrɑːs.roʊdz/", "The historic trading town flourished at the crossroads of two rivers.", "El pueblo comercial histórico floreció en la encrucijada de dos ríos.", "🗺️", "travel"),
    ("waypoint", "punto de referencia de navegación / waypoint", "B2", "/ˈweɪˌpɔɪnt/", "The GPS automatically marked a digital waypoint at the mountain summit.", "El GPS marcó un punto de referencia digital en la cima de la montaña.", "📍", "travel"),
    ("layover", "escala de vuelo en aeropuerto", "A2", "/ˈleɪˌoʊ.vɚ/", "We booked a four-hour layover in Amsterdam to stretch our legs.", "Reservamos una escala de cuatro horas en Ámsterdam para caminar.", "✈️", "travel"),
    ("terminal", "terminal de salidas internacionales", "A2", "/ˈtɝː.mə.nəl/", "Proceed to terminal two for intercontinental departures.", "Dirígete a la terminal dos para salidas intercontinentales.", "🏢", "travel"),
    ("concourse", "pasillo de salas de espera", "B1", "/ˈkɑːn.kɔːrs/", "Travelers walked briskly past tax-free boutiques in the airport concourse.", "Viajeros caminaron por las tiendas del pasillo del aeropuerto.", "🧳", "travel"),

    # Verbs of Action & Crafts
    ("unravel", "desenredar hilos / desentrañar enigmas", "B2", "/ʌnˈræv.əl/", "Carefully unravel the tangled ball of knitting yarn.", "Desenreda con cuidado la bola enredada de estambre de tejer.", "🧶", "verbs_action"),
    ("entwine", "entrelazar ramas o hilos", "B2", "/ɪnˈtwaɪn/", "Ivy vines entwine romantically around the stone veranda pillars.", "Hiedras se entrelazan románticamente en pilares de la terraza.", "🌿", "verbs_action"),
    ("whittle", "tallar madera con navaja", "B2", "/ˈwɪt̬.əl/", "The grandpa whittles smooth toy whistles from willow branches.", "El abuelo talla silbatos de juguete con ramas de sauce.", "🪵", "verbs_action"),
    ("chisel", "cincelar piedra o madera", "B1", "/ˈtʃɪz.əl/", "The sculptor used a steel hammer to chisel fine details on the bust.", "El escultor usó un martillo para cincelar finos detalles en el busto.", "🗿", "verbs_action"),
    ("engrave", "grabar iniciales en metal", "B1", "/ɪnˈɡreɪv/", "Engrave your initials inside the gold wedding band.", "Graba tus iniciales dentro del anillo de matrimonio de oro.", "💍", "verbs_action"),
    ("varnish", "barnizar muebles de madera", "A2", "/ˈvɑːr.nɪʃ/", "Apply two protective coats of clear varnish to the dining table.", "Aplica dos capas de barniz transparente a la mesa de comedor.", "🪑", "verbs_action"),
    ("upholster", "tapizar sillones con tela", "B2", "/ʌpˈhoʊl.stɚ/", "Craftsmen upholster vintage armchairs in rich floral tapestry.", "Artesanos tapizan sillones antiguos con tela de tapiz floral.", "🛋️", "verbs_action"),
    ("wring", "exprimir ropa retorciéndola", "B1", "/rɪŋ/", "Wring excess water from wet bath towels before hanging them.", "Exprime el exceso de agua de toallas mojadas antes de tenderlas.", "🧺", "verbs_action"),
    ("rinse", "enjuagar con agua limpia", "A1", "/rɪns/", "Rinse fresh strawberries under cold running tap water.", "Enjuaga fresas frescas bajo el chorro de agua fría del grifo.", "🍓", "verbs_action"),
    ("dunk", "remojar galleta en leche", "A1", "/dʌŋk/", "Children love to dunk sweet chocolate cookies into cold milk.", "A los niños les encanta remojar galletas de chocolate en leche fría.", "🍪", "verbs_action"),

    # Emotions, Virtues & Mind
    ("compassion", "compasión sincera por los demás", "B1", "/kəmˈpæʃ.ən/", "Nurses treat vulnerable patients with boundless patience and compassion.", "Enfermeras tratan a pacientes vulnerables con paciencia y compasión.", "❤️", "emotions"),
    ("devotion", "devoción y entrega leal", "B1", "/dɪˈvoʊ.ʃən/", "She demonstrated lifelong devotion to ocean coral conservation.", "Demostró una entrega y devoción de por vida al cuidado del coral.", "🪸", "emotions"),
    ("serenity", "serenidad y paz interior", "B1", "/səˈren.ə.t̬i/", "Early dawn walks beside mountain rivers bring deep mental serenity.", "Caminatas al alba junto a ríos de montaña traen profunda serenidad.", "🧘", "emotions"),
    ("zeal", "fervor y entusiasmo apasionado", "B2", "/ziːl/", "Volunteers tackled the community tree planting project with great zeal.", "Voluntarios realizaron el proyecto de reforestación con gran entusiasmo.", "🌳", "emotions"),
    ("enthusiasm", "entusiasmo contagioso", "A2", "/ɪnˈθuː.zi.æz.əm/", "The teacher's vibrant enthusiasm inspired students to study astronomy.", "El entusiasmo del maestro inspiró a los alumnos a estudiar astronomía.", "🔭", "emotions"),
    ("sympathy", "simpatía y condolencia", "B1", "/ˈsɪm.pə.θi/", "Neighbors expressed heartfelt sympathy to the grieving family.", "Vecinos expresaron sinceras condolencias a la familia en duelo.", "💌", "emotions"),
    ("jubilation", "júbilo desbordante y festejo", "B2", "/ˌdʒuː.bəlˈeɪ.ʃən/", "Fans erupted in wild jubilation as their team scored the winning goal.", "Aficionados estallaron en júbilo cuando su equipo anotó el gol de la victoria.", "🎉", "emotions"),
    ("melancholy", "melancolía poética", "B2", "/ˈmel.ən.kɑː.li/", "Soft autumn rain stirs a sweet, reflective sense of melancholy.", "La suave lluvia de otoño despierta una dulce melancolía reflexiva.", "🌧️", "emotions"),
    ("trepidation", "desasosiego / leve temor", "C1", "/ˌtrep.əˈdeɪ.ʃən/", "He knocked on the CEO's office door with slight trepidation.", "Tocó a la puerta de la oficina del director con leve desasosiego.", "🚪", "emotions"),
    ("elation", "euforia y regocijo supremo", "B2", "/iˈleɪ.ʃən/", "Crossing the marathon finish line filled the runner with pure elation.", "Cruzar la meta del maratón llenó al corredor de pura euforia.", "🏅", "emotions")
]
