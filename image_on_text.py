from PIL import Image, ImageFilter, ImageDraw, ImageFont
BASE_DIR = '/Users/alikhundmiri/Desktop/trials_money/'
import re


text_list = []
text_size = []


def take_two():
    # Take two is a code from stackoverflow, it detects the size of image, and assigns the proper font size.
    image = Image.open(BASE_DIR + 'sample_missy.png')
    draw = ImageDraw.Draw(image)
    txt = "wow, part 1"
    txt = "Yes babe, in the end, we are all only one, for this long, this is life of pie, 23.14323482840294, trust me, I do. FOREVER!"
    # This will split the text in to many lines after every 16 character
    print(len(txt))

    if len(txt) < 16:
        text_list = txt.split(",.|")
    else:
        pass

    text_list = re.findall(r'.{1,16}(?:\s+|$)', txt.title())
    w_i, h_i = image.size

    # text_list = ['Trust me', 'baby', 'I ate the last burger', 'xoxo']

    print("--- D E T A I L S ---")
    print("Image")
    print("\t\tHeight : " + str(h_i))
    print("\t\tWidth : " + str(w_i))


    # fontsize = 1  # starting font size
    # portion of image width you want text width to be
    # img_fraction = 0.50
    print("Final Individual Font Size")
    h = 25
    tot_h = 0
    for t in text_list:
        fontsize = 1  # starting font size

        # portion of image width you want text width to be
        img_fraction = 0.40
        font = ImageFont.truetype('/Users/alikhundmiri/Project1/Assets/Standard Assets/Fonts/OpenSans/OpenSansLight.ttf', fontsize)
        while font.getsize(t)[0] < img_fraction * image.size[0]:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype('/Users/alikhundmiri/Project1/Assets/Standard Assets/Fonts/OpenSans/OpenSansLight.ttf', fontsize)

        # optionally de-increment to be sure it is less than criteria
        fontsize -= 1
        font = ImageFont.truetype('/Users/alikhundmiri/Project1/Assets/Standard Assets/Fonts/OpenSans/OpenSansLight.ttf', fontsize)
        print(font.getsize(t))
        print('\t\t\t' + str(fontsize) + '\t\t : \t' + t)
        w_f, h_f = font.getsize(str(fontsize))

        draw.text((10, h), t, font=font, fill=(255,255,255,255))  # put the text on the image
        h += h_f
        tot_h += h
    print("\t\t\t"+str(tot_h-h) + "\t : \ttotal height")
    image.save(BASE_DIR+'take_six.png')  # save it


def create_text(i_size, i_text, i_align):
    # Create a transparent image, with the same size (1_size) as that of 'selected image'.
    # Write text (text) on it, depending on the alignment (i_align) type choosen, Left, Center, Right.
    # return i_textimage
    pass

if __name__ == "__main__":
    text_1 = "Every moment in a super hero's life is a challenge"
    text_2 = "He who is willing to think, must be willing to speak"
    # put_text_on_image(text_1, text_2)
    take_two()