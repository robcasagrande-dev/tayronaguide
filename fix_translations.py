import re
import ast

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

translations = {
    "en": {
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
    "es": {
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
    "it": {
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
    "fr": {
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
    "de": {
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

# Add footer translations to each language block
for lang, trans in translations.items():
    # Construct a string representation of the new key
    footer_str = '        "footer": {\n'
    for k, v in trans.items():
        footer_str += f'            "{k}": "{v}",\n'
    footer_str = footer_str.rstrip(',\n') + '\n        }\n    }'
    
    # Simple regex to append the footer before the end of the language block
    # We find the end of the block which is `    },` or `    }` for the last one
    pattern = r'(    "stays": \{.*?\}[\n\r]+)(    \}|    \},)'
    
    def repl(m):
        return m.group(1) + ',\n' + footer_str.replace('\n    }', m.group(2))

    # To specifically target the right language block, we should perhaps do a more localized search
    # Let's just find "stays" inside the specific language block
    lang_pattern = f'("{lang}": {{[\\s\\S]*?)(    "stays": {{[\\s\\S]*?\\n    }})\\n(    }},|    }})'
    
    def repl_lang(m):
        footer_block = ',\n        "footer": {\n'
        for k, v in trans.items():
            footer_block += f'            "{k}": "{v}",\n'
        footer_block = footer_block.rstrip(',\n') + '\n        }\n'
        return m.group(1) + m.group(2) + footer_block + m.group(3)

    content = re.sub(lang_pattern, repl_lang, content, count=1)


old_footer = """  <footer class="footer">
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
  </footer>"""

new_footer = """  <footer class="footer">
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
          <li><a href="{data['img_prefix']}#concierge">{data['footer']['nav_concierge']}</a></li>
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
  </footer>"""

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print("Replaced footer templates!")
else:
    print("Warning: old_footer string not found in content!")

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Done!")
