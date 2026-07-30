import json
import os

with open('tours_girona_travels.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tours JSON Test Page</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #f8fafc; color: #334155; padding: 20px; }
  .tour-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 20px; padding: 20px; display: flex; gap: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
  .tour-image { width: 300px; height: 200px; object-fit: cover; border-radius: 4px; }
  .tour-content { flex: 1; }
  h2 { margin-top: 0; color: #0f172a; }
  h4 { margin: 10px 0 5px 0; color: #475569; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; }
  p { line-height: 1.5; margin: 0 0 10px 0; }
  .lang-block { background: #f1f5f9; padding: 10px; border-radius: 4px; margin-bottom: 10px; }
</style>
</head>
<body>
<h1>Tours JSON Data Inspector</h1>
"""

for tour in tours:
    # Handle potentially missing fields or strings
    def get_lang_text(field_name, field_data):
        if isinstance(field_data, dict):
            langs = []
            for lang, text in field_data.items():
                langs.append(f"<strong>{lang.upper()}:</strong> {text}")
            return "<br>".join(langs)
        return str(field_data)

    img_src = tour.get('image', '')
    name_html = get_lang_text('nombre', tour.get('nombre', ''))
    short_desc_html = get_lang_text('descripcion_corta', tour.get('descripcion_corta', ''))
    long_desc_html = get_lang_text('descripcion', tour.get('descripcion', ''))

    html += f"""
    <div class="tour-card">
        <img src="{img_src}" alt="Tour Image" class="tour-image" />
        <div class="tour-content">
            <h2>{tour.get('id', 'Unknown ID')}</h2>
            
            <h4>Name</h4>
            <div class="lang-block">{name_html}</div>
            
            <h4>Short Description (descripcion_corta)</h4>
            <div class="lang-block">{short_desc_html}</div>
            
            <h4>Long Description (descripcion)</h4>
            <div class="lang-block">{long_desc_html}</div>
        </div>
    </div>
    """

html += """
</body>
</html>
"""

# Write to root and public for visibility
with open('tours_test.html', 'w', encoding='utf-8') as f:
    f.write(html)

if os.path.exists('public'):
    with open('public/tours_test.html', 'w', encoding='utf-8') as f:
        f.write(html)
if os.path.exists('dist'):
    with open('dist/tours_test.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Test page generated successfully!")
