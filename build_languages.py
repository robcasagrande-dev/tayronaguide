import os

languages = {
    "en": {
        "dir": "",
        "img_prefix": "",
        "lang_name": "English",
        "flag": "🇬🇧",
        "title": "Tayrona National Park Guide 2026 | Official Ticket Info & Guided Tours",
        "description": "Official 2026 Tayrona National Park Travel Guide. Learn how entry passes work, avoid online ticket scams, skip the 2-hour gate queue with certified local guides, and book stays near park entrances.",
        "announcement": "⚠️ <strong>TICKET ALERT:</strong> Park entry passes CANNOT be reserved online in advance. <a href=\"#ticket-truth\">Read how to skip the 2-hour entrance line &rarr;</a>",
        "nav": {
            "truth": "Ticket Truth & Info",
            "skip": "⚡ Skip the Queue",
            "tours": "Guided Tours",
            "trails": "Trails & Beaches",
            "stays": "Lodging & Stays",
            "faq": "FAQ",
            "btn": "Book Stay & Tours &rarr;"
        },
        "hero": {
            "badge": "Verified 2026 Park Travel Guide",
            "title": "Experience <span>Tayrona National Park</span> Without the Stress",
            "subtitle": "Everything you need to know about park entry fees, avoiding ticket scams, navigating jungle trails, and skipping the 2-hour entrance line with a certified local guide.",
            "btn1": "⚡ How to Skip the Entrance Line",
            "btn2": "🏨 Reserve Lodging & Tours at ParqueTayrona.org",
            "trust1_title": "100% Scam-Free Info",
            "trust1_sub": "Verified park entry rules",
            "trust2_title": "Queue Fast-Track",
            "trust2_sub": "Guides handle morning tickets",
            "trust3_title": "Official Lodging Partner",
            "trust3_sub": "Kasankala & Kali Hotels"
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
        }
    },
    "es": {
        "dir": "es",
        "img_prefix": "../",
        "lang_name": "Español",
        "flag": "🇪🇸",
        "title": "Guía Parque Nacional Tayrona 2026 | Entradas y Tours Guiados",
        "description": "Guía oficial 2026 del Parque Nacional Tayrona. Aprende cómo funcionan las entradas, evita estafas en línea y sáltate la fila de 2 horas con guías locales certificados.",
        "announcement": "⚠️ <strong>ALERTA DE ENTRADAS:</strong> Las entradas al parque NO se pueden reservar en línea. <a href=\"#ticket-truth\">Lee cómo saltarte la fila de 2 horas &rarr;</a>",
        "nav": {
            "truth": "Verdad sobre Entradas",
            "skip": "⚡ Saltarse la Fila",
            "tours": "Tours Guiados",
            "trails": "Senderos y Playas",
            "stays": "Alojamientos",
            "faq": "Preguntas Frecuentes",
            "btn": "Reservar Hospedaje y Tours &rarr;"
        },
        "hero": {
            "badge": "Guía de Viaje Verificada 2026",
            "title": "Disfruta el <span>Parque Nacional Tayrona</span> Sin Estrés",
            "subtitle": "Todo lo que necesitas saber sobre las tarifas de entrada, evitar estafas en línea, recorrer senderos y saltarte la fila de 2 horas con un guía local certificado.",
            "btn1": "⚡ Cómo Saltarte la Fila de Entrada",
            "btn2": "🏨 Reservar Hospedaje y Tours en ParqueTayrona.org",
            "trust1_title": "Información 100% Verificada",
            "trust1_sub": "Sin estafas en entradas",
            "trust2_title": "Entrada Preferencial",
            "trust2_sub": "Tu guía gestiona tus tickets",
            "trust3_title": "Aliado Oficial de Hospedaje",
            "trust3_sub": "Kasankala y Kali Hotels"
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
        }
    },
    "it": {
        "dir": "it",
        "img_prefix": "../",
        "lang_name": "Italiano",
        "flag": "🇮🇹",
        "title": "Guida Parco Nazionale Tayrona 2026 | Biglietti e Tour Guidati",
        "description": "Guida ufficiale 2026 del Parco Nazionale Tayrona. Scopri come funzionano i biglietti d'ingresso, evita le truffe online e salta la coda di 2 ore con guide locali certificate.",
        "announcement": "⚠️ <strong>ALLERTA BIGLIETTI:</strong> I biglietti NON possono essere prenotati online. <a href=\"#ticket-truth\">Scopri come saltare la coda di 2 ore &rarr;</a>",
        "nav": {
            "truth": "Verità sui Biglietti",
            "skip": "⚡ Saltare la Coda",
            "tours": "Tour Guidati",
            "trails": "Sentieri e Spiagge",
            "stays": "Alloggi",
            "faq": "FAQ",
            "btn": "Prenota Soggiorno e Tour &rarr;"
        },
        "hero": {
            "badge": "Guida di Viaggio Verificata 2026",
            "title": "Vivi il <span>Parco Nazionale Tayrona</span> Senza Stress",
            "subtitle": "Tutto ciò che devi sapere sulle tariffe d'ingresso, come evitare le truffe online e saltare la coda di 2 ore con una guida locale certificata.",
            "btn1": "⚡ Come Saltare la Coda all'Ingresso",
            "btn2": "🏨 Prenota Alloggio e Tour su ParqueTayrona.org",
            "trust1_title": "Info 100% Senza Truffe",
            "trust1_sub": "Regole ufficiali modificate",
            "trust2_title": "Accesso Fast-Track",
            "trust2_sub": "La guida acquista i biglietti all'alba",
            "trust3_title": "Partner Ufficiale Alloggi",
            "trust3_sub": "Kasankala & Kali Hotels"
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
            "sol_btn": "Prenota il Tuo Tour Guidato &rarr;",
            "box1_title": "🎫 Tariffe d'Ingresso (Tariffe 2026)",
            "box1_item1": "<strong>Turisti Stranieri:</strong> ~90.000 COP ($22 USD)",
            "box1_item2": "<strong>Cittadini Colombiani:</strong> ~35.000 COP ($9 USD)",
            "box1_item3": "<strong>Assicurazione Medica Giornaliera:</strong> ~6.000 COP/giorno ($1.50 USD)",
            "box2_title": "📄 Documenti Obbligatori all'Ingresso",
            "box2_item1": "<strong>Passaporto Fisico Originale</strong> o Carta d'Identità",
            "box2_item2": "Contanti (COP) o carta di credito per biglietti e assicurazione",
            "box2_item3": "Vietata la plastica monouso (Politica Ecologica)"
        },
        "skip": {
            "tag": "🚀 La Soluzione Esclusiva",
            "title": "Come Saltare la Coda di 2 Ore all'Ingresso",
            "desc": "La coda all'ingresso di El Zaino sotto il sole del mattino può richiedere da <strong>1 a oltre 2 ore</strong> mentre centinaia di viaggiatori attendono di pagare e registrare i documenti.",
            "box_title": "🔑 Il Vantaggio dei Tour Guidati Girona Travels:",
            "box_desc": "Anche se non puoi acquistare i biglietti online da solo, <strong>prenotando un tour guidato con Girona Travels</strong> la tua guida arriva presto alla biglietteria e fa la fila per te.",
            "item1": "✅ La tua guida Girona Travels fa la fila mattutina per te.",
            "item2": "✅ Al tuo arrivo l'ingresso è immediato: passi direttamente senza fare coda.",
            "item3": "✅ Scopri la storia indigena Tayrona, avvista la fauna selvatica ed esplora in sicurezza.",
            "btn": "🥾 Prenota Tour Guidato e Salta la Coda &rarr;"
        }
    },
    "fr": {
        "dir": "fr",
        "img_prefix": "../",
        "lang_name": "Français",
        "flag": "🇫🇷",
        "title": "Guide Parc National Tayrona 2026 | Infos Billets & Visites Guidées",
        "description": "Guide de voyage officiel 2026 du parc national Tayrona. Découvrez le fonctionnement des billets, évitez les arnaques en ligne et évitez la file d'attente de 2 heures grâce à des guides locaux certifiés.",
        "announcement": "⚠️ <strong>ALERTE BILLETS :</strong> Les billets NE PEUVENT PAS être réservés en ligne. <a href=\"#ticket-truth\">Découvrez comment éviter 2h de queue &rarr;</a>",
        "nav": {
            "truth": "Vérité sur les Billets",
            "skip": "⚡ Éviter la File",
            "tours": "Visites Guidées",
            "trails": "Sentiers & Plages",
            "stays": "Hébergements",
            "faq": "FAQ",
            "btn": "Réserver Séjour & Tours &rarr;"
        },
        "hero": {
            "badge": "Guide de Voyage Vérifié 2026",
            "title": "Découvrez le <span>Parc National Tayrona</span> Sans Stress",
            "subtitle": "Tout ce que vous devez savoir sur les tarifs d'entrée, éviter les arnaques en ligne et sauter la file d'attente de 2 heures avec un guide local certifié.",
            "btn1": "⚡ Comment Éviter la File d'Attente",
            "btn2": "🏨 Réserver Hébergements & Tours sur ParqueTayrona.org",
            "trust1_title": "Infos 100% Sans Arnaque",
            "trust1_sub": "Règles d'entrée vérifiées",
            "trust2_title": "Accès Fast-Track",
            "trust2_sub": "Votre guide gère vos billets à l'aube",
            "trust3_title": "Partenaire Officiel d'Hébergement",
            "trust3_sub": "Kasankala & Kali Hotels"
        },
        "truth": {
            "tag": "⚠️ Informations Essentielles d'Entrée",
            "title": "La Vérité sur l'Achat des Billets pour Tayrona",
            "lead": "Ne tombez pas dans les arnaques sur Internet. Comprenez le fonctionnement officiel.",
            "warn_title": "Avertissement : Les Billets Officiels NE PEUVENT PAS Être Réservés en Ligne à l'Avance",
            "warn_desc": "NE FAITES PAS confiance aux sites tiers affirmant vendre des billets officiels en ligne.",
            "warn_body": "Selon la réglementation des <em>Parques Nacionales Naturales de Colombia</em>, les billets officiels sont <strong>payés exclusivement en personne aux guichets du parc</strong> (El Zaino ou Palangana) en espèces ou carte à votre arrivée.",
            "sol_title": "⚡ Comment Éviter l'Achat en Personne & Sauter la File :",
            "sol_desc": "<strong>En réservant une visite guidée avec Girona Travels, vous évitez toutes ces démarches !</strong> Votre guide local certifié arrive très tôt le matin au guichet, gère la file d'attente et achète vos billets et assurance obligatoire pour vous. À votre arrivée, vous entrez directement dans le parc sans faire la queue.",
            "sol_btn": "Réserver Votre Visite Guidée &rarr;",
            "box1_title": "🎫 Tarifs d'Entrée (Tarifs 2026)",
            "box1_item1": "<strong>Touristes Étrangers :</strong> ~90 000 COP ($22 USD)",
            "box1_item2": "<strong>Citoyens Colombiens :</strong> ~35 000 COP ($9 USD)",
            "box1_item3": "<strong>Assurance Médicale Obligatoire :</strong> ~6 000 COP/jour ($1.50 USD)",
            "box2_title": "📄 Documents Obligatoires au Guichet",
            "box2_item1": "<strong>Passeport Physique Original</strong> ou Carte d'Identité",
            "box2_item2": "Espèces (COP) ou carte bancaire pour l'entrée et l'assurance",
            "box2_item3": "Plastiques à usage unique interdits (Politique Écologique)"
        },
        "skip": {
            "tag": "🚀 La Solution Privilégiée",
            "title": "Comment Éviter la File d'Attente de 2 Heures",
            "desc": "La file d'attente à l'entrée d'El Zaino sous la chaleur du matin peut facilement durer <strong>1 à 2 heures et plus</strong> pendant que des centaines de visiteurs attendent.",
            "box_title": "🔑 L'Avantage de la Visite Guidée Girona Travels :",
            "box_desc": "Même si vous ne pouvez pas acheter vos billets en ligne vous-même, <strong>en réservant une visite guidée avec Girona Travels</strong>, votre guide arrive tôt le matin et s'occupe de la file d'attente pour vous.",
            "item1": "✅ Votre guide Girona Travels fait la queue matinale pour vous.",
            "item2": "✅ À votre arrivée, l'accès est immédiat : vous entrez directement.",
            "item3": "✅ Découvrez l'histoire indigène Tayrona, observez la faune et randonnez en sécurité.",
            "btn": "🥾 Réserver une Visite Guidée & Éviter la File &rarr;"
        }
    },
    "de": {
        "dir": "de",
        "img_prefix": "../",
        "lang_name": "Deutsch",
        "flag": "🇩🇪",
        "title": "Tayrona Nationalpark Reiseführer 2026 | Ticket-Info & Geführte Touren",
        "description": "Offizieller Reiseführer 2026 für den Tayrona-Nationalpark. Erfahren Sie, wie Eintrittskarten funktionieren, vermeiden Sie Online-Abzocke und umgehen Sie die 2-Stunden-Warteschlange mit zertifizierten lokalen Guides.",
        "announcement": "⚠️ <strong>TICKET-HINWEIS:</strong> Eintrittskarten können NICHT online gebucht werden. <a href=\"#ticket-truth\">So umgehen Sie die 2-Stunden-Warteschlange &rarr;</a>",
        "nav": {
            "truth": "Wahrheit über Tickets",
            "skip": "⚡ Warteschlange Umgehen",
            "tours": "Geführte Touren",
            "trails": "Wanderwege & Strände",
            "stays": "Unterkünfte",
            "faq": "FAQ",
            "btn": "Unterkunft & Touren Buchen &rarr;"
        },
        "hero": {
            "badge": "Geprüfter Reiseführer 2026",
            "title": "Erleben Sie den <span>Tayrona Nationalpark</span> Ohne Stress",
            "subtitle": "Alles, was Sie über Eintrittspreise, Online-Abzocke, Dschungelpfade und das Umgehen der 2-Stunden-Warteschlange mit einem zertifizierten lokalen Guide wissen müssen.",
            "btn1": "⚡ So Umgehen Sie die Warteschlange",
            "btn2": "🏨 Unterkunft & Touren auf ParqueTayrona.org Buchen",
            "trust1_title": "100% Geprüfte Info",
            "trust1_sub": "Keine Ticket-Fallen",
            "trust2_title": "Schnellzugang",
            "trust2_sub": "Guide kauft Tickets am frühen Morgen",
            "trust3_title": "Offizieller Unterkunftspartner",
            "trust3_sub": "Kasankala & Kali Hotels"
        },
        "truth": {
            "tag": "⚠️ Wichtiges Wissen für den Einlass",
            "title": "Die Wahrheit über den Kauf von Tayrona-Tickets",
            "lead": "Fallen Sie nicht auf Online-Fallen herein. Verstehen Sie, wie die offiziellen Tickets funktionieren.",
            "warn_title": "Warnung: Offizielle Park-Tickets können NICHT im Voraus online gebucht werden",
            "warn_desc": "Vertrauen Sie KEINEN Drittanbieter-Websites, die behaupten, offizielle Eintrittskarten im Internet zu verkaufen.",
            "warn_body": "Gemäß den Bestimmungen von <em>Parques Nacionales Naturales de Colombia</em> werden offizielle Eintrittskarten <strong>ausschließlich persönlich an den Parktoren</strong> (El Zaino oder Palangana) bar oder per Kreditkarte bezahlt.",
            "sol_title": "⚡ So vermeiden Sie den Ticketkauf vor Ort & umgehen die Schlange:",
            "sol_desc": "<strong>Wenn Sie eine geführte Tour mit Girona Travels buchen, ersparen Sie sich diesen Aufwand komplett!</strong> Ihr zertifizierter lokaler Guide kommt früh am Morgen zum Ticket-Schalter, kauft Ihre Eintrittskarten und die obligatorische Versicherung für Sie. Bei Ihrer Ankunft gelangen Sie ohne Wartezeit direkt in den Park.",
            "sol_btn": "Geführte Tour Buchen &rarr;",
            "box1_title": "🎫 Eintrittspreise (Tarife 2026)",
            "box1_item1": "<strong>Ausländische Touristen:</strong> ~90.000 COP ($22 USD)",
            "box1_item2": "<strong>Kolumbianische Staatsbürger:</strong> ~35.000 COP ($9 USD)",
            "box1_item3": "<strong>Obligatorische Tagesversicherung:</strong> ~6.000 COP/Tag ($1.50 USD)",
            "box2_title": "📄 Erforderliche Dokumente am Eingang",
            "box2_item1": "<strong>Originaler Reisepass</strong> oder Personalausweis",
            "box2_item2": "Bargeld (COP) oder Kreditkarte für Eintritt & Versicherung",
            "box2_item3": "Einwegplastik streng verboten (Öko-Richtlinie)"
        },
        "skip": {
            "tag": "🚀 Die Insider-Lösung",
            "title": "Wie Sie die 2-Stunden-Warteschlange Umgehen",
            "desc": "Die Warteschlange am Eingang El Zaino in der Morgenhitze kann leicht <strong>1 bis über 2 Stunden</strong> dauern, während hunderte Besucher warten.",
            "box_title": "🔑 Der Vorteil Geführter Touren mit Girona Travels:",
            "box_desc": "Obwohl Sie Tickets nicht selbst online kaufen können, <strong>übernimmt Ihr Guide bei einer Buchung mit Girona Travels</strong> den Ticketkauf am frühen Morgen für Sie.",
            "item1": "✅ Ihr Girona Travels Guide steht morgens früh in der Warteschlange für Sie.",
            "item2": "✅ Bei Ihrer Ankunft gehen Sie ohne Wartezeit direkt durch den Eingang.",
            "item3": "✅ Erfahren Sie mehr über die indigene Geschichte der Tayrona und wandern Sie sicher.",
            "btn": "🥾 Geführte Tour Buchen & Schlange Umgehen &rarr;"
        }
    }
}

def render_html(lang_code, data):
    p = data["img_prefix"]
    
    lang_links = ""
    for code, info in languages.items():
        active = "class=\"active-lang\"" if code == lang_code else ""
        target_path = "/" if code == "en" else f"/{code}/"
        lang_links += f"<li><a href=\"{target_path}\" {active}>{info['flag']} {info['lang_name']} ({code.upper()})</a></li>\n"

    html = f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['description']}">
  <meta name="keywords" content="Tayrona National Park, Tayrona guide, Tayrona tickets, Tayrona entrance fee, Parque Tayrona, Cabo San Juan, El Zaino entrance, Tayrona guided tours">
  <link rel="canonical" href="https://tayronaguide.com/{data['dir']}">
  
  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://tayronaguide.com/{data['dir']}">
  <meta property="og:title" content="{data['title']}">
  <meta property="og:description" content="{data['description']}">
  <meta property="og:image" content="https://tayronaguide.com/images/tayrona_hero.jpg">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Custom CSS -->
  <link rel="stylesheet" href="{p}style.css">
</head>
<body>

  <!-- Announcement Bar -->
  <div class="announcement-bar">
    <span>{data['announcement']}</span>
  </div>

  <!-- Header / Navigation -->
  <header class="navbar">
    <div class="container nav-container">
      <a href="{p}index.html" class="brand-logo">
        <span class="logo-icon">🌿</span>
        <span class="logo-text">Tayrona<strong>Guide</strong></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="#ticket-truth" class="nav-link">{data['nav']['truth']}</a>
        <a href="#skip-queue" class="nav-link highlight-link">{data['nav']['skip']}</a>
        <a href="#guided-tours" class="nav-link">{data['nav']['tours']}</a>
        <a href="#trails" class="nav-link">{data['nav']['trails']}</a>
        <a href="#where-to-stay" class="nav-link">{data['nav']['stays']}</a>
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
    <div class="hero-bg" style="background-image: url('{p}images/tayrona_hero.jpg');"></div>
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <div class="hero-badge">
        <span class="badge-dot"></span> {data['hero']['badge']}
      </div>
      <h1 class="hero-title">{data['hero']['title']}</h1>
      <p class="hero-subtitle">{data['hero']['subtitle']}</p>

      <div class="hero-cta-group">
        <a href="#skip-queue" class="btn btn-accent btn-lg">
          {data['hero']['btn1']}
        </a>
        <a href="https://parquetayrona.org" target="_blank" class="btn btn-outline btn-lg">
          {data['hero']['btn2']}
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

  <!-- Section 1: The Ticket Truth & Scam Warning -->
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
          
          <!-- Highlighted Solution Banner -->
          <div class="guided-solution-banner">
            <div class="banner-icon">⚡</div>
            <div class="banner-text">
              <h4>{data['truth']['sol_title']}</h4>
              <p>{data['truth']['sol_desc']}</p>
              <a href="#guided-tours" class="btn btn-accent btn-sm margin-top-sm">{data['truth']['sol_btn']}</a>
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

  <!-- Section 2: The VIP Skip-The-Queue Secret -->
  <section class="section section-feature" id="skip-queue">
    <div class="container">
      <div class="feature-grid">
        <div class="feature-media">
          <img src="{p}images/tayrona_guide_trek.jpg" alt="Certified local guide in Tayrona National Park" class="feature-img">
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
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-accent btn-lg glow-btn">
              {data['skip']['btn']}
            </a>
            <span class="sub-text">Direct booking available at ParqueTayrona.org & GironaTravels.com</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Guided Tours Showcase -->
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
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-primary btn-block">Reserve Tour &rarr;</a>
          </div>
        </div>

        <div class="tour-card featured-card">
          <div class="tour-badge badge-accent">Best Value</div>
          <h3 class="tour-title">2-Day Tayrona Eco-Lodge & Trail Package</h3>
          <p class="tour-desc">Includes 1 night stay near park gate at Kasankala / Casa Isabella, morning queue fast-track, guided trek to Arrecifes & Cabo San Juan, and Girona Travels private transport.</p>
          <div class="tour-highlights">
            <span>🌙 2 Days / 1 Night</span>
            <span>🏨 Lodging Included</span>
            <span>🚌 Private Transport</span>
          </div>
          <div class="tour-footer">
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-accent btn-block">Book Stay & Tour Package &rarr;</a>
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
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-primary btn-block">Inquire Private Tour &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Trail & Beach Guide -->
  <section class="section section-dark" id="trails">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag">🗺️ Interactive Trail Guide</span>
        <h2 class="section-title">Top Destinations in Tayrona National Park</h2>
        <p class="section-lead">Plan your route from the main El Zaino entrance to iconic beaches.</p>
      </div>

      <div class="trail-grid">
        <div class="trail-card">
          <div class="trail-header">
            <h3>🏝️ Cabo San Juan del Guía</h3>
            <span class="trail-time">2.5 hr hike from entrance</span>
          </div>
          <p>The iconic twin-cove beach featuring the famous hammock hut on the granite hill. Safe for swimming, calm turquoise waters.</p>
        </div>

        <div class="trail-card">
          <div class="trail-header">
            <h3>🌊 Arrecifes Beach</h3>
            <span class="trail-time">1.5 hr hike from entrance</span>
          </div>
          <p>Dramatic coastline with massive granite boulders. Strong dangerous currents—swimming is prohibited, but scenery is breathtaking.</p>
        </div>

        <div class="trail-card">
          <div class="trail-header">
            <h3>🌴 La Piscina</h3>
            <span class="trail-time">2 hr hike from entrance</span>
          </div>
          <p>A natural reef barrier creates a tranquil, pool-like bay perfect for swimming and snorkeling with colorful tropical fish.</p>
        </div>

        <div class="trail-card">
          <div class="trail-header">
            <h3>🐒 Bunkuany & Tayku Sacred Trails</h3>
            <span class="trail-time">Full day mountain trek</span>
          </div>
          <p>Ancient stone terraces and sacred indigenous Kogui settlements hidden in the high jungle of the Sierra Nevada.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Where to Stay (Lodging Showcase) -->
  <section class="section" id="where-to-stay">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag">🏨 Official Lodging Partner</span>
        <h2 class="section-title">Where to Stay Near Tayrona Park Entrances</h2>
        <p class="section-lead">Stay minutes from the park gate to enjoy early morning access and relaxing luxury.</p>
      </div>

      <div class="lodging-grid">
        <div class="lodging-card">
          <div class="lodging-content">
            <h3>🌿 Kasankala Luxury Eco-Lodge</h3>
            <p>Immersed in lush nature right near the El Zaino entrance. Features eco-luxury rooms, pool, and direct Girona Travels tour departure point.</p>
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-outline btn-sm">View Rooms at ParqueTayrona.org &rarr;</a>
          </div>
        </div>

        <div class="lodging-card">
          <div class="lodging-content">
            <h3>🏛️ Casa Isabella & Casa Leda</h3>
            <p>Boutique heritage lodging combining historic charm, swimming pools, and personalized tour concierge services.</p>
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-outline btn-sm">View Availability &rarr;</a>
          </div>
        </div>

        <div class="lodging-card">
          <div class="lodging-content">
            <h3>🏨 Kali Hotels Collection</h3>
            <p>Premium hotel accommodations offering full Girona Travels transport packages, park tour booking, and gourmet dining.</p>
            <a href="https://parquetayrona.org" target="_blank" class="btn btn-outline btn-sm">Explore Kali Hotels &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: FAQ Accordion -->
  <section class="section section-dark" id="faq">
    <div class="container max-w-4xl">
      <div class="section-header text-center">
        <span class="section-tag">❓ Frequently Asked Questions</span>
        <h2 class="section-title">Tayrona Park Entry FAQ</h2>
      </div>

      <div class="faq-accordion">
        <div class="faq-item">
          <button class="faq-question">
            Can I buy Tayrona entrance tickets online before I travel?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>No. Official entrance passes cannot be reserved online in advance by tourists. Passes must be purchased in person at the park gates (El Zaino or Palangana) using cash (COP) or credit card.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            How does booking a guided tour with Girona Travels help me skip the ticket line?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>When you book a certified guided tour with Girona Travels, your guide arrives at the ticket booth early in the morning before the park opens to purchase entry passes on your behalf. When you arrive, you walk past the main queue directly into the park!</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            Is medical insurance required to enter Tayrona National Park?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Yes. Daily medical insurance is mandatory for all visitors and costs approximately 6,000 COP (~$1.50 USD) per day, paid at the gate alongside entry fees.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            Are plastics allowed in Tayrona Park?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Single-use plastics (water bottles, plastic bags, plastic utensils) are strictly prohibited inside the park to protect the ecosystem. Bring a reusable water bottle.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner Footer -->
  <section class="cta-banner">
    <div class="container text-center">
      <h2>Ready to Explore Tayrona National Park Stress-Free?</h2>
      <p>Reserve your certified Girona Travels local guide, private transport, and hotel stay near the park entrance today.</p>
      <a href="https://parquetayrona.org" target="_blank" class="btn btn-accent btn-xl glow-btn">
        🚀 Book Tours & Stays at ParqueTayrona.org &rarr;
      </a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="{p}index.html" class="brand-logo">
          <span class="logo-icon">🌿</span>
          <span class="logo-text">Tayrona<strong>Guide</strong></span>
        </a>
        <p class="footer-text">The official verified travel guide for Tayrona National Park, Colombia. Managed in partnership with Girona Travels & ParqueTayrona.org.</p>
      </div>
      <div class="footer-col">
        <h4>Quick Navigation</h4>
        <ul>
          <li><a href="#ticket-truth">Ticket Truth</a></li>
          <li><a href="#skip-queue">Skip the Queue</a></li>
          <li><a href="#guided-tours">Guided Tours</a></li>
          <li><a href="#trails">Trail Maps</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Official Partner Sites</h4>
        <ul>
          <li><a href="https://gironatravels.com" target="_blank">Girona Travels (Official Operator)</a></li>
          <li><a href="https://parquetayrona.org" target="_blank">ParqueTayrona.org (Booking Hub)</a></li>
          <li><a href="https://kasankala.com" target="_blank">Kasankala Eco-Lodge</a></li>
          <li><a href="https://kalihotels.com" target="_blank">Kali Hotels Collection</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 TayronaGuide.com. All rights reserved. Powered by Girona Travels & ParqueTayrona.org.</p>
    </div>
  </footer>

  <script src="{p}app.js"></script>
</body>
</html>"""
    
    out_dir = "/home/robi/Projects/tayronaguide" if data["dir"] == "" else f"/home/robi/Projects/tayronaguide/{data['dir']}"
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {lang_code.upper()} -> {file_path}")

for lang_code, data in languages.items():
    render_html(lang_code, data)
