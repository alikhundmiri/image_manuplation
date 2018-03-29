# Image Manuplation
All the scripts written for image manuplation, such as blur, resize, or image resolution manager.
#### All the Files (3) Created for personal Use
These scripts were written to learn how Pillow works, but if you feel you can use it for your personal use, you are very much welcome.


## [sort_images.py](https://github.com/alikhundmiri/image_manuplation/blob/master/sort_images.py)
I recently started a new hobby of taking photos of the Moon, late in the night. For editing purpose it is suggested that we use RAW format to edit images. 

I prefer to keep my RAW files in a different directory. Simply.

This script's main purpose is to move RAW files ending with format `.NEF` to a new subfolder called `RAW`. This is suppose to save time when there are 100s of images in question.

### how to use:
1. Change the BASE_DIR if you wish.
2. Inside the BASE_DIR make a folder `new_images` and paste all the new images from DSLR
3. Run the Script
4. Enter the folder name you created: `new_images`
5. ???
6. Profit


## [desktop_image_blurrer.py](https://github.com/alikhundmiri/image_manuplation/blob/master/desktop_image_blurrer.py)
1. Install dependencies, ` pip install pillow `
2. Change the desktop location in the code
3. Place all the images you need to blur, in a folder called `blur_this`, this folder should be in your desktop
4. Run the script
5. ???
6. Profit


## [desktop_image_resizer.py](https://github.com/alikhundmiri/image_manuplation/blob/master/desktop_image_resizer.py)
1. Install dependencies, ` pip install pillow `
2. Change the desktop location in the code
3. Add the sizes you require in the code list `sizes`
4. Add the extensions of images, if not included in `IMAGE_EXTENSIONS`
5. Place all the images you need to resize in your desktop
6. Run the script
7. ???
8. Profit


## Libraries used
Pillow
` pip install  pillow `

## Known Bugs
### [desktop_image_blurrer.py](https://github.com/alikhundmiri/image_manuplation/blob/master/desktop_image_blurrer.py)
This script is not working, If you can solve it, it would be of great help.
### [desktop_image_resizer.py](https://github.com/alikhundmiri/image_manuplation/blob/master/desktop_image_resizer.py)
Doesn't give feedback if no images are found in background
