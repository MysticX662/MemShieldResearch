import re

html = open('MemShield_WhitePaper_Final.html').read()

# Find all imgs
imgs = re.findall(r'<img[^>]*>', html)

# Replace IMG 1 (Bar chart) and IMG 2 (Line chart)
new_html = html
for img in imgs:
    if 'Bar chart' in img:
        new_img = re.sub(r'src="data:image/png;base64[^"]*"', 'src="figures/performance_chart.png"', img)
        new_html = new_html.replace(img, new_img)
    elif 'Line chart' in img:
        new_img = re.sub(r'src="data:image/png;base64[^"]*"', 'src="figures/trust_decay.png"', img)
        new_html = new_html.replace(img, new_img)
    elif 'Revsoc' in img:
        new_img = re.sub(r'src="data:image/png;base64[^"]*"', 'src="figures/cover_graphic.png"', img)
        new_html = new_html.replace(img, new_img)

with open('MemShield_WhitePaper_Final.html', 'w') as f:
    f.write(new_html)

print("Images replaced.")
