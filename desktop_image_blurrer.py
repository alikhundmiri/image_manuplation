from PIL import Image, ImageFilter

import os
# All your images should be here
BASE_DIR = '/Users/alikhundmiri/Desktop/blur_this/'
os.chdir(BASE_DIR)

#the desired output file size
blur_10 = 10
blur_20 = 20
blur_30 = 30

def image_blurrer():
    for f in os.listdir(BASE_DIR):
        # check if the files are image
        if f.endswith('.png' or '.jpg' or '.jpeg'):

            print("Working on : "+f)
            # Make the image object
            i = Image.open(BASE_DIR+f)
            # split the image name
            fname, fext = os.path.splitext(f)

            i.filter(ImageFilter.BLUR())
            i.save('{}image_blur/{}_blur_30{}'.format(BASE_DIR, fname, fext))

        else:
            print("cant work on : " + f)

def create_folders():
    folders = ["image_blur",]

    for f in folders:
        if not os.path.exists(f):
            print('Creating directory : ' + f)
            os.makedirs(f)
        else:
            print("Directory already exists : " + f)


if __name__ == "__main__":
    print("\n\n====================== I N S T R U C T I O N S ======================\n\n")
    print("Place all the images on the desktop, make sure the format is .png, .jpg, jpeg.\n\n")
    input("Whenever you are ready, Press any key to continue...")
    create_folders()
    image_blurrer()