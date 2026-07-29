import json

# 1. Update style.css
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

if ".tour-ribbon" not in css:
    css += """
.tour-ribbon {
  position: absolute;
  top: 24px;
  right: -32px;
  width: 140px;
  background: var(--c-gold);
  color: #000;
  text-align: center;
  font-weight: 800;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 6px 0;
  transform: rotate(45deg);
  z-index: 5;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}
"""
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated style.css")

# 2. Update tours_girona_travels.json
with open("tours_girona_travels.json", "r", encoding="utf-8") as f:
    tdata = json.load(f)

for t in tdata:
    if t["id"] == "cabo-san-juan-tayrona":
        t["badges"] = [{"label": "Best Selling", "class": "badge-green"}]
        t["ribbon"] = "⚡ Fast-Track"

with open("tours_girona_travels.json", "w", encoding="utf-8") as f:
    json.dump(tdata, f, indent=2, ensure_ascii=False)
print("Updated json")

# 3. Update build_languages.py
with open("build_languages.py", "r", encoding="utf-8") as f:
    content = f.read()

# For the dynamic_tours_html
content = content.replace(
    '        badge_html = "<div class=\\"tour-img-badges\\">"',
    '        ribbon_html = f"""<div class=\\"tour-ribbon\\">{t.get("ribbon", "")}</div>""" if t.get("ribbon") else ""\n        badge_html = "<div class=\\"tour-img-badges\\">"'
)
content = content.replace(
    '            {badge_html}\n            <img src="{t.get("image", "")}" alt="{t["nombre"][lang_key]}" />',
    '            {ribbon_html}\n            {badge_html}\n            <img src="{t.get("image", "")}" alt="{t["nombre"][lang_key]}" />'
)

# For the all_tours_html (which uses single quotes for img src)
content = content.replace(
    '            {badge_html}\n            <img src="{t.get(\'image\', \'/images/tours/cabo_san_juan_tour.jpg\')}" alt="{t[\'nombre\'][lang_key]}" />',
    '            {ribbon_html}\n            {badge_html}\n            <img src="{t.get(\'image\', \'/images/tours/cabo_san_juan_tour.jpg\')}" alt="{t[\'nombre\'][lang_key]}" />'
)

with open("build_languages.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_languages.py")
