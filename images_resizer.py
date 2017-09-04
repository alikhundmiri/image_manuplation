from PIL import Image
import os
# All your images should be here
BASE_DIR = '/Users/alikhundmiri/Desktop/sample_images/'
os.chdir(BASE_DIR)

#the desired output file size
size_thumbnail = (300, 180)
size_blog = (600,600)
size_work = (1000, 1000)

def image_resizer():
    for f in os.listdir(BASE_DIR):
        # check if the files are image
        if f.endswith('.png' or '.jpg' or '.jpeg'):
            print("Working on : "+f)
            # Make the image object
            i = Image.open(BASE_DIR+f)
            # split the image name
            fname, fext = os.path.splitext(f)

            ######    B L O G S       I M A G E S     F O R       H I G H    D E F I N A T I O N
            i.thumbnail(size_work)
            i.save('{}work/{}_work{}'.format(BASE_DIR, fname, fext))

            ######    B L O G S       I M A G E S     F O R       L I S T
            i.thumbnail(size_blog)
            i.save('{}blog/{}_blog{}'.format(BASE_DIR, fname, fext))

            ######    T H U M B N A I L S       G E N E R A T O R S
            i.thumbnail(size_thumbnail)
            i.save('{}thumbnail/{}_thumbnail{}'.format(BASE_DIR, fname, fext))
        else:
            print("cant work on : " + f)

def create_folders():
    folders = ["thumbnail", "work", "blog"]
    for f in folders:
        if not os.path.exists(f):
            print('Creating directory : ' + f)
            os.makedirs(f)
        else:
            print("Directory already exists : " + f)


if __name__ == "__main__":
    create_folders()
    image_resizer()