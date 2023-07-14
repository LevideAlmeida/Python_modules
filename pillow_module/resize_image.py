# Pillow:
# This library is the Photoshop of Python 😂
# Doc: https://pillow.readthedocs.io/en/stable/index.html
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'Image.png'
NEW_IMAGE = ROOT_FOLDER / 'New_image.png'

pil_image = Image.open(IMAGE_PATH)
width, height = pil_image.size

new_width = width // 5
new_height = new_width * height // width


new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=100
)
pil_image.close()
