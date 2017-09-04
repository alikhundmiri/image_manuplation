from PIL import Image
import os
# All your images should be here
BASE_DIR = '/Users/alikhundmiri/Desktop/sample_images/'

#the desired output file size
size_thumbnail = (300, 180)

for f in os.listdir(BASE_DIR):
    # check if the files are image
    if f.endswith('.png' or '.jpg' or '.jpeg'):
        # Make the image object
        i = Image.open(BASE_DIR+f)
        # split the image name
        fname, fext = os.path.splitext(f)
        # resize to the desired size, This will ensure the images are in ratio.
        i.thumbnail(size_thumbnail)
        # save in thumbnails directory
        i.save('{}thumbnails/{}_thumbnail.{}'.format(BASE_DIR, fname, fext))
