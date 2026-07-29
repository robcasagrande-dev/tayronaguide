import re

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the HTML block for hero-trust-grid
html_pattern = re.compile(r"<div class=\"hero-trust-grid\">.*?</div>\s*</div>\s*</section>", re.DOTALL)

new_html = """<div class=\"hero-trust-grid\">
        <div class=\"trust-item\" style=\"align-items: center;\">
          <img src=\"{data['img_prefix']}images/lodging/villa_maria.jpg\" alt=\"TayronaGuide Discount\" style=\"width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;\">
          <div>
            <strong>{data['hero']['trust1_title']}</strong>
            <span>{data['hero']['trust1_sub']}</span>
          </div>
        </div>
        <div class=\"trust-item\" style=\"align-items: center;\">
          <img src=\"{data['img_prefix']}images/vat_discount_travelers.jpg\" alt=\"Fast-Track\" style=\"width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;\">
          <div>
            <strong>{data['hero']['trust2_title']}</strong>
            <span>{data['hero']['trust2_sub']}</span>
          </div>
        </div>
        <div class=\"trust-item\" style=\"align-items: center;\">
          <img src=\"{data['img_prefix']}images/kali_hotels_discount.jpg\" alt=\"Kali Hotels\" style=\"width: 56px; height: 56px; object-fit: cover; border-radius: 50%; border: 2px solid var(--c-accent); margin-right: 16px; flex-shrink: 0;\">
          <div>
            <strong>{data['hero']['trust3_title']}</strong>
            <span>{data['hero']['trust3_sub']}</span>
          </div>
        </div>
      </div>
    </div>
  </section>"""

content = html_pattern.sub(new_html, content)

# Now update the dictionaries for EN, ES, IT, FR, DE
replacements = {
    "en": {
        "trust1_title": "TayronaGuide Exclusive",
        "trust1_sub": "Multi-hotel discount & 0% VAT",
        "trust3_title": "Kali Hotels",
        "trust3_sub": "Special rates & 0% VAT"
    },
    "es": {
        "trust1_title": "Exclusivo TayronaGuide",
        "trust1_sub": "Descuento multi-hotel y 0% IVA",
        "trust3_title": "Kali Hotels",
        "trust3_sub": "Tarifas especiales y 0% IVA"
    },
    "it": {
        "trust1_title": "Esclusiva TayronaGuide",
        "trust1_sub": "Sconto multi-hotel e 0% IVA",
        "trust3_title": "Kali Hotels",
        "trust3_sub": "Tariffe speciali e 0% IVA"
    },
    "fr": {
        "trust1_title": "Exclusivité TayronaGuide",
        "trust1_sub": "Remise multi-hôtels et 0% TVA",
        "trust3_title": "Kali Hotels",
        "trust3_sub": "Tarifs spéciaux et 0% TVA"
    },
    "de": {
        "trust1_title": "Exklusiv TayronaGuide",
        "trust1_sub": "Multi-Hotel Rabatt & 0% MwSt.",
        "trust3_title": "Kali Hotels",
        "trust3_sub": "Sondertarife & 0% MwSt."
    }
}

for lang, data in replacements.items():
    title1_pat = re.compile(r"\"trust1_title\":\s*\".*?\"")
    sub1_pat = re.compile(r"\"trust1_sub\":\s*\".*?\"")
    title3_pat = re.compile(r"\"trust3_title\":\s*\".*?\"")
    sub3_pat = re.compile(r"\"trust3_sub\":\s*\".*?\"")

    lang_start = content.find(f'"{lang}": {{')
    lang_end = content.find('        },', content.find('"packages": {', lang_start))
    
    if lang_start != -1 and lang_end != -1:
        block = content[lang_start:lang_end]
        
        block = title1_pat.sub(f'\"trust1_title\": \"{data["trust1_title"]}\"', block)
        block = sub1_pat.sub(f'\"trust1_sub\": \"{data["trust1_sub"]}\"', block)
        block = title3_pat.sub(f'\"trust3_title\": \"{data["trust3_title"]}\"', block)
        block = sub3_pat.sub(f'\"trust3_sub\": \"{data["trust3_sub"]}\"', block)
        
        content = content[:lang_start] + block + content[lang_end:]

# Also update the Lodging Section title to remove "Villa María Tayrona"
content = content.replace("Where to Stay: Kali Hotel &amp; Villa María Tayrona", "Where to Stay: Kali Hotels &amp; Villa María Tayrona")
content = content.replace("Where to Stay: Kali Hotel & Villa María Tayrona", "Where to Stay: Kali Hotels")

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_languages.py successfully")
