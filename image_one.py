from PIL import Image
import os
BASE_DIR = '/Users/alikhundmiri/Desktop/sample_images/'
size_thumbnail = (300,300)

for f in os.listdir(BASE_DIR):
    if f.endswith('.png'):
        i = Image.open(BASE_DIR+f)
        fname, fext = os.path.splitext(f)
        i.thumbnail(size_thumbnail)
        i.save('{}thumbnails/{}_thumbnail.{}'.format(BASE_DIR, fname, fext))
# image1 = Image.open("/Users/alikhundmiri/Desktop/sample_images/cipher_1.png")
#
# image1.save("/Users/alikhundmiri/Desktop/sample_images/cipher_1.jpg")