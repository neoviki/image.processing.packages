'''
{ The following code is free. Happy sharing :-) }

[[Author]] [[ Vignesh Natarajan ]] [[ www.vikiworks.io ]]
'''

'''
	This function pastes/overlaps given foreground image onto a background image

	The foreground image will be aligned centered on top of the background image

	Note:
		background image should be larger than the foreground image
'''

from PIL import Image

def overlap_two_images(background_image, foreground_image):
	foreground_image_width = foreground_image.width
	foreground_image_height = foreground_image.height
	background_image_width = background_image.width
	background_image_height = background_image.height

	#foreground image displacement calculation
	image_displacement_from_top	= int(background_image_height/2) - int(foreground_image_height/2)
	image_displacement_from_left = int(background_image_width/2) - int(foreground_image_width/2)

	background_image.paste(foreground_image, (image_displacement_from_left, image_displacement_from_top))
	return background_image

def save_image(image, image_path, image_file_name):
	image_file_location = image_path + "/" + image_file_name
	image.save(image_file_location)

def open_image(image_path, image_file_name):
	image_file_location = image_path + "/" + image_file_name
	image = Image.open(image_file_location)
	return image

def main():
	background_image_width		= 567
	background_image_height 	= 567
	image_path = "."
	image_name = "resized_image.jpg"
	overlaped_image_name = "overlapped.png"

	#Create a canvas
	background_image = Image.new("RGB", (background_image_width, background_image_height), "white")

	#Open foreground_image
	foreground_image = open_image(image_path, image_name)

	overlap_two_images(background_image, foreground_image)

	save_image(background_image, image_path, overlaped_image_name)

main()
