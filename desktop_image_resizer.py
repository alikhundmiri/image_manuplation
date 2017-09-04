from PIL import Image
import os
import sys

# All your images should be here
BASE_DIR = '/Users/alikhundmiri/Desktop/'
print(BASE_DIR)
os.chdir(BASE_DIR)
IMAGE_EXTENSIONS = ['.png','.jpg','.jpeg']
DESKFILE = "_CUSTOM_IMAGES"
#the desired output file size
sizes = [(300, 180), (600, 600), (1000,1000)]


def image_resizer():
    for f in os.listdir(BASE_DIR):
        # check if the files are image
        if f.endswith(tuple(IMAGE_EXTENSIONS)):

            print("Working on :\t"+f)
            # Make the image object
            i = Image.open(BASE_DIR+f)
            # split the image name
            fname, fext = os.path.splitext(f)

            for si in sizes:
                size_name = 'x'.join(str(s) for s in si) 
                i.thumbnail(tuple(si))
                i.save('{}{}/{}/{}_{}{}'.format(BASE_DIR, DESKFILE, size_name, fname, size_name, fext))
                print("\t\t\t\t\t " + "Created \t " + size_name)

            src = BASE_DIR + f
            dst = BASE_DIR + DESKFILE + "/" + f
            os.rename(src, dst)
            print("\t\t\t\t\t ORIGINAL\t moved to " + str(DESKFILE) + "\n")
            print("---------------------------------------------------------------------------------")

        # else:
        #     print("cant work on\t:\t" + f)

def create_folder():
    f = DESKFILE
    if not os.path.exists(f):
        print('Creating Directory\t\t:\t\t' + f)
        os.makedirs(f)
    else:
        print('Directory already exists\t:\t\t' + f)
    print("---------------------------------------------------------------------------------")
    os.chdir(f)

def change_image_dir():
    for f in os.listdir(BASE_DIR):
        if f. endswith(IMAGE_EXTENSIONS):
            pass

def create_sub_folders():
    folders = list(sizes)
    for f in folders:
        size_name = 'x'.join(str(s) for s in f)
        if not os.path.exists(size_name):
            print('Creating directory\t\t:\t\t' + size_name)
            os.makedirs(size_name)
        else:
            print("Directory already exists\t:\t\t" + size_name)
    print("---------------------------------------------------------------------------------")


if __name__ == "__main__":
    print("\n\n============================ I N S T R U C T I O N S ============================\n\n")
    print("Place all the images on the desktop, make sure the format is " + ", ".join(IMAGE_EXTENSIONS) + ".\n\n")
    signal = input("Whenever you are ready, Press 'y' to continue or anything else to exit.")
    print("---------------------------------------------------------------------------------")
    if signal == 'y':
        pass
    else:
        sys.exit("Closing the program")
    
    create_folder()
    # change_image_dir()
    create_sub_folders()
    image_resizer()
    print("\n\n======================== T H A T ' S   A L L   F O L K S ========================\n\n")
