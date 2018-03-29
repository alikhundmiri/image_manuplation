# THIS IS HOW TO OPEN IMAGES FROM INTERNET (AWS S3) USING PIL & Python3
from PIL import Image
from io import BytesIO
import requests

LINK = 'https://social-images-ritrew-1.s3.amazonaws.com/media/BASE_FILES_STORY/vs/vs_2.png'

def open_AWS():
    response = requests.get(LINK)
    img = Image.open(BytesIO(response.content))
    img.show()
if __name__ == "__main__":
    open_AWS()
