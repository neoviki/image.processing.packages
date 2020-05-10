'''
{ The following code is free. Happy sharing :-) }

[[Author]] [[ Vignesh Natarajan ]] [[ www.vikiworks.io ]]
'''

import PIL
from PIL import Image

def open_image(image_path, image_file_name):
	image_file_location = image_path + "/" + image_file_name
	image = Image.open(image_file_location)
	return image

#resize the image within the specified height and width
def image_resize(image, max_width, max_height):
	original_image_width = float(image.size[0])
	original_image_height = float(image.size[1])

	resizing_width = max_width

	#Ratio between resizing image and actual image
	width_ratio = float( resizing_width / original_image_width)
	#height_ratio = float( resizing_height / original_image_height)

	resizing_height = int(original_image_height * width_ratio)

	while(resizing_height > max_height):
		resizing_width -= 1
		width_ratio = float( resizing_width / original_image_width)
		resizing_height = int(original_image_height * width_ratio)

	print "RESIZED IMAGE : ", resizing_width ,"X", resizing_height
	resized_image = image.resize((resizing_width, resizing_height), PIL.Image.ANTIALIAS)
	return resized_image

def save_image(image, image_path, image_file_name):
	image_file_location = image_path + "/" + image_file_name
	image.save(image_file_location)


def main():
	#Limit for max width or height
	MAX_WIDTH 	= 520
	MAX_HEIGHT 	= 520
	image_path = "."
	image_file_name = "img.jpg"
	resized_image_file_name = "resized_image.jpg"
	image = open_image(image_path, image_file_name)
	resized_image = image_resize(image, MAX_WIDTH, MAX_HEIGHT)
	save_image(resized_image, image_path, resized_image_file_name)

main()


