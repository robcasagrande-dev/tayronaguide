import io

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    (
        '''            "villa_btn": "View Rooms at ParqueTayrona.org &rarr;"\n        }\n    },''',
        '''            "villa_btn": "View Rooms at ParqueTayrona.org &rarr;"\n        },\n        "footer": {\n            "desc": "The official verified travel guide for Tayrona National Park & Santa Marta. Managed in partnership with Girona Travels, Kali Hotels & Villa María Tayrona.",\n            "nav_title": "Quick Navigation",\n            "nav_packages": "Bundled Packages",\n            "nav_concierge": "Concierge Request Tool",\n            "nav_truth": "Ticket Truth",\n            "partners_title": "Official Partners",\n            "partner_operator": "Official Operator",\n            "partner_restaurant": "Kasankala Restaurant",\n            "cert_title": "Certifications",\n            "cert_inclusion": "Seal of Inclusion",\n            "cert_transparencia": "Seal of Transparency",\n            "cert_gaula_alt": "Official GAULA Campaign",\n            "cert_gaula_text": "We support the official anti-kidnapping and anti-extortion campaign. Hotline: 165",\n            "copyright": "&copy; 2026 TayronaGuide.com. All rights reserved. Powered by Girona Travels & Kali Hotels."\n        }\n    },'''
    ),
    (
        '''            "villa_btn": "Ver Habitaciones en ParqueTayrona.org &rarr;"\n        }\n    },''',
        '''            "villa_btn": "Ver Habitaciones en ParqueTayrona.org &rarr;"\n        },\n        "footer": {\n            "desc": "La guía de viaje oficial verificada para el Parque Nacional Tayrona y Santa Marta. Gestionada en asociación con Girona Travels, Kali Hotels y Villa María Tayrona.",\n            "nav_title": "Navegación Rápida",\n            "nav_packages": "Paquetes Combinados",\n            "nav_concierge": "Diseñador de Viaje",\n            "nav_truth": "Verdad sobre Entradas",\n            "partners_title": "Socios Oficiales",\n            "partner_operator": "Operador Oficial",\n            "partner_restaurant": "Restaurante Kasankala",\n            "cert_title": "Certificaciones",\n            "cert_inclusion": "Sello de Inclusión",\n            "cert_transparencia": "Sello de Transparencia",\n            "cert_gaula_alt": "Campaña Oficial GAULA",\n            "cert_gaula_text": "Apoyamos la campaña oficial antisecuestro y antiextorsión. Línea: 165",\n            "copyright": "&copy; 2026 TayronaGuide.com. Todos los derechos reservados. Desarrollado por Girona Travels y Kali Hotels."\n        }\n    },'''
    ),
    (
        '''            "villa_btn": "Vedi Camere su ParqueTayrona.org &rarr;"\n        }\n    },''',
        '''            "villa_btn": "Vedi Camere su ParqueTayrona.org &rarr;"\n        },\n        "footer": {\n            "desc": "La guida di viaggio ufficiale verificata per il Parco Nazionale Tayrona e Santa Marta. Gestita in collaborazione con Girona Travels, Kali Hotels e Villa María Tayrona.",\n            "nav_title": "Navigazione Rapida",\n            "nav_packages": "Pacchetti Inclusivi",\n            "nav_concierge": "Pianificatore di Viaggio",\n            "nav_truth": "Verità sui Biglietti",\n            "partners_title": "Partner Ufficiali",\n            "partner_operator": "Operatore Ufficiale",\n            "partner_restaurant": "Ristorante Kasankala",\n            "cert_title": "Certificazioni",\n            "cert_inclusion": "Sigillo di Inclusione",\n            "cert_transparencia": "Sigillo di Trasparenza",\n            "cert_gaula_alt": "Campagna Ufficiale GAULA",\n            "cert_gaula_text": "Sosteniamo la campagna ufficiale contro i sequestri e le estorsioni. Linea: 165",\n            "copyright": "&copy; 2026 TayronaGuide.com. Tutti i diritti riservati. Sviluppato da Girona Travels & Kali Hotels."\n        }\n    },'''
    ),
    (
        '''            "villa_btn": "Voir les Chambres sur ParqueTayrona.org &rarr;"\n        }\n    },''',
        '''            "villa_btn": "Voir les Chambres sur ParqueTayrona.org &rarr;"\n        },\n        "footer": {\n            "desc": "Le guide de voyage officiel vérifié pour le parc national Tayrona et Santa Marta. Géré en partenariat avec Girona Travels, Kali Hotels et Villa María Tayrona.",\n            "nav_title": "Navigation Rapide",\n            "nav_packages": "Forfaits Combinés",\n            "nav_concierge": "Outil de Planification",\n            "nav_truth": "Vérité sur les Billets",\n            "partners_title": "Partenaires Officiels",\n            "partner_operator": "Opérateur Officiel",\n            "partner_restaurant": "Restaurant Kasankala",\n            "cert_title": "Certifications",\n            "cert_inclusion": "Sceau d'Inclusion",\n            "cert_transparencia": "Sceau de Transparence",\n            "cert_gaula_alt": "Campagne Officielle GAULA",\n            "cert_gaula_text": "Nous soutenons la campagne officielle contre les enlèvements et les extorsions. Ligne: 165",\n            "copyright": "&copy; 2026 TayronaGuide.com. Tous droits réservés. Propulsé par Girona Travels & Kali Hotels."\n        }\n    },'''
    ),
    (
        '''            "villa_btn": "Zimmer auf ParqueTayrona.org Ansehen &rarr;"\n        }\n    }\n}''',
        '''            "villa_btn": "Zimmer auf ParqueTayrona.org Ansehen &rarr;"\n        },\n        "footer": {\n            "desc": "Der offizielle verifizierte Reiseführer für den Tayrona-Nationalpark und Santa Marta. Verwaltet in Partnerschaft mit Girona Travels, Kali Hotels und Villa María Tayrona.",\n            "nav_title": "Schnellnavigation",\n            "nav_packages": "Kombi-Pakete",\n            "nav_concierge": "Reiseplaner",\n            "nav_truth": "Ticket-Wahrheit",\n            "partners_title": "Offizielle Partner",\n            "partner_operator": "Offizieller Veranstalter",\n            "partner_restaurant": "Kasankala Restaurant",\n            "cert_title": "Zertifizierungen",\n            "cert_inclusion": "Siegel der Inklusion",\n            "cert_transparencia": "Siegel der Transparenz",\n            "cert_gaula_alt": "Offizielle GAULA-Kampagne",\n            "cert_gaula_text": "Wir unterstützen die offizielle Anti-Entführungs- und Anti-Erpressungs-Kampagne. Hotline: 165",\n            "copyright": "&copy; 2026 TayronaGuide.com. Alle Rechte vorbehalten. Unterstützt von Girona Travels & Kali Hotels."\n        }\n    }\n}'''
    )
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print("Replaced chunk!")
    else:
        print("MISSING chunk:")

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Done writing build_languages.py")
