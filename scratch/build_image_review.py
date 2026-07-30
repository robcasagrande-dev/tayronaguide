import os
import shutil

art_dir = '/home/robi/.gemini/antigravity/brain/7ecbfb4a-3827-4729-b7fd-775771da9c1a'
imgs = [
    ('free_time_villa_maria.jpg', '/home/robi/Projects/tayronaguide.com/images/tours/free_time_villa_maria.jpg'),
    ('free_time_villa_maria_v2.jpg', '/home/robi/Projects/tayronaguide.com/images/tours/free_time_villa_maria_v2.jpg'),
    ('free_time_villa_maria_v3.jpg', '/home/robi/Projects/tayronaguide.com/images/tours/free_time_villa_maria_v3.jpg'),
    ('villamaria_base.jpg', '/home/robi/Projects/tayronaguide.com/images/rooms/villamaria-base.jpg'),
    ('villamaria_mid.jpg', '/home/robi/Projects/tayronaguide.com/images/rooms/villamaria-mid.jpg'),
    ('villamaria_top.jpg', '/home/robi/Projects/tayronaguide.com/images/rooms/villamaria-top.jpg')
]

md = '# Villa María Image Options Review\n\nPlease check which of the following images is the correct one for **Free Time at Villa María Tayrona**:\n\n'

for name, src in imgs:
    if os.path.exists(src):
        dst = os.path.join(art_dir, name)
        shutil.copy2(src, dst)
        md += f'### Option: `{name}`\n![{name}]({dst})\n\n---\n\n'

with open(os.path.join(art_dir, 'villa_maria_images_review.md'), 'w', encoding='utf-8') as f:
    f.write(md)

print('Generated review document successfully')
