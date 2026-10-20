"""
Lexicon Part C: Travel, Food & Body (~120 graded entries)
Format: (word, translation, level, ipa, example, exampleEs, emoji, categoryId)
"""

PART_C_WORDS = [
    # Travel & Hospitality
    ("layover", "escala de vuelo entre conexiones", "A2", "/ˈleɪˌoʊ.vɚ/", "We booked a four-hour layover in Amsterdam to stretch our legs between flights.", "Reservamos una escala de cuatro horas en Ámsterdam para caminar entre vuelos.", "✈️", "travel"),
    ("terminal", "terminal de aeropuerto o estación", "A1", "/ˈtɝː.mə.nəl/", "Proceed to international terminal three for flights departing to Tokyo.", "Dirígete a la terminal tres internacional para vuelos con salida a Tokio.", "🛫", "travel"),
    ("carry-on", "equipaje de mano de cabina", "A1", "/ˈker.i.ɑːn/", "Stow your rolling carry-on bag wheels-first into the overhead airplane bin.", "Guarda tu maleta de mano en el compartimento superior del avión.", "🧳", "travel"),
    ("customs", "aduana de control fronterizo", "A2", "/ˈkʌs.təmz/", "Declare all packaged agricultural goods when passing through airport customs.", "Declara todos los alimentos empaquetados al pasar por la aduana del aeropuerto.", "🛃", "travel"),
    ("baggage carousel", "banda de reclamo de equipaje", "A2", "/ˈbæɡ.ɪdʒ ˌker.ə.sel/", "Watch the rotating baggage carousel for your red hardshell suitcase.", "Espera en la banda de equipaje giratoria a que salga tu maleta rígida roja.", "🧳", "travel"),
    ("boarding pass", "pase de abordar / tarjeta de embarque", "A1", "/ˈbɔːr.dɪŋ ˌpæs/", "Download your digital airline boarding pass onto your mobile smartphone.", "Descarga tu pase de abordar digital de la aerolínea en tu teléfono inteligente.", "📱", "travel"),
    ("concierge", "conserje de hotel para reservaciones", "B1", "/kɑːn.siˈerʒ/", "The hotel concierge booked premium front-row opera tickets for guests.", "El conserje del hotel reservó boletos de primera fila de ópera para los huéspedes.", "🛎️", "travel"),
    ("hostel", "albergue juvenil para mochileros", "A1", "/ˈhɑː.stəl/", "Backpackers meet fellow world travelers in dormitory rooms at the beach hostel.", "Mochileros conocen a otros viajeros en dormitorios del albergue de playa.", "🛏️", "travel"),
    ("reservation", "reservación anticipada de mesa o cuarto", "A1", "/ˌrez.ɚˈveɪ.ʃən/", "Always call ahead to confirm your dinner reservation at Michelin restaurants.", "Siempre llama con anticipación para confirmar tu reservación para cenar.", "📅", "travel"),
    ("excursion", "excursión guiada de un día", "A2", "/ɪkˈskɝː.ʒən/", "Book a full-day snorkeling excursion out to the barrier coral reef.", "Reserva una excursión de todo el día para bucear en la barrera de coral.", "🤿", "travel"),
    ("souvenir", "recuerdo / souvenir de viaje", "A1", "/ˌsuː.vəˈnɪr/", "Pick up painted ceramic magnet souvenirs to bring home to friends.", "Compra recuerdos de imanes de cerámica pintada para llevar a tus amigos.", "🎁", "travel"),
    ("compass", "brújula magnética de orientación", "A1", "/ˈkʌm.pəs/", "Check your pocket magnetic compass to verify trail direction in foggy forests.", "Revisa tu brújula magnética de bolsillo para verificar la ruta en bosques con niebla.", "🧭", "travel"),
    ("lighthouse", "faro marítimo costero", "A2", "/ˈlaɪt.haʊs/", "The historic whitewashed stone lighthouse warned ships of treacherous reefs.", "El histórico faro de piedra blanca alertaba a los barcos de arrecifes peligrosos.", "🗼", "travel"),
    ("harbor", "puerto abrigado de embarcaciones", "A2", "/ˈhɑːr.bɚ/", "Fishing trawlers and white sailing yachts shelter in the quiet harbor.", "Barcos pesqueros y veleros blancos se resguardan en el apacible puerto.", "⚓", "travel"),
    ("quay", "muelle de atraque para barcos", "B1", "/kiː/", "Stevedores unloaded crates of fresh tropical fruit along the stone dock quay.", "Estibadores descargaron cajas de fruta tropical a lo largo del muelle de piedra.", "🚢", "travel"),

    # Food, Ingredients & Gastronomy
    ("artichoke", "alcachofa tierna de hojas", "A2", "/ˈɑːr.t̬ə.tʃoʊk/", "Steam whole green artichokes and dip leaves into lemon garlic butter.", "Cocina alcachofas verdes al vapor y remoja sus hojas en mantequilla de limón.", "🥬", "food"),
    ("asparagus", "espárragos verdes tiernos", "A2", "/əˈsper.ə.ɡəs/", "Roast tender green asparagus spears in olive oil and shaved parmesan.", "Asa puntas tiernas de espárragos verdes con aceite de oliva y parmesano.", "🌱", "food"),
    ("zucchini", "calabacita / calabacín verde", "A1", "/zuːˈkiː.ni/", "Slice fresh green zucchini into ribbons for healthy vegetable pasta bowls.", "Corta calabacitas verdes en tiras para preparar platillos saludables de pasta vegetal.", "🥒", "food"),
    ("eggplant", "berenjena morada brillante", "A2", "/ˈeɡ.plænt/", "Layer fried eggplant slices with tomato marinara and mozzarella for parmigiana.", "Coloca capas de berenjena frita con salsa marinara y mozzarella para parmigiana.", "🍆", "food"),
    ("avocado", "aguacate cremoso / palta", "A1", "/ˌæv.əˈkɑː.doʊ/", "Mash ripe creamy avocado with lime, diced onions, and cilantro for guacamole.", "Machaca aguacate maduro con limón, cebolla picada y cilantro para hacer guacamole.", "🥑", "food"),
    ("pomegranate", "granada roja con semillas dulces", "A2", "/ˈpɑː.məˌɡræn.ɪt/", "Sprinkle ruby red pomegranate seeds over fresh goat cheese salads.", "Espolvorea semillas rojas de granada sobre ensaladas frescas de queso de cabra.", "🥗", "food"),
    ("fig", "higo dulce y carnoso", "A2", "/fɪɡ/", "Bake ripe black mission figs wrapped in prosciutto with honey drizzle.", "Hornea higos negros maduros envueltos en jamón serrano con un toque de miel.", "🍯", "food"),
    ("cardamom", "cardamomo aromático en vainas", "B1", "/ˈkɑːr.də.məm/", "Crush green cardamom pods into steaming hot Indian chai tea brews.", "Tritura vainas verdes de cardamomo en té chai caliente y espumoso.", "🫖", "food"),
    ("cinnamon", "canela aromática en rama o polvo", "A1", "/ˈsɪn.ə.mən/", "Dust warm baked apple pies with ground cinnamon and brown sugar.", "Espolvorea pays tibios de manzana horneada con canela en polvo y azúcar morena.", "🥧", "food"),
    ("nutmeg", "nuez moscada recién rallada", "B1", "/ˈnʌt.meɡ/", "Grate fresh nutmeg into creamy béchamel sauce for lasagna dishes.", "Ralla nuez moscada fresca en la salsa bechamel cremosa para la lasaña.", "🧀", "food"),
    ("rosemary", "romero fresco de olor", "A2", "/ˈroʊz.mer.i/", "Roast baby potatoes with fragrant sprigs of freshly picked garden rosemary.", "Asa papitas cambray con ramitas aromáticas de romero fresco del jardín.", "🌿", "food"),
    ("thyme", "tomillo aromático de cocina", "A2", "/taɪm/", "Simmer tender beef stew with fresh thyme, bay leaves, and baby carrots.", "Cocina a fuego lento estofado de carne con tomillo fresco y hojas de laurel.", "🍲", "food"),
    ("basil", "albahaca verde fresca", "A1", "/ˈbeɪ.zəl/", "Tear sweet green basil leaves over hot wood-fired margherita pizzas.", "Trocea hojas de albahaca fresca sobre pizzas margarita recién horneadas.", "🍕", "food"),
    ("coriander", "cilantro aromático fresco", "A2", "/ˈkɔːr.i.æn.dɚ/", "Garnish spicy chicken noodle soup bowls with fresh chopped coriander.", "Decora tazones de sopa de pollo con fideos con cilantro fresco picado.", "🍜", "food"),
    ("croissant", "cruasán hojaldrado de mantequilla", "A1", "/kwɑːˈsɑːŋ/", "Enjoy a flaky, buttery golden croissant with espresso every morning.", "Disfruta de un cruasán dorado y hojaldrado de mantequilla con un café expreso.", "🥐", "food"),
    ("bagel", "bagel de pan horneado con ajonjolí", "A1", "/ˈbeɪ.ɡəl/", "Toast a toasted sesame bagel and spread generously with scallion cream cheese.", "Tuesta un bagel de ajonjolí y úntale queso crema con cebollín en abundancia.", "🥯", "food"),
    ("pretzel", "pretzel salado horneado", "A2", "/ˈpret.səl/", "Dip warm twisted sourdough pretzels into spicy whole-grain mustard.", "Remoja pretzels calientes en mostaza picante de grano entero.", "🥨", "food"),
    ("waffle", "gofre / waffle crujiente con miel", "A1", "/ˈwɑː.fəl/", "Pour pure maple syrup over golden crispy Belgian breakfast waffles.", "Vierte miel de maple pura sobre crujientes waffles belgas para el desayuno.", "🧇", "food"),
    ("pancake", "panqueque esponjoso / hot cake", "A1", "/ˈpæn.keɪk/", "Stack blueberry buttermilk pancakes high and top with whipped butter.", "Apila panqueques de arándanos esponjosos y cúbrelos con mantequilla batida.", "🥞", "food"),

    # Body, Health & Wellness
    ("stethoscope", "estetoscopio médico de auscultación", "A2", "/ˈsteθ.ə.skoʊp/", "The doctor placed the cold stethoscope on the child's chest to listen to heartbeats.", "La doctora colocó el estetoscopio frío en el pecho del niño para escuchar latidos.", "🩺", "body"),
    ("syringe", "jeringa médica esterilizada", "A2", "/səˈrɪndʒ/", "Nurses use disposable plastic syringes to inject painless influenza vaccines.", "Enfermeras usan jeringas de plástico desechables para vacunas de influenza.", "💉", "body"),
    ("thermometer", "termómetro digital de fiebre", "A1", "/θɚˈmɑː.mə.t̬ɚ/", "Check your forehead temperature with an infrared digital thermometer.", "Revisa tu temperatura en la frente con un termómetro digital infrarrojo.", "🌡️", "body"),
    ("bandage", "vendaje elástico para torceduras", "A1", "/ˈbæn.dɪdʒ/", "Wrap the sprained ankle tightly with a stretchy elastic compression bandage.", "Envuelve el tobillo torcido firmemente con un vendaje elástico compresivo.", "🩹", "body"),
    ("crutches", "muletas ortopédicas para caminar", "A2", "/ˈkrʌtʃ.ɪz/", "He walked cautiously with aluminum forearm crutches after fracturing his foot.", "Caminó con cautela apoyado en muletas de aluminio tras fracturarse el pie.", "🩼", "body"),
    ("splint", "férula inmovilizadora de huesos", "B1", "/splɪnt/", "Emergency medical technicians immobilized the broken wrist in a rigid splint.", "Los paramédicos inmovilizaron la muñeca fracturada con una férula rígida.", "🦴", "body"),
    ("ointment", "ungüento o pomada cicatrizante", "A2", "/ˈɔɪnt.mənt/", "Apply soothing antiseptic ointment over minor scrapes before covering them.", "Aplica pomada antiséptica calmante sobre raspones leves antes de taparlos.", "🧴", "body"),
    ("capsule", "cápsula médica de gelatina", "A1", "/ˈkæp.səl/", "Swallow two antibiotic gel capsules with a full glass of cool water.", "Traga dos cápsulas de antibiótico con un vaso lleno de agua fresca.", "💊", "body"),
    ("migraine", "migraña o jaqueca pulsante", "B1", "/ˈmaɪ.ɡreɪn/", "Resting quietly in a pitch-dark room helps alleviate throbbing migraine headaches.", "Descansar en un cuarto oscuro ayuda a aliviar jaquecas pulsantes de migraña.", "🤕", "body"),
    ("allergy", "alergia estacional a pólenes", "A2", "/ˈæl.ɚ.dʒi/", "Spring tree pollen frequently triggers a seasonal running nose allergy.", "El polen de los árboles en primavera suele detonar alergia con escurrimiento nasal.", "🤧", "body"),
    ("sprain", "esguince o torcedura de ligamentos", "A2", "/spreɪn/", "Apply crushed ice packs to reduce swelling on an acute ankle sprain.", "Aplica compresas de hielo para bajar la hinchazón en un esguince agudo de tobillo.", "🧊", "body"),
    ("blister", "ampolla dolorosa en la piel", "A2", "/ˈblɪs.tɚ/", "Stiff new leather hiking boots rubbed a painful water blister onto his heel.", "Botas de montaña nuevas le sacaron una dolorosa ampolla en el talón.", "🥾", "body"),
    ("bruise", "moretón o hematoma morado", "A2", "/bruːz/", "The soccer player got a purple shin bruise after colliding with the goalpost.", "El futbolista tuvo un moretón morado en la espinilla tras chocar con el poste.", "⚽", "body"),
    ("pulse", "pulso cardíaco por minuto", "A1", "/pʌls/", "The nurse counted eighty steady resting beats per minute checking his wrist pulse.", "La enfermera contó ochenta latidos estables por minuto al medir su pulso.", "💓", "body"),
    ("inhaler", "inhalador broncodilatador de bolsillo", "A2", "/ɪnˈheɪ.lɚ/", "Asthmatic runners carry a pocket aerosol inhaler during cold morning workouts.", "Corredores asmáticos llevan un inhalador de bolsillo en entrenamientos fríos.", "🫁", "body")
]
