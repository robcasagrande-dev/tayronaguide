import json

def translate_tours():
    with open("tours_girona_travels.json", "r", encoding="utf-8") as f:
        tours = json.load(f)

    for t in tours:
        if t["id"] == "cabo-san-juan-tayrona":
            t["badge"] = {
                "en": "Most Popular", "es": "Más Popular", "it": "Più Popolare", "fr": "Plus Populaire", "de": "Am Beliebtesten"
            }
            t["badges"] = {
                "en": [{"label": "Best Selling", "class": "badge-green"}],
                "es": [{"label": "Más Vendido", "class": "badge-green"}],
                "it": [{"label": "Più Venduto", "class": "badge-green"}],
                "fr": [{"label": "Meilleure Vente", "class": "badge-green"}],
                "de": [{"label": "Bestseller", "class": "badge-green"}]
            }
            t["ribbon"] = {
                "en": "⚡ Fast-Track", "es": "⚡ Fila Rápida", "it": "⚡ Saltafila", "fr": "⚡ Coupe-file", "de": "⚡ Fast-Track"
            }
            t["highlights"] = {
                "en": ["⏱️ 8-9 Hours", "🥾 Moderate Trek", "⚡ Queue Fast-Track"],
                "es": ["⏱️ 8-9 Horas", "🥾 Trekking Moderado", "⚡ Fila Rápida"],
                "it": ["⏱️ 8-9 Ore", "🥾 Trekking Moderato", "⚡ Saltafila"],
                "fr": ["⏱️ 8-9 Heures", "🥾 Trek Modéré", "⚡ Coupe-file"],
                "de": ["⏱️ 8-9 Stunden", "🥾 Mittelschwerer Trek", "⚡ Fast-Track"]
            }
        elif t["id"] == "ruinas-bunkuany":
            t["badge"] = {
                "en": "Cultural Trek", "es": "Trekking Cultural", "it": "Trekking Culturale", "fr": "Trek Culturel", "de": "Kultureller Trek"
            }
            t["highlights"] = {
                "en": ["🐒 Wildlife Focus", "🏛️ Cultural History", "👨‍👩‍👧 Private Group"],
                "es": ["🐒 Enfoque en Vida Silvestre", "🏛️ Historia Cultural", "👨‍👩‍👧 Grupo Privado"],
                "it": ["🐒 Focus sulla Fauna", "🏛️ Storia Culturale", "👨‍👩‍👧 Gruppo Privato"],
                "fr": ["🐒 Faune Sauvage", "🏛️ Histoire Culturelle", "👨‍👩‍👧 Groupe Privé"],
                "de": ["🐒 Wildtiere im Fokus", "🏛️ Kulturgeschichte", "👨‍👩‍👧 Private Gruppe"]
            }
        elif t["id"] == "tour-del-cacao":
            t["badge"] = {
                "en": "Best Value", "es": "Mejor Precio", "it": "Miglior Prezzo", "fr": "Meilleur Prix", "de": "Bester Preis"
            }
            t["highlights"] = {
                "en": ["🍫 Artisan Tasting", "🌱 Farm to Bar", "😋 Hands-on Workshop"],
                "es": ["🍫 Degustación Artesanal", "🌱 De la Finca a la Barra", "😋 Taller Práctico"],
                "it": ["🍫 Degustazione Artigianale", "🌱 Dalla Fabbrica alla Barretta", "😋 Laboratorio Pratico"],
                "fr": ["🍫 Dégustation Artisanale", "🌱 De la Ferme à la Tablette", "😋 Atelier Pratique"],
                "de": ["🍫 Handwerkliche Verkostung", "🌱 Vom Hof zur Tafel", "😋 Praktischer Workshop"]
            }

    with open("tours_girona_travels.json", "w", encoding="utf-8") as f:
        json.dump(tours, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    translate_tours()
