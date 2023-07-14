from PIL import Image, ImageDraw
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'white_screen.png'
NEW_IMAGE = ROOT_FOLDER / 'New_screen.png'


with Image.open(IMAGE_PATH) as image:

    width, height = image.size

    draw = ImageDraw.Draw(image)

    # Red semi-circule
    for i in range(height + 1):

        draw.line((i, 0, 225, i), fill=(255, 0, 0))
        # draw.line((225, 0, i, i), fill=(255, 0, 0))

    # Blue semi-circule
    for i in range(height + 1):

        draw.line((i, 225, 0, i), fill=(0, 0, 255))

    # Yellow semi-circule
    for i in range(height + 1):

        draw.line((225, i, 225 - i, 225), fill=(255, 255, 0))

    # Green semi-circule
    for i in range(height + 1):

        draw.line((0, i, 255 - i, 0), fill=(0, 255, 0))

    # write to stdout
    image.save(NEW_IMAGE)
