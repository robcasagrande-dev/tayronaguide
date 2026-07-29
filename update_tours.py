import os
import re
import json

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the link in the "See All" button
pattern_cta = re.compile(r"<a href=\"#concierge\" class=\"btn btn-accent btn-lg glow-btn\"(.*?)>(\s*)See All Girona Travels Tours")
# we need to replace it with `<a href="{data['img_prefix']}tours.html" ...>`
# Actually we can just find `<a href="#concierge" class="btn btn-accent btn-lg glow-btn"` inside the tours-cta-wrap
content = content.replace(
    '<a href="#concierge" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;">\n          See All Girona Travels Tours &rarr;',
    '<a href="{data[\'img_prefix\']}tours.html" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;">\n          See All Girona Travels Tours &rarr;'
)

# 2. Update the badge generation in index.html to support multiple badges
badge_html_logic = """
        badges_list = t.get("badges", [])
        if t.get("badge"):
            # legacy fallback
            badges_list = [{"label": t.get("badge"), "class": t.get("badge_class", "")}]
            
        badge_html = "<div class=\\"tour-img-badges\\">"
        for b in badges_list:
            badge_html += f\"\"\"<span class="tour-img-badge {b.get('class', '')}">{b.get('label', '')}</span>\"\"\"
        badge_html += "</div>"
"""
# Replace the old badge logic in build_languages.py
old_badge_logic = 'badge_html = f"""<span class="tour-img-badge {t.get("badge_class", "")}"> {t.get("badge", "")}</span>""" if t.get("badge") else ""'
content = content.replace(old_badge_logic, badge_html_logic)

# 3. We need to add code to generate tours.html inside the main loop in build_languages.py.
# Find the end of the loop where it writes index.html
write_index_logic = """    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {lang_code.upper()} -> {os.path.join(out_dir, 'index.html')}")"""

tours_page_logic = """
    # --- Generate tours.html ---
    all_tours_html = ""
    for t in tours_data:
        lang_key = lang_code if lang_code in t["nombre"] else "en"
        badges_list = t.get("badges", [])
        if t.get("badge"):
            badges_list = [{"label": t.get("badge"), "class": t.get("badge_class", "")}]
            
        badge_html = "<div class=\\"tour-img-badges\\">"
        for b in badges_list:
            badge_html += f\"\"\"<span class="tour-img-badge {b.get('class', '')}">{b.get('label', '')}</span>\"\"\"
        badge_html += "</div>"
        
        highlights_html = ""
        for h in t.get("highlights", []):
            highlights_html += f"<span>{h}</span>\\n                "
            
        all_tours_html += f\"\"\"
        <div class="tour-card reveal">
          <div class="tour-image-wrapper">
            {badge_html}
            <img src="{t.get('image', '/images/tours/cabo_san_juan_tour.jpg')}" alt="{t['nombre'][lang_key]}" />
          </div>
          <div class="tour-card-body">
            <div>
              <h3 class="tour-title">{t['nombre'][lang_key]}</h3>
              <p class="tour-desc">{t['descripcion'][lang_key]}</p>
              <div class="tour-highlights">
                {highlights_html}
              </div>
            </div>
            <div class="tour-footer">
              <a href="{data['img_prefix']}index.html#concierge" class="btn btn-primary btn-block">Reserve via Concierge &rarr;</a>
            </div>
          </div>
        </div>
        \"\"\"

    tours_page_html = f\"\"\"<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Girona Travels Tours | TayronaGuide</title>
  <link rel="stylesheet" href="{data['img_prefix']}style.css">
</head>
<body>
  <!-- HEADER -->
  <header class="navbar">
    <div class="nav-container">
      <a href="{data['img_prefix']}index.html" class="brand">
        <span class="brand-icon">🌿</span> TayronaGuide
      </a>
      <div class="nav-links">
        <a href="{data['img_prefix']}index.html" class="nav-link">Home</a>
      </div>
    </div>
  </header>

  <main style="padding-top: 120px; padding-bottom: 80px; max-width: 1200px; margin: 0 auto; padding-left: 24px; padding-right: 24px;">
    <div class="section-header">
      <h2 class="section-title">All Girona Travels Tours</h2>
      <p class="section-lead">Explore our full catalog of guided experiences, eco-treks, and cultural adventures.</p>
    </div>
    <div class="tours-grid" style="margin-top: 40px;">
      {all_tours_html}
    </div>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <h3>TayronaGuide</h3>
        <p>The official 2026 concierge & travel hub.</p>
      </div>
    </div>
  </footer>
  <script src="{data['img_prefix']}script.js"></script>
</body>
</html>
\"\"\"
    with open(os.path.join(out_dir, 'tours.html'), 'w', encoding='utf-8') as f:
        f.write(tours_page_html)
    print(f"Generated {lang_code.upper()} tours -> {os.path.join(out_dir, 'tours.html')}")
"""

content = content.replace(write_index_logic, write_index_logic + "\n" + tours_page_logic)

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated build_languages.py")

# Update style.css to make `.tour-img-badges`
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

if ".tour-img-badges" not in css:
    css = css.replace(".tour-img-badge {", """.tour-img-badges {
  position: absolute;
  top: 16px; left: 16px;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-start;
}
.tour-img-badge {""")
    # Also we must remove `position: absolute; top: 16px; left: 16px;` from `.tour-img-badge`
    css = css.replace("position: absolute;\n  top: 16px; left: 16px;\n  z-index: 2;", "z-index: 2;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Updated style.css")

# Update tours_girona_travels.json to add badges to the first tour
with open("tours_girona_travels.json", "r", encoding="utf-8") as f:
    tdata = json.load(f)

for t in tdata:
    if t["id"] == "cabo-san-juan-tayrona":
        t["badges"] = [
            {"label": "Best Selling", "class": "badge-green"},
            {"label": "⚡ Skip The Line", "class": "badge-gold"}
        ]

with open("tours_girona_travels.json", "w", encoding="utf-8") as f:
    json.dump(tdata, f, indent=2, ensure_ascii=False)
print("Updated json")
