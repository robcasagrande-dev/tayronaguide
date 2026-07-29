import io
import re

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update languages dict
langs = {
    "en": '''        "footer": {
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
        }
    },''',
    "en_new": '''        "footer": {
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
    },''',
    "es": '''        "footer": {
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
        }
    },''',
    "es_new": '''        "footer": {
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
    },''',
    "it": '''        "footer": {
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
        }
    },''',
    "it_new": '''        "footer": {
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
    },''',
    "fr": '''        "footer": {
            "desc": "Le guide de voyage officiel vérifié pour le parc national Tayrona et Santa Marta. Géré en partenariat avec Girona Travels, Kali Hotels et Villa María Tayrona.",
            "nav_title": "Navigation Rapide",
            "nav_packages": "Forfaits Combinés",
            "nav_concierge": "Outil de Planification",
            "nav_truth": "Vérité sur les Billets",
            "partners_title": "Partenaires Officiels",
            "partner_operator": "Opérateur Officiel",
            "partner_restaurant": "Restaurant Kasankala",
            "cert_title": "Certifications",
            "cert_inclusion": "Sceau d\\'Inclusion",
            "cert_transparencia": "Sceau de Transparence",
            "cert_gaula_alt": "Campagne Officielle GAULA",
            "cert_gaula_text": "Nous soutenons la campagne officielle contre les enlèvements et les extorsions. Ligne: 165",
            "copyright": "&copy; 2026 TayronaGuide.com. Tous droits réservés. Propulsé par Girona Travels & Kali Hotels."
        }
    },''',
    "fr_new": '''        "footer": {
            "desc": "Le guide de voyage officiel vérifié pour le parc national Tayrona et Santa Marta. Géré en partenariat avec Girona Travels, Kali Hotels et Villa María Tayrona.",
            "nav_title": "Navigation Rapide",
            "nav_packages": "Forfaits Combinés",
            "nav_concierge": "Outil de Planification",
            "nav_truth": "Vérité sur les Billets",
            "partners_title": "Partenaires Officiels",
            "partner_operator": "Opérateur Officiel",
            "partner_restaurant": "Restaurant Kasankala",
            "cert_title": "Certifications",
            "cert_inclusion": "Sceau d\\'Inclusion",
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
    },''',
    "de": '''        "footer": {
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
        }
    }
}''',
    "de_new": '''        "footer": {
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
}'''
}

for lang_code in ['en', 'es', 'it', 'fr', 'de']:
    content = content.replace(langs[lang_code], langs[lang_code + '_new'])
    print(f"Updated dictionary for {lang_code}")


# 2. Update HTML Templates
replacements = [
    (
        '''              <strong>Save 1 to 2 Hours</strong>\n              <span>Skip the hot morning gate line</span>''',
        '''              <strong>{data['skip_extra']['save_time']}</strong>\n              <span>{data['skip_extra']['skip_line']}</span>'''
    ),
    (
        '''  <!-- Section 8: FAQ Accordion -->
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
  </section>''',
        '''  <!-- Section 8: FAQ Accordion -->
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
  </section>'''
    ),
    (
        '''  <!-- CTA Banner Footer -->
  <section class="cta-banner">
    <div class="container text-center">
      <h2>Ready for an Unforgettable Tayrona & Santa Marta Experience?</h2>
      <p>Enjoy 0% VAT rates at Kali Hotel & Villa María Tayrona with Girona Travel private transport and certified guides.</p>
      <a href="#concierge" class="btn btn-accent btn-xl glow-btn">
        🚀 Launch Concierge Request Tool &rarr;
      </a>
    </div>
  </section>''',
        '''  <!-- CTA Banner Footer -->
  <section class="cta-banner">
    <div class="container text-center">
      <h2>{data['cta']['title']}</h2>
      <p>{data['cta']['desc']}</p>
      <a href="#concierge" class="btn btn-accent btn-xl glow-btn">
        {data['cta']['btn']}
      </a>
    </div>
  </section>'''
    ),
    (
        '''<a href="{data['img_prefix']}index.html#concierge" class="btn btn-primary btn-block">Reserve via Concierge &rarr;</a>''',
        '''<a href="{data['img_prefix']}index.html#concierge" class="btn btn-primary btn-block">{data['tours_page']['reserve']}</a>'''
    ),
    (
        '''<a href="{data['img_prefix']}index.html" class="nav-link">Home</a>''',
        '''<a href="{data['img_prefix']}index.html" class="nav-link">{data['tours_page']['home']}</a>'''
    ),
    (
        '''    <div class="section-header">
      <h2 class="section-title">All Girona Travels Tours</h2>
      <p class="section-lead">Explore our full catalog of guided experiences, eco-treks, and cultural adventures.</p>
    </div>''',
        '''    <div class="section-header">
      <h2 class="section-title">{data['tours_page']['title']}</h2>
      <p class="section-lead">{data['tours_page']['lead']}</p>
    </div>'''
    )
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print("Replaced HTML template chunk!")
    else:
        print("MISSING HTML template chunk:")
        print(old[:100] + "...")

# Also replace the hardcoded footer in tours.html
old_tours_footer = '''  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="/" class="brand-logo" style="margin-bottom: 15px; display: inline-block; color: white; text-decoration: none;">
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
      <div class="footer-col">
        <h4>Certifications</h4>
        <a href="https://parquetayrona.org" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; text-decoration: none; color: #94a3b8;">
          <img src="/images/icons/sello-inclusion.svg" alt="Sello de Inclusión" style="height: 40px; width: auto; flex-shrink: 0;">
          <span style="font-size: 0.85rem; line-height: 1.3; font-weight: 500; color: white;">Sello de Inclusión<br><span style="opacity:0.7; font-weight: 400; font-size: 0.75rem; color: #94a3b8;">ParqueTayrona.org</span></span>
        </a>
        <a href="https://parquetayrona.org" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px; text-decoration: none; color: #94a3b8;">
          <img src="/images/icons/sello-transparencia.svg" alt="Sello de Transparencia" style="height: 40px; width: auto; flex-shrink: 0;">
          <span style="font-size: 0.85rem; line-height: 1.3; font-weight: 500; color: white;">Sello de Transparencia<br><span style="opacity:0.7; font-weight: 400; font-size: 0.75rem; color: #94a3b8;">ParqueTayrona.org</span></span>
        </a>
        <div class="gaula-badge-container">
          <a href="https://adenunciar.policia.gov.co/Adenunciar/" target="_blank" rel="noopener noreferrer" style="display:block; color:#94a3b8; text-decoration:none;">
            <img src="/images/icons/gaula-badge.svg" alt="Campaña Oficial GAULA" style="height: 46px; width: auto; margin-bottom: 8px;">
            <div style="font-size: 0.8rem; line-height: 1.3;">Apoyamos la campaña oficial antisecuestro y antiextorsión. Línea: 165</div>
          </a>
        </div>
      </div>
    </div>
    <div class="footer-bottom text-center">
      <p>&copy; 2026 TayronaGuide.com. All rights reserved. Powered by Girona Travels & Kali Hotels.</p>
    </div>
  </footer>'''

new_tours_footer = '''  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="{data['img_prefix']}index.html" class="brand-logo" style="margin-bottom: 15px; display: inline-block; color: white; text-decoration: none;">
          <span class="logo-icon">🌿</span>
          <span class="logo-text">Tayrona<strong>Guide</strong></span>
        </a>
        <p class="footer-text">{data['footer']['desc']}</p>
      </div>
      <div class="footer-col">
        <h4>{data['footer']['nav_title']}</h4>
        <ul>
          <li><a href="{data['img_prefix']}index.html#no-vat">{data['nav']['no_vat']}</a></li>
          <li><a href="{data['img_prefix']}index.html#packages">{data['footer']['nav_packages']}</a></li>
          <li><a href="{data['img_prefix']}index.html#concierge">{data['footer']['nav_concierge']}</a></li>
          <li><a href="{data['img_prefix']}index.html#ticket-truth">{data['footer']['nav_truth']}</a></li>
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
  </footer>'''

if old_tours_footer in content:
    content = content.replace(old_tours_footer, new_tours_footer)
    print("Replaced tours footer chunk!")
else:
    print("MISSING tours footer chunk")


with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished fixing missing translations!")
