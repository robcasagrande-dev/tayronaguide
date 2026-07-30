import json
with open('build_languages.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's just find each language's section manually
# Since we know the order of "tours": { is EN, ES, IT, FR, DE, we can replace them sequentially

tours_replacements = [
    '"tours_sec": {"tag": "Girona Travels Experiences", "title": "Girona Travels Direct Tours", "lead": "Combine professional Girona Travels guides, seamless gate access, and comfortable lodging."},\n        "tours": {',
    '"tours_sec": {"tag": "Experiencias Girona Travels", "title": "Tours Directos Girona Travels", "lead": "Combina guías profesionales, acceso sin filas al parque y alojamiento confortable."},\n        "tours": {',
    '"tours_sec": {"tag": "Esperienze Girona Travels", "title": "Tour Diretti Girona Travels", "lead": "Combina guide professionali, accesso rapido al parco e alloggi confortevoli."},\n        "tours": {',
    '"tours_sec": {"tag": "Expériences Girona Travels", "title": "Circuits Directs Girona Travels", "lead": "Combinez des guides professionnels, un accès rapide et un hébergement confortable."},\n        "tours": {',
    '"tours_sec": {"tag": "Girona Travels Erlebnisse", "title": "Girona Travels Direkttouren", "lead": "Kombinieren Sie professionelle Guides, schnellen Zugang und komfortable Unterkünfte."},\n        "tours": {'
]

for repl in tours_replacements:
    content = content.replace('"tours": {', repl, 1)

stays_replacements = [
    '"stays": {\n            "tag": "Official Lodging Partner", "title": "Where to Stay: Kali Hotels", "lead": "Enjoy city vibe at Kali Hotel Santa Marta & jungle eco-luxury at Villa María Tayrona with 0% VAT.", "eco": "Nature Eco-Lodge", "city": "City Boutique Hotel", "dining": "Jungle Dining", "kali_desc": "Boutique hotel in the heart of Santa Marta historic center, featuring stylish rooms, rooftop pool, and fine dining. 0% VAT for all guests.", "kasankala_desc": "Gourmet jungle dining at Villa María Tayrona. Fresh Caribbean ingredients, al fresco ambiance overlooking the rainforest canopy.", "book_btn": "Book via Concierge", "visit_btn": "Visit Kasankala",',
    '"stays": {\n            "tag": "Socio Oficial de Alojamiento", "title": "Dónde Quedarse: Hoteles Kali", "lead": "Disfruta de la ciudad en Kali Hotel Santa Marta y del lujo ecológico en Villa María Tayrona con 0% IVA.", "eco": "Eco-Lodge Natural", "city": "Hotel Boutique de Ciudad", "dining": "Comida en la Selva", "kali_desc": "Hotel boutique en el centro histórico de Santa Marta, con elegantes habitaciones, piscina en la azotea y excelente comida. 0% IVA para todos.", "kasankala_desc": "Comida gourmet en la selva en Villa María Tayrona. Ingredientes frescos, ambiente al aire libre.", "book_btn": "Reservar vía Conserje", "visit_btn": "Visitar Kasankala",',
    '"stays": {\n            "tag": "Partner Ufficiale di Alloggio", "title": "Dove Alloggiare: Kali Hotels", "lead": "Vivi la città al Kali Hotel Santa Marta e il lusso ecologico a Villa María Tayrona con 0% IVA.", "eco": "Eco-Lodge Naturale", "city": "Boutique Hotel in Città", "dining": "Ristorazione nella Giungla", "kali_desc": "Boutique hotel nel cuore del centro storico di Santa Marta, con camere eleganti e piscina sul tetto. 0% IVA.", "kasankala_desc": "Cucina gourmet nella giungla presso Villa María Tayrona. Ingredienti freschi dei Caraibi.", "book_btn": "Prenota via Concierge", "visit_btn": "Visita Kasankala",',
    '"stays": {\n            "tag": "Partenaire d\'Hébergement Officiel", "title": "Où Séjourner: Kali Hotels", "lead": "Profitez de la ville au Kali Hotel Santa Marta et du luxe écologique à Villa María Tayrona avec 0% TVA.", "eco": "Eco-Lodge Nature", "city": "Boutique Hôtel de Ville", "dining": "Dîner dans la Jungle", "kali_desc": "Boutique hôtel au cœur du centre historique de Santa Marta. 0% TVA pour tous.", "kasankala_desc": "Dîner gastronomique dans la jungle à Villa María Tayrona. Ingrédients caribéens frais.", "book_btn": "Réserver via Concierge", "visit_btn": "Visiter Kasankala",',
    '"stays": {\n            "tag": "Offizieller Unterkunftspartner", "title": "Wo übernachten: Kali Hotels", "lead": "Erleben Sie das Stadtleben im Kali Hotel Santa Marta & Öko-Luxus in der Villa María Tayrona mit 0% MwSt.", "eco": "Natur Öko-Lodge", "city": "Stadt-Boutique-Hotel", "dining": "Dschungel-Essen", "kali_desc": "Boutique-Hotel im Herzen der Altstadt von Santa Marta, mit eleganten Zimmern und Dachpool. 0% MwSt.", "kasankala_desc": "Gourmet-Dschungel-Essen in der Villa María Tayrona. Frische karibische Zutaten.", "book_btn": "Über Concierge buchen", "visit_btn": "Kasankala besuchen",'
]

for repl in stays_replacements:
    content = content.replace('"stays": {', repl, 1)

with open('build_languages.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done patching simply!")
