IMAGE_EXTENSIONS = ['.png','.jpg','.jpeg']
BASE_DIR    = '../Desktop/'
ARCHIVE_DIR = '../Desktop/_ARCHIVES/_IMAGES'

def archive_images():
    # Get the Date
    today = datetime.date.today()
    week = today.strftime("%d")
    year = today.year
    month = today.strftime("%B")
    # Generate week file. Example '2019_12/'
    WEEK_FILE = str(year) +"_"+ str(week) + "/"

    for f in os.listdir(BASE_DIR):
        if f.endswith(tuple(IMAGE_EXTENSIONS)):
            print("Working on :\t"+f)
            src = BASE_DIR    + f
            dst = ARCHIVE_DIR + WEEK_FILE + f
            os.rename(src, dst)
            print("Image : " + str(f) + " Archived\n")