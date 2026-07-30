import sys

def patch_build():
    with open("build_languages.py", "r", encoding="utf-8") as f:
        content = f.read()
        
    old_code = """    # Load tours from JSON
    with open("tours_girona_travels.json", "r", encoding="utf-8") as tf:
        tours_data = json.load(tf)
    
    target_tour_ids = ["cabo-san-juan-tayrona", "ruinas-bunkuany", "tour-del-cacao"]
    selected_tours = [t for t in tours_data if t["id"] in target_tour_ids]
    
    # Sort them in the exact order requested
    selected_tours.sort(key=lambda x: target_tour_ids.index(x["id"]))

    dynamic_tours_html = ""
    for t in selected_tours:
        # Fallback to English if the current language is not available in the JSON
        lang_key = lang_code if lang_code in t["nombre"] else "en"
        
        # Build badges HTML
        badges_html = ""
        
        if "badge" in t and "badge_class" in t:
            badges_html += f'<span class="tour-badge {t["badge_class"]}">{t["badge"]}</span>\\n'
            
        if "badges" in t:
            for b in t["badges"]:
                badges_html += f'<span class="tour-badge {b["class"]}">{b["label"]}</span>\\n'
                
        # Build ribbon HTML
        ribbon_html = ""
        if "ribbon" in t:
            ribbon_html = f'<div class="tour-ribbon">{t["ribbon"]}</div>'
            
        # Build highlights HTML
        highlights_html = ""
        if "highlights" in t:
            highlights_html = '<div class="tour-highlights">'
            for h in t["highlights"]:
                highlights_html += f'<span class="highlight-item">{h}</span>'
            highlights_html += '</div>'

        tour_html = f'''
        <div class="tour-card reveal">
          {ribbon_html}
          <div class="tour-img-wrap">
            <img src="{data['img_prefix']}{t["image"].lstrip("/")}" alt="{t["nombre"][lang_key]}" class="tour-img">
            <div class="tour-badges">
              {badges_html}
            </div>
          </div>
          <div class="tour-content">
            <h3 class="tour-title">{t["nombre"][lang_key]}</h3>
            <p class="tour-desc">{t["descripcion"][lang_key]}</p>
            {highlights_html}
            <a href="#concierge" class="btn btn-accent tour-reserve-btn">Reserve via Concierge &rarr;</a>
          </div>
        </div>
        '''
        dynamic_tours_html += tour_html"""

    new_code = """    # Load tours from JSON
    with open("tours_girona_travels.json", "r", encoding="utf-8") as tf:
        tours_data = json.load(tf)
    
    all_tours = [t for t in tours_data if not t.get("id", "").startswith("free-time-")]
    
    target_tour_ids = ["cabo-san-juan-tayrona", "ruinas-bunkuany", "tour-del-cacao"]
    top_tours = [t for t in all_tours if t["id"] in target_tour_ids]
    top_tours.sort(key=lambda x: target_tour_ids.index(x["id"]))
    other_tours = [t for t in all_tours if t["id"] not in target_tour_ids]
    
    selected_tours = top_tours + other_tours

    dynamic_tours_html = ""
    for idx, t in enumerate(selected_tours):
        lang_key = lang_code if lang_code in t["nombre"] else "en"
        
        # Build badges HTML
        badges_html = ""
        if "badge" in t and "badge_class" in t:
            b_text = t["badge"].get(lang_key, t["badge"].get("en", "")) if isinstance(t["badge"], dict) else t["badge"]
            badges_html += f'<span class="tour-badge {t["badge_class"]}">{b_text}</span>\\n'
            
        if "badges" in t:
            b_list = t["badges"].get(lang_key, t["badges"].get("en", [])) if isinstance(t["badges"], dict) else t["badges"]
            for b in b_list:
                badges_html += f'<span class="tour-badge {b["class"]}">{b["label"]}</span>\\n'
                
        # Build ribbon HTML
        ribbon_html = ""
        if "ribbon" in t:
            r_text = t["ribbon"].get(lang_key, t["ribbon"].get("en", "")) if isinstance(t["ribbon"], dict) else t["ribbon"]
            ribbon_html = f'<div class="tour-ribbon">{r_text}</div>'
            
        # Build highlights HTML
        highlights_html = ""
        if "highlights" in t:
            h_list = t["highlights"].get(lang_key, t["highlights"].get("en", [])) if isinstance(t["highlights"], dict) else t["highlights"]
            highlights_html = '<div class="tour-highlights">'
            for h in h_list:
                highlights_html += f'<span class="highlight-item">{h}</span>'
            highlights_html += '</div>'

        hidden_class = " hidden-tour" if idx >= 3 else ""

        tour_html = f'''
        <div class="tour-card reveal{hidden_class}">
          {ribbon_html}
          <div class="tour-img-wrap">
            <img src="{data['img_prefix']}{t["image"].lstrip("/")}" alt="{t["nombre"][lang_key]}" class="tour-img">
            <div class="tour-badges">
              {badges_html}
            </div>
          </div>
          <div class="tour-content">
            <h3 class="tour-title">{t["nombre"][lang_key]}</h3>
            <p class="tour-desc">{t["descripcion"][lang_key]}</p>
            {highlights_html}
            <a href="#concierge" class="btn btn-accent tour-reserve-btn">{data["tours_page"]["reserve"]}</a>
          </div>
        </div>
        '''
        dynamic_tours_html += tour_html"""

    if old_code in content:
        content = content.replace(old_code, new_code)
    else:
        print("Failed to replace dynamic_tours_html logic")
        sys.exit(1)

    old_cta_button = """      <div class="tours-cta-wrap">
        <a href="{data['img_prefix']}tours.html" target="_blank" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;">
          See All Girona Travels Tours &rarr;
        </a>
      </div>"""
      
    new_cta_button = """      <div class="tours-cta-wrap">
        <button onclick="document.querySelectorAll('.hidden-tour').forEach(el => el.classList.remove('hidden-tour')); this.style.display='none';" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;cursor:pointer;border:none;">
          {data['tours_page']['title']} &rarr;
        </button>
      </div>"""

    if old_cta_button in content:
        content = content.replace(old_cta_button, new_cta_button)
    else:
        print("Failed to replace CTA button")
        sys.exit(1)

    with open("build_languages.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Patched build_languages.py!")

if __name__ == "__main__":
    patch_build()
