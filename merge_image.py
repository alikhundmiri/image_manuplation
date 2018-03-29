from PIL import Image
BASE_DIR = '/Users/alikhundmiri/Desktop/test_01/'
DEFAULT_DIR = '/Users/alikhundmiri/Desktop/trials_money/'

def merge_images():
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """

    image1 = Image.open(BASE_DIR + 'sample_missy.png')
    image2 = Image.open(BASE_DIR + 'sample_missy.png')

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.save(BASE_DIR + 'merge_two.png')  # save it
    # return result

def story_vote(file_one, file_two, versus_no, divider_no, output_name, payment):

    vs = Image.open(DEFAULT_DIR + "perms/vs/" + 'vs_' + str(versus_no) + '.png')
    divider = Image.open(DEFAULT_DIR + "perms/lines/" + '638x50_border_' + str(divider_no) + '.png')
    image1 = Image.open(BASE_DIR + file_one)
    image2 = Image.open(BASE_DIR + file_two)
    placeholder = Image.open(DEFAULT_DIR + 'placeholder_watermark1.png')
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    # D I A G O N A S T I C S
    print("Height 1 : " + str(height1))
    print("Width 1 : " + str(width1))
    print("\t")
    print("Height 2 : " + str(height2))
    print("Width 2 : " + str(width2))

    # TODO
    # DONE convert images to square
    # DONE which ever image is largest, being it down to size of lower's resolution


    longer_side1 = min(image1.size)
    image1 = image1.crop((0,0,longer_side1,longer_side1))

    longer_side2 = min(image2.size)
    image2 = image2.crop((0,0,longer_side2,longer_side2))

    if longer_side1 <= longer_side2:
        image2.thumbnail((longer_side1, longer_side1))
    else:
        image1.thumbnail((longer_side2, longer_side2))

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_height = height1 + height2
    result_width = max(width1, width2)

    print("\t")
    print("result Height: " + str(result_height))
    print("result Width: " + str(result_width))

    # D I A G O N A S T I C S
    print("\t")
    print("\t")
    print("height 1 : " + str(height1))
    print("width 1 : " + str(width1))
    print("\t")
    print("height 2 : " + str(height2))
    print("width 2 : " + str(width2))

    story = Image.new('RGB', (result_width, result_height))
    story.paste(im=image1, box=(0, 0))
    story.paste(im=image2, box=(0, height1))

    # This line of code will paste the divider line and the VS words on to image,
    # This line looks different that's because we are pasting a transparent image,
    # this require a Mask, that the last variable on the code
    story.thumbnail((638, 1200))

    story.paste(divider, (0, 470), divider)

    if divider_no == 9:
        # move left
        story.paste(vs, (0, 450), vs)
        pass
    elif divider_no == 10:
        # move right
        story.paste(vs, (500, 450), vs)
        pass

    elif divider_no == 12:
        # move left
        story.paste(vs, (35, 450), vs)

    elif divider_no == 13:
        # move right
        story.paste(vs, (490, 450), vs)

    else:
        # keep in center
        story.paste(vs, (240, 450), vs)

    if payment:
        pass
    else:
        story.paste(placeholder, (0, 0), placeholder)
    # TODO
    # DONE add VS line, height1 - 20px, 0
    # DONE add VS text, height1 - 20px. width1/2

    story.save(BASE_DIR + 'compares/' + output_name)

if __name__ == "__main__":

    file_one = "batman_comic.jpg"
    file_two = "arrow_comic.jpg"
    versus = 8
    divider = 12
    compare_name = "compare_04.png"
    paid = True
    story_vote(file_one, file_two, versus, divider, compare_name, paid)
