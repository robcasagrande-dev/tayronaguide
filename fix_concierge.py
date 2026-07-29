import json
import re

with open("tours_girona_travels.json", "r", encoding="utf-8") as f:
    tours = json.load(f)

img_map = {t["id"]: t["image"] for t in tours}

with open("concierge-module.js", "r", encoding="utf-8") as f:
    content = f.read()

# Add images to ACTIVITIES
for tour_id, img_path in img_map.items():
    pattern = r"(id:\s*'" + re.escape(tour_id) + r"',)"
    replacement = r"\1\n      image: '" + img_path + r"',"
    content = re.sub(pattern, replacement, content)

# Fix the rendering
old_render = """<button class="concierge-option ${selected}" data-wishlist="${act.id}" style="text-align:left;">
        <div style="font-size:1.5rem;margin-bottom:5px;">${act.emoji}</div>
        <div class="option-label" style="text-align:left;">${txt(act.name)}</div>
        <div class="option-sub" style="text-align:left;margin-top:4px;opacity:0.8;">${txt(act.desc)}</div>
      </button>"""

new_render = """<button class="concierge-option ${selected}" data-wishlist="${act.id}" style="text-align:left; padding: 0; overflow: hidden; display: flex; flex-direction: column; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--c-border); transition: all 0.3s ease;">
        ${act.image ? `<img src="${act.image}" alt="" style="width: 100%; height: 160px; object-fit: cover; border-bottom: 1px solid var(--c-border);">` : `<div style="font-size:1.5rem; padding: 15px 15px 0 15px;">${act.emoji}</div>`}
        <div style="padding: 16px;">
          <div class="option-label" style="text-align:left; font-size: 1.05rem; margin-bottom: 8px; font-weight: 600; color: white;">${txt(act.name)}</div>
          <div class="option-sub" style="text-align:left; opacity:0.75; font-size: 0.85rem; line-height: 1.4;">${txt(act.desc)}</div>
        </div>
      </button>"""

if old_render in content:
    content = content.replace(old_render, new_render)
    print("Render block replaced successfully.")
else:
    print("WARNING: Render block not found!")

with open("concierge-module.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated concierge-module.js")
