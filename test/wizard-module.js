/* ==========================================================================
   TAYRONA GUIDE — TRIP WIZARD MODULE JS (2026)
   Self-contained module. Call TripWizard.init('#container-id') to mount.
   ========================================================================== */

window.TripWizard = (function () {

  /* -------------------------------------------------------------------------
   * DATA — Accommodations
   * ----------------------------------------------------------------------- */
  const ACCOMMODATIONS = {
    'casa-isabella': {
      id: 'casa-isabella',
      emoji: '🏛️',
      name: { en: 'Casa de Isabella', es: 'Casa de Isabella', it: 'Casa de Isabella', fr: 'Casa de Isabella', de: 'Casa de Isabella' },
      location: { en: 'Santa Marta Historic Center', es: 'Centro Histórico Santa Marta', it: 'Centro Storico Santa Marta', fr: 'Centre Historique Santa Marta', de: 'Historisches Zentrum Santa Marta' },
      desc: {
        en: 'A boutique colonial house in the heart of Santa Marta\'s Historic Center. Elegant rooms, rooftop terrace and authentic Caribbean atmosphere steps from the Cathedral.',
        es: 'Casa boutique colonial en el corazón del Centro Histórico de Santa Marta. Habitaciones elegantes, terraza en azotea y auténtica atmósfera caribeña a pasos de la Catedral.',
        it: 'Casa boutique coloniale nel cuore del Centro Storico di Santa Marta. Camere eleganti, terrazza sul tetto e autentica atmosfera caraibica a pochi passi dalla Cattedrale.',
        fr: 'Maison boutique coloniale au cœur du Centre Historique de Santa Marta. Chambres élégantes, terrasse sur le toit et atmosphère caribéenne authentique à deux pas de la Cathédrale.',
        de: 'Boutique-Kolonialhaus im Herzen des Historischen Zentrums von Santa Marta. Elegante Zimmer, Dachterrasse und authentische karibische Atmosphäre, nur wenige Schritte von der Kathedrale entfernt.'
      },
      type: 'city',
      priceUSD: 75,
      rooms: [
        {
          tier: 'base',
          priceUSD: 75,
          name: { en: 'Standard Room', es: 'Habitación Estándar', it: 'Camera Standard', fr: 'Chambre Standard', de: 'Standardzimmer' },
          desc: { en: 'Comfortable colonial-style room with private bathroom, AC and courtyard views. Perfect for a great value stay in the Historic Center.', es: 'Cómoda habitación de estilo colonial con baño privado, aire acondicionado y vistas al patio. Perfecta para una estadía de gran valor en el Centro Histórico.', it: 'Confortevole camera in stile coloniale con bagno privato, AC e vista sul cortile. Perfetta per un soggiorno di grande valore nel Centro Storico.', fr: 'Chambre coloniale confortable avec salle de bain privée, AC et vue sur la cour. Parfaite pour un séjour de grande valeur dans le Centre Historique.', de: 'Komfortables Zimmer im Kolonialstil mit eigenem Bad, Klimaanlage und Innenhofblick. Perfekt für einen günstigen Aufenthalt im Historischen Zentrum.' }
        },
        {
          tier: 'mid',
          priceUSD: 105,
          name: { en: 'Superior Room', es: 'Habitación Superior', it: 'Camera Superiore', fr: 'Chambre Supérieure', de: 'Superiorzimmer' },
          desc: { en: 'Spacious superior room with colonial decor, premium amenities, king bed and garden or street views. Includes daily breakfast on the rooftop terrace.', es: 'Amplia habitación superior con decoración colonial, amenidades premium, cama king y vistas al jardín o la calle. Incluye desayuno diario en la terraza.', it: 'Spaziosa camera superiore con arredamento coloniale, servizi premium, letto king e viste sul giardino o sulla strada. Include colazione giornaliera in terrazza.', fr: 'Chambre supérieure spacieuse avec décor colonial, équipements premium, lit king et vues sur le jardin ou la rue. Comprend le petit-déjeuner quotidien sur la terrasse.', de: 'Geräumiges Superiorzimmer mit Kolonialdekor, Premium-Ausstattung, Kingsize-Bett und Garten- oder Straßenblick. Mit täglichem Frühstück auf der Dachterrasse.' }
        },
        {
          tier: 'top',
          priceUSD: 145,
          name: { en: 'Rooftop Suite', es: 'Suite Terraza', it: 'Suite Terrazza', fr: 'Suite Terrasse', de: 'Dachterrassen-Suite' },
          desc: { en: 'Exclusive rooftop suite with private terrace, panoramic views of the Historic Center and Cathedral, luxury bath and butler service. The ultimate colonial luxury experience.', es: 'Suite exclusiva en azotea con terraza privada, vistas panorámicas del Centro Histórico y la Catedral, baño de lujo y servicio de mayordomo. La experiencia colonial de lujo definitiva.', it: 'Suite esclusiva sul tetto con terrazza privata, viste panoramiche del Centro Storico e della Cattedrale, bagno di lusso e servizio maggiordomo. L\'esperienza coloniale di lusso definitiva.', fr: 'Suite exclusive sur le toit avec terrasse privée, vues panoramiques sur le Centre Historique et la Cathédrale, bain de luxe et service de majordome. L\'expérience coloniale de luxe ultime.', de: 'Exklusive Dachsuite mit privater Terrasse, Panoramablick auf das Historische Zentrum und die Kathedrale, Luxusbad und Butler-Service. Das ultimative koloniale Luxuserlebnis.' }
        }
      ]
    },
    'casa-leda': {
      id: 'casa-leda',
      emoji: '🌊',
      name: { en: 'Casa de Leda', es: 'Casa de Leda', it: 'Casa de Leda', fr: 'Casa de Leda', de: 'Casa de Leda' },
      location: { en: 'Santa Marta', es: 'Santa Marta', it: 'Santa Marta', fr: 'Santa Marta', de: 'Santa Marta' },
      desc: {
        en: 'A charming, intimate guesthouse in Santa Marta offering a warm, home-like feel with personalized service and easy access to the city\'s best restaurants and beaches.',
        es: 'Una encantadora posada íntima en Santa Marta que ofrece un ambiente cálido y hogareño con servicio personalizado y fácil acceso a los mejores restaurantes y playas de la ciudad.',
        it: 'Un\'affascinante e intima guest house a Santa Marta che offre un\'atmosfera calda e familiare con servizio personalizzato e facile accesso ai migliori ristoranti e spiagge della città.',
        fr: 'Une charmante maison d\'hôtes intime à Santa Marta offrant une ambiance chaleureuse et familiale avec un service personnalisé et un accès facile aux meilleurs restaurants et plages de la ville.',
        de: 'Ein charmantes, intimes Gästehaus in Santa Marta mit warmer, heimeliger Atmosphäre, persönlichem Service und einfachem Zugang zu den besten Restaurants und Stränden der Stadt.'
      },
      type: 'city',
      priceUSD: 65,
      rooms: [
        {
          tier: 'base',
          priceUSD: 65,
          name: { en: 'Cozy Room', es: 'Habitación Acogedora', it: 'Camera Accogliente', fr: 'Chambre Cosy', de: 'Gemütliches Zimmer' },
          desc: { en: 'A warm, intimate room with all essentials: comfortable bed, private bath, fan and AC. Ideal for solo travelers and couples seeking authentic charm.', es: 'Habitación acogedora con todo lo esencial: cama cómoda, baño privado, ventilador y AC. Ideal para viajeros solos y parejas que buscan auténtico encanto.', it: 'Camera calda e intima con tutto l\'essenziale: letto comodo, bagno privato, ventilatore e AC. Ideale per viaggiatori solitari e coppie in cerca di autentico fascino.', fr: 'Chambre chaleureuse et intime avec tout l\'essentiel : lit confortable, salle de bain privée, ventilateur et AC. Idéale pour les voyageurs solos et les couples cherchant un charme authentique.', de: 'Warmes, intimes Zimmer mit allem Notwendigen: bequemes Bett, eigenem Bad, Ventilator und Klimaanlage. Ideal für Alleinreisende und Paare, die echten Charme suchen.' }
        },
        {
          tier: 'mid',
          priceUSD: 90,
          name: { en: 'Deluxe Room', es: 'Habitación Deluxe', it: 'Camera Deluxe', fr: 'Chambre Deluxe', de: 'Deluxe-Zimmer' },
          desc: { en: 'Larger room with premium bedding, air conditioning, enhanced decor and a seating area. Access to the shared garden terrace and complimentary breakfast.', es: 'Habitación más amplia con ropa de cama premium, aire acondicionado, decoración mejorada y zona de estar. Acceso a la terraza jardín compartida y desayuno incluido.', it: 'Camera più spaziosa con biancheria premium, aria condizionata, arredamento migliorato e zona salotto. Accesso alla terrazza giardino condivisa e colazione inclusa.', fr: 'Chambre plus grande avec literie premium, climatisation, décoration améliorée et coin salon. Accès à la terrasse jardin commune et petit-déjeuner inclus.', de: 'Größeres Zimmer mit Premium-Bettwäsche, Klimaanlage, aufgewerteter Dekoration und Sitzbereich. Zugang zur gemeinsamen Gartentetrasse und Frühstück inklusive.' }
        },
        {
          tier: 'top',
          priceUSD: 125,
          name: { en: 'Garden Suite', es: 'Suite Jardín', it: 'Suite Giardino', fr: 'Suite Jardin', de: 'Garten-Suite' },
          desc: { en: 'Private garden suite with independent entrance, king bed, hammock terrace, premium bath products and personalized daily service. Privacy and tranquility at its finest.', es: 'Suite jardín privada con entrada independiente, cama king, terraza con hamaca, productos de baño premium y servicio diario personalizado. Privacidad y tranquilidad en su máxima expresión.', it: 'Suite giardino privata con ingresso indipendente, letto king, terrazza con amaca, prodotti da bagno premium e servizio giornaliero personalizzato. Privacy e tranquillità nella loro massima espressione.', fr: 'Suite jardin privée avec entrée indépendante, lit king, terrasse avec hamac, produits de bain premium et service quotidien personnalisé. Intimité et tranquillité dans toute leur splendeur.', de: 'Private Gartensuite mit eigenem Eingang, Kingsize-Bett, Hängematten-Terrasse, Premium-Badprodukten und personalisiertem Tagesservice. Privatsphäre und Ruhe in ihrer schönsten Form.' }
        }
      ]
    },
    'villa-maria': {
      id: 'villa-maria',
      emoji: '🌿',
      name: { en: 'Villa María Tayrona', es: 'Villa María Tayrona', it: 'Villa María Tayrona', fr: 'Villa María Tayrona', de: 'Villa María Tayrona' },
      location: { en: 'Jungle & Sea — Tayrona Area', es: 'Jungla y Mar — Área Tayrona', it: 'Giungla e Mare — Area Tayrona', fr: 'Jungle et Mer — Zone Tayrona', de: 'Dschungel & Meer — Tayrona-Gebiet' },
      desc: {
        en: 'A luxury jungle sanctuary where the Sierra Nevada meets the Caribbean Sea. Private beach access, infinity pool with ocean panorama, howler monkeys, tropical birds and the finest nature experience in the Tayrona area.',
        es: 'Un santuario de lujo en la selva donde la Sierra Nevada se encuentra con el mar Caribe. Acceso a playa privada, piscina infinita con panorama oceánico, monos aulladores, aves tropicales y la mejor experiencia natural en el área de Tayrona.',
        it: 'Un santuario di lusso nella giungla dove la Sierra Nevada incontra il mar dei Caraibi. Accesso a spiaggia privata, piscina a sfioro con panorama oceanico, scimmie urlatrici, uccelli tropicali e la migliore esperienza naturale nell\'area di Tayrona.',
        fr: 'Un sanctuaire de luxe dans la jungle où la Sierra Nevada rencontre la mer des Caraïbes. Accès à une plage privée, piscine à débordement avec panorama sur l\'océan, singes hurleurs, oiseaux tropicaux et la meilleure expérience naturelle de la zone Tayrona.',
        de: 'Ein Luxusrefugium im Dschungel, wo die Sierra Nevada auf die Karibik trifft. Privatstrandzugang, Infinity-Pool mit Meerpanorama, Brüllaffen, Tropenvögel und das beste Naturerlebnis in der Tayrona-Region.'
      },
      type: 'jungle',
      priceUSD: 110,
      hasKasankala: true,
      rooms: [
        {
          tier: 'base',
          priceUSD: 110,
          name: { en: 'Jungle Room', es: 'Habitación Selva', it: 'Camera Jungle', fr: 'Chambre Jungle', de: 'Dschungelzimmer' },
          desc: { en: 'Immersed in the tropical forest with natural ventilation, bamboo decor and outdoor shower. Wake up to birdsong and the sound of the sea — pure nature at an accessible price.', es: 'Inmersa en el bosque tropical con ventilación natural, decoración en bambú y ducha exterior. Despierta con el canto de las aves y el sonido del mar — naturaleza pura a un precio accesible.', it: 'Immersa nella foresta tropicale con ventilazione naturale, arredamento in bambù e doccia esterna. Svegliati con il canto degli uccelli e il suono del mare — natura pura a un prezzo accessibile.', fr: 'Immergée dans la forêt tropicale avec ventilation naturelle, décor en bambou et douche extérieure. Réveillez-vous au chant des oiseaux et au bruit de la mer — nature pure à un prix accessible.', de: 'Im tropischen Wald eingebettet mit natürlicher Belüftung, Bambus-Dekor und Außendusche. Wachen Sie beim Vogelgesang und Meeresrauschen auf — pure Natur zu einem zugänglichen Preis.' }
        },
        {
          tier: 'mid',
          priceUSD: 155,
          name: { en: 'Ocean View Bungalow', es: 'Bungalow Vista al Mar', it: 'Bungalow Vista Oceano', fr: 'Bungalow Vue Mer', de: 'Meerblick-Bungalow' },
          desc: { en: 'Private bungalow with Caribbean sea and Sierra Nevada panoramic views, king bed, en-suite bathroom, private terrace with hammock and direct path to the beach.', es: 'Bungalow privado con vistas panorámicas al mar Caribe y la Sierra Nevada, cama king, baño en suite, terraza privada con hamaca y sendero directo a la playa.', it: 'Bungalow privato con viste panoramiche sul mar dei Caraibi e la Sierra Nevada, letto king, bagno en-suite, terrazza privata con amaca e sentiero diretto alla spiaggia.', fr: 'Bungalow privé avec vues panoramiques sur la mer des Caraïbes et la Sierra Nevada, lit king, salle de bain en suite, terrasse privée avec hamac et chemin direct vers la plage.', de: 'Privater Bungalow mit Panoramablick auf die Karibik und die Sierra Nevada, Kingsize-Bett, eigenem Bad, privater Terrasse mit Hängematte und direktem Weg zum Strand.' }
        },
        {
          tier: 'top',
          priceUSD: 210,
          name: { en: 'Infinity Pool Villa Suite', es: 'Villa Suite Piscina Infinita', it: 'Villa Suite Piscina Infinita', fr: 'Suite Villa Piscine à Débordement', de: 'Infinity-Pool Villa Suite' },
          desc: { en: 'The ultimate sanctuary: private villa with exclusive infinity pool access, panoramic ocean and Sierra Nevada views, butler service, curated minibar and a plunge pool on the terrace. An experience beyond imagination.', es: 'El santuario definitivo: villa privada con acceso exclusivo a la piscina infinita, vistas panorámicas al océano y la Sierra Nevada, servicio de mayordomo, minibar curado y plunge pool en la terraza. Una experiencia más allá de la imaginación.', it: 'Il santuario definitivo: villa privata con accesso esclusivo alla piscina infinita, viste panoramiche sull\'oceano e la Sierra Nevada, servizio maggiordomo, minibar curato e plunge pool in terrazza. Un\'esperienza oltre l\'immaginazione.', fr: 'Le sanctuaire ultime : villa privée avec accès exclusif à la piscine à débordement, vues panoramiques sur l\'océan et la Sierra Nevada, service de majordome, minibar sélectionné et plunge pool sur la terrasse. Une expérience au-delà de l\'imagination.', de: 'Das ultimative Refugium: private Villa mit exklusivem Infinity-Pool-Zugang, Panoramablick auf Ozean und Sierra Nevada, Butler-Service, kurierter Minibar und Plunge-Pool auf der Terrasse. Ein Erlebnis jenseits der Vorstellungskraft.' }
        }
      ]
    }
  };

  /* -------------------------------------------------------------------------
   * DATA — Activities (loaded from tours_girona_travels.json or inline)
   * ----------------------------------------------------------------------- */
  const ACTIVITIES = [
    {
      id: 'free-time-santa-marta',
      emoji: '☕',
      isFreeTime: true,
      location: 'city',
      name: { en: 'Free Time in Santa Marta', es: 'Tiempo Libre en Santa Marta', it: 'Tempo Libero a Santa Marta', fr: 'Temps Libre à Santa Marta', de: 'Freizeit in Santa Marta' },
      desc: {
        en: 'Explore the colonial Historic Center, the Paseo de Bastidas waterfront, artisan markets and the city\'s vibrant Caribbean rhythm at your own pace.',
        es: 'Explora el Centro Histórico colonial, el malecón del Paseo de Bastidas, mercados artesanales y el vibrante ritmo caribeño de la ciudad a tu propio ritmo.',
        it: 'Esplora il Centro Storico coloniale, il lungomare del Paseo de Bastidas, i mercati artigianali e il vivace ritmo caraibico della città al tuo ritmo.',
        fr: 'Explorez le Centre Historique colonial, la promenade Paseo de Bastidas, les marchés artisanaux et le rythme caribéen vibrant de la ville à votre propre rythme.',
        de: 'Erkunden Sie das koloniale Historische Zentrum, die Uferpromenade Paseo de Bastidas, Kunsthandwerksmärkte und den lebhaften karibischen Rhythmus der Stadt in Ihrem eigenen Tempo.'
      },
      priceUSD: 0
    },
    {
      id: 'free-time-villa-maria',
      emoji: '🌅',
      isFreeTime: true,
      location: 'jungle',
      name: { en: 'Free Time at Villa María Tayrona', es: 'Tiempo Libre en Villa María Tayrona', it: 'Tempo Libero a Villa María Tayrona', fr: 'Temps Libre à Villa María Tayrona', de: 'Freizeit in der Villa María Tayrona' },
      desc: {
        en: 'Relax at Villa Maria. Explore private beach access, jungle paths, sightseeing, birdwatching, howler monkeys, and the infinity pool.',
        es: 'Playa privada, piscina infinita, monos, aves y el horizonte oceánico infinito — el día definitivo de naturaleza y lujo sin agenda.',
        it: 'Spiaggia privata, piscina a sfioro, scimmie, uccelli e l\'orizzonte oceanico infinito — la giornata definitiva di natura e lusso senza programma.',
        fr: 'Plage privée, piscine à débordement, singes, oiseaux et l\'horizon océanique infini — la journée ultime de nature et de luxe sans agenda.',
        de: 'Privatstrand, Infinity-Pool, Affen, Vögel und der endlose Meerhorizont — der ultimative Tag Natur und Luxus ohne Programm.'
      },
      priceUSD: 0,
      requiresVillaMariaStay: true
    },
    {
      id: 'city-tour-santa-marta',
      emoji: '🗺️',
      location: 'city',
      name: { en: 'Santa Marta City Tour (3 hrs)', es: 'City Tour Santa Marta (3 h)', it: 'City Tour Santa Marta (3 h)', fr: 'City Tour Santa Marta (3 h)', de: 'Stadtrundfahrt Santa Marta (3 Std.)' },
      desc: {
        en: 'Walk the oldest city in Colombia: Bolívar Park, Cathedral Basilica, Fishermen\'s Quarter, craft market and waterfront with an expert local guide.',
        es: 'Recorre la ciudad más antigua de Colombia: Parque Bolívar, Catedral Basílica, Barrio de Pescadores, mercado artesanal y malecón con guía local experto.',
        it: 'Passeggia per la città più antica della Colombia: Parco Bolívar, Cattedrale Basilica, Quartiere dei Pescatori, mercato artigianale e lungomare con guida locale esperta.',
        fr: 'Visitez la plus ancienne ville de Colombie : Parc Bolívar, Cathédrale Basilique, Quartier des Pêcheurs, marché artisanal et front de mer avec un guide local expert.',
        de: 'Erkunden Sie Kolumbiens älteste Stadt: Bolívar-Park, Kathedrale, Fischerviertel, Kunsthandwerksmarkt und Uferpromenade mit einem erfahrenen lokalen Guide.'
      },
      priceUSD: 35
    },
    {
      id: 'cabo-san-juan-tayrona',
      emoji: '🏖️',
      location: 'tayrona',
      name: { en: 'Cabo San Juan — Tayrona Park Trek', es: 'Cabo San Juan — Caminata Parque Tayrona', it: 'Cabo San Juan — Trek Parco Tayrona', fr: 'Cabo San Juan — Randonnée Tayrona', de: 'Cabo San Juan — Tayrona Wanderung' },
      desc: {
        en: 'Epic 2.5 h private trek through Tayrona: Arrecifes, natural pool, Arenilla and the iconic Cabo San Juan beach where white sand meets turquoise sea.',
        es: 'Épica caminata privada de 2.5 h por Tayrona: Arrecifes, piscina natural, Arenilla y la icónica playa de Cabo San Juan donde la arena blanca se funde con el mar turquesa.',
        it: 'Epico trek privato di 2.5 h attraverso Tayrona: Arrecifes, piscina naturale, Arenilla e la iconica spiaggia di Cabo San Juan dove la sabbia bianca incontra il mar turchese.',
        fr: 'Randonnée privée épique de 2h30 à travers Tayrona : Arrecifes, piscine naturelle, Arenilla et l\'emblématique plage de Cabo San Juan où le sable blanc rencontre la mer turquoise.',
        de: 'Epische 2,5-stündige Privatwanderung durch Tayrona: Arrecifes, natürlicher Pool, Arenilla und der ikonische Cabo San Juan Strand, wo weißer Sand auf türkisfarbenes Meer trifft.'
      },
      priceUSD: 55
    },
    {
      id: 'tubbing-rio-guachaca',
      emoji: '🛟',
      location: 'jungle',
      name: { en: 'River Tubing — Guachaca River', es: 'Tubbing Río Guachaca', it: 'Tubing Fiume Guachaca', fr: 'Tubing Rivière Guachaca', de: 'River Tubing — Guachaca-Fluss' },
      desc: {
        en: '1 h ecological hike through native jungle, then tube downstream on the Guachaca river — a thrilling and refreshing natural adventure.',
        es: '1 h de caminata ecológica por selva nativa y luego descenso en flotador por el río Guachaca — una emocionante y refrescante aventura natural.',
        it: '1 h di escursione ecologica nella giungla nativa, poi discesa in ciambella lungo il fiume Guachaca — un\'avventura naturale emozionante e rinfrescante.',
        fr: '1 h de randonnée écologique en jungle native, puis descente sur bouée sur la rivière Guachaca — une aventure naturelle thrillante et rafraîchissante.',
        de: '1 Std. ökologische Wanderung durch den nativen Dschungel, dann auf Schwimmreifen den Guachaca-Fluss hinunter — ein aufregendes Naturerlebnis.'
      },
      priceUSD: 45
    },
    {
      id: 'ruinas-bunkuany',
      emoji: '🏛️',
      location: 'tayrona',
      name: { en: 'Bunkuany Ruins (Mini Lost City)', es: 'Ruinas Bunkuany (Mini Ciudad Perdida)', it: 'Rovine Bunkuany (Mini Città Perduta)', fr: 'Ruines Bunkuany (Mini Cité Perdue)', de: 'Bunkuany-Ruinen (Mini Verlorene Stadt)' },
      desc: {
        en: '7 km trek through the Sierra Nevada to explore ancient Tayrona ruins amid lush biodiversity — a window into pre-Columbian civilization.',
        es: 'Caminata de 7 km por la Sierra Nevada para explorar ruinas antiguas Tayrona en medio de exuberante biodiversidad — una ventana a la civilización precolombina.',
        it: 'Trek di 7 km attraverso la Sierra Nevada per esplorare antiche rovine Tayrona in mezzo a rigogliosa biodiversità — una finestra sulla civiltà precolombiana.',
        fr: 'Randonnée de 7 km à travers la Sierra Nevada pour explorer d\'anciennes ruines Tayrona au milieu d\'une biodiversité luxuriante — une fenêtre sur la civilisation précolombienne.',
        de: '7 km Wanderung durch die Sierra Nevada zu alten Tayrona-Ruinen inmitten üppiger Natur — ein Fenster in die präkolumbianische Zivilisation.'
      },
      priceUSD: 50
    },
    {
      id: 'comunidades-indigenas-kogui-tayku',
      emoji: '🪶',
      location: 'jungle',
      name: { en: 'Kogui Indigenous Community Visit', es: 'Visita Comunidades Indígenas Kogui', it: 'Visita Comunità Indigene Kogui', fr: 'Visite Communautés Indigènes Kogui', de: 'Kogui-Gemeinschaft Besuch' },
      desc: {
        en: '1h20 uphill hike to sacred Kogui territory, direct descendants of the Tayrona. A profound cultural immersion — traditions, spirituality and ancestral connection.',
        es: '1h20 de caminata en ascenso hasta territorio sagrado Kogui, descendientes directos de los Tayrona. Inmersión cultural profunda — tradiciones, espiritualidad y conexión ancestral.',
        it: '1h20 di cammino in salita verso il territorio sacro Kogui, discendenti diretti dei Tayrona. Profonda immersione culturale — tradizioni, spiritualità e connessione ancestrale.',
        fr: '1h20 de montée vers le territoire sacré des Kogui, descendants directs des Tayrona. Immersion culturelle profonde — traditions, spiritualité et connexion ancestrale.',
        de: '1 Std. 20 Min. Aufstieg in heiliges Kogui-Gebiet, direkte Nachfahren der Tayrona. Tiefe kulturelle Immersion — Traditionen, Spiritualität und Ahnenverbindung.'
      },
      priceUSD: 50
    },
    {
      id: 'tour-coguis-cabalgata-orinoco',
      emoji: '🐴',
      location: 'jungle',
      name: { en: 'Kogui Horseback & Orinoco Waterfall', es: 'Coguis Cabalgata y Cascada Orinoco', it: 'Kogui a Cavallo e Cascata Orinoco', fr: 'Kogui à Cheval et Cascade Orinoco', de: 'Kogui-Reittour & Orinoco-Wasserfall' },
      desc: {
        en: 'Forest trail to an indigenous cacao village, learn about chocolate making, then reach the stunning Orinoco Waterfall for a natural swim in paradise.',
        es: 'Sendero forestal hasta un caserío cacao indígena, aprende sobre el chocolate, luego llega a la impresionante Cascada Orinoco para un baño natural en el paraíso.',
        it: 'Sentiero forestale fino a un caserío cacao indigeno, scopri la lavorazione del cioccolato, poi raggiungi la magnifica Cascata Orinoco per un bagno naturale in paradiso.',
        fr: 'Sentier forestier jusqu\'à un village indigène de cacao, apprenez la fabrication du chocolat, puis atteignez la magnifique cascade Orinoco pour une baignade naturelle au paradis.',
        de: 'Waldpfad zu einem indigenen Kakao-Dorf, Schokoladenherstellung kennenlernen, dann zum atemberaubenden Orinoco-Wasserfall für ein Bad im Naturparadies.'
      },
      priceUSD: 60
    },
    {
      id: 'tour-del-cacao',
      emoji: '🍫',
      location: 'jungle',
      name: { en: 'Cacao Farm Tour (Flavors of the Sierra)', es: 'Tour del Cacao (Del Paladar de la Sierra)', it: 'Tour del Cacao (Sapori della Sierra)', fr: 'Circuit du Cacao (Saveurs de la Sierra)', de: 'Kakao-Tour (Gaumenfreuden der Sierra)' },
      desc: {
        en: '2–3 h agritourism experience: guided cacao farm walk, hands-on chocolate workshop (roasting, grinding) and fresh artisan tasting — near Tayrona Park.',
        es: 'Experiencia agroturística de 2–3 h: recorrido guiado por finca de cacao, taller práctico de chocolate (tueste, molienda) y degustación artesanal fresca — cerca del Parque Tayrona.',
        it: 'Esperienza agrituristica di 2–3 ore: visita guidata a una finca di cacao, laboratorio pratico di cioccolato (tostatura, macinazione) e degustazione artigianale fresca — vicino al Parco Tayrona.',
        fr: 'Expérience d\'agrotourisme de 2–3 h : visite guidée d\'une plantation de cacao, atelier pratique de chocolat (torréfaction, moulage) et dégustation artisanale fraîche — près du parc Tayrona.',
        de: '2–3-stündiges Agrotourismus-Erlebnis: geführte Kakaofarm, praktischer Schokoladen-Workshop (Rösten, Mahlen) und frische handwerkliche Verkostung — nahe dem Tayrona-Park.'
      },
      priceUSD: 40
    },
    {
      id: 'poza-encantada',
      emoji: '💧',
      location: 'jungle',
      name: { en: 'Enchanted Sacred Pool (Poza Encantada)', es: 'Tour Poza Encantada - Sagrada', it: 'Tour Poza Encantada - Sacra', fr: 'Circuit Poza Encantada - Sacrée', de: 'Heiliger Naturpool (Poza Encantada)' },
      desc: {
        en: '35 min eco-hike to natural Sierra Nevada jacuzzis and crystal freshwater pools — a magical, sacred spot hidden in the jungle.',
        es: '35 min de eco-caminata hasta los jacuzzis naturales de la Sierra Nevada y pozas de agua cristalina — un lugar mágico y sagrado escondido en la selva.',
        it: '35 minuti di eco-escursione fino ai jacuzzi naturali della Sierra Nevada e pozze d\'acqua cristallina — un luogo magico e sacro nascosto nella giungla.',
        fr: '35 min d\'éco-randonnée jusqu\'aux jacuzzis naturels de la Sierra Nevada et bassins d\'eau cristalline — un endroit magique et sacré caché dans la jungle.',
        de: '35 Min. Ökowanderung zu natürlichen Sierra Nevada-Jacuzzis und kristallklaren Süßwasserpools — ein magischer, heiliger Ort versteckt im Dschungel.'
      },
      priceUSD: 40
    },
    {
      id: 'cabalgata-playa-los-naranjos',
      emoji: '🐎',
      location: 'tayrona',
      name: { en: 'Los Naranjos Beach Horseback Ride', es: 'Cabalgata Playa Los Naranjos (Tayrona)', it: 'Cavallo Playa Los Naranjos (Tayrona)', fr: 'Cheval Playa Los Naranjos (Tayrona)', de: 'Reittour Los Naranjos Strand (Tayrona)' },
      desc: {
        en: '2 h excursion from San Martín gate: cross Piedra river, ride through Tayrona jungle to the exclusive Los Naranjos private beach for a sunset horseback ride.',
        es: '2 h de excursión desde la entrada San Martín: cruza el río Piedra, cabalgata por la selva Tayrona hasta la exclusiva playa privada Los Naranjos para un paseo a caballo al atardecer.',
        it: '2 ore di escursione dall\'ingresso San Martín: attraversa il fiume Piedra, cavalcata nella giungla Tayrona fino all\'esclusiva spiaggia privata Los Naranjos per un\'equitazione al tramonto.',
        fr: '2 h d\'excursion depuis l\'entrée San Martín : traversez la rivière Piedra, cavalcade dans la jungle Tayrona jusqu\'à la plage privée exclusive Los Naranjos pour une balade au coucher du soleil.',
        de: '2-stündiger Ausflug vom Eingang San Martín: Überquerung des Piedra-Flusses, Ritt durch den Tayrona-Dschungel zur exklusiven Privatstrand Los Naranjos für einen Sonnenuntergangsritt.'
      },
      priceUSD: 50
    },
    {
      id: 'avistamiento-de-aves-tayrona',
      emoji: '🦜',
      location: 'tayrona',
      name: { en: 'Bird Watching — Tayrona Reserve', es: 'Avistamiento Aves Parque Tayrona', it: 'Birdwatching Riserva Tayrona', fr: 'Observation Oiseaux Tayrona', de: 'Vogelbeobachtung Tayrona' },
      desc: {
        en: '5:30 am–11 am expert-guided birdwatching: spot rare native and migratory species with specialized optics in the heart of the Tayrona nature reserve.',
        es: 'Avistamiento de aves guiado por expertos de 5:30 am–11 am: observa especies nativas y migratorias raras con óptica especializada en el corazón de la reserva natural Tayrona.',
        it: 'Birdwatching guidato da esperti dalle 5:30 alle 11:00: osserva specie native e migratorie rare con ottica specializzata nel cuore della riserva naturale Tayrona.',
        fr: 'Observation d\'oiseaux guidée par des experts de 5h30 à 11h : observez des espèces natives et migratoires rares avec des optiques spécialisées au cœur de la réserve naturelle Tayrona.',
        de: 'Expertengeführte Vogelbeobachtung 5:30–11:00 Uhr: seltene heimische und Zugvogelarten mit spezialisierter Optik im Herzen des Tayrona-Naturschutzgebiets beobachten.'
      },
      priceUSD: 45
    }
  ];

  /* -------------------------------------------------------------------------
   * TRANSPORT
   * ----------------------------------------------------------------------- */
  const TRANSPORT = {
    airport: { en: 'Airport → Hotel transfer (Girona Travel private vehicle)', es: 'Traslado aeropuerto → hotel (vehículo privado Girona Travel)', it: 'Transfer aeroporto → hotel (veicolo privato Girona Travel)', fr: 'Transfert aéroport → hôtel (véhicule privé Girona Travel)', de: 'Flughafen → Hotel Transfer (Girona Travel Privatfahrzeug)' },
    cityToJungle: { en: 'Santa Marta → Villa María Tayrona transfer', es: 'Traslado Santa Marta → Villa María Tayrona', it: 'Transfer Santa Marta → Villa María Tayrona', fr: 'Transfert Santa Marta → Villa María Tayrona', de: 'Santa Marta → Villa María Tayrona Transfer' },
    jungleToCity: { en: 'Villa María Tayrona → Santa Marta transfer', es: 'Traslado Villa María Tayrona → Santa Marta', it: 'Transfer Villa María Tayrona → Santa Marta', fr: 'Transfert Villa María Tayrona → Santa Marta', de: 'Villa María Tayrona → Santa Marta Transfer' },
    toAirport: { en: 'Hotel → Airport transfer (Girona Travel)', es: 'Traslado hotel → aeropuerto (Girona Travel)', it: 'Transfer hotel → aeroporto (Girona Travel)', fr: 'Transfert hôtel → aéroport (Girona Travel)', de: 'Hotel → Flughafen Transfer (Girona Travel)' },
    pricePerTransfer: 35
  };

  /* -------------------------------------------------------------------------
   * TRANSLATIONS
   * ----------------------------------------------------------------------- */
  const T = {
    en: {
      steps: ['1. Basics', '2. Plan', '3. Add-ons', '4. Send'],
      p1Title: '🗓️ Trip Basics',
      p1Sub: 'Tell us your dates and group size.',
      arrivalDate: 'Arrival Date',
      departureDate: 'Departure Date',
      invalidDates: 'Please select valid arrival and departure dates.',
      p2Title: '🗺️ Itinerary Builder',
      p2Sub: 'Select where to stay and what to do day by day.',
      nightLabel: 'Night',
      dayLabel: 'Day',
      chooseAcc: 'Select Accommodation',
      chooseAct: 'Select Activity',
      noActivity: 'No Activity',
      p3Title: '✨ Extras & Add-ons',
      p3Sub: 'Customize your rooms and transfers.',
      p4Title: '🗓️ Your Itinerary is Ready!',
      p4Sub: 'Enter your name and email to receive the full program with prices.',
      sectionTag: '⚡ Trip Architect',
      sectionTitle: 'Build Your Perfect <span>Santa Marta & Tayrona</span> Stay',
      sectionSubtitle: 'Tell us how you travel and we\'ll design a day-by-day itinerary with accommodation, guided tours and private transfers — tailored just for you.',
      steps: ['Arrival', 'Nights & Stay', 'Activities', 'Add-ons', 'Your Itinerary'],
      // Panel 1
      p1Title: '✈️ How are you arriving to Santa Marta?',
      p1Sub: 'This helps us plan your first transfer and suggest the best arrival-day experience.',
      byPlane: 'By Plane', byPlaneSub: 'Flying into Simón Bolívar Airport (SMR)',
      byCar: 'By Car', byCarSub: 'Driving to Santa Marta',
      arrivalTimeLabel: 'Estimated arrival time in Santa Marta:',
      earlyMorning: 'Early morning', earlyMorningSub: 'Before 9:00 am',
      morning: 'Morning', morningSub: '9:00 am – 1:00 pm',
      afternoon: 'Afternoon', afternoonSub: '1:00 pm – 6:00 pm',
      evening: 'Evening', eveningSub: 'After 6:00 pm',
      adultsLabel: '👤 Adults', adultsSub: 'Determines vehicle type (SUV ≤ 5 | Van > 5)',
      babiesLabel: '👶 Babies under 2 y.o.', babiesSub: 'Cot/crib on request — pricing set by reception',
      // Panel 2
      p2Title: '🏠 Where would you like to sleep?',
      p2Sub: 'Mix and match nights across our accommodations. Add at least 1 night to continue.',
      nightsAt: 'Nights at',
      totalNights: 'Total nights',
      // Panel 3
      p3Title: '🌿 Plan your days',
      p3Sub: 'Choose an activity for each day. You can always leave a day free!',
      // Panel 4
      p4Title: '✨ Final touches',
      p4Sub: 'Round off your trip with these optional add-ons.',
      kasankalaLabel: '🍽️ Dinner at Kasankala Restaurant',
      kasankalaSub: 'Exclusive restaurant at Villa María Tayrona — special discount for guests. Farm-to-table Caribbean cuisine with ocean views.',
      addAirportReturn: 'Add return airport transfer (Girona Travel)',
      requestCustom: 'I need a custom itinerary — contact me',
      // Panel 5
      p5Title: '🗓️ Your Itinerary is Ready!',
      p5Sub: 'Enter your name and email — our team will send you the complete program with personalised pricing.',
      yourStay: 'Your Stay',
      groupInfo: 'Your Group',
      guestNameLabel: 'Your name',
      guestNamePlaceholder: 'Full name',
      guestEmailLabel: 'Your email',
      guestEmailPlaceholder: 'email@example.com',
      vatNote: '🇨🇴 Colombian guests pay 0% VAT on accommodation.',
      discountNote: '✨ Group discounts may apply — our team will confirm.',
      sendProgram: '📩 Send me my itinerary',
      sending: 'Sending…',
      sentOk: '✅ Sent! Check your inbox — our team will contact you shortly with pricing.',
      sentErr: '❌ Something went wrong. Please try again or contact us directly.',
      nightsLabel: 'nights',
      roomTypeLabel: '🛏️ Choose your room type',
      addNightHint: 'Add at least 1 night to continue.',
      accSequenceNote: 'Recommended order: Santa Marta city stays first, then Villa María Tayrona for the full city-to-nature experience.',
      restartLabel: '↺ Start over',
      transportNote: 'Private SUV (≤5 adults) or Van/Minibus (>5 adults). All transfers with Girona Travel.',
      next: 'Continue →',
      back: '← Back',
      day: 'Day',
      arrival: 'Arrival',
      departure: 'Departure',
      freeDay: 'Free time',
      adultsCount: 'adult', adultsCountP: 'adults',
      babiesCount: 'baby under 2', babiesCountP: 'babies under 2'
    },
    es: {
      steps: ['1. Básico', '2. Plan', '3. Extras', '4. Enviar'],
      p1Title: '🗓️ Datos Básicos',
      p1Sub: 'Dinos tus fechas y tamaño del grupo.',
      arrivalDate: 'Fecha de Llegada',
      departureDate: 'Fecha de Salida',
      invalidDates: 'Por favor selecciona fechas válidas.',
      p2Title: '🗺️ Constructor de Itinerario',
      p2Sub: 'Selecciona dónde dormir y qué hacer día a día.',
      nightLabel: 'Noche',
      dayLabel: 'Día',
      chooseAcc: 'Seleccionar Alojamiento',
      chooseAct: 'Seleccionar Actividad',
      noActivity: 'Sin actividad',
      p3Title: '✨ Extras y Adicionales',
      p3Sub: 'Personaliza tus habitaciones y traslados.',
      p4Title: '🗓️ ¡Tu Itinerario está Listo!',
      p4Sub: 'Ingresa tu nombre y correo para recibir el programa con precios.',
      sectionTag: '⚡ Arquitecto de Viaje',
      sectionTitle: 'Diseña tu Estancia Perfecta en <span>Santa Marta y Tayrona</span>',
      sectionSubtitle: 'Cuéntanos cómo viajas y diseñaremos un itinerario día a día con alojamiento, tours guiados y traslados privados — totalmente personalizado.',
      steps: ['Llegada', 'Noches y Aloj.', 'Actividades', 'Extras', 'Tu Itinerario'],
      p1Title: '✈️ ¿Cómo llegas a Santa Marta?',
      p1Sub: 'Esto nos ayuda a planear tu primer traslado y sugerir la mejor experiencia del día de llegada.',
      byPlane: 'En Avión', byPlaneSub: 'Vuelo al aeropuerto Simón Bolívar (SMR)',
      byCar: 'En Carro', byCarSub: 'Viajando en carro a Santa Marta',
      arrivalTimeLabel: 'Hora estimada de llegada a Santa Marta:',
      earlyMorning: 'Madrugada', earlyMorningSub: 'Antes de las 9:00 am',
      morning: 'Mañana', morningSub: '9:00 am – 1:00 pm',
      afternoon: 'Tarde', afternoonSub: '1:00 pm – 6:00 pm',
      evening: 'Noche', eveningSub: 'Después de las 6:00 pm',
      adultsLabel: '👤 Adultos', adultsSub: 'Determina el tipo de vehículo (SUV ≤5 | Van >5)',
      babiesLabel: '👶 Bebés menores de 2 años', babiesSub: 'Cuna disponible — precio definido por la recepción',
      p2Title: '🏠 ¿Dónde quieres dormir?',
      p2Sub: 'Combina noches entre nuestros alojamientos. Agrega al menos 1 noche para continuar.',
      nightsAt: 'Noches en',
      totalNights: 'Total noches',
      p3Title: '🌿 Planea tus días',
      p3Sub: 'Elige una actividad para cada día. ¡Siempre puedes dejar un día libre!',
      p4Title: '✨ Toques finales',
      p4Sub: 'Complementa tu viaje con estos opcionales.',
      kasankalaLabel: '🍽️ Cena en Restaurante Kasankala',
      kasankalaSub: 'Restaurante exclusivo en Villa María Tayrona — descuento especial para huéspedes. Cocina caribeña de la finca al mar con vistas al océano.',
      addAirportReturn: 'Agregar traslado de regreso al aeropuerto (Girona Travel)',
      requestCustom: 'Necesito un itinerario personalizado — contáctenme',
      p5Title: '🗓️ ¡Tu Itinerario está Listo!',
      p5Sub: 'Ingresa tu nombre y correo — nuestro equipo te enviará el programa completo con precios personalizados.',
      yourStay: 'Tu Alojamiento',
      groupInfo: 'Tu Grupo',
      guestNameLabel: 'Tu nombre',
      guestNamePlaceholder: 'Nombre completo',
      guestEmailLabel: 'Tu correo',
      guestEmailPlaceholder: 'correo@ejemplo.com',
      vatNote: '🇨🇴 Colombianos pagan 0% IVA en alojamiento.',
      discountNote: '✨ Pueden aplicar descuentos de grupo — nuestro equipo lo confirmará.',
      sendProgram: '📩 Enviarme mi itinerario',
      sending: 'Enviando…',
      sentOk: '✅ ¡Enviado! Revisa tu bandeja — nuestro equipo te contactará pronto con los precios.',
      sentErr: '❌ Algo salió mal. Intenta de nuevo o contáctanos directamente.',
      vatNote2: '0% IVA Hotelero',
      nightsLabel: 'noches',
      roomTypeLabel: '🛏️ Elige el tipo de habitación',
      addNightHint: 'Agrega al menos 1 noche para continuar.',
      accSequenceNote: 'Orden recomendado: primero alojamiento en Santa Marta, luego Villa María Tayrona para la experiencia completa de ciudad a naturaleza.',
      restartLabel: '↺ Empezar de nuevo',
      transportNote: 'SUV privado (≤5 adultos) o Van/Microbús (>5 adultos). Todos los traslados con Girona Travel.',
      next: 'Continuar →',
      back: '← Atrás',
      day: 'Día',
      arrival: 'Llegada',
      departure: 'Salida',
      freeDay: 'Tiempo libre',
      adultsCount: 'adulto', adultsCountP: 'adultos',
      babiesCount: 'bebé menor de 2', babiesCountP: 'bebés menores de 2'
    },
    it: {
      steps: ['1. Basi', '2. Piano', '3. Extra', '4. Invia'],
      p1Title: '🗓️ Dati di Base',
      p1Sub: 'Indicaci le date e la dimensione del gruppo.',
      arrivalDate: 'Data di Arrivo',
      departureDate: 'Data di Partenza',
      invalidDates: 'Seleziona date valide.',
      p2Title: '🗺️ Costruttore di Itinerari',
      p2Sub: 'Scegli dove dormire e cosa fare giorno per giorno.',
      nightLabel: 'Notte',
      dayLabel: 'Giorno',
      chooseAcc: 'Seleziona Alloggio',
      chooseAct: 'Seleziona Attività',
      noActivity: 'Nessuna attività',
      p3Title: '✨ Extra e Opzioni',
      p3Sub: 'Personalizza camere e trasferimenti.',
      p4Title: '🗓️ Il Tuo Itinerario è Pronto!',
      p4Sub: 'Inserisci nome e email per ricevere il programma con i prezzi.',
      sectionTag: '⚡ Architetto di Viaggio',
      sectionTitle: 'Progetta il tuo Soggiorno Perfetto a <span>Santa Marta e Tayrona</span>',
      sectionSubtitle: 'Dicci come viaggi e progetteremo un itinerario giorno per giorno con alloggio, tour guidati e trasferimenti privati — su misura per te.',
      steps: ['Arrivo', 'Notti & Soggiorno', 'Attività', 'Extra', 'Il Tuo Itinerario'],
      p1Title: '✈️ Come arrivi a Santa Marta?',
      p1Sub: 'Questo ci aiuta a pianificare il tuo primo trasferimento e suggerire la migliore esperienza del giorno di arrivo.',
      byPlane: 'In Aereo', byPlaneSub: 'Volo all\'aeroporto Simón Bolívar (SMR)',
      byCar: 'In Auto', byCarSub: 'In auto verso Santa Marta',
      arrivalTimeLabel: 'Orario di arrivo stimato a Santa Marta:',
      earlyMorning: 'Mattina presto', earlyMorningSub: 'Prima delle 9:00',
      morning: 'Mattina', morningSub: '9:00 – 13:00',
      afternoon: 'Pomeriggio', afternoonSub: '13:00 – 18:00',
      evening: 'Sera', eveningSub: 'Dopo le 18:00',
      adultsLabel: '👤 Adulti', adultsSub: 'Determina il tipo di veicolo (SUV ≤5 | Van >5)',
      babiesLabel: '👶 Neonati sotto i 2 anni', babiesSub: 'Culla disponibile — prezzo definito dalla reception',
      p2Title: '🏠 Dove vorresti dormire?',
      p2Sub: 'Combina le notti tra i nostri alloggi. Aggiungi almeno 1 notte per continuare.',
      nightsAt: 'Notti a',
      totalNights: 'Notti totali',
      p3Title: '🌿 Pianifica le tue giornate',
      p3Sub: 'Scegli un\'attività per ogni giorno. Puoi sempre lasciare un giorno libero!',
      p4Title: '✨ Tocchi finali',
      p4Sub: 'Completa il tuo viaggio con questi optional.',
      kasankalaLabel: '🍽️ Cena al Ristorante Kasankala',
      kasankalaSub: 'Ristorante esclusivo a Villa María Tayrona — 10% di sconto per gli ospiti. Cucina caraibica dal campo al mare con vista sull\'oceano.',
      addAirportReturn: 'Aggiungi trasferimento aeroporto di ritorno (Girona Travel)',
      requestCustom: 'Ho bisogno di un itinerario personalizzato — contattatemi',
      p5Title: '🗓️ Il Tuo Itinerario è Pronto!',
      p5Sub: 'Inserisci il tuo nome e la tua email — il nostro team ti invierà il programma completo con i prezzi personalizzati.',
      yourStay: 'Il tuo soggiorno',
      groupInfo: 'Il tuo gruppo',
      guestNameLabel: 'Il tuo nome',
      guestNamePlaceholder: 'Nome completo',
      guestEmailLabel: 'La tua email',
      guestEmailPlaceholder: 'email@esempio.com',
      vatNote: '🇨🇴 Gli ospiti colombiani pagano 0% IVA sull\'alloggio.',
      discountNote: '✨ Possibili sconti di gruppo — il nostro team confermerà.',
      sendProgram: '📩 Inviami il mio itinerario',
      sending: 'Invio in corso…',
      sentOk: '✅ Inviato! Controlla la tua casella — il nostro team ti contatterà presto con i prezzi.',
      sentErr: '❌ Qualcosa è andato storto. Riprova o contattaci direttamente.',
      nightsLabel: 'notti',
      roomTypeLabel: '🛏️ Scegli il tipo di camera',
      addNightHint: 'Aggiungi almeno 1 notte per continuare.',
      accSequenceNote: 'Ordine consigliato: prima i soggiorni in città a Santa Marta, poi Villa María Tayrona per la piena esperienza dalla città alla natura.',
      restartLabel: '↺ Ricominciare',
      transportNote: 'SUV privato (≤5 adulti) o Van/Minibus (>5 adulti). Tutti i trasferimenti con Girona Travel.',
      next: 'Continua →',
      back: '← Indietro',
      day: 'Giorno',
      arrival: 'Arrivo',
      departure: 'Partenza',
      freeDay: 'Tempo libero',
      adultsCount: 'adulto', adultsCountP: 'adulti',
      babiesCount: 'neonato sotto i 2', babiesCountP: 'neonati sotto i 2'
    },
    fr: {
      steps: ['1. Bases', '2. Plan', '3. Extras', '4. Envoyer'],
      p1Title: '🗓️ Informations de Base',
      p1Sub: 'Indiquez vos dates et la taille du groupe.',
      arrivalDate: 'Date d\'arrivée',
      departureDate: 'Date de départ',
      invalidDates: 'Veuillez sélectionner des dates valides.',
      p2Title: '🗺️ Constructeur d\'Itinéraire',
      p2Sub: 'Choisissez où dormir et quoi faire jour par jour.',
      nightLabel: 'Nuit',
      dayLabel: 'Jour',
      chooseAcc: 'Sélectionner Hébergement',
      chooseAct: 'Sélectionner Activité',
      noActivity: 'Aucune activité',
      p3Title: '✨ Extras et Options',
      p3Sub: 'Personnalisez vos chambres et transferts.',
      p4Title: '🗓️ Votre Itinéraire est Prêt !',
      p4Sub: 'Entrez votre nom et email pour recevoir le programme avec les prix.',
      sectionTag: '⚡ Architecte de Voyage',
      sectionTitle: 'Concevez votre Séjour Parfait à <span>Santa Marta & Tayrona</span>',
      sectionSubtitle: 'Dites-nous comment vous voyagez et nous concevrons un itinéraire jour par jour avec hébergement, visites guidées et transferts privés — sur mesure pour vous.',
      steps: ['Arrivée', 'Nuits & Séjour', 'Activités', 'Options', 'Votre Itinéraire'],
      p1Title: '✈️ Comment arrivez-vous à Santa Marta?',
      p1Sub: 'Cela nous aide à planifier votre premier transfert et à suggérer la meilleure expérience du jour d\'arrivée.',
      byPlane: 'En Avion', byPlaneSub: 'Vol à l\'aéroport Simón Bolívar (SMR)',
      byCar: 'En Voiture', byCarSub: 'En voiture vers Santa Marta',
      arrivalTimeLabel: 'Heure d\'arrivée estimée à Santa Marta :',
      earlyMorning: 'Tôt le matin', earlyMorningSub: 'Avant 9h00',
      morning: 'Matin', morningSub: '9h00 – 13h00',
      afternoon: 'Après-midi', afternoonSub: '13h00 – 18h00',
      evening: 'Soir', eveningSub: 'Après 18h00',
      adultsLabel: '👤 Adultes', adultsSub: 'Détermine le type de véhicule (SUV ≤5 | Van >5)',
      babiesLabel: '👶 Bébés de moins de 2 ans', babiesSub: 'Lit bébé disponible — tarif défini par la réception',
      p2Title: '🏠 Où souhaitez-vous dormir ?',
      p2Sub: 'Combinez les nuits entre nos hébergements. Ajoutez au moins 1 nuit pour continuer.',
      nightsAt: 'Nuits à',
      totalNights: 'Total nuits',
      p3Title: '🌿 Planifiez vos journées',
      p3Sub: 'Choisissez une activité pour chaque jour. Vous pouvez toujours laisser une journée libre !',
      p4Title: '✨ Touches finales',
      p4Sub: 'Complétez votre voyage avec ces options.',
      kasankalaLabel: '🍽️ Dîner au Restaurant Kasankala',
      kasankalaSub: 'Restaurant exclusif à Villa María Tayrona — 10% de remise pour les clients. Cuisine caribéenne de la ferme à la mer avec vue sur l\'océan.',
      addAirportReturn: 'Ajouter le transfert retour aéroport (Girona Travel)',
      requestCustom: 'J\'ai besoin d\'un itinéraire personnalisé — contactez-moi',
      p5Title: '🗓️ Votre Itinéraire est Prêt !',
      p5Sub: 'Entrez votre nom et email — notre équipe vous enverra le programme complet avec les tarifs personnalisés.',
      yourStay: 'Votre séjour',
      groupInfo: 'Votre groupe',
      guestNameLabel: 'Votre nom',
      guestNamePlaceholder: 'Nom complet',
      guestEmailLabel: 'Votre email',
      guestEmailPlaceholder: 'email@exemple.com',
      vatNote: '🇨🇴 Les clients colombiens paient 0% de TVA sur l\'hébergement.',
      discountNote: '✨ Des remises de groupe peuvent s\'appliquer — notre équipe confirmera.',
      sendProgram: '📩 M\'envoyer mon itinéraire',
      sending: 'Envoi en cours…',
      sentOk: '✅ Envoyé ! Vérifiez votre boîte de réception — notre équipe vous contactera bientôt avec les tarifs.',
      sentErr: '❌ Une erreur s\'est produite. Veuillez réessayer ou nous contacter directement.',
      nightsLabel: 'nuits',
      roomTypeLabel: '🛏️ Choisissez votre type de chambre',
      addNightHint: 'Ajoutez au moins 1 nuit pour continuer.',
      accSequenceNote: 'Ordre recommandé : séjours en ville à Santa Marta en premier, puis Villa María Tayrona pour une expérience complète de la ville à la nature.',
      restartLabel: '↺ Recommencer',
      transportNote: 'SUV privé (≤5 adultes) ou Van/Minibus (>5 adultes). Tous les transferts avec Girona Travel.',
      next: 'Continuer →',
      back: '← Retour',
      day: 'Jour',
      arrival: 'Arrivée',
      departure: 'Départ',
      freeDay: 'Temps libre',
      adultsCount: 'adulte', adultsCountP: 'adultes',
      babiesCount: 'bébé de moins de 2 ans', babiesCountP: 'bébés de moins de 2 ans'
    },
    de: {
      steps: ['1. Basis', '2. Plan', '3. Extras', '4. Senden'],
      p1Title: '🗓️ Grunddaten',
      p1Sub: 'Teilen Sie uns Ihre Daten und Gruppengröße mit.',
      arrivalDate: 'Ankunftsdatum',
      departureDate: 'Abreisedatum',
      invalidDates: 'Bitte wählen Sie gültige Daten.',
      p2Title: '🗺️ Reiseplaner',
      p2Sub: 'Wählen Sie, wo Sie schlafen und was Sie jeden Tag tun.',
      nightLabel: 'Nacht',
      dayLabel: 'Tag',
      chooseAcc: 'Unterkunft wählen',
      chooseAct: 'Aktivität wählen',
      noActivity: 'Keine Aktivität',
      p3Title: '✨ Extras & Optionen',
      p3Sub: 'Personalisieren Sie Zimmer und Transfers.',
      p4Title: '🗓️ Ihr Reiseplan ist Fertig!',
      p4Sub: 'Geben Sie Name und E-Mail ein, um das Programm mit Preisen zu erhalten.',
      sectionTag: '⚡ Reisearchitekt',
      sectionTitle: 'Bauen Sie Ihren perfekten <span>Santa Marta & Tayrona</span> Aufenthalt',
      sectionSubtitle: 'Sagen Sie uns, wie Sie reisen, und wir entwerfen einen täglichen Reiseplan mit Unterkunft, geführten Touren und privaten Transfers — maßgeschneidert für Sie.',
      steps: ['Anreise', 'Nächte & Hotel', 'Aktivitäten', 'Extras', 'Ihr Reiseplan'],
      p1Title: '✈️ Wie reisen Sie nach Santa Marta?',
      p1Sub: 'Dies hilft uns, Ihren ersten Transfer zu planen und das beste Anreiseerlebnis vorzuschlagen.',
      byPlane: 'Mit dem Flugzeug', byPlaneSub: 'Flug zum Flughafen Simón Bolívar (SMR)',
      byCar: 'Mit dem Auto', byCarSub: 'Mit dem Auto nach Santa Marta',
      arrivalTimeLabel: 'Geschätzte Ankunftszeit in Santa Marta:',
      earlyMorning: 'Früh morgens', earlyMorningSub: 'Vor 9:00 Uhr',
      morning: 'Morgen', morningSub: '9:00 – 13:00 Uhr',
      afternoon: 'Nachmittag', afternoonSub: '13:00 – 18:00 Uhr',
      evening: 'Abend', eveningSub: 'Nach 18:00 Uhr',
      adultsLabel: '👤 Erwachsene', adultsSub: 'Bestimmt den Fahrzeugtyp (SUV ≤5 | Van >5)',
      babiesLabel: '👶 Babys unter 2 Jahre', babiesSub: 'Kinderbett auf Anfrage — Preis von der Rezeption',
      p2Title: '🏠 Wo möchten Sie schlafen?',
      p2Sub: 'Kombinieren Sie Nächte in unseren Unterkünften. Fügen Sie mindestens 1 Nacht hinzu, um fortzufahren.',
      nightsAt: 'Nächte in',
      totalNights: 'Nächte gesamt',
      p3Title: '🌿 Planen Sie Ihre Tage',
      p3Sub: 'Wählen Sie eine Aktivität für jeden Tag. Sie können immer einen freien Tag lassen!',
      p4Title: '✨ Letzte Details',
      p4Sub: 'Vervollständigen Sie Ihre Reise mit diesen optionalen Extras.',
      kasankalaLabel: '🍽️ Abendessen im Restaurant Kasankala',
      kasankalaSub: 'Exklusives Restaurant in Villa María Tayrona — 10% Rabatt für Gäste. Karibische Farm-to-Sea-Küche mit Meerblick.',
      addAirportReturn: 'Rücktransfer zum Flughafen hinzufügen (Girona Travel)',
      requestCustom: 'Ich brauche einen individuellen Reiseplan — kontaktieren Sie mich',
      p5Title: '🗓️ Ihr Reiseplan ist Fertig!',
      p5Sub: 'Geben Sie Ihren Namen und Ihre E-Mail ein — unser Team sendet Ihnen das vollständige Programm mit persönlichen Preisen.',
      yourStay: 'Ihr Aufenthalt',
      groupInfo: 'Ihre Gruppe',
      guestNameLabel: 'Ihr Name',
      guestNamePlaceholder: 'Vollständiger Name',
      guestEmailLabel: 'Ihre E-Mail',
      guestEmailPlaceholder: 'email@beispiel.de',
      vatNote: '🇨🇴 Kolumbianische Gäste zahlen 0% Hotelsteuer.',
      discountNote: '✨ Gruppenrabatte möglich — unser Team bestätigt dies.',
      sendProgram: '📩 Meinen Reiseplan zusenden',
      sending: 'Wird gesendet…',
      sentOk: '✅ Gesendet! Überprüfen Sie Ihren Posteingang — unser Team kontaktiert Sie bald mit den Preisen.',
      sentErr: '❌ Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut oder kontaktieren Sie uns direkt.',
      nightsLabel: 'Nächte',
      roomTypeLabel: '🛏️ Wählen Sie Ihren Zimmertyp',
      addNightHint: 'Fügen Sie mindestens 1 Nacht hinzu, um fortzufahren.',
      accSequenceNote: 'Empfohlene Reihenfolge: Zuerst Stadtaufenthalte in Santa Marta, dann Villa María Tayrona für das vollständige Stadt-zu-Natur-Erlebnis.',
      restartLabel: '↺ Von vorne beginnen',
      transportNote: 'Privat-SUV (≤5 Erw.) oder Van/Minibus (>5 Erw.). Alle Transfers mit Girona Travel.',
      next: 'Weiter →',
      back: '← Zurück',
      day: 'Tag',
      arrival: 'Ankunft',
      departure: 'Abreise',
      freeDay: 'Freizeit',
      adultsCount: 'Erwachsener', adultsCountP: 'Erwachsene',
      babiesCount: 'Baby unter 2', babiesCountP: 'Babys unter 2'
    }
  };

  /* -------------------------------------------------------------------------
   * STATE
   * ----------------------------------------------------------------------- */

  const defaultState = () => ({
    step: 1,
    lang: 'en',
    arrivalDate: '',
    departureDate: '',
    arrivalMode: 'plane',
    adults: 2,
    babies: 0,
    itinerary: [], // array of { nightAcc, dayAct } length = (departure - arrival)
    roomTypes: {
      'casa-isabella': 'base',
      'casa-leda': 'base',
      'villa-maria': 'base'
    },
    kasankala: false,
    returnTransfer: true,
    customRequest: false,
    guestName: '',
    guestEmail: '',
    _sending: false,
    _sent: false,
    _sendError: false
  });

  let state = defaultState();
  let container = null;

  function t(key) { return T[state.lang]?.[key] || T.en[key] || key; }
  function txt(obj) { if (typeof obj === 'string') return obj; return obj?.[state.lang] || obj?.en || ''; }

  function getTotalNights() {
    if (!state.arrivalDate || !state.departureDate) return 0;
    const a = new Date(state.arrivalDate);
    const d = new Date(state.departureDate);
    const diffTime = d - a;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays > 0 ? diffDays : 0;
  }

  function getAccById(id) { return ACCOMMODATIONS[id]; }
  function getActivityById(id) { return ACTIVITIES.find(a => a.id === id); }

  function render() {
    if (!container) return;
    container.innerHTML = buildHTML();
    bindEvents();
    updateProgress();
    updateStepperState();
  }

  function buildHTML() {
    return `
      <section class="trip-wizard-section" id="trip-wizard-module">
        <div class="container">
          <div class="wizard-section-header">
            <div class="wizard-section-tag">${t('sectionTag')}</div>
            <h2 class="wizard-section-title">${t('sectionTitle')}</h2>
            <p class="wizard-section-subtitle">${t('sectionSubtitle')}</p>
          </div>
          <div class="trip-wizard-box">
            <div class="wizard-progress-bar">
              <div class="wizard-progress-fill" id="wizProgress" style="width:${progressPct()}%"></div>
            </div>
            ${buildStepper()}
            <div class="wizard-panels">
              ${buildPanel1()}
              ${buildPanel2()}
              ${buildPanel3()}
              ${buildPanel4()}
            </div>
            <div class="wizard-nav-actions">
              <button class="wiz-btn wiz-btn-ghost" id="wizRestart">↺ ${t('restartLabel')}</button>
              <div style="display:flex;gap:10px;align-items:center;">
                ${state.step > 1 && state.step < 4 ? `<button class="wiz-btn wiz-btn-outline" id="wizBack">${t('back')}</button>` : ''}
                ${state.step < 4 ? `<button class="wiz-btn wiz-btn-primary" id="wizNext">${t('next')}</button>` : ''}
              </div>
            </div>
          </div>
        </div>
      </section>
    `;
  }

  function progressPct() { return Math.round(((state.step - 1) / 3) * 100); }

  function buildStepper() {
    const steps = t('steps');
    return `
      <div class="wizard-stepper" id="wizStepper">
        ${steps.map((label, i) => {
          const n = i + 1;
          const cls = n < state.step ? 'completed' : n === state.step ? 'active' : '';
          return `
            <div class="wizard-step-item ${cls}" data-step="${n}">
              <div class="wizard-step-circle">${n < state.step ? '✓' : n}</div>
              <span class="wizard-step-label">${label}</span>
            </div>`;
        }).join('')}
      </div>`;
  }

  function buildPanel1() {
    return `
      <div class="wizard-panel ${state.step === 1 ? 'active' : ''}" data-panel="1">
        <h3 class="wizard-panel-title">${t('p1Title')}</h3>
        <p class="wizard-panel-subtitle">${t('p1Sub')}</p>

        <div style="display:flex;gap:20px;margin-bottom:24px;flex-wrap:wrap;">
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">${t('arrivalDate')}</label>
            <input type="date" id="wizArrDate" class="wizard-input" value="${state.arrivalDate}" style="width:100%;">
          </div>
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">${t('departureDate')}</label>
            <input type="date" id="wizDepDate" class="wizard-input" value="${state.departureDate}" style="width:100%;">
          </div>
        </div>

        <div class="wizard-options-grid cols-2" style="margin-bottom:24px;">
          <button class="wizard-option ${state.arrivalMode === 'plane' ? 'selected' : ''}" data-select="arrivalMode" data-val="plane">
            <div class="option-emoji">✈️</div>
            <div class="option-label">${t('byPlane')}</div>
            <div class="option-sub">${t('byPlaneSub')}</div>
          </button>
          <button class="wizard-option ${state.arrivalMode === 'car' ? 'selected' : ''}" data-select="arrivalMode" data-val="car">
            <div class="option-emoji">🚗</div>
            <div class="option-label">${t('byCar')}</div>
            <div class="option-sub">${t('byCarSub')}</div>
          </button>
        </div>

        <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:8px;">
          <div class="pax-selector">
            <div class="pax-label">${t('adultsLabel')}<span>${t('adultsSub')}</span></div>
            <div class="counter-controls">
              <button class="counter-btn" id="adultsDec">−</button>
              <span class="counter-value">${state.adults}</span>
              <button class="counter-btn" id="adultsInc">+</button>
            </div>
          </div>
          <div class="pax-selector">
            <div class="pax-label">${t('babiesLabel')}<span>${t('babiesSub')}</span></div>
            <div class="counter-controls">
              <button class="counter-btn" id="babiesDec">−</button>
              <span class="counter-value">${state.babies}</span>
              <button class="counter-btn" id="babiesInc">+</button>
            </div>
          </div>
        </div>
      </div>`;
  }

  function buildPanel2() {
    const tn = getTotalNights();
    if (tn <= 0) {
      return `<div class="wizard-panel ${state.step === 2 ? 'active' : ''}" data-panel="2">
        <p>${t('invalidDates')}</p>
      </div>`;
    }

    // Sync itinerary array length
    if (state.itinerary.length !== tn) {
      const newItinerary = [];
      for (let i = 0; i < tn; i++) {
        newItinerary.push(state.itinerary[i] || { nightAcc: '', dayAct: '' });
      }
      state.itinerary = newItinerary;
    }

    let html = `<div class="wizard-panel ${state.step === 2 ? 'active' : ''}" data-panel="2">
      <h3 class="wizard-panel-title">${t('p2Title')}</h3>
      <p class="wizard-panel-subtitle">${t('p2Sub')}</p>
      <div class="wizard-timeline">`;

    const getLocalDate = (base, offsetDays) => {
      const d = new Date(base);
      d.setDate(d.getDate() + offsetDays);
      return d.toLocaleDateString(state.lang, { weekday: 'short', month: 'short', day: 'numeric' });
    };

    for (let i = 0; i < tn; i++) {
      const dayDate = getLocalDate(state.arrivalDate, i);
      const accId = state.itinerary[i].nightAcc;
      
      html += `
        <div class="timeline-item" style="padding:15px; background:var(--wiz-surface); border:1px solid var(--wiz-border); border-radius:12px; margin-bottom:15px;">
          <div style="font-weight:600;margin-bottom:10px;">${t('dayLabel')} ${i+1} • ${dayDate}</div>
      `;

      // Activity Dropdown (only for day 2+)
      if (i > 0) {
        const prevAcc = state.itinerary[i-1].nightAcc;
        const acts = ACTIVITIES.filter(a => !a.requiresVillaMariaStay || prevAcc === 'villa-maria');
        
        html += `
          <div style="margin-bottom:10px;">
            <label style="font-size:0.85rem;color:var(--wiz-text-muted);">${t('chooseAct')}</label>
            <select class="wizard-input act-select" data-index="${i}" style="width:100%;margin-top:4px;">
              <option value="">-- ${t('noActivity')} --</option>
              ${acts.map(a => `
                <option value="${a.id}" ${state.itinerary[i].dayAct === a.id ? 'selected' : ''}>
                  ${a.emoji} ${txt(a.name)}
                </option>
              `).join('')}
            </select>
          </div>
        `;
      }

      // Accommodation Dropdown for this night
      html += `
          <div>
            <label style="font-size:0.85rem;color:var(--wiz-text-muted);">${t('nightLabel')} ${i+1} (${t('chooseAcc')})</label>
            <select class="wizard-input acc-select" data-index="${i}" style="width:100%;margin-top:4px;">
              <option value="">-- ${t('chooseAcc')} --</option>
              ${Object.values(ACCOMMODATIONS).map(a => `
                <option value="${a.id}" ${state.itinerary[i].nightAcc === a.id ? 'selected' : ''}>
                  ${a.emoji} ${txt(a.name)}
                </option>
              `).join('')}
            </select>
          </div>
        </div>
      `;
    }
    html += `</div></div>`;
    return html;
  }

  function buildPanel3() {
    let vmSelected = state.itinerary.some(day => day.nightAcc === 'villa-maria');

    // Gather unique accommodations selected
    const selectedAccs = new Set(state.itinerary.map(d => d.nightAcc).filter(Boolean));

    let html = `<div class="wizard-panel ${state.step === 3 ? 'active' : ''}" data-panel="3">
      <h3 class="wizard-panel-title">${t('p3Title')}</h3>
      <p class="wizard-panel-subtitle">${t('p3Sub')}</p>
      
      <div style="margin-bottom:24px;">
        <h4 style="margin-bottom:12px;font-size:1.05rem;">${t('roomTypeLabel')}</h4>
        <div class="wizard-options-grid cols-1">`;

    for (const accId of selectedAccs) {
      const acc = getAccById(accId);
      html += `
        <div style="padding:12px; background:var(--wiz-surface); border-radius:8px; border:1px solid var(--wiz-border);">
          <div style="font-weight:600; margin-bottom:8px;">${acc.emoji} ${txt(acc.name)}</div>
          <div class="wizard-options-grid cols-3" style="gap:10px;">
            ${acc.rooms.map(r => `
              <button class="wizard-option ${state.roomTypes[accId] === r.tier ? 'selected' : ''}" data-room="${accId}" data-tier="${r.tier}" style="padding:10px;text-align:center;">
                <div class="option-label" style="font-size:0.9rem;">${txt(r.name)}</div>
              </button>
            `).join('')}
          </div>
        </div>
      `;
    }

    if (selectedAccs.size === 0) {
      html += `<p style="color:var(--wiz-text-muted);">No accommodations selected yet.</p>`;
    }

    html += `</div></div>`;

    html += `<div class="wizard-checkbox-list">`;
    
    if (vmSelected) {
      html += `
        <label class="wizard-checkbox-item ${state.kasankala ? 'selected' : ''}">
          <input type="checkbox" id="chkKasankala" ${state.kasankala ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">${t('kasankalaAddon')}</div>
            <div class="wizard-checkbox-desc">${t('kasankalaSub')}</div>
          </div>
        </label>`;
    }

    if (state.arrivalMode === 'plane') {
      html += `
        <label class="wizard-checkbox-item ${state.returnTransfer ? 'selected' : ''}">
          <input type="checkbox" id="chkReturn" ${state.returnTransfer ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">${t('addAirportReturn')}</div>
            <div class="wizard-checkbox-desc">${t('transportNote')}</div>
          </div>
        </label>`;
    }

    html += `
        <label class="wizard-checkbox-item ${state.customRequest ? 'selected' : ''}">
          <input type="checkbox" id="chkCustom" ${state.customRequest ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">${t('requestCustom')}</div>
          </div>
        </label>
      </div>
    </div>`;

    return html;
  }

  function buildPanel4() {
    if (state._sending) {
      return `<div class="wizard-panel ${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;"><h3>${t('sending')}</h3></div>
      </div>`;
    }
    if (state._sent) {
      return `<div class="wizard-panel ${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;color:#10b981;">
          <h3 style="margin-bottom:15px;">${t('sentOk')}</h3>
          <button class="wiz-btn wiz-btn-outline" id="wizRestartSent" style="margin:0 auto;">↺ ${t('restartLabel')}</button>
        </div>
      </div>`;
    }
    if (state._sendError) {
      return `<div class="wizard-panel ${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;color:#ef4444;">
          <h3 style="margin-bottom:15px;">${t('sentErr')}</h3>
          <button class="wiz-btn wiz-btn-primary" id="wizRetrySent" style="margin:0 auto;">${t('sendProgram')}</button>
        </div>
      </div>`;
    }

    const tn = getTotalNights();
    return `
      <div class="wizard-panel ${state.step === 4 ? 'active' : ''}" data-panel="4">
        <h3 class="wizard-panel-title">${t('p4Title')}</h3>
        <p class="wizard-panel-subtitle">${t('p4Sub')}</p>

        <div class="wizard-summary-box">
          <div class="summary-section">
            <h4>${t('groupInfo')}</h4>
            <div class="summary-line">
              <span class="summary-name">${state.adults} ${state.adults === 1 ? t('adultsCount') : t('adultsCountP')}${state.babies > 0 ? ` + ${state.babies} ${state.babies === 1 ? t('babiesCount') : t('babiesCountP')}` : ''}</span>
            </div>
            <div class="summary-line">
              <span class="summary-name">Dates: ${state.arrivalDate} ➔ ${state.departureDate} (${tn} ${t('nightsLabel')})</span>
            </div>
          </div>
          
          <div class="summary-section">
            <h4>${t('yourStay')}</h4>
            ${state.itinerary.map((day, i) => {
              const acc = day.nightAcc ? getAccById(day.nightAcc) : null;
              const act = day.dayAct ? getActivityById(day.dayAct) : null;
              return `
                <div class="timeline-item">
                  <div class="timeline-dot"></div>
                  <div class="timeline-day-label">${t('dayLabel')} ${i+1}</div>
                  <div class="timeline-day-title">${acc ? acc.emoji + ' ' + txt(acc.name) : '---'}</div>
                  <div class="timeline-day-detail">${i === 0 ? t('arrival') : (act ? act.emoji + ' ' + txt(act.name) : t('noActivity'))}</div>
                </div>
              `;
            }).join('')}
            <div class="timeline-item">
              <div class="timeline-dot"></div>
              <div class="timeline-day-label">${t('departure')}</div>
              <div class="timeline-day-detail">${state.returnTransfer ? 'Girona Travel Transfer' : ''}</div>
            </div>
          </div>
        </div>

        <div style="background:var(--wiz-surface); border:1px solid var(--wiz-border); padding:20px; border-radius:12px; margin-top:20px;">
          <div style="margin-bottom:15px;">
            <label style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:6px;">${t('guestNameLabel')}</label>
            <input type="text" id="wizGuestName" class="wizard-input" style="width:100%" placeholder="${t('guestNamePlaceholder')}" value="${state.guestName}">
          </div>
          <div style="margin-bottom:20px;">
            <label style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:6px;">${t('guestEmailLabel')}</label>
            <input type="email" id="wizGuestEmail" class="wizard-input" style="width:100%" placeholder="${t('guestEmailPlaceholder')}" value="${state.guestEmail}">
          </div>
          
          <div class="wizard-alert">
            ${t('vatNote')}<br>${t('discountNote')}
          </div>

          <button class="wiz-btn wiz-btn-primary" id="wizSubmit" style="width:100%;margin-top:15px;height:50px;">
            ${t('sendProgram')}
          </button>
        </div>
      </div>
    `;
  }

  function bindEvents() {
    // Nav
    container.querySelector('#wizNext')?.addEventListener('click', () => {
      if (state.step === 1 && getTotalNights() <= 0) {
        alert(t('invalidDates'));
        return;
      }
      if (state.step < 4) { state.step++; render(); }
    });
    container.querySelector('#wizBack')?.addEventListener('click', () => {
      if (state.step > 1) { state.step--; render(); }
    });
    container.querySelector('#wizRestart')?.addEventListener('click', () => {
      state = defaultState(); render();
    });
    container.querySelector('#wizRestartSent')?.addEventListener('click', () => {
      state = defaultState(); render();
    });

    // Panel 1
    const arrDate = container.querySelector('#wizArrDate');
    if (arrDate) arrDate.addEventListener('change', (e) => { state.arrivalDate = e.target.value; });
    const depDate = container.querySelector('#wizDepDate');
    if (depDate) depDate.addEventListener('change', (e) => { state.departureDate = e.target.value; });

    container.querySelectorAll('[data-select="arrivalMode"]').forEach(b => {
      b.addEventListener('click', (e) => {
        state.arrivalMode = e.currentTarget.dataset.val; render();
      });
    });

    container.querySelector('#adultsDec')?.addEventListener('click', () => { if (state.adults > 1) { state.adults--; render(); } });
    container.querySelector('#adultsInc')?.addEventListener('click', () => { if (state.adults < 20) { state.adults++; render(); } });
    container.querySelector('#babiesDec')?.addEventListener('click', () => { if (state.babies > 0) { state.babies--; render(); } });
    container.querySelector('#babiesInc')?.addEventListener('click', () => { if (state.babies < 10) { state.babies++; render(); } });

    // Panel 2 Dropdowns
    container.querySelectorAll('.acc-select').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.index);
        state.itinerary[idx].nightAcc = e.target.value;
        render();
      });
    });
    container.querySelectorAll('.act-select').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.index);
        state.itinerary[idx].dayAct = e.target.value;
        // no render needed just for this unless dependencies change
      });
    });

    // Panel 3
    container.querySelectorAll('[data-room]').forEach(b => {
      b.addEventListener('click', (e) => {
        const d = e.currentTarget.dataset;
        state.roomTypes[d.room] = d.tier;
        render();
      });
    });
    const chkKas = container.querySelector('#chkKasankala');
    if (chkKas) chkKas.addEventListener('change', e => { state.kasankala = e.target.checked; });
    const chkRet = container.querySelector('#chkReturn');
    if (chkRet) chkRet.addEventListener('change', e => { state.returnTransfer = e.target.checked; });
    const chkCus = container.querySelector('#chkCustom');
    if (chkCus) chkCus.addEventListener('change', e => { state.customRequest = e.target.checked; });

    // Panel 4 form sync & submit
    const nameEl = container.querySelector('#wizGuestName');
    if (nameEl) nameEl.addEventListener('input', e => { state.guestName = e.target.value; });
    const emailEl = container.querySelector('#wizGuestEmail');
    if (emailEl) emailEl.addEventListener('input', e => { state.guestEmail = e.target.value; });

    const btnSubmit = container.querySelector('#wizSubmit') || container.querySelector('#wizRetrySent');
    if (btnSubmit) {
      btnSubmit.addEventListener('click', async () => {
        if (!state.guestName || !state.guestEmail) {
          alert('Please enter your name and email');
          return;
        }
        state._sending = true;
        render();

        const payload = {
          to: 'reservas.kalihotels@gmail.com',
          subject: `New Trip Wizard Itinerary: ${state.guestName}`,
          data: {
            guest: { name: state.guestName, email: state.guestEmail },
            group: { adults: state.adults, babies: state.babies },
            dates: { arrival: state.arrivalDate, departure: state.departureDate, nights: getTotalNights() },
            transport: { arrival: state.arrivalMode, return_transfer: state.returnTransfer },
            itinerary: state.itinerary.map(day => ({
              accommodation: day.nightAcc ? getAccById(day.nightAcc).name.en : null,
              activity: day.dayAct ? getActivityById(day.dayAct).name.en : null
            })),
            rooms: state.roomTypes,
            addons: { kasankala: state.kasankala, custom: state.customRequest }
          }
        };

        try {
          const res = await fetch('https://api.kalihotels.com/wizard/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          if (!res.ok) throw new Error('HTTP ' + res.status);
          state._sent = true;
          state._sending = false;
          state._sendError = false;
        } catch (err) {
          console.error('Wizard send error:', err);
          state._sent = false;
          state._sending = false;
          state._sendError = true;
        }
        render();
      });
    }
  }

  function updateProgress() {
    const fill = container.querySelector('#wizProgress');
    if (fill) fill.style.width = progressPct() + '%';
  }
  function updateStepperState() {
    container.querySelectorAll('.wizard-step-item').forEach(item => {
      const n = parseInt(item.dataset.step);
      item.classList.remove('active', 'completed');
      if (n === state.step) item.classList.add('active');
      else if (n < state.step) item.classList.add('completed');
    });
  }

  /* -------------------------------------------------------------------------

   * PUBLIC API
   * ----------------------------------------------------------------------- */
  function init(selector, options = {}) {
    container = typeof selector === 'string' ? document.querySelector(selector) : selector;
    if (!container) { console.warn('TripWizard: container not found:', selector); return; }

    // Detect language from page URL or option
    if (options.lang) {
      state.lang = options.lang;
    } else {
      const path = window.location.pathname;
      if (path.startsWith('/es')) state.lang = 'es';
      else if (path.startsWith('/it')) state.lang = 'it';
      else if (path.startsWith('/fr')) state.lang = 'fr';
      else if (path.startsWith('/de')) state.lang = 'de';
      else state.lang = 'en';
    }

    render();
  }

  function setLang(lang) {
    if (T[lang]) { state.lang = lang; render(); }
  }

  return { init, setLang };

})();
