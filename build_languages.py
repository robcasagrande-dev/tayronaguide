import os

languages = {
    "en": {
        "dir": "",
        "img_prefix": "/",
        "lang_name": "English",
        "flag": "🇬🇧",
        "title": "Tayrona National Park Guide 2026 | Official Ticket Info & Guided Tours",
        "description": "Official 2026 Tayrona National Park Travel Guide. Learn how entry passes work, avoid online ticket scams, skip the 2-hour gate queue with certified local guides, and book stays near park entrances.",
        "announcement": "✨ <strong>0% HOTEL VAT CAMPAIGN:</strong> Colombians & Foreigners pay 0% IVA on hotel stays! <a href=\"#wizard\">Build your concierge trip &rarr;</a>",
        "nav": {
            "truth": "🎫 Ticket Truth",
            "no_vat": "🏷️ 0% VAT",
            "guide": "🌿 Park Guide",
            "wizard": "🛎️ Concierge Request",
            "skip": "⚡ Skip Queue",
            "tours": "🥾 Tours",
            "trails": "Trails",
            "stays": "🏨 Lodging",
            "faq": "❓ FAQ",
            "btn": "Book Stay & Tours &rarr;"
        },
        "hero": {
            "badge": "Verified 2026 Park Travel Guide & Hospitality Hub",
            "title": "Experience <span>Santa Marta & Tayrona</span> Without the Stress",
            "subtitle": "Discover curated packages combining Kali Hotel Santa Marta, Villa María Tayrona, Girona Travel transfers, and an exclusive concierge trip builder with 0% hotel VAT for EVERYONE.",
            "btn1": "⚡ Build Your Trip (0% VAT)",
            "btn2": "🏨 View Bundled Packages",
            "trust1_title": "0% VAT Guarantee",
            "trust1_sub": "No IVA for Colombians & Foreigners",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Queue skip at park gate",
            "trust3_title": "Kali Hotel + Villa María Tayrona",
            "trust3_sub": "City & Jungle Luxury Duo"
        },
        "no_vat": {
            "tag": "✨ 2026 Hospitality Equity Campaign",
            "title": "Colombians Should Not Pay VAT at Hotels <span>As Foreigners Do</span>",
            "subtitle": "In Colombia, international tourists are exempt from 19% hotel VAT (IVA). We believe Colombian travelers deserve the exact same tax-free experience! At Kali Hotel Santa Marta & Villa María Tayrona, we offer a 0% VAT rate for ALL guests.",
            "card1_title": "🇨🇴 Colombian Nationals",
            "card1_desc": "Save 19% IVA automatically! We absorb hotel tax so domestic travelers enjoy the exact same 0% VAT pricing as foreign visitors.",
            "card2_title": "🌎 International Travelers",
            "card2_desc": "100% Tax-Exempt & Transparent pricing. No surprise fees, no hidden taxes, and clear upfront rate guarantees at check-in.",
            "card3_title": "🏨 Kali Hotel & Villa María Tayrona",
            "card3_desc": "Valid across all stay combinations: Kali Hotel in Santa Marta Historic Center and Villa María Tayrona Nature Sanctuary."
        },
        "packages": {
            "tag": "📦 Curated All-Inclusive Combos",
            "title": "Santa Marta, Tayrona & Girona Travel Packages",
            "subtitle": "Turnkey travel packages combining Kali Hotel (City), Villa María Tayrona (Tayrona Nature), Girona Travel Transfers & Fast-Track Guided Tours."
        },
        "truth": {
            "tag": "⚠️ Essential Entry Knowledge",
            "title": "The Truth About Buying Tayrona Park Passes",
            "lead": "Don't fall for online scams. Understand how official entrance tickets actually work.",
            "warn_title": "Warning: Official Park Passes Cannot Be Reserved Online in Advance",
            "warn_desc": "Do NOT trust third-party websites claiming to sell official park entry tickets on the internet.",
            "warn_body": "By regulation of <em>Parques Nacionales Naturales de Colombia</em>, official park entrance passes are <strong>paid strictly in person at the park gates</strong> (El Zaino or Palangana entrances) in cash or credit card upon arrival.",
            "sol_title": "⚡ How to Avoid Buying Tickets In Person & Skip the Queue:",
            "sol_desc": "<strong>When you reserve a guided tour with Girona Travels, you avoid all of this hassle!</strong> Your certified local guide arrives at the gate early in the morning, handles the ticket booth queue, and buys your entry passes and mandatory insurance for you. When you arrive, your guide takes you directly into the park entrance without waiting in line.",
            "sol_btn": "Reserve Your Guided Tour &rarr;",
            "box1_title": "🎫 Entry Fees (2026 Rates)",
            "box1_item1": "<strong>Foreign Tourists:</strong> ~90,000 COP ($22 USD)",
            "box1_item2": "<strong>Colombian Citizens / Residents:</strong> ~35,000 COP ($9 USD)",
            "box1_item3": "<strong>Mandatory Daily Medical Insurance:</strong> ~6,000 COP/day ($1.50 USD)",
            "box2_title": "📄 What You Must Bring to the Gate",
            "box2_item1": "<strong>Original Physical Passport</strong> or Colombian Cedula",
            "box2_item2": "Cash (COP) or credit card for entry & insurance fees",
            "box2_item3": "No single-use plastics allowed (Strict Eco Policy)"
        },
        "skip": {
            "tag": "🚀 The Insider Solution",
            "title": "How to Skip the 2-Hour Gate Queue",
            "desc": "The queue at the El Zaino park entrance in the morning heat can easily take <strong>1 to 2+ hours</strong> as hundreds of travelers line up to pay fees and verify IDs.",
            "box_title": "🔑 The Girona Travels Guided Advantage:",
            "box_desc": "While you cannot buy entry passes online yourself, <strong>when you book a certified guided tour with Girona Travels</strong>, your local guide arrives at the entrance booth early in the morning and handles the ticket purchasing line on your behalf.",
            "item1": "✅ Your Girona Travels guide waits in the early ticket line for you.",
            "item2": "✅ When you arrive, your entrance is seamless—you walk right past the main line.",
            "item3": "✅ Learn indigenous Tayrona history, spot wildlife, and navigate trails safely.",
            "btn": "🥾 Reserve a Guided Tour & Skip Queue &rarr;"
        },
        "tours": {
            "pkg2_desc": "Includes 1 night stay near park gate at Villa María Tayrona / Casa Isabella, morning queue fast-track, guided trek to Arrecifes & Cabo San Juan, gourmet dining at Kasankala Restaurant, and Girona Travels private transport."
        },
        "stays": {
            "villa_title": "🌿 Villa María Tayrona & Kasankala Restaurant",
            "villa_desc": "Villa María Tayrona is a luxury jungle eco-lodge located right near the El Zaino entrance, featuring eco-luxury rooms, pool, and gourmet dining at Kasankala Restaurant.",
            "villa_btn": "View Rooms at ParqueTayrona.org &rarr;"
        }
    },
    "es": {
        "dir": "es",
        "img_prefix": "/",
        "lang_name": "Español",
        "flag": "🇪🇸",
        "title": "Guía Parque Nacional Tayrona 2026 | Entradas y Tours Guiados",
        "description": "Guía oficial 2026 del Parque Nacional Tayrona. Aprende cómo funcionan las entradas, evita estafas en línea y sáltate la fila de 2 horas con guías locales certificados.",
        "announcement": "✨ <strong>CAMPAÑA SIN IVA:</strong> ¡Colombianos y extranjeros pagan 0% IVA en hospedaje! <a href=\"#wizard\">Diseña tu viaje elástico &rarr;</a>",
        "nav": {
            "truth": "🎫 Entradas",
            "no_vat": "🏷️ Sin IVA",
            "guide": "🌿 Guía Parque",
            "wizard": "🛎️ Solicitar Concierge",
            "skip": "⚡ Fila",
            "tours": "🥾 Tours",
            "trails": "Senderos",
            "stays": "🏨 Hospedaje",
            "faq": "❓ FAQ",
            "btn": "Reservar Hospedaje y Tours &rarr;"
        },
        "hero": {
            "badge": "Guía de Viaje Verificada 2026 y Centro Turístico",
            "title": "Disfruta <span>Santa Marta y Tayrona</span> Sin Estrés",
            "subtitle": "Descubre paquetes exclusivos combinando Kali Hotel Santa Marta, Villa María Tayrona, transportes Girona Travel y un diseñador elástico con tarifa SIN IVA para TODOS.",
            "btn1": "⚡ Diseña tu Viaje (0% IVA)",
            "btn2": "🏨 Ver Paquetes Combinados",
            "trust1_title": "Garantía Sin IVA",
            "trust1_sub": "0% IVA para colombianos y extranjeros",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Ingreso preferencial en taquilla",
            "trust3_title": "Kali Hotel + Villa María Tayrona",
            "trust3_sub": "Dúo Ciudad y Selva de Lujo"
        },
        "no_vat": {
            "tag": "✨ Campaña de Equidad Hotelera 2026",
            "title": "Los Colombianos No Deberían Pagar IVA <span>Como los Extranjeros</span>",
            "subtitle": "En Colombia, los turistas internacionales están exentos del 19% de IVA hotelero. ¡Creemos que los viajeros colombianos merecen el mismo beneficio! En Kali Hotel Santa Marta y Villa María Tayrona ofrecemos tarifa 0% IVA para TODOS.",
            "card1_title": "🇨🇴 Nacionales Colombianos",
            "card1_desc": "¡Ahorra el 19% de IVA automáticamente! Absorbemos el impuesto hotelero para que disfrutes la misma tarifa exenta que los extranjeros.",
            "card2_title": "🌎 Turistas Internacionales",
            "card2_desc": "Tarifa 100% exenta de impuestos según la normativa oficial de turismo en Colombia. Transparencia total sin sorpresas al momento del check-in.",
            "card3_title": "🏨 Kali Hotel y Villa María Tayrona",
            "card3_desc": "Válido en todas las combinaciones: Kali Hotel en el Centro Histórico de Santa Marta y Villa María Tayrona en el Parque Tayrona."
        },
        "packages": {
            "tag": "📦 Combos Todo Incluido",
            "title": "Paquetes Santa Marta, Tayrona y Girona Travel",
            "subtitle": "Paquetes turísticos completos que combinan Kali Hotel (Ciudad), Villa María Tayrona (Selva Tayrona), transportes Girona Travel y tours guiados preferenciales."
        },
        "truth": {
            "tag": "⚠️ Información Esencial de Ingreso",
            "title": "La Verdad sobre Comprar Entradas al Tayrona",
            "lead": "No caigas en estafas por internet. Comprende cómo funcionan las entradas oficiales.",
            "warn_title": "Advertencia: Las Entradas Oficiales NO se Pueden Reservar en Línea",
            "warn_desc": "NO confíes en páginas web de terceros que afirmen vender entradas oficiales por internet.",
            "warn_body": "Por disposición de <em>Parques Nacionales Naturales de Colombia</em>, las entradas oficiales se <strong>pagan estrictamente de manera presencial en las taquillas del parque</strong> (El Zaino o Palangana) en efectivo o tarjeta al llegar.",
            "sol_title": "⚡ Cómo Evitar el Trámite Presencial y Saltarte la Fila:",
            "sol_desc": "<strong>¡Al reservar un tour guiado con Girona Travels, te evitas todo este trámite!</strong> Tu guía local certificado llega a la taquilla muy temprano en la mañana, gestiona la fila y compra tus entradas y seguro obligatorio por ti. Al llegar, tu guía te ingresa directamente al parque sin hacer fila.",
            "sol_btn": "Reservar Tour Guiado &rarr;",
            "box1_title": "🎫 Tarifas de Ingreso (Tarifas 2026)",
            "box1_item1": "<strong>Turistas Extranjeros:</strong> ~90,000 COP ($22 USD)",
            "box1_item2": "<strong>Ciudadanos / Residentes Colombianos:</strong> ~35,000 COP ($9 USD)",
            "box1_item3": "<strong>Seguro Médico Diario Obligatorio:</strong> ~6,000 COP/día ($1.50 USD)",
            "box2_title": "📄 Requisitos Obligatorios para la Taquilla",
            "box2_item1": "<strong>Pasaporte Físico Original</strong> o Cédula Colombiana",
            "box2_item2": "Efectivo (COP) o tarjeta para entradas y seguro",
            "box2_item3": "Prohibido plásticos de un solo uso (Política Ecológica)"
        },
        "skip": {
            "tag": "🚀 La Solución Estratégica",
            "title": "Cómo Saltarte la Fila de 2 Horas en la Entrada",
            "desc": "La fila en la entrada de El Zaino bajo el calor de la mañana puede tomar fácilmente de <strong>1 a 2+ horas</strong> mientras cientos de viajeros hacen fila para pagar y validar documentos.",
            "box_title": "🔑 La Ventaja del Tour Guiado con Girona Travels:",
            "box_desc": "Aunque no puedes comprar las entradas por internet tú mismo, <strong>al reservar un tour guiado con Girona Travels</strong>, tu guía llega temprano a la taquilla y realiza la fila de compra por ti.",
            "item1": "✅ Tu guía de Girona Travels hace la fila madrugadora por ti.",
            "item2": "✅ Al llegar, tu ingreso es fluido: pasas directo sin hacer fila.",
            "item3": "✅ Aprende historia indígena Tayrona, avista fauna silvestre y camina seguro.",
            "btn": "🥾 Reservar Tour Guiado y Saltarse la Fila &rarr;"
        },
        "tours": {
            "pkg2_desc": "Incluye 1 noche de hospedaje cerca del parque en Villa María Tayrona / Casa Isabella, entrada preferencial sin fila, trek guiado a Arrecifes y Cabo San Juan, cena gourmet en Restaurante Kasankala y transporte privado Girona Travels."
        },
        "stays": {
            "villa_title": "🌿 Villa María Tayrona y Restaurante Kasankala",
            "villa_desc": "Villa María Tayrona es un eco-lodge de lujo en la selva ubicado cerca de la entrada El Zaino, con habitaciones ecológicas de lujo, piscina y gastronomía gourmet en el Restaurante Kasankala.",
            "villa_btn": "Ver Habitaciones en ParqueTayrona.org &rarr;"
        }
    },
    "it": {
        "dir": "it",
        "img_prefix": "/",
        "lang_name": "Italiano",
        "flag": "🇮🇹",
        "title": "Guida Parco Nazionale Tayrona 2026 | Biglietti e Tour Guidati",
        "description": "Guida ufficiale 2026 del Parco Nazionale Tayrona. Scopri come funzionano i biglietti d'ingresso, evita le truffe online e salta la coda di 2 ore con guide locali certificate.",
        "announcement": "✨ <strong>CAMPAGNA NO IVA HOTEL:</strong> Colombiani e stranieri pagano 0% IVA! <a href=\"#wizard\">Crea il tuo viaggio elastico &rarr;</a>",
        "nav": {
            "truth": "🎫 Biglietti",
            "no_vat": "🏷️ 0% IVA",
            "guide": "🌿 Guida Parco",
            "wizard": "🛎️ Richiedi Concierge",
            "skip": "⚡ Salta Coda",
            "tours": "🥾 Tour",
            "trails": "Sentieri",
            "stays": "🏨 Alloggi",
            "faq": "❓ FAQ",
            "btn": "Prenota Soggiorno e Tour &rarr;"
        },
        "hero": {
            "badge": "Guida di Viaggio Verificata 2026",
            "title": "Vivi <span>Santa Marta & Tayrona</span> Senza Stress",
            "subtitle": "Scopri i pacchetti che combinano Kali Hotel Santa Marta, Villa María Tayrona, trasferimenti Girona Travel e un servizio concierge con prezzo SENZA IVA per TUTTI.",
            "btn1": "⚡ Configura il Tuo Viaggio (0% IVA)",
            "btn2": "🏨 Vedi i Pacchetti",
            "trust1_title": "Garanzia 0% IVA",
            "trust1_sub": "No IVA per colombiani e stranieri",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Salta la coda all'ingresso",
            "trust3_title": "Kali Hotel + Villa María Tayrona",
            "trust3_sub": "Città e Natura di Lusso"
        },
        "no_vat": {
            "tag": "✨ Campagna Equità Alberghiera 2026",
            "title": "I Colombiani Non Dovrebbero Pagare l'IVA <span>Come gli Stranieri</span>",
            "subtitle": "In Colombia, i turisti internazionali sono esenti dall'IVA del 19% sugli hotel. Riteniamo che anche i viaggiatori colombiani debbano godere dello stesso beneficio! Presso Kali Hotel Santa Marta e Villa María Tayrona offriamo la tariffa 0% IVA per TUTTI.",
            "card1_title": "🇨🇴 Cittadini Colombiani",
            "card1_desc": "Risparmia l'IVA del 19% automaticamente! Assorbiamo la tassa alberghiera così paghi la stessa tariffa esente degli stranieri.",
            "card2_title": "🌎 Turisti Internazionali",
            "card2_desc": "Tariffa esente da imposte secondo le norme ufficiali colombiane. Trasparenza totale senza sorprese al check-in.",
            "card3_title": "🏨 Kali Hotel & Villa María Tayrona",
            "card3_desc": "Valido per tutte le combinazioni: Kali Hotel nel centro storico di Santa Marta e Villa María Tayrona nella riserva di Tayrona."
        },
        "packages": {
            "tag": "📦 Pacchetti Tutto Incluso",
            "title": "Pacchetti Santa Marta, Tayrona e Girona Travel",
            "subtitle": "Pacchetti completi che combinano Kali Hotel (Città), Villa María Tayrona (Natura Tayrona), trasferimenti Girona Travel e tour guidati salta-coda."
        },
        "truth": {
            "tag": "⚠️ Informazioni Essenziali d'Ingresso",
            "title": "La Verità sull'Acquisto dei Biglietti Tayrona",
            "lead": "Non cadere nelle truffe online. Comprendi come funzionano i biglietti ufficiali.",
            "warn_title": "Attenzione: I Biglietti Ufficiali NON Si Possono Prenotare Online in Anticipo",
            "warn_desc": "NON fidarti di siti web di terze parti che affermano di vendere biglietti ufficiali su internet.",
            "warn_body": "Per disposizione di <em>Parques Nacionales Naturales de Colombia</em>, i biglietti ufficiali si <strong>pagano esclusivamente di persona alle biglietterie del parco</strong> (El Zaino o Palangana) in contanti o carta all'arrivo.",
            "sol_title": "⚡ Come Evitare l'Acquisto di Persona e Saltare la Coda:",
            "sol_desc": "<strong>Prenotando un tour guidato con Girona Travels eviti tutto questo stress!</strong> La tua guida locale arriva alla biglietteria di mattina presto, gestisce la fila e acquista i biglietti e l'assicurazione per te. Al tuo arrivo entri direttamente al parco senza fare la fila.",
            "sol_btn": "Prenota Tour Guidato &rarr;",
            "box1_title": "🎫 Tariffe d'Ingresso (Tariffe 2026)",
            "box1_item1": "<strong>Turisti Stranieri:</strong> ~90,000 COP ($22 USD)",
            "box1_item2": "<strong>Cittadini / Residenti Colombiani:</strong> ~35,000 COP ($9 USD)",
            "box1_item3": "<strong>Assicurazione Medica Giornaliera Obbligatoria:</strong> ~6,000 COP/giorno ($1.50 USD)",
            "box2_title": "📄 Requisiti Obbligatori per la Biglietteria",
            "box2_item1": "<strong>Passaporto Fisico Originale</strong> o Carta d'Identità Colombiana",
            "box2_item2": "Contanti (COP) o carta di credito per biglietti e assicurazione",
            "box2_item3": "Vietata la plastica monouso (Politica Ecologica)"
        },
        "skip": {
            "tag": "🚀 La Soluzione Strategica",
            "title": "Come Saltare la Coda di 2 Ore all'Ingresso",
            "desc": "La coda all'ingresso di El Zaino sotto il calore del mattino può richiedere da <strong>1 a 2+ ore</strong> per pagare i biglietti e verificare i documenti.",
            "box_title": "🔑 Il Vantaggio del Tour Guidato Girona Travels:",
            "box_desc": "Anche se non puoi acquistare i biglietti online da solo, <strong>prenotando un tour guidato con Girona Travels</strong> la tua guida arriva presto e gestisce la fila per te.",
            "item1": "✅ La guida Girona Travels fa la fila all'alba al posto tuo.",
            "item2": "✅ All'arrivo entri senza fare alcuna coda.",
            "item3": "✅ Scopri la storia indigena Tayrona, avvista la fauna e cammina in sicurezza.",
            "btn": "🥾 Prenota Tour Guidato e Salta la Coda &rarr;"
        },
        "tours": {
            "pkg2_desc": "Include 1 notte vicino al parco a Villa María Tayrona / Casa Isabella, ingresso fast-track, trek guidato ad Arrecifes e Cabo San Juan, cena gourmet al Ristorante Kasankala e trasporto privato Girona Travels."
        },
        "stays": {
            "villa_title": "🌿 Villa María Tayrona e Ristorante Kasankala",
            "villa_desc": "Villa María Tayrona è un eco-lodge di lusso situato vicino all'ingresso El Zaino, con camere ecologiche di lusso, piscina e ristorazione gourmet presso il Ristorante Kasankala.",
            "villa_btn": "Vedi Camere su ParqueTayrona.org &rarr;"
        }
    },
    "fr": {
        "dir": "fr",
        "img_prefix": "/",
        "lang_name": "Français",
        "flag": "🇫🇷",
        "title": "Guide Parc National Tayrona 2026 | Billets et Visites Guidées",
        "description": "Guide officiel 2026 du Parc National Tayrona. Découvrez le fonctionnement des billets, évitez les arnaques et évitez la file de 2 heures avec des guides locaux certifiés.",
        "announcement": "✨ <strong>CAMPAGNE HÔTEL SANS TVA:</strong> Colombiens et étrangers ne paient pas de TVA! <a href=\"#wizard\">Concevez votre voyage &rarr;</a>",
        "nav": {
            "truth": "🎫 Billets",
            "no_vat": "🏷️ 0% TVA",
            "guide": "🌿 Guide Parc",
            "wizard": "🛎️ Demande de Conciergerie",
            "skip": "⚡ Coupe-File",
            "tours": "🥾 Tours",
            "trails": "Sentiers",
            "stays": "🏨 Hébergements",
            "faq": "❓ FAQ",
            "btn": "Réserver Séjour et Tours &rarr;"
        },
        "hero": {
            "badge": "Guide Touristique Vérifié 2026",
            "title": "Découvrez <span>Santa Marta & Tayrona</span> Sans Stress",
            "subtitle": "Combinez Kali Hotel Santa Marta, Villa María Tayrona, les transports Girona Travel et un planificateur élastique avec 0% de TVA pour TOUS.",
            "btn1": "⚡ Créez votre Voyage (0% TVA)",
            "btn2": "🏨 Voir les Forfaits",
            "trust1_title": "Garantie 0% TVA",
            "trust1_sub": "Pas de TVA pour Colombiens et étrangers",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Entrée prioritaire au parc",
            "trust3_title": "Kali Hotel + Villa María Tayrona",
            "trust3_sub": "Luxe Ville et Jungle"
        },
        "no_vat": {
            "tag": "✨ Campagne Équité Hôtelière 2026",
            "title": "Les Colombiens Ne Devraient Pas Payer la TVA <span>Comme les Étrangers</span>",
            "subtitle": "En Colombie, les touristes internationaux sont exonérés de 19% de TVA sur les hôtels. Nous pensons que les voyageurs colombiens méritent le même privilège! À Kali Hotel Santa Marta et Villa María Tayrona, nous offrons un tarif 0% TVA pour TOUS.",
            "card1_title": "🇨🇴 Citoyens Colombiens",
            "card1_desc": "Économisez 19% de TVA automatiquement! Nous prenons en charge la taxe pour vous offrir le même tarif exonéré que les visiteurs étrangers.",
            "card2_title": "🌎 Touristes Internationaux",
            "card2_desc": "Tarif 100% exonéré selon les règles du tourisme colombien. Transparence totale sans frais cachés au check-in.",
            "card3_title": "🏨 Kali Hotel & Villa María Tayrona",
            "card3_desc": "Valable pour toutes les combinaisons: Kali Hotel dans le centre historique de Santa Marta et Villa María Tayrona au Parc Tayrona."
        },
        "packages": {
            "tag": "📦 Offres Combinées",
            "title": "Forfaits Santa Marta, Tayrona et Girona Travel",
            "subtitle": "Des séjours clés en main combinant Kali Hotel (Ville), Villa María Tayrona (Jungle Tayrona), transports Girona Travel et visites guidées prioritaires."
        },
        "truth": {
            "tag": "⚠️ Informations Essentielles d'Entrée",
            "title": "La Vérité sur l'Achat des Billets pour Tayrona",
            "lead": "Ne tombez pas dans les arnaques en ligne. Comprenez le fonctionnement des billets officiels.",
            "warn_title": "Attention: Les Billets Officiels Ne Peuvent Pas Être Réservés en Ligne",
            "warn_desc": "Ne faites pas confiance aux sites tiers affirmant vendre des billets officiels sur Internet.",
            "warn_body": "Selon la réglementation des <em>Parques Nacionales Naturales de Colombia</em>, les billets s'achètent <strong>strictement en personne aux guichets du parc</strong> (El Zaino ou Palangana) en espèces ou carte à votre arrivée.",
            "sol_title": "⚡ Comment Éviter l'Achat en Personne et Passer la File:",
            "sol_desc": "<strong>En réservant une visite guidée avec Girona Travels, vous évitez tout ce stress!</strong> Votre guide arrive tôt le matin au guichet, achète vos billets et votre assurance. À votre arrivée, vous entrez directement sans faire la queue.",
            "sol_btn": "Réserver une Visite Guidée &rarr;",
            "box1_title": "🎫 Tarifs d'Entrée (Tarifs 2026)",
            "box1_item1": "<strong>Touristes Étrangers:</strong> ~90 000 COP ($22 USD)",
            "box1_item2": "<strong>Citoyens / Résidents Colombiens:</strong> ~35 000 COP ($9 USD)",
            "box1_item3": "<strong>Assurance Médicale Obligatoire:</strong> ~6 000 COP/jour ($1.50 USD)",
            "box2_title": "📄 Requis Obligatoires pour le Guichet",
            "box2_item1": "<strong>Passeport Physique Original</strong> ou Carte d'Identité Colombienne",
            "box2_item2": "Espèces (COP) ou carte pour l'entrée et l'assurance",
            "box2_item3": "Plastiques à usage unique interdits (Politique Écologique)"
        },
        "skip": {
            "tag": "🚀 La Solution Stratégique",
            "title": "Comment Éviter la File de 2 Heures à l'Entrée",
            "desc": "La file à l'entrée d'El Zaino sous la chaleur matinale peut durer de <strong>1 à 2+ heures</strong>.",
            "box_title": "🔑 L'Avantage de la Visite Guidée Girona Travels:",
            "box_desc": "Même s'il est impossible d'acheter les billets en ligne vous-même, <strong>en réservant avec Girona Travels</strong>, votre guide fait la queue très tôt pour vous.",
            "item1": "✅ Votre guide Girona Travels fait la queue à l'aube pour vous.",
            "item2": "✅ À votre arrivée, vous entrez sans attendre.",
            "item3": "✅ Découvrez l'histoire indigène Tayrona et observez la faune en sécurité.",
            "btn": "🥾 Réserver une Visite et Éviter la File &rarr;"
        },
        "tours": {
            "pkg2_desc": "Inclut 1 nuit près du parc à Villa María Tayrona / Casa Isabella, entrée prioritaire sans file, randonnée guidée à Arrecifes & Cabo San Juan, dîner gastronomique au Restaurant Kasankala et transport privé Girona Travels."
        },
        "stays": {
            "villa_title": "🌿 Villa María Tayrona et Restaurant Kasankala",
            "villa_desc": "Villa María Tayrona est un éco-lodge de luxe dans la jungle près de l'entrée El Zaino, proposant des chambres écologiques de luxe, une piscine et une cuisine gastronomique au Restaurant Kasankala.",
            "villa_btn": "Voir les Chambres sur ParqueTayrona.org &rarr;"
        }
    },
    "de": {
        "dir": "de",
        "img_prefix": "/",
        "lang_name": "Deutsch",
        "flag": "🇩🇪",
        "title": "Tayrona Nationalpark Reiseführer 2026 | Tickets & Geführte Touren",
        "description": "Offizieller Reiseführer 2026 für den Tayrona-Nationalpark. Erfahren Sie, wie Eintrittskarten funktionieren, vermeiden Sie Online-Betrug und überspringen Sie die 2-Stunden-Schlange mit zertifizierten lokalen Guides.",
        "announcement": "✨ <strong>0% MWST. HOTEL-AKTION:</strong> Kolumbianer & Ausländer zahlen 0% MwSt.! <a href=\"#wizard\">Reise konfigurieren &rarr;</a>",
        "nav": {
            "truth": "🎫 Tickets",
            "no_vat": "🏷️ 0% MwSt.",
            "guide": "🌿 Park-Guide",
            "wizard": "🛎️ Concierge-Anfrage",
            "skip": "⚡ Fast-Track",
            "tours": "🥾 Touren",
            "trails": "Wanderwege",
            "stays": "🏨 Unterkünfte",
            "faq": "❓ FAQ",
            "btn": "Unterkunft & Touren Buchen &rarr;"
        },
        "hero": {
            "badge": "Verifizierter Reiseführer 2026",
            "title": "Erleben Sie <span>Santa Marta & Tayrona</span> Ohne Stress",
            "subtitle": "Kombinieren Sie Kali Hotel Santa Marta, Villa María Tayrona, Girona Travel Transfers und einen elastischen Reiseplaner mit 0% MwSt. für ALLE.",
            "btn1": "⚡ Reise Planen (0% MwSt.)",
            "btn2": "🏨 Kombi-Pakete Ansehen",
            "trust1_title": "0% MwSt. Garantie",
            "trust1_sub": "Keine MwSt. für Kolumbianer & Ausländer",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Einlass ohne Wartezeit",
            "trust3_title": "Kali Hotel + Villa María Tayrona",
            "trust3_sub": "Stadt & Dschungel Luxus"
        },
        "no_vat": {
            "tag": "✨ Hotel-Gerechtigkeits-Kampagne 2026",
            "title": "Kolumbianer Sollten Keine MwSt. Zahlen <span>Wie Ausländische Touristen</span>",
            "subtitle": "In Kolumbien sind ausländische Touristen von 19% Hotel-MwSt. befreit. Wir glauben, kolumbianische Reisende verdienen das gleiche Recht! Im Kali Hotel Santa Marta & Villa María Tayrona bieten wir 0% MwSt. für ALLE Gäste.",
            "card1_title": "🇨🇴 Kolumbianische Staatsbürger",
            "card1_desc": "Sparen Sie automatisch 19% MwSt.! Wir übernehmen die Steuer, sodass Sie den gleichen steuerfreien Preis wie internationale Gäste zahlen.",
            "card2_title": "🌎 Internationale Touristen",
            "card2_desc": "100% steuerfrei nach offiziellen kolumbianischen Tourismusregeln. Vollständige Transparenz ohne versteckte Gebühren beim Check-in.",
            "card3_title": "🏨 Kali Hotel & Villa María Tayrona",
            "card3_desc": "Gültig für alle Kombinationen: Kali Hotel im historischen Zentrum von Santa Marta & Villa María Tayrona im Tayrona-Park."
        },
        "packages": {
            "tag": "📦 All-Inclusive Pakete",
            "title": "Santa Marta, Tayrona & Girona Travel Pakete",
            "subtitle": "Komplettpakete kombiniert aus Kali Hotel (Stadt), Villa María Tayrona (Tayrona Natur), Girona Travel Transfers und geführten Touren."
        },
        "truth": {
            "tag": "⚠️ Wichtiges Wissen zum Einlass",
            "title": "Die Wahrheit über den Kauf von Tayrona-Tickets",
            "lead": "Fallen Sie nicht auf Online-Betrug herein. Verstehen Sie, wie die offiziellen Tickets funktionieren.",
            "warn_title": "Warnung: Offizielle Park-Tickets Können Nicht Im Voraus Online Reserviert Werden",
            "warn_desc": "Vertrauen Sie KANEN Drittanbieter-Websites, die behaupten, offizielle Tickets im Internet zu verkaufen.",
            "warn_body": "Gemäß den Bestimmungen von <em>Parques Nacionales Naturales de Colombia</em> werden offizielle Eintrittskarten <strong>ausschließlich persönlich an den Parktoren</strong> (El Zaino oder Palangana) in bar oder mit Karte vor Ort bezahlt.",
            "sol_title": "⚡ Wie Sie den Vor-Ort-Kauf Vermeiden & Die Schlange Überspringen:",
            "sol_desc": "<strong>Wenn Sie eine geführte Tour mit Girona Travels buchen, vermeiden Sie diesen Stress!</strong> Ihr zertifizierter Guide kommt frühmorgens am Schalter an, kauft Ihre Tickets und Ihre Versicherung. Bei Ihrer Ankunft gehen Sie direkt ohne Wartezeit hinein.",
            "sol_btn": "Geführte Tour Buchen &rarr;",
            "box1_title": "🎫 Eintrittspreise (Preise 2026)",
            "box1_item1": "<strong>Ausländische Touristen:</strong> ~90.000 COP ($22 USD)",
            "box1_item2": "<strong>Kolumbianische Staatsbürger:</strong> ~35.000 COP ($9 USD)",
            "box1_item3": "<strong>Obligatorische Tages-Krankenversicherung:</strong> ~6.000 COP/Tag ($1.50 USD)",
            "box2_title": "📄 Erforderliche Dokumente am Eingang",
            "box2_item1": "<strong>Originaler Physischer Reisepass</strong> oder kolumbianische Cédula",
            "box2_item2": "Bargeld (COP) oder Kreditkarte für Eintritt & Versicherung",
            "box2_item3": "Einwegplastik streng verboten (Öko-Richtlinie)"
        },
        "skip": {
            "tag": "🚀 Die Insider-Lösung",
            "title": "So Überspringen Sie Die 2-Stunden-Schlange",
            "desc": "Die Schlange am Eingang El Zaino in der Morgenhitze kann leicht <strong>1 bis 2+ Stunden</strong> dauern.",
            "box_title": "🔑 Der Vorteil Mit Girona Travels Guides:",
            "box_desc": "Obwohl Sie selbst keine Tickets online kaufen können, <strong>übernimmt Ihr Guide bei einer Buchung über Girona Travels</strong> den Ticketkauf frühmorgens für Sie.",
            "item1": "✅ Ihr Girona Travels Guide wartet morgens in der Schlange für Sie.",
            "item2": "✅ Bei Ihrer Ankunft gehen Sie ohne Wartezeit direkt hinein.",
            "item3": "✅ Erfahren Sie mehr über die Geschichte der Tayrona und wandern Sie sicher.",
            "btn": "🥾 Geführte Tour Buchen & Schlange Meiden &rarr;"
        },
        "tours": {
            "pkg2_desc": "Inklusive 1 Übernachtung nahe am Park in Villa María Tayrona / Casa Isabella, Fast-Track-Einlass, geführter Wanderung nach Arrecifes & Cabo San Juan, Gourmet-Abendessen im Kasankala Restaurant und Girona Travels Transfer."
        },
        "stays": {
            "villa_title": "🌿 Villa María Tayrona & Kasankala Restaurant",
            "villa_desc": "Villa María Tayrona ist eine Luxus-Dschungel-Ökolodge nahe dem Eingang El Zaino mit Öko-Luxuszimmern, Pool und Gourmet-Gastronomie im Kasankala Restaurant.",
            "villa_btn": "Zimmer auf ParqueTayrona.org Ansehen &rarr;"
        }
    }
}

def render_html(lang_code, data):
    js_path = "/app.js"
    css_path = "/style.css"
    hero_img = "/public/images/tayrona_hero.jpg"
    trek_img = "/public/images/tayrona_trek.jpg"

    lang_links = ""
    for code, ldata in languages.items():
        active_cls = ' class="active-lang"' if code == lang_code else ""
        href = "/" if ldata["dir"] == "" else f"/{ldata['dir']}/"
        lang_links += f'<li><a href="{href}"{active_cls}>{ldata["flag"]} {ldata["lang_name"]} ({code.upper()})</a></li>\n'

    html = f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['description']}">
  <meta name="keywords" content="Tayrona National Park, Tayrona guide, Kali Hotel, Villa María Tayrona, Girona Travel, Tayrona tickets, Parque Tayrona, Cabo San Juan, Santa Marta">
  <link rel="canonical" href="https://tayronaguide.com{data['img_prefix'] if data['dir'] != '' else '/'}">
  
  <!-- Favicon & Site Icons -->
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="96x96" href="/public/favicon-96x96.png">
  <link rel="icon" type="image/svg+xml" href="/public/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/public/apple-touch-icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://tayronaguide.com/">
  <meta property="og:title" content="{data['title']}">
  <meta property="og:description" content="{data['description']}">
  <meta property="og:image" content="https://tayronaguide.com/public/images/tayrona_hero.jpg">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Custom CSS -->
  <link rel="stylesheet" href="{css_path}">
  <link rel="stylesheet" href="/concierge-module.css?v=20260729_rework_photos">
</head>
<body>

  <!-- Announcement Bar -->
  <div class="announcement-bar">
    <span>{data['announcement']}</span>
  </div>

  <!-- Header / Navigation -->
  <header class="navbar">
    <div class="container nav-container">
      <a href="/" class="brand-logo">
        <span class="logo-icon">🌿</span>
        <span class="logo-text">Tayrona<strong>Guide</strong></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="#no-vat" class="nav-link">{data['nav']['no_vat']}</a>
        <a href="#concierge" class="nav-link highlight-link">{data['nav']['wizard']}</a>
        <a href="#ticket-truth" class="nav-link">{data['nav']['truth']}</a>
        <a href="#skip-queue" class="nav-link">{data['nav']['skip']}</a>
        <a href="#guided-tours" class="nav-link">{data['nav']['tours']}</a>
        <a href="#where-to-stay" class="nav-link">{data['nav']['stays']}</a>
        <a href="https://parquetayrona.org" target="_blank" class="nav-link">{data['nav']['guide']}</a>
        <a href="#faq" class="nav-link">{data['nav']['faq']}</a>
      </nav>

      <div class="nav-actions">
        <!-- Language Switcher Dropdown -->
        <div class="lang-dropdown">
          <button class="lang-btn">{data['flag']} {lang_code.upper()} ▾</button>
          <ul class="lang-menu">
            {lang_links}
          </ul>
        </div>

        <a href="https://parquetayrona.org" target="_blank" class="btn btn-primary btn-sm">
          {data['nav']['btn']}
        </a>
        <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-bg" style="background-image: url('{hero_img}');"></div>
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <div class="hero-badge">
        <span class="badge-dot"></span> {data['hero']['badge']}
      </div>
      <h1 class="hero-title">{data['hero']['title']}</h1>
      <p class="hero-subtitle">{data['hero']['subtitle']}</p>

      <div class="hero-cta-group">
        <a href="#concierge" class="btn btn-accent btn-lg glow-btn" style="font-size:1.25rem;padding:18px 36px;font-weight:800;border-radius:12px;box-shadow:0 10px 30px rgba(245,158,11,0.4);">
          {data['hero']['btn1']}
        </a>
      </div>

      <!-- Quick Trust Indicators -->
      <div class="hero-trust-grid">
        <div class="trust-item">
          <span class="trust-icon">🛡️</span>
          <div>
            <strong>{data['hero']['trust1_title']}</strong>
            <span>{data['hero']['trust1_sub']}</span>
          </div>
        </div>
        <div class="trust-item">
          <span class="trust-icon">⚡</span>
          <div>
            <strong>{data['hero']['trust2_title']}</strong>
            <span>{data['hero']['trust2_sub']}</span>
          </div>
        </div>
        <div class="trust-item">
          <span class="trust-icon">🌴</span>
          <div>
            <strong>{data['hero']['trust3_title']}</strong>
            <span>{data['hero']['trust3_sub']}</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 1: No VAT Campaign Banner -->
  <section class="vat-campaign-section" id="no-vat">
    <div class="container">
      <div class="vat-hero-banner">
        <div class="vat-badge-tag">
          <span>✨</span> {data['no_vat']['tag']}
        </div>
        <h2 class="vat-title">{data['no_vat']['title']}</h2>
        <p class="vat-subtitle">{data['no_vat']['subtitle']}</p>
      </div>

      <div class="vat-grid">
        <div class="vat-card">
          <span class="vat-card-icon">🇨🇴</span>
          <h3>{data['no_vat']['card1_title']}</h3>
          <p>{data['no_vat']['card1_desc']}</p>
          <span class="vat-highlight-pill">19% IVA Absorbed & Exempt</span>
        </div>

        <div class="vat-card">
          <span class="vat-card-icon">🌎</span>
          <h3>{data['no_vat']['card2_title']}</h3>
          <p>{data['no_vat']['card2_desc']}</p>
          <span class="vat-highlight-pill">Official 0% Tourist Rate</span>
        </div>

        <div class="vat-card">
          <span class="vat-card-icon">🏨</span>
          <h3>{data['no_vat']['card3_title']}</h3>
          <p>{data['no_vat']['card3_desc']}</p>
          <span class="vat-highlight-pill">City & Jungle Eco-Duo</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Concierge Request Tool -->
  <div id="concierge" class="concierge-section"></div>

  <!-- Section 4: Ticket Truth & Scam Warning -->
  <section class="section section-dark" id="ticket-truth">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag tag-warning">{data['truth']['tag']}</span>
        <h2 class="section-title">{data['truth']['title']}</h2>
        <p class="section-lead">{data['truth']['lead']}</p>
      </div>

      <div class="warning-card">
        <div class="warning-header">
          <span class="warning-icon">🛑</span>
          <div>
            <h3>{data['truth']['warn_title']}</h3>
            <p>{data['truth']['warn_desc']}</p>
          </div>
        </div>
        <div class="warning-body">
          <p>{data['truth']['warn_body']}</p>
          
          <!-- Guided Solution Banner -->
          <div class="guided-solution-banner">
            <div class="banner-icon">⚡</div>
            <div class="banner-text">
              <h4>{data['truth']['sol_title']}</h4>
              <p>{data['truth']['sol_desc']}</p>
              <a href="#concierge" class="btn btn-accent btn-sm margin-top-sm">{data['truth']['sol_btn']}</a>
            </div>
          </div>

          <div class="info-grid">
            <div class="info-box">
              <h4>{data['truth']['box1_title']}</h4>
              <ul>
                <li>{data['truth']['box1_item1']}</li>
                <li>{data['truth']['box1_item2']}</li>
                <li>{data['truth']['box1_item3']}</li>
              </ul>
            </div>
            <div class="info-box">
              <h4>{data['truth']['box2_title']}</h4>
              <ul>
                <li>{data['truth']['box2_item1']}</li>
                <li>{data['truth']['box2_item2']}</li>
                <li>{data['truth']['box2_item3']}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: VIP Skip-The-Queue -->
  <section class="section section-feature" id="skip-queue">
    <div class="container">
      <div class="feature-grid">
        <div class="feature-media">
          <img src="{trek_img}" alt="Certified local guide leading group in Tayrona National Park" class="feature-img">
          <div class="floating-badge">
            <span class="badge-icon">⚡</span>
            <div>
              <strong>Save 1 to 2 Hours</strong>
              <span>Skip the hot morning gate line</span>
            </div>
          </div>
        </div>

        <div class="feature-content">
          <span class="section-tag tag-success">{data['skip']['tag']}</span>
          <h2 class="feature-title">{data['skip']['title']}</h2>
          <p class="feature-desc">{data['skip']['desc']}</p>

          <div class="solution-box">
            <h3>{data['skip']['box_title']}</h3>
            <p>{data['skip']['box_desc']}</p>
            <ul class="checklist">
              <li>{data['skip']['item1']}</li>
              <li>{data['skip']['item2']}</li>
              <li>{data['skip']['item3']}</li>
            </ul>
          </div>

          <div class="feature-cta">
            <a href="#concierge" class="btn btn-accent btn-lg glow-btn">
              {data['skip']['btn']}
            </a>
            <span class="sub-text">Direct booking available at GironaTravels.com & ParqueTayrona.org</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: Guided Tours Showcase -->
  <section class="section" id="guided-tours">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag">🌿 Girona Travels Experiences</span>
        <h2 class="section-title">Explore Guided Tour Packages</h2>
        <p class="section-lead">Combine professional Girona Travels guides, seamless gate access, and comfortable lodging.</p>
      </div>

      <div class="tours-grid">
        <div class="tour-card">
          <div class="tour-badge">Most Popular</div>
          <h3 class="tour-title">Cabo San Juan Day Trek + Fast-Track Entry</h3>
          <p class="tour-desc">Full-day guided hike through jungle trails to Cabo San Juan beach. Includes early ticket queue handling by Girona Travels, bilingual guide, and fruit tasting.</p>
          <div class="tour-highlights">
            <span>⏱️ 8-9 Hours</span>
            <span>🥾 Moderate Trek</span>
            <span>⚡ Queue Fast-Track</span>
          </div>
          <div class="tour-footer">
            <a href="#concierge" class="btn btn-primary btn-block">Reserve via Concierge &rarr;</a>
          </div>
        </div>

        <div class="tour-card featured-card">
          <div class="tour-badge badge-accent">Best Value</div>
          <h3 class="tour-title">2-Day Tayrona Eco-Lodge & Trail Package</h3>
          <p class="tour-desc">{data['tours']['pkg2_desc']}</p>
          <div class="tour-highlights">
            <span>🌙 2 Days / 1 Night</span>
            <span>🏨 Lodging Included</span>
            <span>🍽️ Kasankala Dining</span>
          </div>
          <div class="tour-footer">
            <a href="#concierge" class="btn btn-accent btn-block">Book Stay & Tour Package &rarr;</a>
          </div>
        </div>

        <div class="tour-card">
          <div class="tour-badge">Cultural Trek</div>
          <h3 class="tour-title">Bunkuany Ruins & Kogui Indigenous Experience</h3>
          <p class="tour-desc">Private certified Girona Travels guide exploring ancient Bunkuany stone terraces, visiting the sacred Kogui village of Tayku, and mountain rivers.</p>
          <div class="tour-highlights">
            <span>🐒 Wildlife Focus</span>
            <span>🏛️ Cultural History</span>
            <span>👨‍👩‍👧 Private Group</span>
          </div>
          <div class="tour-footer">
            <a href="#concierge" class="btn btn-primary btn-block">Inquire Private Tour &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 7: Lodging Showcase -->
  <section class="section" id="where-to-stay">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag">🏨 Official Lodging Partner</span>
        <h2 class="section-title">Where to Stay: Kali Hotel & Villa María Tayrona</h2>
        <p class="section-lead">Enjoy city vibe at Kali Hotel Santa Marta & jungle eco-luxury at Villa María Tayrona with 0% VAT.</p>
      </div>

      <div class="lodging-grid">
        <div class="lodging-card">
          <div class="lodging-content">
            <h3>{data['stays']['villa_title']}</h3>
            <p>{data['stays']['villa_desc']}</p>
            <a href="#concierge" class="btn btn-outline btn-sm">Book via Concierge &rarr;</a>
          </div>
        </div>

        <div class="lodging-card">
          <div class="lodging-content">
            <h3>🏛️ Kali Hotel Santa Marta</h3>
            <p>Boutique hotel in the heart of Santa Marta historic center, featuring stylish rooms, rooftop pool, and fine dining.</p>
            <a href="#concierge" class="btn btn-outline btn-sm">Book via Concierge &rarr;</a>
          </div>
        </div>

        <div class="lodging-card">
          <div class="lodging-content">
            <h3>🌴 Villa María Tayrona Nature Sanctuary</h3>
            <p>Eco-luxury sanctuary right near Tayrona entrance, featuring jungle suites, pool, river views & Kasankala dining.</p>
            <a href="#concierge" class="btn btn-outline btn-sm">Book via Concierge &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8: FAQ Accordion -->
  <section class="section section-dark" id="faq">
    <div class="container max-w-4xl">
      <div class="section-header text-center">
        <span class="section-tag">❓ Frequently Asked Questions</span>
        <h2 class="section-title">Tayrona & Hotel FAQ</h2>
      </div>

      <div class="faq-accordion">
        <div class="faq-item">
          <button class="faq-question">
            Why do Colombians pay 0% VAT (IVA) on hotel stays with Kali Hotels & Villa María Tayrona?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Under Colombian law, foreign tourists are tax-exempt from 19% VAT on lodging. As part of our 2026 Hospitality Equity Campaign, Girona Travel, Kali Hotel & Villa María Tayrona absorb the tax for Colombian residents so EVERY guest enjoys 0% VAT rates!</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            How does the Concierge Request Tool work if my flight lands after 12:00 PM?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>If your flight arrives in Santa Marta after 12:00 PM, the wizard automatically places your 1st night at Kali Hotel in Santa Marta historic center. On Day 2 afternoon, private Girona Travel transport moves you to Villa María Tayrona near Tayrona, allowing you to trek Tayrona Park on Day 2 afternoon or Day 3 without rushing!</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            Can I buy Tayrona entrance tickets online before I travel?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>No. Official entrance passes cannot be reserved online in advance by individual tourists. However, when you book a guided tour with Girona Travels, your guide buys your entry passes early in the morning so you skip the line.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner Footer -->
  <section class="cta-banner">
    <div class="container text-center">
      <h2>Ready for an Unforgettable Tayrona & Santa Marta Experience?</h2>
      <p>Enjoy 0% VAT rates at Kali Hotel & Villa María Tayrona with Girona Travel private transport and certified guides.</p>
      <a href="#concierge" class="btn btn-accent btn-xl glow-btn">
        🚀 Launch Concierge Request Tool &rarr;
      </a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="/" class="brand-logo">
          <span class="logo-icon">🌿</span>
          <span class="logo-text">Tayrona<strong>Guide</strong></span>
        </a>
        <p class="footer-text">The official verified travel guide for Tayrona National Park & Santa Marta. Managed in partnership with Girona Travels, Kali Hotels & Villa María Tayrona.</p>
      </div>
      <div class="footer-col">
        <h4>Quick Navigation</h4>
        <ul>
          <li><a href="#no-vat">0% VAT Campaign</a></li>
          <li><a href="#packages">Bundled Packages</a></li>
          <li><a href="#concierge">Concierge Request Tool</a></li>
          <li><a href="#ticket-truth">Ticket Truth</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Official Partners</h4>
        <ul>
          <li><a href="https://gironatravels.com" target="_blank">Girona Travels (Official Operator)</a></li>
          <li><a href="https://kalihotels.com" target="_blank">Kali Hotels Collection</a></li>
          <li><a href="https://parquetayrona.org" target="_blank">ParqueTayrona.org</a></li>
          <li><a href="https://kasankala.com" target="_blank">Kasankala Restaurant</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 TayronaGuide.com. All rights reserved. Powered by Girona Travels & Kali Hotels.</p>
    </div>
  </footer>

  <script src="/concierge-module.js?v=20260729_rework_photos"></script>
  <script src="{js_path}"></script>
</body>
</html>"""
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = base_dir if data["dir"] == "" else os.path.join(base_dir, data["dir"])
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {lang_code.upper()} -> {file_path}")

for lang_code, data in languages.items():
    render_html(lang_code, data)

import shutil

def sync_to_dirs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for target in ["public", "dist"]:
        target_dir = os.path.join(base_dir, target)
        os.makedirs(target_dir, exist_ok=True)
        for f in ["index.html", "app.js", "style.css", "concierge-module.js", "concierge-module.css", "favicon.ico", "robots.txt", "sitemap.xml"]:
            src = os.path.join(base_dir, f)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(target_dir, f))
        
        # Copy images directory
        img_src = os.path.join(base_dir, "images")
        img_dest = os.path.join(target_dir, "images")
        if os.path.exists(img_src):
            shutil.copytree(img_src, img_dest, dirs_exist_ok=True)

        for lang in ["es", "it", "fr", "de"]:
            lang_src = os.path.join(base_dir, lang)
            lang_dest = os.path.join(target_dir, lang)
            if os.path.exists(lang_src):
                shutil.copytree(lang_src, lang_dest, dirs_exist_ok=True)

sync_to_dirs()
print("Synced build output across root, public/, and dist/ directories for Cloudflare Pages.")
