import os
import json

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
            "truth": "Park Passes",
            "no_vat": "0% Tax Benefit",
            "badge_new": "NEW",
            "guide": "Tayrona Guide",
            "wizard": "Trip Builder",
            "skip": "Fast-Track",
            "tours": "Girona Tours",
            "trails": "Trails",
            "stays": "Luxury Stays",
            "faq": "FAQ",
            "btn": "Book Stay & Tours &rarr;"
        },
        "hero": {
            "badge": "Verified 2026 Park Travel Guide & Hospitality Hub",
            "title": "Experience <span>Santa Marta & Tayrona</span> Without the Stress",
            "subtitle": "Discover curated packages combining Kali Hotel Santa Marta, Villa María Tayrona, Girona Travel transfers, and an exclusive concierge trip builder with 0% hotel VAT for EVERYONE.",
            "btn1": "⚡ Build Your Trip (0% VAT)",
            "btn2": "🏨 View Bundled Packages",
            "trust1_title": "TayronaGuide Exclusive",
            "trust1_sub": "Multi-hotel discount & 0% VAT",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Queue skip at park gate",
            "trust3_title": "Kali Hotels",
            "trust3_sub": "Special rates & 0% VAT"
        },
        "no_vat": {
            "tag": "✨ 2026 Hospitality Equity Campaign",
            "title": "Colombians Should Not Pay VAT at Hotels <span>As Foreigners Do</span>",
            "subtitle": "In Colombia, international tourists are exempt from 19% hotel VAT (IVA). We believe Colombian travelers deserve the exact same tax-free experience! At Kali Hotel Santa Marta & Villa María Tayrona, we offer a 0% VAT rate for ALL guests.",
            "card1_title": "TayronaGuide Exclusive",
            "card1_desc": "Book through TayronaGuide to access our multi-hotel exclusive discount. We absorb the hotel tax, so Colombians and international travelers enjoy the exact same 0% VAT pricing.",
            "card2_title": "0% VAT For Everyone",
            "card2_desc": "Whether you are a Colombian national or an international traveler, enjoy 100% tax-exempt & transparent pricing. No surprise fees and clear upfront rate guarantees.",
            "card3_title": "Kali Hotels",
            "card3_desc": "Enjoy our special TayronaGuide discount at Kali Hotels. Experience premium stays in Santa Marta with an automatic 0% VAT tax benefit included."
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
        },
        "footer": {
            "desc": "The official verified travel guide for Tayrona National Park & Santa Marta. Managed in partnership with Girona Travels, Kali Hotels & Villa María Tayrona.",
            "nav_title": "Quick Navigation",
            "nav_packages": "Bundled Packages",
            "nav_concierge": "Concierge Request Tool",
            "nav_truth": "Ticket Truth",
            "partners_title": "Official Partners",
            "partner_operator": "Official Operator",
            "partner_restaurant": "Kasankala Restaurant",
            "cert_title": "Certifications",
            "cert_inclusion": "Seal of Inclusion",
            "cert_transparencia": "Seal of Transparency",
            "cert_gaula_alt": "Official GAULA Campaign",
            "cert_gaula_text": "We support the official anti-kidnapping and anti-extortion campaign. Hotline: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. All rights reserved. Powered by Girona Travels & Kali Hotels."
        },
        "faq": {
            "tag": "❓ Frequently Asked Questions",
            "title": "Tayrona & Hotel FAQ",
            "q1": "Why do Colombians pay 0% VAT (IVA) on hotel stays with Kali Hotels & Villa María Tayrona?",
            "a1": "Under Colombian law, foreign tourists are tax-exempt from 19% VAT on lodging. As part of our 2026 Hospitality Equity Campaign, Girona Travel, Kali Hotel & Villa María Tayrona absorb the tax for Colombian residents so EVERY guest enjoys 0% VAT rates!",
            "q2": "How does the Trip Builder tool work?",
            "a2": "The Trip Builder allows you to combine stays at Kali Hotels in Santa Marta and Villa María Tayrona, along with private transfers and official guided tours. We customize the itinerary to fit your schedule.",
            "q3": "Can I buy Tayrona entrance tickets online before I travel?",
            "a3": "No. Official entrance passes cannot be reserved online in advance by individual tourists. However, when you book a guided tour with Girona Travels, your guide buys your entry passes early in the morning so you skip the line."
        },
        "cta": {
            "title": "Ready for an Unforgettable Tayrona & Santa Marta Experience?",
            "desc": "Enjoy 0% VAT rates at Kali Hotel & Villa María Tayrona with Girona Travel private transport and certified guides.",
            "btn": "🚀 Launch Trip Builder &rarr;"
        },
        "tours_page": {
            "reserve": "Reserve via Trip Builder &rarr;",
            "home": "Home",
            "title": "All Girona Travels Tours",
            "lead": "Explore our full catalog of guided experiences, eco-treks, and cultural adventures."
        },
        "skip_extra": {
            "save_time": "Save 1 to 2 Hours",
            "skip_line": "Skip the hot morning gate line"
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
            "truth": "Entradas Parque",
            "no_vat": "Beneficio 0% IVA",
            "badge_new": "NUEVO",
            "guide": "Guía Tayrona",
            "wizard": "Diseñador de Viaje",
            "skip": "Fast-Track",
            "tours": "Tours Girona",
            "trails": "Senderos",
            "stays": "Hospedajes de Lujo",
            "faq": "FAQ",
            "btn": "Reservar Hospedaje y Tours &rarr;"
        },
        "hero": {
            "badge": "Guía de Viaje Verificada 2026 y Centro Turístico",
            "title": "Disfruta <span>Santa Marta y Tayrona</span> Sin Estrés",
            "subtitle": "Descubre paquetes exclusivos combinando Kali Hotel Santa Marta, Villa María Tayrona, transportes Girona Travel y un diseñador elástico con tarifa SIN IVA para TODOS.",
            "btn1": "⚡ Diseña tu Viaje (0% IVA)",
            "btn2": "🏨 Ver Paquetes Combinados",
            "trust1_title": "Exclusivo TayronaGuide",
            "trust1_sub": "Descuento multi-hotel y 0% IVA",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Ingreso preferencial en taquilla",
            "trust3_title": "Kali Hotels",
            "trust3_sub": "Tarifas especiales y 0% IVA"
        },
        "no_vat": {
            "tag": "✨ Campaña de Equidad Hotelera 2026",
            "title": "Los Colombianos No Deberían Pagar IVA <span>Como los Extranjeros</span>",
            "subtitle": "En Colombia, los turistas internacionales están exentos del 19% de IVA hotelero. ¡Creemos que los viajeros colombianos merecen el mismo beneficio! En Kali Hotel Santa Marta y Villa María Tayrona ofrecemos tarifa 0% IVA para TODOS.",
            "card1_title": "Exclusivo TayronaGuide",
            "card1_desc": "Reserva a través de TayronaGuide para acceder a nuestro descuento exclusivo en múltiples hoteles. Absorbemos el impuesto hotelero para que colombianos y extranjeros disfruten del mismo precio sin IVA.",
            "card2_title": "0% IVA Para Todos",
            "card2_desc": "Ya sea nacional colombiano o viajero internacional, disfruta de precios transparentes y 100% libres de impuestos. Sin tarifas sorpresa ni cobros ocultos garantizados.",
            "card3_title": "Kali Hotels",
            "card3_desc": "Disfruta de nuestro descuento especial TayronaGuide en Kali Hotels. Vive estadías premium en Santa Marta con el beneficio automático del 0% de IVA incluido."
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
        },
        "footer": {
            "desc": "La guía de viaje oficial verificada para el Parque Nacional Tayrona y Santa Marta. Gestionada en asociación con Girona Travels, Kali Hotels y Villa María Tayrona.",
            "nav_title": "Navegación Rápida",
            "nav_packages": "Paquetes Combinados",
            "nav_concierge": "Diseñador de Viaje",
            "nav_truth": "Verdad sobre Entradas",
            "partners_title": "Socios Oficiales",
            "partner_operator": "Operador Oficial",
            "partner_restaurant": "Restaurante Kasankala",
            "cert_title": "Certificaciones",
            "cert_inclusion": "Sello de Inclusión",
            "cert_transparencia": "Sello de Transparencia",
            "cert_gaula_alt": "Campaña Oficial GAULA",
            "cert_gaula_text": "Apoyamos la campaña oficial antisecuestro y antiextorsión. Línea: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. Todos los derechos reservados. Desarrollado por Girona Travels y Kali Hotels."
        },
        "faq": {
            "tag": "❓ Preguntas Frecuentes",
            "title": "Preguntas Frecuentes - Tayrona y Hoteles",
            "q1": "¿Por qué los colombianos pagan 0% de IVA en estadías con Kali Hotels y Villa María Tayrona?",
            "a1": "Según la ley colombiana, los turistas extranjeros están exentos del IVA del 19% en alojamiento. Como parte de nuestra Campaña de Equidad Hotelera 2026, Girona Travel, Kali Hotel y Villa María Tayrona absorben el impuesto para los residentes colombianos, ¡así TODOS disfrutan de 0% de IVA!",
            "q2": "¿Cómo funciona la herramienta Diseñador de Viaje?",
            "a2": "El Diseñador de Viaje te permite combinar estadías en Kali Hotels en Santa Marta y Villa María Tayrona, junto con traslados privados y tours guiados oficiales. Personalizamos el itinerario para adaptarnos a tus horarios.",
            "q3": "¿Puedo comprar las entradas al Tayrona por internet antes de viajar?",
            "a3": "No. Las entradas oficiales no pueden ser reservadas por internet con antelación por turistas individuales. Sin embargo, al reservar un tour guiado con Girona Travels, tu guía compra las entradas temprano en la mañana para que evites la fila."
        },
        "cta": {
            "title": "¿Listo para una Experiencia Inolvidable en Santa Marta y Tayrona?",
            "desc": "Disfruta de 0% de IVA en Kali Hotel y Villa María Tayrona con transporte privado de Girona Travel y guías certificados.",
            "btn": "🚀 Iniciar Diseñador de Viaje &rarr;"
        },
        "tours_page": {
            "reserve": "Reservar vía Diseñador de Viaje &rarr;",
            "home": "Inicio",
            "title": "Todos los Tours de Girona Travels",
            "lead": "Explora nuestro catálogo completo de experiencias guiadas, caminatas ecológicas y aventuras culturales."
        },
        "skip_extra": {
            "save_time": "Ahorra 1 a 2 Horas",
            "skip_line": "Evita la fila bajo el sol"
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
            "truth": "Pass Parco",
            "no_vat": "Beneficio 0% IVA",
            "badge_new": "NUOVO",
            "guide": "Guida Tayrona",
            "wizard": "Pianificatore Viaggio",
            "skip": "Ingresso Rapido",
            "tours": "Tour Girona",
            "trails": "Sentieri",
            "stays": "Soggiorni di Lusso",
            "faq": "FAQ",
            "btn": "Prenota Soggiorno e Tour &rarr;"
        },
        "hero": {
            "badge": "Guida di Viaggio Verificata 2026",
            "title": "Vivi <span>Santa Marta & Tayrona</span> Senza Stress",
            "subtitle": "Scopri i pacchetti che combinano Kali Hotel Santa Marta, Villa María Tayrona, trasferimenti Girona Travel e un servizio concierge con prezzo SENZA IVA per TUTTI.",
            "btn1": "⚡ Configura il Tuo Viaggio (0% IVA)",
            "btn2": "🏨 Vedi i Pacchetti",
            "trust1_title": "Esclusiva TayronaGuide",
            "trust1_sub": "Sconto multi-hotel e 0% IVA",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Salta la coda all'ingresso",
            "trust3_title": "Kali Hotels",
            "trust3_sub": "Tariffe speciali e 0% IVA"
        },
        "no_vat": {
            "tag": "✨ Campagna Equità Alberghiera 2026",
            "title": "I Colombiani Non Dovrebbero Pagare l'IVA <span>Come gli Stranieri</span>",
            "subtitle": "In Colombia, i turisti internazionali sono esenti dall'IVA del 19% sugli hotel. Riteniamo che anche i viaggiatori colombiani debbano godere dello stesso beneficio! Presso Kali Hotel Santa Marta e Villa María Tayrona offriamo la tariffa 0% IVA per TUTTI.",
            "card1_title": "Esclusiva TayronaGuide",
            "card1_desc": "Prenota tramite TayronaGuide per accedere al nostro sconto esclusivo multi-hotel. Assorbiamo la tassa di soggiorno così colombiani e viaggiatori internazionali godono dello stesso prezzo 0% IVA.",
            "card2_title": "0% IVA Per Tutti",
            "card2_desc": "Che tu sia cittadino colombiano o viaggiatore internazionale, goditi un prezzo trasparente e 100% esente da tasse. Nessuna commissione a sorpresa e tariffe garantite.",
            "card3_title": "Kali Hotels",
            "card3_desc": "Approfitta del nostro speciale sconto TayronaGuide nei Kali Hotels. Vivi soggiorni premium a Santa Marta con il beneficio automatico dello 0% di IVA incluso."
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
        },
        "footer": {
            "desc": "La guida di viaggio ufficiale verificata per il Parco Nazionale Tayrona e Santa Marta. Gestita in collaborazione con Girona Travels, Kali Hotels e Villa María Tayrona.",
            "nav_title": "Navigazione Rapida",
            "nav_packages": "Pacchetti Inclusivi",
            "nav_concierge": "Pianificatore di Viaggio",
            "nav_truth": "Verità sui Biglietti",
            "partners_title": "Partner Ufficiali",
            "partner_operator": "Operatore Ufficiale",
            "partner_restaurant": "Ristorante Kasankala",
            "cert_title": "Certificazioni",
            "cert_inclusion": "Sigillo di Inclusione",
            "cert_transparencia": "Sigillo di Trasparenza",
            "cert_gaula_alt": "Campagna Ufficiale GAULA",
            "cert_gaula_text": "Sosteniamo la campagna ufficiale contro i sequestri e le estorsioni. Linea: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. Tutti i diritti riservati. Sviluppato da Girona Travels & Kali Hotels."
        },
        "faq": {
            "tag": "❓ Domande Frequenti",
            "title": "FAQ - Tayrona e Hotel",
            "q1": "Perché i colombiani pagano lo 0% di IVA sui soggiorni presso Kali Hotels e Villa María Tayrona?",
            "a1": "Secondo la legge colombiana, i turisti stranieri sono esenti dall'IVA del 19% sugli alloggi. Come parte della nostra Campagna di Equità Alberghiera 2026, Girona Travel, Kali Hotel e Villa María Tayrona assorbono la tassa per i residenti colombiani, così TUTTI gli ospiti godono dello 0% di IVA!",
            "q2": "Come funziona lo strumento Pianificatore di Viaggio?",
            "a2": "Il Pianificatore di Viaggio ti permette di combinare soggiorni presso Kali Hotels a Santa Marta e Villa María Tayrona, insieme a trasferimenti privati e tour guidati ufficiali. Personalizziamo l'itinerario in base ai tuoi orari.",
            "q3": "Posso comprare i biglietti d'ingresso per Tayrona online prima di viaggiare?",
            "a3": "No. I pass d'ingresso ufficiali non possono essere prenotati online in anticipo da singoli turisti. Tuttavia, se prenoti un tour guidato con Girona Travels, la tua guida acquista i biglietti la mattina presto per farti saltare la fila."
        },
        "cta": {
            "title": "Pronto per un'Esperienza Indimenticabile a Santa Marta e Tayrona?",
            "desc": "Approfitta dello 0% di IVA presso Kali Hotel e Villa María Tayrona con trasporto privato Girona Travel e guide certificate.",
            "btn": "🚀 Avvia Pianificatore di Viaggio &rarr;"
        },
        "tours_page": {
            "reserve": "Prenota via Pianificatore di Viaggio &rarr;",
            "home": "Home",
            "title": "Tutti i Tour Girona Travels",
            "lead": "Esplora il nostro catalogo completo di esperienze guidate, eco-trekking e avventure culturali."
        },
        "skip_extra": {
            "save_time": "Risparmia da 1 a 2 Ore",
            "skip_line": "Salta la coda sotto il sole"
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
            "truth": "Passes du Parc",
            "no_vat": "Avantage 0% TVA",
            "badge_new": "NOUVEAU",
            "guide": "Guide Tayrona",
            "wizard": "Planificateur de Voyage",
            "skip": "Fast-Track",
            "tours": "Tours Girona",
            "trails": "Sentiers",
            "stays": "Séjours de Luxe",
            "faq": "FAQ",
            "btn": "Réserver Séjour et Tours &rarr;"
        },
        "hero": {
            "badge": "Guide Touristique Vérifié 2026",
            "title": "Découvrez <span>Santa Marta & Tayrona</span> Sans Stress",
            "subtitle": "Combinez Kali Hotel Santa Marta, Villa María Tayrona, les transports Girona Travel et un planificateur élastique avec 0% de TVA pour TOUS.",
            "btn1": "⚡ Créez votre Voyage (0% TVA)",
            "btn2": "🏨 Voir les Forfaits",
            "trust1_title": "Exclusivité TayronaGuide",
            "trust1_sub": "Remise multi-hôtels et 0% TVA",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Entrée prioritaire au parc",
            "trust3_title": "Kali Hotels",
            "trust3_sub": "Tarifs spéciaux et 0% TVA"
        },
        "no_vat": {
            "tag": "✨ Campagne Équité Hôtelière 2026",
            "title": "Les Colombiens Ne Devraient Pas Payer la TVA <span>Comme les Étrangers</span>",
            "subtitle": "En Colombie, les touristes internationaux sont exonérés de 19% de TVA sur les hôtels. Nous pensons que les voyageurs colombiens méritent le même privilège! À Kali Hotel Santa Marta et Villa María Tayrona, nous offrons un tarif 0% TVA pour TOUS.",
            "card1_title": "Exclusivité TayronaGuide",
            "card1_desc": "Réservez via TayronaGuide pour accéder à notre remise exclusive multi-hôtels. Nous absorbons la taxe hôtelière pour que les Colombiens et les voyageurs internationaux bénéficient du même prix à 0% de TVA.",
            "card2_title": "0% TVA Pour Tous",
            "card2_desc": "Que vous soyez de nationalité colombienne ou un voyageur international, profitez de prix transparents et 100% exonérés de taxes. Pas de frais surprises et des tarifs garantis.",
            "card3_title": "Kali Hotels",
            "card3_desc": "Profitez de notre remise spéciale TayronaGuide dans les Kali Hotels. Vivez des séjours premium à Santa Marta avec l'avantage automatique de 0% de TVA inclus."
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
        },
        "footer": {
            "desc": "Le guide de voyage officiel vérifié pour le parc national Tayrona et Santa Marta. Géré en partenariat avec Girona Travels, Kali Hotels et Villa María Tayrona.",
            "nav_title": "Navigation Rapide",
            "nav_packages": "Forfaits Combinés",
            "nav_concierge": "Outil de Planification",
            "nav_truth": "Vérité sur les Billets",
            "partners_title": "Partenaires Officiels",
            "partner_operator": "Opérateur Officiel",
            "partner_restaurant": "Restaurant Kasankala",
            "cert_title": "Certifications",
            "cert_inclusion": "Sceau d'Inclusion",
            "cert_transparencia": "Sceau de Transparence",
            "cert_gaula_alt": "Campagne Officielle GAULA",
            "cert_gaula_text": "Nous soutenons la campagne officielle contre les enlèvements et les extorsions. Ligne: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. Tous droits réservés. Propulsé par Girona Travels & Kali Hotels."
        },
        "faq": {
            "tag": "❓ Foire Aux Questions",
            "title": "FAQ Tayrona et Hôtels",
            "q1": "Pourquoi les Colombiens paient-ils 0 % de TVA (IVA) sur les séjours à Kali Hotels et Villa María Tayrona ?",
            "a1": "Selon la loi colombienne, les touristes étrangers sont exonérés de la TVA de 19 % sur l'hébergement. Dans le cadre de notre campagne d'équité hôtelière 2026, Girona Travel, Kali Hotel et Villa María Tayrona absorbent la taxe pour les résidents colombiens, de sorte que TOUS les clients bénéficient de 0 % de TVA !",
            "q2": "Comment fonctionne l'outil de Planification de Voyage ?",
            "a2": "L'outil de Planification vous permet de combiner des séjours dans les Kali Hotels à Santa Marta et la Villa María Tayrona, avec des transferts privés et des visites guidées officielles. Nous personnalisons l'itinéraire pour l'adapter à votre emploi du temps.",
            "q3": "Puis-je acheter des billets d'entrée pour Tayrona en ligne avant de voyager ?",
            "a3": "Non. Les billets d'entrée officiels ne peuvent pas être réservés en ligne à l'avance par des touristes individuels. Cependant, lorsque vous réservez une visite guidée avec Girona Travels, votre guide achète vos billets tôt le matin pour que vous évitiez la file d'attente."
        },
        "cta": {
            "title": "Prêt pour une expérience inoubliable à Tayrona et Santa Marta ?",
            "desc": "Profitez de 0 % de TVA à Kali Hotel et Villa María Tayrona avec le transport privé Girona Travel et des guides certifiés.",
            "btn": "🚀 Lancer l'Outil de Planification &rarr;"
        },
        "tours_page": {
            "reserve": "Réserver via l'Outil de Planification &rarr;",
            "home": "Accueil",
            "title": "Tous les Circuits Girona Travels",
            "lead": "Explorez notre catalogue complet d'expériences guidées, de randonnées écologiques et d'aventures culturelles."
        },
        "skip_extra": {
            "save_time": "Gagnez 1 à 2 heures",
            "skip_line": "Évitez la file d'attente matinale"
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
            "truth": "Park-Pässe",
            "no_vat": "0% MwSt. Vorteil",
            "badge_new": "NEU",
            "guide": "Tayrona Führer",
            "wizard": "Reise-Builder",
            "skip": "Fast-Track",
            "tours": "Girona Touren",
            "trails": "Wanderwege",
            "stays": "Luxus-Unterkünfte",
            "faq": "FAQ",
            "btn": "Unterkunft & Touren Buchen &rarr;"
        },
        "hero": {
            "badge": "Verifizierter Reiseführer 2026",
            "title": "Erleben Sie <span>Santa Marta & Tayrona</span> Ohne Stress",
            "subtitle": "Kombinieren Sie Kali Hotel Santa Marta, Villa María Tayrona, Girona Travel Transfers und einen elastischen Reiseplaner mit 0% MwSt. für ALLE.",
            "btn1": "⚡ Reise Planen (0% MwSt.)",
            "btn2": "🏨 Kombi-Pakete Ansehen",
            "trust1_title": "Exklusiv TayronaGuide",
            "trust1_sub": "Multi-Hotel Rabatt & 0% MwSt.",
            "trust2_title": "Girona Travel Fast-Track",
            "trust2_sub": "Einlass ohne Wartezeit",
            "trust3_title": "Kali Hotels",
            "trust3_sub": "Sondertarife & 0% MwSt."
        },
        "no_vat": {
            "tag": "✨ Hotel-Gerechtigkeits-Kampagne 2026",
            "title": "Kolumbianer Sollten Keine MwSt. Zahlen <span>Wie Ausländische Touristen</span>",
            "subtitle": "In Kolumbien sind ausländische Touristen von 19% Hotel-MwSt. befreit. Wir glauben, kolumbianische Reisende verdienen das gleiche Recht! Im Kali Hotel Santa Marta & Villa María Tayrona bieten wir 0% MwSt. für ALLE Gäste.",
            "card1_title": "Exklusiv TayronaGuide",
            "card1_desc": "Buchen Sie über TayronaGuide, um unseren exklusiven Multi-Hotel-Rabatt zu nutzen. Wir übernehmen die Hotelsteuer, damit Kolumbianer und internationale Reisende den gleichen 0% MwSt.-Preis genießen.",
            "card2_title": "0% MwSt. Für Alle",
            "card2_desc": "Ob kolumbianischer Staatsbürger oder internationaler Reisender, genießen Sie 100% steuerfreie & transparente Preise. Keine Überraschungsgebühren und klare Preisgarantien.",
            "card3_title": "Kali Hotels",
            "card3_desc": "Genießen Sie unseren speziellen TayronaGuide-Rabatt in den Kali Hotels. Erleben Sie Premium-Aufenthalte in Santa Marta mit dem automatischen 0% MwSt.-Vorteil inklusive."
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
        },
        "footer": {
            "desc": "Der offizielle verifizierte Reiseführer für den Tayrona-Nationalpark und Santa Marta. Verwaltet in Partnerschaft mit Girona Travels, Kali Hotels und Villa María Tayrona.",
            "nav_title": "Schnellnavigation",
            "nav_packages": "Kombi-Pakete",
            "nav_concierge": "Reiseplaner",
            "nav_truth": "Ticket-Wahrheit",
            "partners_title": "Offizielle Partner",
            "partner_operator": "Offizieller Veranstalter",
            "partner_restaurant": "Kasankala Restaurant",
            "cert_title": "Zertifizierungen",
            "cert_inclusion": "Siegel der Inklusion",
            "cert_transparencia": "Siegel der Transparenz",
            "cert_gaula_alt": "Offizielle GAULA-Kampagne",
            "cert_gaula_text": "Wir unterstützen die offizielle Anti-Entführungs- und Anti-Erpressungs-Kampagne. Hotline: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. Alle Rechte vorbehalten. Unterstützt von Girona Travels & Kali Hotels."
        },
        "faq": {
            "tag": "❓ Häufig Gestellte Fragen",
            "title": "Tayrona & Hotel FAQ",
            "q1": "Warum zahlen Kolumbianer 0% Mehrwertsteuer (IVA) auf Hotelübernachtungen bei Kali Hotels & Villa María Tayrona?",
            "a1": "Nach kolumbianischem Recht sind ausländische Touristen von der 19%igen Mehrwertsteuer auf Beherbergung befreit. Im Rahmen unserer Kampagne für Hotelgerechtigkeit 2026 übernehmen Girona Travel, Kali Hotel und Villa María Tayrona die Steuer für kolumbianische Staatsbürger, sodass JEDER Gast 0% Mehrwertsteuer zahlt!",
            "q2": "Wie funktioniert der Reiseplaner?",
            "a2": "Mit dem Reiseplaner können Sie Aufenthalte im Kali Hotel in Santa Marta und in der Villa María Tayrona mit privaten Transfers und offiziellen geführten Touren kombinieren. Wir passen die Reiseroute an Ihren Zeitplan an.",
            "q3": "Kann ich Eintrittskarten für Tayrona vor meiner Reise online kaufen?",
            "a3": "Nein. Offizielle Eintrittskarten können von individuellen Touristen nicht im Voraus online reserviert werden. Wenn Sie jedoch eine geführte Tour mit Girona Travels buchen, kauft Ihr Reiseleiter Ihre Eintrittskarten früh morgens, damit Sie die Warteschlange umgehen können."
        },
        "cta": {
            "title": "Bereit für ein unvergessliches Erlebnis in Tayrona & Santa Marta?",
            "desc": "Profitieren Sie von 0% MwSt. im Kali Hotel & Villa María Tayrona mit privatem Transport von Girona Travel und zertifizierten Reiseleitern.",
            "btn": "🚀 Reiseplaner starten &rarr;"
        },
        "tours_page": {
            "reserve": "Über Reiseplaner reservieren &rarr;",
            "home": "Startseite",
            "title": "Alle Girona Travels Touren",
            "lead": "Entdecken Sie unseren vollständigen Katalog an geführten Erlebnissen, Öko-Treks und kulturellen Abenteuern."
        },
        "skip_extra": {
            "save_time": "Sparen Sie 1 bis 2 Stunden",
            "skip_line": "Vermeiden Sie die morgendliche Warteschlange"
        }
    }
}

TB_STRINGS = {
    "es": { "step1_title": "Planea tu Viaje", "step1_subtitle": "Para formular un mejor plan para tu grupo, por favor dinos cómo y cuándo llegarás.", "step2_title": "Elige tus Tours", "step2_subtitle": "Selecciona cómo te gustaría pasar tu tiempo, ya sea con un tour guiado o tiempo libre para explorar por tu cuenta.", "step3_title": "Tu Solicitud al Conserje", "step3_subtitle": "Revisa tu información y envíala a nuestro conserje. Tu conserje dedicado preparará un itinerario personalizado día a día con todos los precios de los tours adjuntos. Aplica 0% de IVA exclusivamente en la tarifa de alojamiento, la cual se cotiza a nuestra tarifa especial de socios multihotel para asegurarnos de que recibas el mejor precio posible.", "transport_label": "¿Cómo llegas a Santa Marta?", "flight": "Vuelo Comercial", "flight_sub": "Llegada al Aeropuerto Simón Bolívar", "car": "Vehículo Privado", "car_sub": "Transporte por tierra / overland", "time_label": "¿A qué hora llega tu vuelo?", "time_before_6": "Madrugada", "time_before_6_sub": "Medianoche – 6:00 AM", "time_6_12": "Mañana", "time_6_12_sub": "6:00 AM – Mediodía", "time_12_18": "Tarde", "time_12_18_sub": "Mediodía – 6:00 PM", "time_after_18": "Noche", "time_after_18_sub": "6:00 PM – Medianoche", "adults_label": "Adultos", "kids_label": "Niños (<2 años)", "btn_next": "Siguiente", "btn_back": "Atrás", "btn_send": "Enviar por WhatsApp", "resume_transport": "Transporte", "resume_time": "Llegada", "resume_guests": "Huéspedes", "resume_tours": "Tours Seleccionados", "name_label": "Nombre completo", "email_label": "Correo electrónico", "arrival_date_label": "Fecha de llegada", "departure_date_label": "Fecha de salida", "resume_arrival_date": "Llegada", "resume_departure_date": "Salida" },
    "en": { "step1_title": "Plan Your Trip", "step1_subtitle": "To formulate a better plan for your group, please tell us how and when you will arrive.", "step2_title": "Choose Your Tours", "step2_subtitle": "Select how you would like to spend your time, whether with a guided tour or spending free time exploring on your own.", "step3_title": "Your Concierge Request", "step3_subtitle": "Review your information and send it to our concierge. Your dedicated concierge will prepare a personalized day-by-day itinerary with all tour prices attached. 0% VAT applies exclusively to the accommodation rate, which is quoted at our exclusive multi-hotel partner tariff to ensure you receive the best possible rate.", "transport_label": "How are you arriving in Santa Marta?", "flight": "Commercial Flight", "flight_sub": "Arrival via Simón Bolívar Airport", "car": "Private Vehicle / Overland", "car_sub": "Self-drive or arranged ground transfer", "time_label": "What time does your flight arrive?", "time_before_6": "Early Morning", "time_before_6_sub": "Midnight – 6:00 AM", "time_6_12": "Morning Arrival", "time_6_12_sub": "6:00 AM – Noon", "time_12_18": "Afternoon Arrival", "time_12_18_sub": "Noon – 6:00 PM", "time_after_18": "Evening Arrival", "time_after_18_sub": "6:00 PM – Midnight", "adults_label": "Adults", "kids_label": "Kids (<2 years)", "btn_next": "Next", "btn_back": "Back", "btn_send": "Send via WhatsApp", "resume_transport": "Transport", "resume_time": "Arrival Time", "resume_guests": "Guests", "resume_tours": "Selected Tours", "name_label": "Full Name", "email_label": "Email Address", "arrival_date_label": "Arrival Date", "departure_date_label": "Departure Date", "resume_arrival_date": "Arrival", "resume_departure_date": "Departure" },
    "it": { "step1_title": "Pianifica il tuo Viaggio", "step1_subtitle": "Per formulare un piano migliore per il tuo gruppo, ti preghiamo di dirci come e quando arriverai.", "step2_title": "Scegli i tuoi Tour", "step2_subtitle": "Seleziona come vorresti trascorrere il tuo tempo, che sia con un tour guidato o del tempo libero per esplorare da solo.", "step3_title": "La Tua Richiesta al Concierge", "step3_subtitle": "Rivedi le tue informazioni e inviale al nostro concierge. Il tuo concierge dedicato preparerà un itinerario personalizzato giorno per giorno con tutti i prezzi dei tour allegati. Lo 0% di IVA si applica esclusivamente alla tariffa di alloggio, che è quotata alla nostra esclusiva tariffa partner multi-hotel per assicurarti di ricevere il miglior prezzo possibile.", "transport_label": "Come arrivi a Santa Marta?", "flight": "Volo Commerciale", "flight_sub": "Arrivo all'Aeroporto Simón Bolívar", "car": "Veicolo Privato / Overland", "car_sub": "Guida autonoma o transfer su strada", "time_label": "A che ora arriva il tuo volo?", "time_before_6": "Primo Mattino", "time_before_6_sub": "Mezzanotte – 6:00", "time_6_12": "Mattina", "time_6_12_sub": "6:00 – Mezzogiorno", "time_12_18": "Pomeriggio", "time_12_18_sub": "Mezzogiorno – 18:00", "time_after_18": "Sera", "time_after_18_sub": "18:00 – Mezzanotte", "adults_label": "Adulti", "kids_label": "Bambini (<2 anni)", "btn_next": "Avanti", "btn_back": "Indietro", "btn_send": "Invia via WhatsApp", "resume_transport": "Trasporto", "resume_time": "Arrivo", "resume_guests": "Ospiti", "resume_tours": "Tour Selezionati", "name_label": "Nome e cognome", "email_label": "Indirizzo Email", "arrival_date_label": "Data di arrivo", "departure_date_label": "Data di partenza", "resume_arrival_date": "Arrivo", "resume_departure_date": "Partenza" },
    "fr": { "step1_title": "Planifiez votre Voyage", "step1_subtitle": "Pour formuler un meilleur plan pour votre groupe, veuillez nous indiquer comment et quand vous arriverez.", "step2_title": "Choisissez vos Visites", "step2_subtitle": "Sélectionnez comment vous souhaitez passer votre temps, que ce soit avec une visite guidée ou du temps libre pour explorer par vous-même.", "step3_title": "Votre Demande Concierge", "step3_subtitle": "Passez en revue vos informations et envoyez-les à notre concierge. Votre concierge dédié préparera un itinéraire personnalisé jour par jour avec tous les prix des visites ci-joints. La TVA à 0 % s'applique exclusivement au tarif d'hébergement, qui est proposé à notre tarif partenaire exclusif multi-hôtel pour vous assurer de recevoir le meilleur prix possible.", "transport_label": "Comment arrivez-vous à Santa Marta ?", "flight": "Vol Commercial", "flight_sub": "Arrivée à l'Aéroport Simón Bolívar", "car": "Véhicule Privé / Overland", "car_sub": "Conduite autonome ou transfert terrestre", "time_label": "À quelle heure arrive votre vol ?", "time_before_6": "Petit Matin", "time_before_6_sub": "Minuit – 6h00", "time_6_12": "Matinée", "time_6_12_sub": "6h00 – Midi", "time_12_18": "Après-midi", "time_12_18_sub": "Midi – 18h00", "time_after_18": "Soirée", "time_after_18_sub": "18h00 – Minuit", "adults_label": "Adultes", "kids_label": "Enfants (<2 ans)", "btn_next": "Suivant", "btn_back": "Retour", "btn_send": "Envoyer via WhatsApp", "resume_transport": "Transport", "resume_time": "Arrivée", "resume_guests": "Invités", "resume_tours": "Visites Sélectionnées", "name_label": "Nom complet", "email_label": "Adresse Email", "arrival_date_label": "Date d'arrivée", "departure_date_label": "Date de départ", "resume_arrival_date": "Arrivée", "resume_departure_date": "Départ" },
    "de": { "step1_title": "Planen Sie Ihre Reise", "step1_subtitle": "Um einen besseren Plan für Ihre Gruppe zu erstellen, teilen Sie uns bitte mit, wie und wann Sie ankommen.", "step2_title": "Wählen Sie Ihre Touren", "step2_subtitle": "Wählen Sie, wie Sie Ihre Zeit verbringen möchten, sei es mit einer geführten Tour oder mit Freizeit für eigene Erkundungen.", "step3_title": "Ihre Concierge-Anfrage", "step3_subtitle": "Überprüfen Sie Ihre Informationen und senden Sie sie an unseren Concierge. Ihr engagierter Concierge bereitet einen personalisierten Reiseplan für jeden Tag mit allen beigefügten Tourpreisen vor. 0 % MwSt. gelten ausschließlich für den Übernachtungspreis, der zu unserem exklusiven Multi-Hotel-Partnertarif angeboten wird, um sicherzustellen, dass Sie den bestmöglichen Preis erhalten.", "transport_label": "Wie kommen Sie in Santa Marta an?", "flight": "Linienflug", "flight_sub": "Ankunft am Flughafen Simón Bolívar", "car": "Privatfahrzeug / Overland", "car_sub": "Eigenanreise oder Bodentransfer", "time_label": "Wann kommt Ihr Flug an?", "time_before_6": "Früher Morgen", "time_before_6_sub": "Mitternacht – 6:00 Uhr", "time_6_12": "Vormittag", "time_6_12_sub": "6:00 – 12:00 Uhr", "time_12_18": "Nachmittag", "time_12_18_sub": "12:00 – 18:00 Uhr", "time_after_18": "Abend", "time_after_18_sub": "18:00 – Mitternacht", "adults_label": "Erwachsene", "kids_label": "Kinder (<2 Jahre)", "btn_next": "Weiter", "btn_back": "Zurück", "btn_send": "Über WhatsApp senden", "resume_transport": "Transport", "resume_time": "Ankunft", "resume_guests": "Gäste", "resume_tours": "Ausgewählte Touren", "name_label": "Vollständiger Name", "email_label": "E-Mail-Adresse", "arrival_date_label": "Ankunftsdatum", "departure_date_label": "Abreisedatum", "resume_arrival_date": "Ankunft", "resume_departure_date": "Abreise" }
}

def render_html(lang_code, data):
    js_path = "/app.js"
    css_path = "/style.css"
    hero_img = f"{data['img_prefix']}images/tayrona_hero.jpg"
    trek_img = f"{data['img_prefix']}images/tayrona_guide_trek.jpg"

    lang_links = ""
    for code, ldata in languages.items():
        active_cls = ' class="active-lang"' if code == lang_code else ""
        href = "/" if ldata["dir"] == "" else f"/{ldata['dir']}/"
        lang_links += f'<li><a href="{href}"{active_cls}>{ldata["lang_name"]} ({code.upper()})</a></li>\n'

    
    # Load tours from JSON
    with open("tours_girona_travels.json", "r", encoding="utf-8") as tf:
        tours_data = json.load(tf)
    
    all_tours = [t for t in tours_data if not t.get("id", "").startswith("free-time-")]
    
    valid_tours = [t for t in all_tours if not t.get("isFreeTime", False)]
    
    target_tour_ids = ["cabo-san-juan-tayrona", "ruinas-bunkuany", "tour-del-cacao"]
    top_tours = [t for t in valid_tours if t["id"] in target_tour_ids]
    top_tours.sort(key=lambda x: target_tour_ids.index(x["id"]))
    other_tours = [t for t in valid_tours if t["id"] not in target_tour_ids]
    
    selected_tours = top_tours + other_tours

    dynamic_tours_html = ""
    for idx, t in enumerate(selected_tours):
        # Fallback to English if the current language is not available in the JSON
        lang_key = lang_code if lang_code in t["nombre"] else "en"
        
        badges_list = t.get("badges", {}).get(lang_key, t.get("badges", {}).get("en", [])) if isinstance(t.get("badges"), dict) else t.get("badges", [])
        if t.get("badge"):
            b_val = t["badge"].get(lang_key, t["badge"].get("en", "")) if isinstance(t["badge"], dict) else t["badge"]
            b_class = t.get("badge_class", "")
            badges_list = [{"label": b_val, "class": b_class}]
            
        r_val = t.get("ribbon", {}).get(lang_key, t.get("ribbon", {}).get("en", "")) if isinstance(t.get("ribbon"), dict) else t.get("ribbon", "")
        ribbon_html = f"""<div class=\"tour-ribbon\">{r_val}</div>""" if r_val else ""
        
        badge_html = "<div class=\"tour-img-badges\">"
        for b in badges_list:
            badge_html += f"""<span class="tour-img-badge {b.get('class', '')}">{b.get('label', '')}</span>"""
        badge_html += "</div>"

        highlights_html = ""
        h_list = t.get("highlights", {}).get(lang_key, t.get("highlights", {}).get("en", [])) if isinstance(t.get("highlights"), dict) else t.get("highlights", [])
        for h in h_list:
            highlights_html += f"<span>{h}</span>\n                "
            
        hidden_class = " hidden-tour" if idx >= 3 else ""

        read_more_text = {"en": "Read more", "es": "Leer más", "it": "Leggi di più", "fr": "Lire la suite", "de": "Weiterlesen"}.get(lang_code, "Read more")
        short_desc = t.get("descripcion_corta", t.get("descripcion", {})).get(lang_key, "")
        long_desc = t.get("descripcion", {}).get(lang_key, "")

        dynamic_tours_html += f"""
        <div class="tour-card reveal{hidden_class}">
          <div class="tour-image-wrapper">
            {ribbon_html}
            {badge_html}
            <img src="{t.get("image", "")}" alt="{t["nombre"][lang_key]}" />
          </div>
          <div class="tour-card-body">
            <div>
              <h3 class="tour-title">{t["nombre"][lang_key]}</h3>
              <p class="tour-desc" id="short-desc-{idx}">{short_desc}</p>
              <div id="long-desc-{idx}" style="display:none; margin-bottom: 15px;">
                <p class="tour-desc" style="white-space: pre-line;">{long_desc}</p>
              </div>
              <button onclick="document.getElementById('long-desc-{idx}').style.display='block'; document.getElementById('short-desc-{idx}').style.display='none'; this.style.display='none';" style="background:none; border:none; color:var(--primary); font-weight:bold; cursor:pointer; padding:0; margin-bottom:15px; text-decoration:underline;">{read_more_text}</button>
              <div class="tour-highlights">
                {highlights_html}
              </div>
            </div>
            <div class="tour-footer">
              <a href="#wizard" class="btn btn-primary btn-block">{data["tours_page"]["reserve"]}</a>
            </div>
          </div>
        </div>
        """

    # Prepare Trip Builder Data
    tb_tours = []
    for t in tours_data:
        lang_key = lang_code if lang_code in t["nombre"] else "en"
        tb_tours.append({
            "id": t["id"],
            "name": t["nombre"].get(lang_key, t["nombre"].get("en", "")),
            "desc": t.get("descripcion_corta", {}).get(lang_key, t.get("descripcion_corta", {}).get("en", "")),
            "image": f"{data['img_prefix']}{t['image'].lstrip('/')}" if t.get("image") else ""
        })
    tb_config = {
        "strings": TB_STRINGS.get(lang_code, TB_STRINGS["en"]),
        "tours": tb_tours,
        "whatsappNumber": "573001234567"
    }
    tb_config_json = json.dumps(tb_config)

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

  <!-- Google Fonts (Google Gemini / Inter Clean) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Custom CSS -->
  <link rel="stylesheet" href="{css_path}">
  <link rel="stylesheet" href="{data['img_prefix']}trip-builder.css">
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
        <a href="#wizard" class="nav-link highlight" style="font-weight: bold; position: relative; display: inline-flex; align-items: center; gap: 6px;">
          {data['nav']['wizard']}
          <span style="background-color: var(--c-gold, #f59e0b); color: #111827; font-size: 10px; padding: 2px 6px; border-radius: 9999px; text-transform: uppercase; font-weight: 800; line-height: 1;">{data['nav']['badge_new']}</span>
        </a>
        <a href="#no-vat" class="nav-link highlight" style="color: var(--c-gold, #f59e0b); font-weight: bold;">{data['nav']['no_vat']}</a>
        <a href="#ticket-truth" class="nav-link">{data['nav']['truth']}</a>
        <a href="#skip-queue" class="nav-link" style="display: inline-flex; align-items: center;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width:16px;height:16px;margin-right:4px;color:var(--c-gold, #f59e0b);">
            <path fill-rule="evenodd" d="M14.615 1.595a.75.75 0 0 1 .359.852L12.982 9.75h7.268a.75.75 0 0 1 .548 1.262l-10.5 11.25a.75.75 0 0 1-1.272-.71l1.992-7.302H3.75a.75.75 0 0 1-.548-1.262l10.5-11.25a.75.75 0 0 1 .913-.143Z" clip-rule="evenodd" />
          </svg>
          {data['nav']['skip']}
        </a>
        <a href="#guided-tours" class="nav-link">{data['nav']['tours']}</a>
        <a href="#where-to-stay" class="nav-link">{data['nav']['stays']}</a>
        <a href="https://parquetayrona.org" target="_blank" class="nav-link">{data['nav']['guide']}</a>
        <a href="#faq" class="nav-link">{data['nav']['faq']}</a>
      </nav>

      <div class="nav-actions">
        <!-- Language Switcher Dropdown -->
        <div class="lang-dropdown">
          <button class="lang-btn">{lang_code.upper()} ▾</button>
          <div class="lang-menu-wrapper">
            <ul class="lang-menu">
              {lang_links}
            </ul>
          </div>
        </div>

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
        <a href="#wizard" class="btn btn-accent btn-lg glow-btn" style="font-size:1.25rem;padding:18px 36px;font-weight:800;border-radius:12px;box-shadow:0 10px 30px rgba(245,158,11,0.4);">
          {data['hero']['btn1']}
        </a>
      </div>

      <!-- Quick Trust Indicators -->
      <div class="hero-trust-grid">
        <div class="trust-item" style="align-items: center;">
          <img src="{data['img_prefix']}images/lodging/villa_maria.jpg" alt="TayronaGuide Discount" style="width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;">
          <div>
            <strong>{data['hero']['trust1_title']}</strong>
            <span>{data['hero']['trust1_sub']}</span>
          </div>
        </div>
        <div class="trust-item" style="align-items: center;">
          <img src="{data['img_prefix']}images/vat_discount_travelers.jpg" alt="Fast-Track" style="width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;">
          <div>
            <strong>{data['hero']['trust2_title']}</strong>
            <span>{data['hero']['trust2_sub']}</span>
          </div>
        </div>
        <div class="trust-item" style="align-items: center;">
          <img src="{data['img_prefix']}images/kali_hotels_discount.jpg" alt="Kali Hotels" style="width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;">
          <div>
            <strong>{data['hero']['trust3_title']}</strong>
            <span>{data['hero']['trust3_sub']}</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Trip Builder Module -->
  <section id="wizard" class="trip-builder-section" style="position: relative; z-index: 10;">
    <div class="container">
      <div id="trip-builder-container"><div id="trip-builder"></div></div>
    </div>
  </section>

  <!-- Section 1: No VAT Campaign Banner -->
  <section class="vat-campaign-section" id="no-vat">
    <div class="container">
      <div class="vat-hero-banner reveal">
        <div class="vat-badge-tag">
          <span>✨</span> {data['no_vat']['tag']}
        </div>
        <h2 class="vat-title">{data['no_vat']['title']}</h2>
        <p class="vat-subtitle">{data['no_vat']['subtitle']}</p>
      </div>

      <div class="vat-grid">
        <div class="vat-card reveal">
          <img src="{data['img_prefix']}images/lodging/villa_maria.jpg" alt="TayronaGuide Discount" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
          <h3>{data['no_vat']['card1_title']}</h3>
          <p>{data['no_vat']['card1_desc']}</p>
          <span class="vat-highlight-pill">19% IVA Absorbed &amp; Exempt</span>
        </div>

        <div class="vat-card reveal">
          <img src="{data['img_prefix']}images/vat_discount_travelers.jpg" alt="0% VAT For Everyone" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
          <h3>{data['no_vat']['card2_title']}</h3>
          <p>{data['no_vat']['card2_desc']}</p>
          <span class="vat-highlight-pill">Official 0% Tourist Rate</span>
        </div>

        <div class="vat-card reveal">
          <img src="{data['img_prefix']}images/kali_hotels_discount.jpg" alt="Kali Hotels Discount" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;">
          <h3>{data['no_vat']['card3_title']}</h3>
          <p>{data['no_vat']['card3_desc']}</p>
          <span class="vat-highlight-pill">Exclusive TayronaGuide Discount</span>
        </div>
      </div>
    </div>
  </section>

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
              <a href="#wizard" class="btn btn-accent btn-sm margin-top-sm">{data['truth']['sol_btn']}</a>
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
              <strong>{data['skip_extra']['save_time']}</strong>
              <span>{data['skip_extra']['skip_line']}</span>
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
            <a href="#wizard" class="btn btn-accent btn-lg glow-btn">
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
        <h2 class="section-title">Girona Travels Direct Tours</h2>
        <p class="section-lead">Combine professional Girona Travels guides, seamless gate access, and comfortable lodging.</p>
      </div>

      <div class="tours-grid">
        {dynamic_tours_html}
      </div>

      <div class="tours-cta-wrap">
        <button onclick="document.querySelectorAll('.hidden-tour').forEach(el => el.classList.remove('hidden-tour')); this.style.display='none';" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;cursor:pointer;border:none;">
          {data['tours_page']['title']} &rarr;
        </button>
      </div>
    </div>
  </section>

  <!-- Section 7: Lodging Showcase -->
  <section class="section" id="where-to-stay">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag">🏨 Official Lodging Partner</span>
        <h2 class="section-title">Where to Stay: Kali Hotels</h2>
        <p class="section-lead">Enjoy city vibe at Kali Hotel Santa Marta & jungle eco-luxury at Villa María Tayrona with 0% VAT.</p>
      </div>

      <div class="lodging-grid">
        <div class="lodging-card reveal">
          <div class="lodging-image-wrapper">
            <img src="/images/lodging/villa_maria.jpg" alt="Villa María Tayrona" />
          </div>
          <div class="lodging-card-body">
            <div class="lodging-icon-row">
              <div class="lodging-icon-wrap">🌿</div>
              <span class="lodging-label">Nature Eco-Lodge</span>
            </div>
            <div class="lodging-content">
              <h3>Villa María Tayrona</h3>
              <p>{data['stays']['villa_desc']}</p>
              <a href="#wizard" class="btn btn-outline btn-sm">Book via Concierge &rarr;</a>
            </div>
          </div>
        </div>

        <div class="lodging-card reveal">
          <div class="lodging-image-wrapper">
            <img src="/images/lodging/kali_hotel.jpg" alt="Kali Hotel Santa Marta" />
          </div>
          <div class="lodging-card-body">
            <div class="lodging-icon-row">
              <div class="lodging-icon-wrap">🏛️</div>
              <span class="lodging-label">City Boutique Hotel</span>
            </div>
            <div class="lodging-content">
              <h3>Kali Hotel Santa Marta</h3>
              <p>Boutique hotel in the heart of Santa Marta historic center, featuring stylish rooms, rooftop pool, and fine dining. 0% VAT for all guests.</p>
              <a href="#wizard" class="btn btn-outline btn-sm">Book via Concierge &rarr;</a>
            </div>
          </div>
        </div>

        <div class="lodging-card reveal">
          <div class="lodging-image-wrapper">
            <img src="/images/lodging/kasankala.jpg" alt="Kasankala Restaurant" />
          </div>
          <div class="lodging-card-body">
            <div class="lodging-icon-row">
              <div class="lodging-icon-wrap">🍽️</div>
              <span class="lodging-label">Jungle Dining</span>
            </div>
            <div class="lodging-content">
              <h3>Kasankala Restaurant</h3>
              <p>Gourmet jungle dining at Villa María Tayrona. Fresh Caribbean ingredients, al fresco ambiance overlooking the rainforest canopy.</p>
              <a href="https://kasankala.com" target="_blank" class="btn btn-outline btn-sm">Visit Kasankala &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- Section 8: FAQ Accordion -->
  <section class="section section-dark" id="faq">
    <div class="container max-w-4xl">
      <div class="section-header text-center">
        <span class="section-tag">{data['faq']['tag']}</span>
        <h2 class="section-title">{data['faq']['title']}</h2>
      </div>

      <div class="faq-accordion">
        <div class="faq-item">
          <button class="faq-question">
            {data['faq']['q1']}
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{data['faq']['a1']}</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            {data['faq']['q2']}
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{data['faq']['a2']}</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            {data['faq']['q3']}
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{data['faq']['a3']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner Footer -->
  <section class="cta-banner">
    <div class="container text-center">
      <h2>{data['cta']['title']}</h2>
      <p>{data['cta']['desc']}</p>
      <a href="#wizard" class="btn btn-accent btn-xl glow-btn">
        {data['cta']['btn']}
      </a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="{data['img_prefix']}" class="brand-logo">
          <span class="logo-icon">🌿</span>
          <span class="logo-text">Tayrona<strong>Guide</strong></span>
        </a>
        <p class="footer-text">{data['footer']['desc']}</p>
      </div>
      <div class="footer-col">
        <h4>{data['footer']['nav_title']}</h4>
        <ul>
          <li><a href="{data['img_prefix']}#no-vat">{data['nav']['no_vat']}</a></li>
          <li><a href="{data['img_prefix']}#packages">{data['footer']['nav_packages']}</a></li>
          <li><a href="{data['img_prefix']}#guided-tours">{data['nav']['tours']}</a></li>
          <li><a href="{data['img_prefix']}#ticket-truth">{data['footer']['nav_truth']}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{data['footer']['partners_title']}</h4>
        <ul>
          <li><a href="https://gironatravels.com" target="_blank">Girona Travels ({data['footer']['partner_operator']})</a></li>
          <li><a href="https://kalihotels.com" target="_blank">Kali Hotels Collection</a></li>
          <li><a href="https://parquetayrona.org" target="_blank">ParqueTayrona.org</a></li>
          <li><a href="https://kasankala.com" target="_blank">{data['footer']['partner_restaurant']}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{data['footer']['cert_title']}</h4>
        <a href="https://parquetayrona.org" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; text-decoration: none; color: #94a3b8;">
          <img src="/images/icons/sello-inclusion.svg" alt="{data['footer']['cert_inclusion']}" style="height: 40px; width: auto; flex-shrink: 0;">
          <span style="font-size: 0.85rem; line-height: 1.3; font-weight: 500; color: white;">{data['footer']['cert_inclusion']}<br><span style="opacity:0.7; font-weight: 400; font-size: 0.75rem; color: #94a3b8;">ParqueTayrona.org</span></span>
        </a>
        <a href="https://parquetayrona.org" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px; text-decoration: none; color: #94a3b8;">
          <img src="/images/icons/sello-transparencia.svg" alt="{data['footer']['cert_transparencia']}" style="height: 40px; width: auto; flex-shrink: 0;">
          <span style="font-size: 0.85rem; line-height: 1.3; font-weight: 500; color: white;">{data['footer']['cert_transparencia']}<br><span style="opacity:0.7; font-weight: 400; font-size: 0.75rem; color: #94a3b8;">ParqueTayrona.org</span></span>
        </a>
        <div class="gaula-badge-container">
          <a href="https://adenunciar.policia.gov.co/Adenunciar/" target="_blank" rel="noopener noreferrer" style="display:block; color:#94a3b8; text-decoration:none;">
            <img src="/images/icons/gaula-badge.svg" alt="{data['footer']['cert_gaula_alt']}" style="height: 46px; width: auto; margin-bottom: 8px;">
            <div style="font-size: 0.8rem; line-height: 1.3;">{data['footer']['cert_gaula_text']}</div>
          </a>
        </div>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>{data['footer']['copyright']}</p>
    </div>
  </footer>

  <script>
    window.GIRONA_TOURS_DATA = {json.dumps(tours_data)};
    window.TB_CONFIG = {tb_config_json};
  </script>
  <script src="{js_path}"></script>
  <script src="{data['img_prefix']}trip-builder.js"></script>

  <!-- Scroll Reveal Observer -->
  <script>
    (function() {{
      const els = document.querySelectorAll('.reveal');
      if (!els.length) return;
      const obs = new IntersectionObserver((entries, obs) => {{
        entries.forEach(e => {{
          if (e.isIntersecting) {{
            e.target.classList.add('visible');
            obs.unobserve(e.target);
          }}
        }});
      }}, {{ threshold: 0.10, rootMargin: '0px 0px -40px 0px' }});
      els.forEach(function(el) {{ obs.observe(el); }});
    }})();
  </script>
</body>
</html>
"""
    
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
        for f in ["index.html", "tours_test.html", "app.js", "style.css", "trip-builder.css", "trip-builder.js", "favicon.ico", "robots.txt", "sitemap.xml"]:
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
