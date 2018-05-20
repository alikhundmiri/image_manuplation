from PIL import Image
import os
import sys
import datetime

# All your images should be here
BASE_DIR = '/Users/alikhundmiri/Desktop/'
DESKFILE = "_ARCHIVES/"

IMAGES = "_IMAGES/"
DOCUMENTS = "_DOCUMENTS/"
VIDEOS  = "_VIDEOS/"
AUDIOS = "_AUDIOS/"

AUDIO_EXTENSIONS = ['.mp3',]
DOCUMENT_EXTENSIONS = ['.pdf','.txt',]
IMAGE_EXTENSIONS = ['.png','.jpg','.jpeg',]
VIDEO_EXTENSIONS = [".mp4", '.avi', '.mkv',]
# WEEK_FILE = ''
# WEEK_PATH = ''

def move_files(WEEK_FILE):
    _file = BASE_DIR + DESKFILE
    print("\n Directories")
    print("BASE_DIR: " + BASE_DIR)
    print("WEEK_FILE: " + WEEK_FILE)
    print("\n")
    for f in os.listdir(BASE_DIR):

        if f.endswith(tuple(IMAGE_EXTENSIONS)):
            print("Working on :\t"+f)
            create_type_folder(WEEK_FILE, IMAGES)
            src = BASE_DIR + f
            dst = _file + IMAGES + WEEK_FILE + f
            os.rename(src, dst)
            print("IMAGE \t:" + str(dst) + "\n")


        if f.endswith(tuple(DOCUMENT_EXTENSIONS)):
            print("Working on :\t"+f)
            create_type_folder(WEEK_FILE, DOCUMENTS)
            src = BASE_DIR + f
            dst = _file + DOCUMENTS + WEEK_FILE + f
            os.rename(src, dst)
            print("DOCUMENT \t:" + str(dst) + "\n")


        if f.endswith(tuple(VIDEO_EXTENSIONS)):
            create_type_folder(WEEK_FILE, VIDEOS)
            print("Working on :\t"+f)
            src = BASE_DIR + f
            dst = _file + VIDEOS + WEEK_FILE + f
            os.rename(src, dst)
            print("VIDEO \t:" + str(dst) + "\n")


        if f.endswith(tuple(AUDIO_EXTENSIONS)):
            create_type_folder(WEEK_FILE, AUDIOS)
            print("Working on :\t"+f)
            src = BASE_DIR + f
            dst = _file + AUDIOS + WEEK_FILE + f
            os.rename(src, dst)
            print("AUDIO \t:" + str(dst) + "\n")            
    print("---------------------------------------------------------------------------------")


def create_type_folder(WEEK_FILE, NAME):
    type_folder = BASE_DIR + DESKFILE + NAME + WEEK_FILE
    if not os.path.exists(type_folder):
        print("Creating directory\t\t:\t\t" + type_folder)
        os.makedirs(type_folder)
    else:
        pass

def create_date_folder():
    today = datetime.date.today()
    week = today.strftime("%d")
    year = today.year
    month = today.strftime("%B")
    WEEK_FILE = str(week) +"_"+ str(month) +"_"+ str(year) + "/"
    
    WEEK_PATH = BASE_DIR + DESKFILE + WEEK_FILE


    # if not os.path.exists(WEEK_PATH):
    #     print('Creating directory\t\t:\t\t' + WEEK_FILE)
    #     os.makedirs(WEEK_PATH)
    # else:
    #     print("Directory already exists\t:\t\t" + WEEK_FILE)
    # print("---------------------------------------------------------------------------------")
    return WEEK_FILE

def create_desktop_folder():
    f = DESKFILE
    if not os.path.exists(f):
        print('Creating Directory\t\t:\t\t' + f)
        os.makedirs(f)
    else:
        print('Directory already exists\t:\t\t' + f)
    print("---------------------------------------------------------------------------------")
    # os.chdir(f)


if __name__ == "__main__":

    bypass_UI = False
    input_1 = None

    if len(sys.argv) > 1:
        input_1 = sys.argv[1]
        if input_1 == 'auto':
            bypass_UI = True

    os.chdir(BASE_DIR)

    if not bypass_UI:
        print("\n\n============================ I N S T R U C T I O N S ============================\n\n")
        print("All the images on the desktop will be moved to __IMAGES folder.\n\n")
        print("\t T H E    F I L E     S T R U C T U R E ")
        print("\n")
        print("\t Desktop")
        print("\t ├── _ARCHIVES")
        print("\t │     ├── _AUDIOS")
        print("\t │     │     ├── _DATE_MONTH_YEAR")
        print("\t │     │     │    ├── Your audio file 1")
        print("\t │     │     │    ├── Your audio file 2")
        print("\t │     │     │    └── Your audio file nth")
        print("\t │     ├── _DOCUMENTS")
        print("\t │     │     ├── _DATE_MONTH_YEAR")
        print("\t │     │     │     ├── Your document file 1")
        print("\t │     │     │     ├── Your document file 2")
        print("\t │     │     │     └── Your document file nth")
        print("\t │     ├── _IMAGES")
        print("\t │     │     ├── _DATE_MONTH_YEAR")
        print("\t │     │     │     ├── Your image file 1")
        print("\t │     │     │     ├── Your image file 2")
        print("\t │     │     │     └── Your image file nth")
        print("\t │     ├── _VIDEOS")
        print("\t │     │     ├── _DATE_MONTH_YEAR")
        print("\t │     │     │     ├── Your video file 1")
        print("\t │     │     │     ├── Your video file 2")
        print("\t │     │     │     └── Your video file nth")
        print("\n\n")

        signal = input("Whenever you are ready, Press 'y' to continue or anything else to exit.")
        print("---------------------------------------------------------------------------------")
        if signal == 'y':
            pass
        else:
            sys.exit("Closing the program")
    

    create_desktop_folder()             # create "_IMAGES" folder
    WEEK_FILE = create_date_folder()         # Create 'week_year' folder
    move_files(WEEK_FILE)
    print("\n\n======================== T H A T ' S   A L L   F O L K S ========================\n\n")
