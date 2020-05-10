
'''
{ This piece of code is free. Happy sharing :-) }

[[Author]] [[ Vignesh Natarajan ]] [[ www.vikiworks.io ]]
'''

import pygame
import os
import sys
from random import shuffle

def static_variable(**args):
    def decorate(function):
        for i in args:
            setattr(function, i, args[i])
        return function
    return decorate


#Create a display
def screen_create(screen_name, width, height):
	pygame.init()
	#pygame.display.init()
	pygame.display.set_caption(screen_name)
	screen = pygame.display.set_mode((width, height))
	white = [255, 255, 255]
	screen.fill(white)
	return screen

def screen_update():
	pygame.display.update()

def clock_create():
	return pygame.time.Clock()

#Update the clock with a delay (delay can be 0)
#delay should be in frames per second
def clock_update(clock, delay):
	clock.tick(delay)

#clear the screen (screen will become full white after this call)
def screen_clear(screen):
	white = [255, 255, 255]
	screen.fill(white)


#display given image on the screen at x, y coordinates
def screen_display(screen, x, y, image):
	screen_clear(screen)
	screen.blit(image, (x, y))

#align image at center of the screen
def screen_display_align_center(screen, image):
	screen_clear(screen)
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	center_x = (screen_width/2) - (image_width/2)
	center_y = (screen_height/2) - (image_height/2)
	screen_display(screen, center_x, center_y, image)

#align image at the left side of the screen with white margin space
def screen_display_align_left(screen, image, margin):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = margin
	y = (screen_height/2) - (image_height/2)
	screen_display(screen, x, y, image)


#align image at the right side of the screen with white margin space
def screen_display_align_right(screen, image, margin):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = screen_width -  image_width	 - margin
	y = (screen_height/2) - (image_height/2)
	screen_display(screen, x, y, image)


#align image at the top of the screen with white margin space
def screen_display_align_top(screen, image, margin):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = (screen_width/2) - (image_width/2)
	y = margin
	screen_clear(screen)
	screen_display(screen, x, y, image)


#align image at the bottom of the screen with white margin space
def screen_display_align_bottom(screen, image, margin):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = (screen_width/2) - (image_width/2)
	y = screen_height - image_height - margin
	screen_display(screen, x, y, image)

def screen_displace_image_horizantal(screen, image, displacement):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = displacement
	y = (screen_height/2) - (image_height/2)
	screen_display(screen, x, y, image)

def screen_displace_image_vertical(screen, image, displacement):
	screen_clear(screen)
	image_width, image_height = image.get_rect().size
	screen_width, screen_height = pygame.display.get_surface().get_size()
	x = (screen_width/2) - (image_width/2)
	y = displacement
	screen_clear(screen)
	screen_display(screen, x, y, image)



#Scroll screen with dx rate in x axis and dy rate towards y axis
def screen_scroll(screen, dx, dy):
	screen.scroll(dx, dy)

#Scroll screen vertically
def screen_scroll_vertical(screen, rate):
	screen.scroll(0, rate)

#Scrool screen horizantally
def screen_scroll_horizantal(screen, rate):
	screen.scroll(rate, 0)



'''
Get images with full location info inside the given path and add them to a list

Note: This function shuffel the image list before returning
'''
def get_image_list(path):
	image_list = os.listdir(path)
	shuffle(image_list)
	return image_list

@static_variable(index=0)
def get_next_image_info(path, image_list):
	list_len = len(image_list)
	get_next_image_info.index = (get_next_image_info.index + 1)%list_len
	return (path + "/" + image_list[get_next_image_info.index])


def open_image(image_info):
	image = None
	try:
		image = pygame.image.load(image_info).convert_alpha()
	except:
		print "error(open) = ", image_info

	return image

#Check for game events and handle them
def check_and_handle_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
