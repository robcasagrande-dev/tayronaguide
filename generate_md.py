import json
import os
import urllib.parse

with open('/home/robi/Projects/tayronaguide.com/tours_girona_travels.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

md = "# Tours JSON Content Review\n\nThis document shows the exact content of the `tours_girona_travels.json` file for your review.\n\n"

for tour in tours:
    img = tour.get('image', '')
    if img.startswith('images/') or img.startswith('/images/'):
        # Copy image to artifact directory
        img_rel = img.lstrip('/')
        src_img = os.path.join('/home/robi/Projects/tayronaguide.com', img_rel)
        dest_img = os.path.join('/home/robi/.gemini/antigravity/brain/7ecbfb4a-3827-4729-b7fd-775771da9c1a', os.path.basename(img_rel))
        if os.path.exists(src_img):
            import shutil
            shutil.copy2(src_img, dest_img)
            img = dest_img
        else:
            img = ''
        
    md += f"## Tour ID: {tour.get('id', 'Unknown')}\n"
    if img:
        md += f"![{tour.get('id')}]({img})\n\n"
    
    # Nombre
    md += "### Name (`nombre`)\n"
    for lang, val in tour.get('nombre', {}).items():
        md += f"- **{lang.upper()}**: {val}\n"
    md += "\n"
    
    # Short Desc
    md += "### Short Description (`descripcion_corta`)\n"
    for lang, val in tour.get('descripcion_corta', {}).items():
        md += f"- **{lang.upper()}**: {val}\n"
    md += "\n"
    
    # Long Desc
    md += "### Long Description (`descripcion`)\n"
    for lang, val in tour.get('descripcion', {}).items():
        md += f"- **{lang.upper()}**: {val}\n"
    md += "\n---\n\n"

with open('/home/robi/.gemini/antigravity/brain/7ecbfb4a-3827-4729-b7fd-775771da9c1a/tours_json_review.md', 'w', encoding='utf-8') as f:
    f.write(md)
