"""
Generate small placeholder PNG icons into `notesassets/`.
Run: python generate_notesassets.py
Requires: Pillow (pip install pillow)
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = "notesassets"
os.makedirs(OUT_DIR, exist_ok=True)

icons = {
    "create.png": ("C", (66, 135, 245)),
    "open.png": ("O", (60, 179, 113)),
    "exit.png": ("X", (239, 83, 80)),
    "save_note.png": ("SN", (124, 77, 255)),
    "save.png": ("S", (124, 77, 255)),
    "back.png": ("<", (158, 158, 158)),
    "folder.png": ("F", (255, 193, 7)),
    "note.png": ("N", (3, 169, 244)),
    "delete.png": ("D", (244, 67, 54)),
    "export.png": ("E", (0, 150, 136)),
}

SIZE = (32, 32)
BG = (255, 255, 255, 0)

# load a default font
try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:
    font = ImageFont.load_default()

for name, (label, color) in icons.items():
    img = Image.new("RGBA", SIZE, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # draw rounded rectangle background
    padding = 2
    rect = [padding, padding, SIZE[0]-padding-1, SIZE[1]-padding-1]
    draw.rounded_rectangle(rect, radius=6, fill=color)
    # draw label centered (use textbbox or font.getsize for compatibility)
    try:
        bbox = draw.textbbox((0, 0), label, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except Exception:
        try:
            w, h = font.getsize(label)
        except Exception:
            w, h = 10, 10
    draw.text(((SIZE[0]-w)/2, (SIZE[1]-h)/2), label, fill=(255,255,255), font=font)
    path = os.path.join(OUT_DIR, name)
    img.save(path)
    print(f"Created: {path}")

print("Done. Place these files in your app's UI by loading from the notesassets folder.")