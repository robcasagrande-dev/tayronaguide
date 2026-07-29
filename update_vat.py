import re

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the HTML block first
html_pattern = re.compile(r"<div class=\"vat-grid\">.*?</div>\s*</div>\s*</section>", re.DOTALL)

new_html = """<div class=\"vat-grid\">
        <div class=\"vat-card reveal\">
          <img src=\"{data['img_prefix']}images/lodging/villa_maria.jpg\" alt=\"TayronaGuide Discount\" style=\"width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;\">
          <h3>{data['no_vat']['card1_title']}</h3>
          <p>{data['no_vat']['card1_desc']}</p>
          <span class=\"vat-highlight-pill\">19% IVA Absorbed &amp; Exempt</span>
        </div>

        <div class=\"vat-card reveal\">
          <img src=\"{data['img_prefix']}images/vat_discount_travelers.jpg\" alt=\"0% VAT For Everyone\" style=\"width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;\">
          <h3>{data['no_vat']['card2_title']}</h3>
          <p>{data['no_vat']['card2_desc']}</p>
          <span class=\"vat-highlight-pill\">Official 0% Tourist Rate</span>
        </div>

        <div class=\"vat-card reveal\">
          <img src=\"{data['img_prefix']}images/kali_hotels_discount.jpg\" alt=\"Kali Hotels Discount\" style=\"width: 100%; height: 200px; object-fit: cover; border-radius: 12px; margin-bottom: 16px;\">
          <h3>{data['no_vat']['card3_title']}</h3>
          <p>{data['no_vat']['card3_desc']}</p>
          <span class=\"vat-highlight-pill\">Exclusive TayronaGuide Discount</span>
        </div>
      </div>
    </div>
  </section>"""

content = html_pattern.sub(new_html, content)

# Now we need to update the dictionaries for EN, ES, IT, FR, DE
replacements = {
    "en": {
        "card1_title": "TayronaGuide Exclusive",
        "card1_desc": "Book through TayronaGuide to access our multi-hotel exclusive discount. We absorb the hotel tax, so Colombians and international travelers enjoy the exact same 0% VAT pricing.",
        "card2_title": "0% VAT For Everyone",
        "card2_desc": "Whether you are a Colombian national or an international traveler, enjoy 100% tax-exempt & transparent pricing. No surprise fees and clear upfront rate guarantees.",
        "card3_title": "Kali Hotels",
        "card3_desc": "Enjoy our special TayronaGuide discount at Kali Hotels. Experience premium stays in Santa Marta with an automatic 0% VAT tax benefit included."
    },
    "es": {
        "card1_title": "Exclusivo TayronaGuide",
        "card1_desc": "Reserva a través de TayronaGuide para acceder a nuestro descuento exclusivo en múltiples hoteles. Absorbemos el impuesto hotelero para que colombianos y extranjeros disfruten del mismo precio sin IVA.",
        "card2_title": "0% IVA Para Todos",
        "card2_desc": "Ya sea nacional colombiano o viajero internacional, disfruta de precios transparentes y 100% libres de impuestos. Sin tarifas sorpresa ni cobros ocultos garantizados.",
        "card3_title": "Kali Hotels",
        "card3_desc": "Disfruta de nuestro descuento especial TayronaGuide en Kali Hotels. Vive estadías premium en Santa Marta con el beneficio automático del 0% de IVA incluido."
    },
    "it": {
        "card1_title": "Esclusiva TayronaGuide",
        "card1_desc": "Prenota tramite TayronaGuide per accedere al nostro sconto esclusivo multi-hotel. Assorbiamo la tassa di soggiorno così colombiani e viaggiatori internazionali godono dello stesso prezzo 0% IVA.",
        "card2_title": "0% IVA Per Tutti",
        "card2_desc": "Che tu sia cittadino colombiano o viaggiatore internazionale, goditi un prezzo trasparente e 100% esente da tasse. Nessuna commissione a sorpresa e tariffe garantite.",
        "card3_title": "Kali Hotels",
        "card3_desc": "Approfitta del nostro speciale sconto TayronaGuide nei Kali Hotels. Vivi soggiorni premium a Santa Marta con il beneficio automatico dello 0% di IVA incluso."
    },
    "fr": {
        "card1_title": "Exclusivité TayronaGuide",
        "card1_desc": "Réservez via TayronaGuide pour accéder à notre remise exclusive multi-hôtels. Nous absorbons la taxe hôtelière pour que les Colombiens et les voyageurs internationaux bénéficient du même prix à 0% de TVA.",
        "card2_title": "0% TVA Pour Tous",
        "card2_desc": "Que vous soyez de nationalité colombienne ou un voyageur international, profitez de prix transparents et 100% exonérés de taxes. Pas de frais surprises et des tarifs garantis.",
        "card3_title": "Kali Hotels",
        "card3_desc": "Profitez de notre remise spéciale TayronaGuide dans les Kali Hotels. Vivez des séjours premium à Santa Marta avec l'avantage automatique de 0% de TVA inclus."
    },
    "de": {
        "card1_title": "Exklusiv TayronaGuide",
        "card1_desc": "Buchen Sie über TayronaGuide, um unseren exklusiven Multi-Hotel-Rabatt zu nutzen. Wir übernehmen die Hotelsteuer, damit Kolumbianer und internationale Reisende den gleichen 0% MwSt.-Preis genießen.",
        "card2_title": "0% MwSt. Für Alle",
        "card2_desc": "Ob kolumbianischer Staatsbürger oder internationaler Reisender, genießen Sie 100% steuerfreie & transparente Preise. Keine Überraschungsgebühren und klare Preisgarantien.",
        "card3_title": "Kali Hotels",
        "card3_desc": "Genießen Sie unseren speziellen TayronaGuide-Rabatt in den Kali Hotels. Erleben Sie Premium-Aufenthalte in Santa Marta mit dem automatischen 0% MwSt.-Vorteil inklusive."
    }
}

for lang, data in replacements.items():
    # Replace titles
    title1_pat = re.compile(r"\"card1_title\":\s*\".*?\"")
    title2_pat = re.compile(r"\"card2_title\":\s*\".*?\"")
    title3_pat = re.compile(r"\"card3_title\":\s*\".*?\"")
    
    desc1_pat = re.compile(r"\"card1_desc\":\s*\".*?\"")
    desc2_pat = re.compile(r"\"card2_desc\":\s*\".*?\"")
    desc3_pat = re.compile(r"\"card3_desc\":\s*\".*?\"")

    lang_start = content.find(f'"{lang}": {{')
    
    # Next language block start or end of dict
    lang_end = content.find('        },', content.find('"packages": {', lang_start))
    
    if lang_start != -1 and lang_end != -1:
        block = content[lang_start:lang_end]
        
        block = title1_pat.sub(f'\"card1_title\": \"{data["card1_title"]}\"', block)
        block = title2_pat.sub(f'\"card2_title\": \"{data["card2_title"]}\"', block)
        block = title3_pat.sub(f'\"card3_title\": \"{data["card3_title"]}\"', block)
        
        block = desc1_pat.sub(f'\"card1_desc\": \"{data["card1_desc"]}\"', block)
        block = desc2_pat.sub(f'\"card2_desc\": \"{data["card2_desc"]}\"', block)
        block = desc3_pat.sub(f'\"card3_desc\": \"{data["card3_desc"]}\"', block)
        
        content = content[:lang_start] + block + content[lang_end:]

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_languages.py successfully")
