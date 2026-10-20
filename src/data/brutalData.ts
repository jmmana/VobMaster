export type BrutalCategory = 'all' | 'homophone' | 'false_friend' | 'homograph';

export interface ConfusableItem {
  word: string;
  phonetic: string;
  meaning: string;
  emoji: string;
  exampleSentence?: string;
  exampleSentenceEs?: string;
}

export interface BrutalQuestion {
  id: string;
  category: 'homophone' | 'false_friend' | 'homograph';
  typeLabel: string; // e.g. "👂 Suenan Parecido", "🚫 Falso Amigo", "🔤 Homógrafo"
  targetWord: string;
  phonetic: string;
  prompt: string;
  contextSentence?: string;
  audioText: string;
  correctAnswer: string;
  options: string[];
  explanation: {
    title: string;
    description: string;
    trick: string;
  };
  confusables: ConfusableItem[];
}

export const brutalQuestions: BrutalQuestion[] = [
  // 1. Desert vs Dessert (Requested specifically: "DESIERTO , DULCE")
  {
    id: 'brutal_desert_dessert',
    category: 'homophone',
    typeLabel: '👂 Suenan Casi Igual',
    targetWord: 'dessert',
    phonetic: '/dɪˈzɝːt/',
    prompt: '¿Cuál es el significado correcto de "DESSERT" (con doble S)?',
    contextSentence: 'Would you like some chocolate cake for dessert?',
    audioText: 'Would you like some chocolate cake for dessert?',
    correctAnswer: 'Postre o dulce',
    options: ['Postre o dulce', 'Desierto árido con arena', 'Abandonar o desamparar', 'Plato fuerte principal'],
    explanation: {
      title: '¡Cuidado con la doble S!',
      description: 'DESSERT (/dɪˈzɝːt/) es el postre dulce que tomas después de comer. DESERT (/ˈdez.ɚt/) con una sola S es el desierto árido (o como verbo /dɪˈzɝːt/, abandonar).',
      trick: '💡 Truco infalible: "Dessert" lleva doble S porque siempre quieres dos porciones de dulce (Super Sweet).'
    },
    confusables: [
      { word: 'dessert', phonetic: '/dɪˈzɝːt/', meaning: 'Postre o dulce al final de la comida', emoji: '🍨', exampleSentence: 'We ate strawberry ice cream for dessert.' },
      { word: 'desert', phonetic: '/ˈdez.ɚt/', meaning: 'Desierto árido de arena / sequía', emoji: '🏜️', exampleSentence: 'Camels can survive in the dry desert.' }
    ]
  },
  {
    id: 'brutal_desert_meaning',
    category: 'homophone',
    typeLabel: '👂 Suenan Casi Igual',
    targetWord: 'desert',
    phonetic: '/ˈdez.ɚt/',
    prompt: '¿Cómo se dice "DESIERTO DE ARENA" en inglés?',
    contextSentence: 'The Sahara is the largest hot desert in the world.',
    audioText: 'The Sahara is the largest hot desert in the world.',
    correctAnswer: 'Desert',
    options: ['Desert', 'Dessert', 'Deserte', 'Disert'],
    explanation: {
      title: 'Solo una "S" para el desierto',
      description: 'El desierto geográfico de arena se escribe "DESERT" (una sola S) y se pronuncia con acento en la primera sílaba /ˈdez.ɚt/.',
      trick: '💡 Solo hay una "s" en el desierto porque la arena es solitaria; "dessert" tiene dos "s" de dulce.'
    },
    confusables: [
      { word: 'desert', phonetic: '/ˈdez.ɚt/', meaning: 'Desierto árido de arena', emoji: '🏜️', exampleSentence: 'Water is very scarce in the desert.' },
      { word: 'dessert', phonetic: '/dɪˈzɝːt/', meaning: 'Postre dulce', emoji: '🍰', exampleSentence: 'Apple pie is my favorite dessert.' }
    ]
  },

  // 2. Bear vs Beard vs Beer vs Bird (Requested specifically: "OSO BARBA CERVEZA")
  {
    id: 'brutal_bear_beard_beer',
    category: 'homophone',
    typeLabel: '👂 El Cuarteto de la Confusión',
    targetWord: 'beard',
    phonetic: '/bɪrd/',
    prompt: '¿Qué significa exactamente "BEARD"?',
    contextSentence: 'He decided to grow a thick winter beard.',
    audioText: 'He decided to grow a thick winter beard.',
    correctAnswer: 'Barba facial',
    options: ['Barba facial', 'Cerveza fría', 'Oso salvaje', 'Pájaro o ave'],
    explanation: {
      title: '¡El clásico terror de los hispanohablantes!',
      description: '• Beard (/bɪrd/) = Barba.\n• Bear (/ber/) = Oso.\n• Beer (/bɪr/) = Cerveza.\n• Bird (/bɝːd/) = Pájaro.',
      trick: '💡 "Beard" termina en D como barba en español. "Beer" tiene dos E como "cervEEza".'
    },
    confusables: [
      { word: 'bear', phonetic: '/ber/', meaning: 'Oso salvaje', emoji: '🐻', exampleSentence: 'A brown bear caught a fish in the river.' },
      { word: 'beard', phonetic: '/bɪrd/', meaning: 'Barba en el rostro', emoji: '🧔', exampleSentence: 'He shaved his beard yesterday.' },
      { word: 'beer', phonetic: '/bɪr/', meaning: 'Cerveza fría', emoji: '🍺', exampleSentence: 'Let us drink a cold beer.' },
      { word: 'bird', phonetic: '/bɝːd/', meaning: 'Pájaro o ave', emoji: '🐦', exampleSentence: 'The blue bird sang in the tree.' }
    ]
  },
  {
    id: 'brutal_beer_choice',
    category: 'homophone',
    typeLabel: '👂 El Cuarteto de la Confusión',
    targetWord: 'beer',
    phonetic: '/bɪr/',
    prompt: '¿Cómo pides una "CERVEZA" en inglés sin confundirte?',
    contextSentence: 'Can I please have a cold beer?',
    audioText: 'Can I please have a cold beer?',
    correctAnswer: 'Beer',
    options: ['Beer', 'Bear', 'Beard', 'Bird'],
    explanation: {
      title: '¡No vayas a pedir un oso en el bar!',
      description: 'Si dices "Can I have a bear?", estás pidiendo un oso salvaje. Para cerveza debes decir "BEER" (/bɪr/).',
      trick: '💡 "Beer" rima con "cheer" (¡salud!). "Bear" rima con "hair" (pelo).'
    },
    confusables: [
      { word: 'beer', phonetic: '/bɪr/', meaning: 'Cerveza', emoji: '🍺' },
      { word: 'bear', phonetic: '/ber/', meaning: 'Oso', emoji: '🐻' },
      { word: 'beard', phonetic: '/bɪrd/', meaning: 'Barba', emoji: '🧔' }
    ]
  },

  // 3. Library vs Bookstore (Requested specifically: "LIBRERIA Y BIBLOTECA")
  {
    id: 'brutal_library_bookstore',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'library',
    phonetic: '/ˈlaɪ.brer.i/',
    prompt: 'Si alguien en inglés te dice "I am going to the LIBRARY", ¿a dónde va?',
    contextSentence: 'You must be quiet in the city library.',
    audioText: 'You must be quiet in the city library.',
    correctAnswer: 'A la biblioteca pública (a leer o estudiar)',
    options: [
      'A la biblioteca pública (a leer o estudiar)',
      'A la librería de la esquina (a comprar libros)',
      'A la tienda de papelería escolar',
      'Al librero o estantería de casa'
    ],
    explanation: {
      title: '¡Uno de los falsos amigos más famosos!',
      description: 'LIBRARY NO es librería. "Library" es una BIBLIOTECA donde pides libros prestados. La tienda donde compras libros se llama "BOOKSTORE" o "BOOKSHOP".',
      trick: '💡 Piensa en "Libre": en la biblioteca (library) los libros son libres / gratis para consultar; en la "bookstore" tienes que pagar.'
    },
    confusables: [
      { word: 'library', phonetic: '/ˈlaɪ.brer.i/', meaning: 'Biblioteca (préstamo gratuito de libros)', emoji: '🏛️', exampleSentence: 'She borrowed three novels from the library.' },
      { word: 'bookstore', phonetic: '/ˈbʊk.stɔːr/', meaning: 'Librería (tienda comercial de libros)', emoji: '🏪', exampleSentence: 'I bought this dictionary at the downtown bookstore.' }
    ]
  },
  {
    id: 'brutal_bookstore_question',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'bookstore',
    phonetic: '/ˈbʊk.stɔːr/',
    prompt: '¿Cómo se dice en inglés "LIBRERÍA" (el comercio donde compras libros)?',
    contextSentence: 'She works as a cashier in the local bookstore.',
    audioText: 'She works as a cashier in the local bookstore.',
    correctAnswer: 'Bookstore',
    options: ['Bookstore', 'Library', 'Librarian', 'Bookcase'],
    explanation: {
      title: 'Comprar libros = Bookstore',
      description: 'Para comprar libros vas a una Bookstore. "Library" es la biblioteca pública.',
      trick: '💡 "Store" significa tienda. Book + Store = Tienda de libros = Librería.'
    },
    confusables: [
      { word: 'bookstore', phonetic: '/ˈbʊk.stɔːr/', meaning: 'Librería comercial', emoji: '📚' },
      { word: 'library', phonetic: '/ˈlaɪ.brer.i/', meaning: 'Biblioteca', emoji: '🏛️' }
    ]
  },

  // 4. Actually vs Currently
  {
    id: 'brutal_actually',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'actually',
    phonetic: '/ˈæk.tʃu.ə.li/',
    prompt: '¿Qué significa la palabra "ACTUALLY" en inglés?',
    contextSentence: 'Actually, that is not what happened.',
    audioText: 'Actually, that is not what happened.',
    correctAnswer: 'En realidad / De hecho',
    options: ['En realidad / De hecho', 'Actualmente / Hoy en día', 'En este momento exacto', 'Eventualmente'],
    explanation: {
      title: '"Actually" NO significa actualmente',
      description: '"Actually" significa "en realidad" o "de hecho". Si quieres decir "actualmente", debes usar "CURRENTLY" o "NOWADAYS".',
      trick: '💡 "Actually" viene de "actual" en el sentido de real/verdadero, como en inglés "fact".'
    },
    confusables: [
      { word: 'actually', phonetic: '/ˈæk.tʃu.ə.li/', meaning: 'En realidad / de hecho', emoji: '🤔', exampleSentence: 'I actually love learning languages.' },
      { word: 'currently', phonetic: '/ˈkɝː.ənt.li/', meaning: 'Actualmente / en la actualidad', emoji: '⏳', exampleSentence: 'He is currently studying in London.' }
    ]
  },

  // 5. Embarrassed vs Pregnant
  {
    id: 'brutal_embarrassed',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'embarrassed',
    phonetic: '/ɪmˈber.əst/',
    prompt: 'Si alguien dice "I feel so EMBARRASSED!", ¿qué le ocurre?',
    contextSentence: 'She felt embarrassed when she spilled her drink.',
    audioText: 'She felt embarrassed when she spilled her drink.',
    correctAnswer: 'Siente mucha pena o vergüenza',
    options: ['Siente mucha pena o vergüenza', 'Está esperando un bebé (embarazada)', 'Tiene dolor de estómago', 'Está muy ocupada'],
    explanation: {
      title: '¡El falso amigo más vergonzoso!',
      description: '"Embarrassed" significa avergonzado/a o apenado/a. Estar embarazada en inglés se dice "PREGNANT". ¡Decir "I am embarrassed" no significa que vas a ser mamá!',
      trick: '💡 Embarrassed = cara roja de vergüenza. Pregnant = esperando un bebé.'
    },
    confusables: [
      { word: 'embarrassed', phonetic: '/ɪmˈber.əst/', meaning: 'Avergonzado/a o con pena', emoji: '😳', exampleSentence: 'He was embarrassed by his silly mistake.' },
      { word: 'pregnant', phonetic: '/ˈpreɡ.nənt/', meaning: 'Embarazada / gestando un bebé', emoji: '🤰', exampleSentence: 'She is six months pregnant.' }
    ]
  },

  // 6. Sensible vs Sensitive
  {
    id: 'brutal_sensible_sensitive',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Cruzado',
    targetWord: 'sensible',
    phonetic: '/ˈsen.sə.bəl/',
    prompt: '¿Qué significa que una persona sea "SENSIBLE" en inglés?',
    contextSentence: 'Wearing a raincoat was a very sensible decision.',
    audioText: 'Wearing a raincoat was a very sensible decision.',
    correctAnswer: 'Sensata, razonable y prudente',
    options: ['Sensata, razonable y prudente', 'Sensible y llorona', 'Enojona y reactiva', 'Susceptible a alergias'],
    explanation: {
      title: '¡Están invertidas en inglés!',
      description: '• SENSIBLE = Sensato, con sentido común.\n• SENSITIVE = Sensible (emocional o físicamente).',
      trick: '💡 "Sensible" tiene "Sense" (sentido común). "Sensitive" tiene "feelings" (sensible).'
    },
    confusables: [
      { word: 'sensible', phonetic: '/ˈsen.sə.bəl/', meaning: 'Sensato / prudente / con sentido común', emoji: '🧠', exampleSentence: 'It is sensible to save money for emergencies.' },
      { word: 'sensitive', phonetic: '/ˈsen.sə.t̬ɪv/', meaning: 'Sensible emocional o físicamente', emoji: '🥺', exampleSentence: 'He has very sensitive eyes in sunlight.' }
    ]
  },

  // 7. Exit vs Success
  {
    id: 'brutal_exit_success',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'exit',
    phonetic: '/ˈek.sɪt/',
    prompt: '¿Qué significa el letrero verde luminoso "EXIT" en los cines o edificios?',
    contextSentence: 'Emergency exit doors must remain unlocked.',
    audioText: 'Emergency exit doors must remain unlocked.',
    correctAnswer: 'Salida de emergencia',
    options: ['Salida de emergencia', 'Éxito en taquilla', 'Exhibición especial', 'Entrada exclusiva'],
    explanation: {
      title: 'EXIT es SALIDA, no éxito',
      description: '"Exit" es una salida. "Éxito" en inglés es "SUCCESS" o "HIT".',
      trick: '💡 Piensa en el verbo latino "exire" (salir). El éxito es el "Success".'
    },
    confusables: [
      { word: 'exit', phonetic: '/ˈek.sɪt/', meaning: 'Salida de un lugar', emoji: '🚪', exampleSentence: 'Turn right at the freeway exit.' },
      { word: 'success', phonetic: '/səkˈses/', meaning: 'Éxito / logro triunfal', emoji: '🏆', exampleSentence: 'Her new startup was a huge success.' }
    ]
  },

  // 8. Carpet vs Folder
  {
    id: 'brutal_carpet_folder',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'carpet',
    phonetic: '/ˈkɑːr.pət/',
    prompt: 'Si derramas café en la "CARPET", ¿dónde cayó el café?',
    contextSentence: 'She cleaned the stain off the living room carpet.',
    audioText: 'She cleaned the stain off the living room carpet.',
    correctAnswer: 'En la alfombra del piso',
    options: ['En la alfombra del piso', 'En una carpeta de papeles', 'En la cartera personal', 'En el mantel de la mesa'],
    explanation: {
      title: 'CARPET = ALFOMBRA (no carpeta)',
      description: 'Carpet es una alfombra o moqueta. Para guardar documentos usas un "FOLDER" o "BINDER".',
      trick: '💡 La alfombra (carpet) la pisas con los pies; la carpeta (folder) la abres con las manos.'
    },
    confusables: [
      { word: 'carpet', phonetic: '/ˈkɑːr.pət/', meaning: 'Alfombra o moqueta de piso', emoji: '🛋️', exampleSentence: 'Vacuum the bedroom carpet twice a week.' },
      { word: 'folder', phonetic: '/ˈfoʊl.dɚ/', meaning: 'Carpeta de archivos para documentos', emoji: '📁', exampleSentence: 'Save the contracts inside this plastic folder.' }
    ]
  },

  // 9. Attend vs Assist
  {
    id: 'brutal_attend_assist',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'attend',
    phonetic: '/əˈtend/',
    prompt: 'Si tu jefe te dice "You must ATTEND the meeting", ¿qué te está pidiendo?',
    contextSentence: 'All members must attend the morning conference.',
    audioText: 'All members must attend the morning conference.',
    correctAnswer: 'Que asistas o acudas a la reunión',
    options: ['Que asistas o acudas a la reunión', 'Que atiendas a los clientes sirviendo café', 'Que canceles la reunión', 'Que tomes notas'],
    explanation: {
      title: 'Attend = Asistir / Acudir',
      description: 'ATTEND significa acudir o estar presente. ATENDER a alguien (servir o ayudar) es ASSIST o SERVE.',
      trick: '💡 Attendance = asistencia a clase; Assistant = persona que ayuda / atiende.'
    },
    confusables: [
      { word: 'attend', phonetic: '/əˈtend/', meaning: 'Asistir / acudir a un evento', emoji: '🎟️', exampleSentence: 'Hundreds of doctors attended the symposium.' },
      { word: 'assist', phonetic: '/əˈsɪst/', meaning: 'Ayudar / atender a alguien', emoji: '🤝', exampleSentence: 'Can I assist you with your luggage, sir?' }
    ]
  },

  // 10. Flour vs Flower
  {
    id: 'brutal_flour_flower',
    category: 'homophone',
    typeLabel: '👂 Suenan Exactamente Igual',
    targetWord: 'flour',
    phonetic: '/flaʊ.ɚ/',
    prompt: 'Para hornear un pastel necesitas "FLOUR". ¿Qué ingrediente es?',
    contextSentence: 'Mix two cups of wheat flour with baking powder.',
    audioText: 'Mix two cups of wheat flour with baking powder.',
    correctAnswer: 'Harina de trigo',
    options: ['Harina de trigo', 'Flores aromáticas de jardín', 'Piso o suelo', 'Mantequilla derretida'],
    explanation: {
      title: '¡Misma pronunciación, diferente escritura!',
      description: 'FLOUR (/flaʊ.ɚ/) es harina para cocinar. FLOWER (/flaʊ.ɚ/) es la flor que crece en el jardín. Se pronuncian exactamente idénticas.',
      trick: '💡 "Flour" termina en "-ur" de trigo horneado; "Flower" tiene "w" como las flores del campo.'
    },
    confusables: [
      { word: 'flour', phonetic: '/flaʊ.ɚ/', meaning: 'Harina molida para hornear', emoji: '🌾', exampleSentence: 'Dust the kitchen counter with flour.' },
      { word: 'flower', phonetic: '/flaʊ.ɚ/', meaning: 'Flor de planta o jardín', emoji: '🌸', exampleSentence: 'He gave her a red flower.' }
    ]
  },

  // 11. Weather vs Whether
  {
    id: 'brutal_weather_whether',
    category: 'homophone',
    typeLabel: '👂 Suenan Exactamente Igual',
    targetWord: 'whether',
    phonetic: '/ˈweð.ɚ/',
    prompt: '¿Qué significa la palabra "WHETHER" (con Wh)?',
    contextSentence: 'I do not know whether it will rain tomorrow.',
    audioText: 'I do not know whether it will rain tomorrow.',
    correctAnswer: 'Si (condicional / duda de dos opciones)',
    options: ['Si (condicional / duda de dos opciones)', 'El clima y temperatura exterior', 'Vellón de lana de oveja', 'Cuero curtido'],
    explanation: {
      title: 'Weather = Clima | Whether = Si condicional',
      description: 'WEATHER es el clima o el tiempo atmosférico. WHETHER es una conjunción condicional (equivalente a "si... o no").',
      trick: '💡 Weather empieza como Wet (húmedo por la lluvia del clima).'
    },
    confusables: [
      { word: 'weather', phonetic: '/ˈweð.ɚ/', meaning: 'Clima / tiempo atmosférico', emoji: '⛅', exampleSentence: 'The weather is warm and sunny today.' },
      { word: 'whether', phonetic: '/ˈweð.ɚ/', meaning: 'Si (conjunción de duda entre opciones)', emoji: '❓', exampleSentence: 'Let me know whether you can come or not.' }
    ]
  },

  // 12. Peace vs Piece
  {
    id: 'brutal_peace_piece',
    category: 'homophone',
    typeLabel: '👂 Suenan Exactamente Igual',
    targetWord: 'piece',
    phonetic: '/piːs/',
    prompt: 'Si alguien pide "A PIECE of cake", ¿qué está pidiendo?',
    contextSentence: 'Can I have another piece of pizza, please?',
    audioText: 'Can I have another piece of pizza, please?',
    correctAnswer: 'Un pedazo o rebanada',
    options: ['Un pedazo o rebanada', 'Paz y tranquilidad mental', 'Un precio barato', 'Una receta'],
    explanation: {
      title: 'Peace = Paz | Piece = Pedazo / Pieza',
      description: 'Ambas se pronuncian exactamente /piːs/. PEACE es la ausencia de conflicto (paz). PIECE es una porción o fragmento.',
      trick: '💡 "Piece of pie" (pedazo de pay) ambos empiezan con "pie".'
    },
    confusables: [
      { word: 'piece', phonetic: '/piːs/', meaning: 'Pedazo, porción o fragmento', emoji: '🧩', exampleSentence: 'Fit the last puzzle piece into place.' },
      { word: 'peace', phonetic: '/piːs/', meaning: 'Paz y serenidad', emoji: '🕊️', exampleSentence: 'The treaty brought peace to the region.' }
    ]
  },

  // 13. Knight vs Night
  {
    id: 'brutal_knight_night',
    category: 'homophone',
    typeLabel: '👂 Suenan Exactamente Igual',
    targetWord: 'knight',
    phonetic: '/naɪt/',
    prompt: '¿Quién es un "KNIGHT" con K muda inicial?',
    contextSentence: 'The medieval knight wore shiny steel armor.',
    audioText: 'The medieval knight wore shiny steel armor.',
    correctAnswer: 'Un caballero con armadura o espada',
    options: ['Un caballero con armadura o espada', 'La noche oscura', 'Un cuchillo de cocina', 'Un nudo de cuerda'],
    explanation: {
      title: 'La "K" es completamente muda',
      description: 'KNIGHT se pronuncia idéntico a NIGHT (/naɪt/). Knight es el guerrero noble con armadura; Night es la noche con luna.',
      trick: '💡 Recuerda que en ajedrez el caballo es el "Knight" (/naɪt/).'
    },
    confusables: [
      { word: 'knight', phonetic: '/naɪt/', meaning: 'Caballero medieval con armadura', emoji: '⚔️', exampleSentence: 'The knight rode into the castle courtyard.' },
      { word: 'night', phonetic: '/naɪt/', meaning: 'Noche oscura con estrellas', emoji: '🌙', exampleSentence: 'Stars shine brightly in the night sky.' }
    ]
  },

  // 14. Hear vs Here
  {
    id: 'brutal_hear_here',
    category: 'homophone',
    typeLabel: '👂 Suenan Exactamente Igual',
    targetWord: 'hear',
    phonetic: '/hɪr/',
    prompt: '¿Qué significa el verbo "HEAR"?',
    contextSentence: 'Speak louder, I cannot hear you clearly.',
    audioText: 'Speak louder, I cannot hear you clearly.',
    correctAnswer: 'Oír o escuchar sonidos',
    options: ['Oír o escuchar sonidos', 'Aquí / en este lugar', 'El corazón humano', 'Calentar comida'],
    explanation: {
      title: 'Oír (Hear) vs Aquí (Here)',
      description: 'Ambas se pronuncian /hɪr/. "Hear" es percibir con los oídos (Ear). "Here" indica el lugar donde estás.',
      trick: '💡 "Hear" contiene la palabra "EAR" (oreja / oído). ¡Escuchas con tu ear!'
    },
    confusables: [
      { word: 'hear', phonetic: '/hɪr/', meaning: 'Oír o escuchar con el oído', emoji: '👂', exampleSentence: 'Did you hear the thunder outside?' },
      { word: 'here', phonetic: '/hɪr/', meaning: 'Aquí / en este lugar presente', emoji: '📍', exampleSentence: 'Come over here and sit with us.' }
    ]
  },

  // 15. Breathe vs Breath
  {
    id: 'brutal_breathe_breath',
    category: 'homophone',
    typeLabel: '👂 Trampa de Pronunciación y Letra',
    targetWord: 'breathe',
    phonetic: '/briːð/',
    prompt: '¿Cuál es la diferencia entre "BREATHE" (con E al final) y "BREATH"?',
    contextSentence: 'Inhale deeply and breathe slowly through your nose.',
    audioText: 'Inhale deeply and breathe slowly through your nose.',
    correctAnswer: 'Breathe es el verbo respirar (con E final); Breath es el aliento',
    options: [
      'Breathe es el verbo respirar (con E final); Breath es el aliento',
      'Son idénticas y se usan como sustantivo',
      'Breathe es el aliento y Breath es el verbo respirar',
      'Breathe es brisa suave del mar'
    ],
    explanation: {
      title: 'Breathe (verbo) vs Breath (sustantivo)',
      description: '• BREATHE (/briːð/) es el VERBO: respirar. Su vocal es larga (como "ee").\n• BREATH (/breθ/) es el SUSTANTIVO: el aliento o la bocanada de aire.',
      trick: '💡 La "E" final le da fuerza al verbo "breathe" para respirar.'
    },
    confusables: [
      { word: 'breathe', phonetic: '/briːð/', meaning: 'Respirar (verbo en acción)', emoji: '🫁', exampleSentence: 'Take a deep breath and breathe calmly.' },
      { word: 'breath', phonetic: '/breθ/', meaning: 'Aliento o respiración (sustantivo)', emoji: '🌬️', exampleSentence: 'His breath was visible in the cold morning air.' }
    ]
  },

  // 16. Lose vs Loose
  {
    id: 'brutal_lose_loose',
    category: 'homophone',
    typeLabel: '👂 Una O contra Doble O',
    targetWord: 'lose',
    phonetic: '/luːz/',
    prompt: 'Si no quieres extraviar tus llaves, ¿qué verbo usas en inglés?',
    contextSentence: 'Be careful not to lose your room keys.',
    audioText: 'Be careful not to lose your room keys.',
    correctAnswer: 'Lose (con una sola O)',
    options: ['Lose (con una sola O)', 'Loose (con doble O)', 'Loss (con doble S)', 'Lost (en pasado)'],
    explanation: {
      title: 'Lose (/luːz/) vs Loose (/luːs/)',
      description: '• LOSE (1 sola O) = Perder o extraviar algo (termina en sonido Z).\n• LOOSE (2 Oes) = Flojo, holgado o suelto (ropa floja, tornillo suelto).',
      trick: '💡 "Loose" tiene doble O porque le sobra espacio y está flojo.'
    },
    confusables: [
      { word: 'lose', phonetic: '/luːz/', meaning: 'Perder o extraviar algo', emoji: '🔑', exampleSentence: 'Do not lose your wallet in the subway.' },
      { word: 'loose', phonetic: '/luːs/', meaning: 'Flojo, holgado o suelto', emoji: '👖', exampleSentence: 'These jeans are too loose on my waist.' }
    ]
  },

  // 17. Tear (Homograph)
  {
    id: 'brutal_tear_homograph',
    category: 'homograph',
    typeLabel: '🔤 Homógrafo (Doble Sonido)',
    targetWord: 'tear',
    phonetic: '/tɪr/ o /ter/',
    prompt: 'La palabra "TEAR" tiene dos pronunciaciones diferentes. ¿Cuáles son sus dos significados?',
    contextSentence: 'A tear fell from her eye when she tore the letter.',
    audioText: 'A tear fell from her eye when she began to tear the letter.',
    correctAnswer: 'Lágrima (/tɪr/) y Rasgar o romper papel (/ter/)',
    options: [
      'Lágrima (/tɪr/) y Rasgar o romper papel (/ter/)',
      'Té caliente y Té frío con hielo',
      'Terreno campestre y Terror nocturno',
      'Cansado y Con sueño'
    ],
    explanation: {
      title: '¡Dos palabras gemelas en escritura!',
      description: '• TEAR (/tɪr/): Lágrima que sale del ojo.\n• TEAR (/ter/): Rasgar o desgarrar tela o papel.',
      trick: '💡 Si rima con "near", es la lágrima (/tɪr/). Si rima con "bear", es rasgar (/ter/).'
    },
    confusables: [
      { word: 'tear (lágrima)', phonetic: '/tɪr/', meaning: 'Gota de llanto que cae del ojo', emoji: '😢' },
      { word: 'tear (rasgar)', phonetic: '/ter/', meaning: 'Romper o desgarrar papel o tela', emoji: '📄' }
    ]
  },

  // 18. Lead (Homograph)
  {
    id: 'brutal_lead_homograph',
    category: 'homograph',
    typeLabel: '🔤 Homógrafo (Doble Sonido)',
    targetWord: 'lead',
    phonetic: '/liːd/ o /led/',
    prompt: '¿Qué dos significados completamente distintos tiene "LEAD"?',
    contextSentence: 'The general will lead the army; the pipe is made of heavy lead.',
    audioText: 'The captain will lead the team, but the heavy metal pipe was made of lead.',
    correctAnswer: 'Guiar / liderar (/liːd/) y Plomo mineral (/led/)',
    options: [
      'Guiar / liderar (/liːd/) y Plomo mineral (/led/)',
      'Leer un libro y Hojear una revista',
      'Salto gimnástico y Carrera veloz',
      'Cable eléctrico y Enchufe de pared'
    ],
    explanation: {
      title: 'Liderar (/liːd/) vs Plomo (/led/)',
      description: 'Como verbo, "to lead" (/liːd/) es guiar o dirigir. Como metal pesado, "lead" (/led/) es el plomo químico.',
      trick: '💡 El líder guía con energía (/liːd/); el plomo pesa como el pasado de read (/led/).'
    },
    confusables: [
      { word: 'lead (guiar)', phonetic: '/liːd/', meaning: 'Dirigir o liderar un grupo', emoji: '🧭' },
      { word: 'lead (plomo)', phonetic: '/led/', meaning: 'Metal pesado tóxico (Pb)', emoji: '🔩' }
    ]
  },

  // 19. Soap vs Soup
  {
    id: 'brutal_soap_soup',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo en la Cocina y Baño',
    targetWord: 'soap',
    phonetic: '/soʊp/',
    prompt: 'Si te lavas las manos en el baño, ¿qué usas?',
    contextSentence: 'Wash your hands thoroughly with warm water and soap.',
    audioText: 'Wash your hands thoroughly with warm water and soap.',
    correctAnswer: 'Soap (jabón para higiene)',
    options: ['Soap (jabón para higiene)', 'Soup (sopa caliente con fideos)', 'Supper (cena ligera)', 'Spoon (cuchara sopera)'],
    explanation: {
      title: '¡No te comas el jabón!',
      description: 'SOAP (/soʊp/) es el JABÓN para bañarte o lavarte las manos. SOUP (/suːp/) es la SOPA caliente de comer.',
      trick: '💡 "Soup" tiene la "u" de comer con cuchara. "Soap" tiene la "oa" de espuma.'
    },
    confusables: [
      { word: 'soap', phonetic: '/soʊp/', meaning: 'Jabón para lavar la piel', emoji: '🧼', exampleSentence: 'Lather the fragrant soap in your hands.' },
      { word: 'soup', phonetic: '/suːp/', meaning: 'Sopa caliente comestible', emoji: '🥣', exampleSentence: 'She cooked chicken noodle soup for dinner.' }
    ]
  },

  // 20. Rope vs Clothes (Ropa)
  {
    id: 'brutal_rope_clothes',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'rope',
    phonetic: '/roʊp/',
    prompt: '¿Qué es una "ROPE" en inglés?',
    contextSentence: 'Tie the wooden boat securely to the dock with a thick rope.',
    audioText: 'Tie the wooden boat securely to the dock with a thick rope.',
    correctAnswer: 'Una cuerda o soga resistente',
    options: ['Una cuerda o soga resistente', 'Ropa o prendas de vestir', 'Ropero o armario de madera', 'Un robo a mano armada'],
    explanation: {
      title: 'ROPE = CUERDA (¡No es ropa!)',
      description: 'Rope es una soga o mecate. Las prendas de vestir que te pones todos los días son "CLOTHES" (/kloʊðz/).',
      trick: '💡 Imagina a un vaquero lazando con una cuerda (rope) para recordar que es soga.'
    },
    confusables: [
      { word: 'rope', phonetic: '/roʊp/', meaning: 'Cuerda o soga resistente', emoji: '🪢', exampleSentence: 'The mountain climbers tied their safety rope.' },
      { word: 'clothes', phonetic: '/kloʊðz/', meaning: 'Ropa / prendas de vestir', emoji: '👕', exampleSentence: 'Put your clean clothes in the dresser.' }
    ]
  },

  // 21. Fabric vs Factory
  {
    id: 'brutal_fabric_factory',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Doble',
    targetWord: 'fabric',
    phonetic: '/ˈfæb.rɪk/',
    prompt: 'Si vas a una tienda y compras "FABRIC", ¿qué compraste?',
    contextSentence: 'She bought five meters of floral cotton fabric to sew curtains.',
    audioText: 'She bought five meters of floral cotton fabric to sew curtains.',
    correctAnswer: 'Tela o tejido para confeccionar',
    options: ['Tela o tejido para confeccionar', 'Una fábrica con chimeneas industriales', 'Ladrillos de construcción', 'Herramientas de hierro'],
    explanation: {
      title: 'Fabric = Tela | Factory = Fábrica',
      description: 'FABRIC es tela o tejido (seda, algodón, etc.). La instalación donde fabrican autos o máquinas es una FACTORY.',
      trick: '💡 Fabric = fibra textil (tela); Factory = manufactura (fábrica).'
    },
    confusables: [
      { word: 'fabric', phonetic: '/ˈfæb.rɪk/', meaning: 'Tela o material textil', emoji: '🧵', exampleSentence: 'Silk is a very soft and expensive fabric.' },
      { word: 'factory', phonetic: '/ˈfæk.tɚ.i/', meaning: 'Fábrica o planta industrial', emoji: '🏭', exampleSentence: 'He works as an engineer at the automobile factory.' }
    ]
  },

  // 22. College vs School
  {
    id: 'brutal_college_school',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Escolar',
    targetWord: 'college',
    phonetic: '/ˈkɑː.lɪdʒ/',
    prompt: 'En Estados Unidos, cuando dicen "She is going to COLLEGE", ¿adónde va?',
    contextSentence: 'After high school, he enrolled in a four-year engineering college.',
    audioText: 'After high school, he enrolled in a four-year engineering college.',
    correctAnswer: 'A la universidad (estudios superiores / licenciatura)',
    options: ['A la universidad (estudios superiores / licenciatura)', 'A la escuela primaria o colegio infantil', 'A un colegio privado de monjas', 'A un club de colegas'],
    explanation: {
      title: 'College = Universidad',
      description: 'En inglés, "College" se refiere a la educación universitaria terciaria. Para niños de primaria se usa "Elementary School" o simplemente "School".',
      trick: '💡 College student = estudiante universitario con licenciatura en curso.'
    },
    confusables: [
      { word: 'college', phonetic: '/ˈkɑː.lɪdʒ/', meaning: 'Universidad / educación superior', emoji: '🎓', exampleSentence: 'College degrees open many career opportunities.' },
      { word: 'school', phonetic: '/skuːl/', meaning: 'Colegio escolar / escuela', emoji: '🏫', exampleSentence: 'The school bus picks up children at eight.' }
    ]
  },

  // 23. Constipated
  {
    id: 'brutal_constipated',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Médico',
    targetWord: 'constipated',
    phonetic: '/ˈkɑːn.stə.peɪ.t̬ɪd/',
    prompt: 'Si un paciente en el hospital dice que está "CONSTIPATED", ¿qué malestar tiene?',
    contextSentence: 'Eating more dietary fiber helps when you are constipated.',
    audioText: 'Eating more dietary fiber helps when you are constipated.',
    correctAnswer: 'Tiene estreñimiento digestivo',
    options: ['Tiene estreñimiento digestivo', 'Tiene un resfriado con mocos en la nariz', 'Tiene dolor de cabeza', 'Tiene fiebre alta'],
    explanation: {
      title: '¡No confundas estreñido con resfriado!',
      description: 'En español "estar constipado" a veces se usa coloquialmente para decir resfriado. Pero en inglés CONSTIPATED es exclusivamente estreñimiento digestivo. Estar resfriado es "HAVE A COLD".',
      trick: '💡 Para la nariz tapada di: "I have a cold". ¡Nunca digas "I am constipated" si tienes gripe!'
    },
    confusables: [
      { word: 'constipated', phonetic: '/ˈkɑːn.stə.peɪ.t̬ɪd/', meaning: 'Estreñido (dificultad digestiva)', emoji: '😣', exampleSentence: 'Drink lots of water if you are constipated.' },
      { word: 'having a cold', phonetic: '/ˌhæv.ɪŋ ə ˈkoʊld/', meaning: 'Estar resfriado / acatarrado', emoji: '🤧', exampleSentence: 'I stayed in bed because I had a cold.' }
    ]
  },

  // 24. Sea vs See
  {
    id: 'brutal_sea_see',
    category: 'homophone',
    typeLabel: '👂 Suenan Idénticas',
    targetWord: 'sea',
    phonetic: '/siː/',
    prompt: '¿Qué significa la palabra "SEA" (escrita con ea)?',
    contextSentence: 'Dolphins swim peacefully in the blue sea.',
    audioText: 'Dolphins swim peacefully in the blue sea.',
    correctAnswer: 'El mar salado',
    options: ['El mar salado', 'El verbo ver o mirar', 'La letra C del abecedario', 'Sentarse en una silla'],
    explanation: {
      title: 'Sea = Mar | See = Ver',
      description: 'Ambas se pronuncian exactamente /siː/. "Sea" es el mar oceánico. "See" es el verbo mirar con los ojos (ojos = doble e).',
      trick: '💡 "See" tiene dos ojos (las dos letras "e") para ver.'
    },
    confusables: [
      { word: 'sea', phonetic: '/siː/', meaning: 'Mar de aguas saladas', emoji: '🌊', exampleSentence: 'Ships sail across the Mediterranean Sea.' },
      { word: 'see', phonetic: '/siː/', meaning: 'Ver o mirar con los ojos', emoji: '👀', exampleSentence: 'I can see the mountains in the distance.' }
    ]
  },

  // 25. Brake vs Break
  {
    id: 'brutal_brake_break',
    category: 'homophone',
    typeLabel: '👂 Suenan Idénticas',
    targetWord: 'brake',
    phonetic: '/breɪk/',
    prompt: 'Si vas manejando tu auto y necesitas detenerte en el semáforo, ¿qué pisas?',
    contextSentence: 'Step on the brake pedal to bring the car to a halt.',
    audioText: 'Step on the brake pedal to bring the car to a halt.',
    correctAnswer: 'The brake (el pedal de freno)',
    options: ['The brake (el pedal de freno)', 'The break (la pausa de café)', 'The brick (el ladrillo)', 'The broke (el quebrado)'],
    explanation: {
      title: 'Brake = Freno | Break = Romper / Pausa',
      description: 'BRAKE (/breɪk/) es el freno del auto o bicicleta. BREAK (/breɪk/) es romper algo, o tomarse un descanso ("coffee break").',
      trick: '💡 Brake termina con K-E de frenado; Break tiene EA como "tear" (deshacer/romper).'
    },
    confusables: [
      { word: 'brake', phonetic: '/breɪk/', meaning: 'Freno de vehículo o bicicleta', emoji: '🛑', exampleSentence: 'Bicycle brakes need regular maintenance.' },
      { word: 'break', phonetic: '/breɪk/', meaning: 'Romper algo o tomar una pausa de descanso', emoji: '☕', exampleSentence: 'Let us take a ten-minute coffee break.' }
    ]
  },

  // 26. Through vs Thorough vs Though vs Thought vs Tough
  {
    id: 'brutal_five_th_words',
    category: 'homophone',
    typeLabel: '💀 El Monstruo de las 5 Palabras',
    targetWord: 'thorough',
    phonetic: '/ˈθɝː.oʊ/',
    prompt: '¿Qué significa la palabra "THOROUGH" (con doble o y ugh)?',
    contextSentence: 'The forensic police conducted a thorough investigation.',
    audioText: 'The forensic police conducted a thorough investigation.',
    correctAnswer: 'Minucioso, exhaustivo y a fondo',
    options: [
      'Minucioso, exhaustivo y a fondo',
      'A través de un túnel (through)',
      'Aunque o a pesar de (though)',
      'Pensamiento o pensó (thought)'
    ],
    explanation: {
      title: '¡El quinteto que vuelve locos a todos!',
      description: '• Through (/θruː/) = A través de.\n• Thorough (/ˈθɝː.oʊ/) = Minucioso / exhaustivo.\n• Though (/ðoʊ/) = Aunque.\n• Thought (/θɔːt/) = Pensó / pensamiento.\n• Tough (/tʌf/) = Difícil / duro.',
      trick: '💡 "Thorough" tiene dos "o" como si revisaras todo dos veces con lupa (a fondo).'
    },
    confusables: [
      { word: 'thorough', phonetic: '/ˈθɝː.oʊ/', meaning: 'Minucioso y detallado', emoji: '🔍' },
      { word: 'through', phonetic: '/θruː/', meaning: 'A través de un lugar', emoji: '🚇' },
      { word: 'thought', phonetic: '/θɔːt/', meaning: 'Pensó o pensamiento', emoji: '💭' },
      { word: 'though', phonetic: '/ðoʊ/', meaning: 'Aunque / a pesar de', emoji: '🤷' },
      { word: 'tough', phonetic: '/tʌf/', meaning: 'Duro, fuerte o difícil', emoji: '💪' }
    ]
  },

  // 27. Wind (Homograph)
  {
    id: 'brutal_wind_homograph',
    category: 'homograph',
    typeLabel: '🔤 Homógrafo (Doble Sonido)',
    targetWord: 'wind',
    phonetic: '/wɪnd/ o /waɪnd/',
    prompt: '¿Qué dos significados y pronunciaciones tiene "WIND"?',
    contextSentence: 'The wind was blowing cold, so he had to wind up the clock.',
    audioText: 'The chilly wind blew hard, so remember to wind up your watch.',
    correctAnswer: 'Viento del aire (/wɪnd/) y Dar cuerda / serpentear (/waɪnd/)',
    options: [
      'Viento del aire (/wɪnd/) y Dar cuerda / serpentear (/waɪnd/)',
      'Ventana de cristal y Marco de madera',
      'Alambre de cobre y Tubo de plástico',
      'Caminar despacio y Correr rápido'
    ],
    explanation: {
      title: 'Wind (/wɪnd/) vs Wind (/waɪnd/)',
      description: '• WIND con "i" corta (/wɪnd/) = El viento que sopla.\n• WIND con "i" larga (/waɪnd/) = Dar cuerda a un reloj, o un río que serpentea ("winding road").',
      trick: '💡 Si sopla en tu cara es /wɪnd/; si das vueltas con la mano es /waɪnd/.'
    },
    confusables: [
      { word: 'wind (viento)', phonetic: '/wɪnd/', meaning: 'Corriente de aire atmosférico', emoji: '💨' },
      { word: 'wind (dar cuerda)', phonetic: '/waɪnd/', meaning: 'Girar o enrollar cuerda o mecanismo', emoji: '🔄' }
    ]
  },

  // 28. Close (Homograph)
  {
    id: 'brutal_close_homograph',
    category: 'homograph',
    typeLabel: '🔤 Homógrafo (Sonido S vs Z)',
    targetWord: 'close',
    phonetic: '/kloʊs/ o /kloʊz/',
    prompt: '¿Cómo cambia "CLOSE" según se pronuncie con sonido /s/ o /z/?',
    contextSentence: 'Close the door; my friend lives close to my house.',
    audioText: 'Please close the front door. We are very close friends.',
    correctAnswer: 'Con /z/ es cerrar la puerta; con /s/ es cercano o íntimo',
    options: [
      'Con /z/ es cerrar la puerta; con /s/ es cercano o íntimo',
      'Con /z/ es ropa y con /s/ es reloj',
      'Son exactamente idénticas sin ninguna diferencia',
      'Con /z/ es clavel y con /s/ es nube'
    ],
    explanation: {
      title: '¡El sonido final cambia la palabra!',
      description: '• TO CLOSE (/kloʊz/ con vibración de abeja Z) = El verbo CERRAR.\n• CLOSE (/kloʊs/ con sonido sordo de serpiente S) = Adjetivo CERCANO.',
      trick: '💡 "Close friends" se dice con S suave; "Close the door" vibra con Z.'
    },
    confusables: [
      { word: 'close (verbo)', phonetic: '/kloʊz/', meaning: 'Cerrar una puerta o ventana', emoji: '🚪' },
      { word: 'close (adjetivo)', phonetic: '/kloʊs/', meaning: 'Cercano en distancia o amistad', emoji: '🤝' }
    ]
  },

  // 29. Avocado vs Lawyer (Abogado)
  {
    id: 'brutal_avocado_lawyer',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Chistoso',
    targetWord: 'avocado',
    phonetic: '/ˌæv.əˈkɑː.doʊ/',
    prompt: 'Si necesitas contratar a un profesional legal que te defienda en la corte, ¿a quién buscas?',
    contextSentence: 'The defense lawyer presented evidence in the court trial.',
    audioText: 'The defense lawyer presented evidence in the court trial.',
    correctAnswer: 'A lawyer (o attorney)',
    options: ['A lawyer (o attorney)', 'An avocado (delicioso con sal)', 'An advocate', 'A solicitor'],
    explanation: {
      title: '¡No contrates a un aguacate en el juzgado!',
      description: 'En francés abogado es "avocat", lo que confunde a muchos. Pero en inglés "AVOCADO" es únicamente el fruto verde (aguacate / palta). El profesional de leyes es "LAWYER" o "ATTORNEY".',
      trick: '💡 El "Avocado" lo pones en el guacamole con totopos; el "Lawyer" te defiende ante el juez.'
    },
    confusables: [
      { word: 'avocado', phonetic: '/ˌæv.əˈkɑː.doʊ/', meaning: 'Aguacate o palta vegetal', emoji: '🥑' },
      { word: 'lawyer', phonetic: '/ˈlɔɪ.ɚ/', meaning: 'Abogado profesional de leyes', emoji: '⚖️' }
    ]
  },

  // 30. Argument vs Plot
  {
    id: 'brutal_argument_plot',
    category: 'false_friend',
    typeLabel: '🚫 Falso Amigo Peligroso',
    targetWord: 'argument',
    phonetic: '/ˈɑːrɡ.jə.mənt/',
    prompt: 'Si dos personas tienen un "ARGUMENT" en la calle, ¿qué está ocurriendo?',
    contextSentence: 'The neighbors had a loud argument over the parking space.',
    audioText: 'The neighbors had a loud argument over the parking space.',
    correctAnswer: 'Están discutiendo acaloradamente o peleando',
    options: [
      'Están discutiendo acaloradamente o peleando',
      'Están redactando la trama de una novela',
      'Están presentando un argumento filosófico formal',
      'Están contando una anécdota cómica'
    ],
    explanation: {
      title: 'Argument = Discusión / Pelea verbal',
      description: 'En el día a día, un "argument" es una discusión o pelea entre personas. La trama o argumento literario de una película o libro es "PLOT" o "STORYLINE".',
      trick: '💡 Si gritan en la sala, es un "argument" (pleito).'
    },
    confusables: [
      { word: 'argument', phonetic: '/ˈɑːrɡ.jə.mənt/', meaning: 'Discusión / riña verbal acalorada', emoji: '🤬' },
      { word: 'plot', phonetic: '/plɑːt/', meaning: 'Argumento o trama de un libro o filme', emoji: '🎬' }
    ]
  }
];
