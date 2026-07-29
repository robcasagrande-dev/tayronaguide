import os

with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

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
        
        ribbon_html = f\"\"\"<div class="tour-ribbon">{t.get('ribbon', '')}</div>\"\"\" if t.get('ribbon') else ""
        
        highlights_html = ""
        for h in t.get("highlights", []):
            highlights_html += f"<span>{h}</span>\\n                "
            
        all_tours_html += f\"\"\"
        <div class="tour-card reveal">
          <div class="tour-image-wrapper">
            {ribbon_html}
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
    tours_file_path = os.path.join(out_dir, 'tours.html')
    with open(tours_file_path, 'w', encoding='utf-8') as f:
        f.write(tours_page_html)
    print(f"Generated {lang_code.upper()} tours -> {tours_file_path}")
"""

target = """    file_path = os.path.join(out_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {lang_code.upper()} -> {file_path}")"""

if "all_tours_html = " not in content:
    content = content.replace(target, target + "\n" + tours_page_logic)
    with open("build_languages.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully injected tours_page_logic")
else:
    print("tours_page_logic already exists")

# Also fix the CTA button target to open in a new tab
content = content.replace(
    'class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;">\n          See All Girona Travels Tours &rarr;',
    'target="_blank" class="btn btn-accent btn-lg glow-btn" style="padding:16px 40px;font-size:1.05rem;font-weight:700;border-radius:9999px;">\n          See All Girona Travels Tours &rarr;'
)
with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)
