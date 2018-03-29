import os
import sys

IMAGE_EXTENSIONS = ['.PNG','.JPG','.JPEG', '.RAW', '.NEF']
BASE_DIR = '/Users/alikhundmiri/Desktop/Images/Night_Photography/'
file_name = ''
# setting the variables
counter_total = 0
counter_moved = 0

SHOW_ALL_RESULTS = False

def sorting():
	# move to location
	file_list = os.listdir(".")
	# iterate over all the files and folders
	for file in file_list:
		# Skip anything that does end with extensions provide in IMAGE_EXTENSIONS
		if file.endswith(tuple(IMAGE_EXTENSIONS)):
			# Delare global variables to increment them
			global counter_total
			global counter_moved	
			counter_total += 1
			if SHOW_ALL_RESULTS:
				print("Working on: " + str(file))
			name, extension = file.split(".")
			# specifying the curent location and the new location.
			src = BASE_DIR + file_name + file
			dst = BASE_DIR + file_name + "RAW/" + file
			# if raw files exist, move them to a new location
			if extension == "NEF":
				os.rename(src, dst)
				if SHOW_ALL_RESULTS:
					print("moved " + str(file) + "\t to RAW")
				counter_moved += 1


def create_raw_folder():
	f = "RAW"
	if not os.path.exists(f):
		# Creating a new folder
		print('Creating Directory\t\t:\t\t' + f)
		os.makedirs(f)
	else:
		print('Directory already exists\t:\t\t' + f)
	print("----------------------------------------------------------------------------------")

if __name__ == '__main__':
	# ask for file name
	print("\n\n============================ I N S T R U C T I O N S ============================\n\n")
	print("This will work ONLY for the files inside the folder:")
	print("\n\t{}\n").format(BASE_DIR)
	print("use exit() or Ctrl-D to exit the program \n\n")

	print("\n\n============================   U S E R    I N P U T   ============================\n\n")
	name = input("Please enter the file name: ")
	print("\n\n----------------------------------------------------------------------------------")
	if name:
		file_name = str(name) + str("/")
	else:
		sys.exit("Closing the program")

	os.chdir(BASE_DIR+file_name)

	# Create a RAW File if it doesnt exist already
	create_raw_folder()

	# start sorting
	sorting()

	# print results
	print("\n\n==============================    R E S U L T S    ===============================\n\n")
	print("Total Images Found\t\t:\t\t{}").format(counter_total)
	print("Total Images Moved\t\t:\t\t{}").format(counter_moved)

	print("\n\n======================== T H A T ' S   A L L   F O L K S ========================\n\n")
