import pygame
# initialize pygame
pygame.init()

# create screen
screen =  pygame.display.set_mode((1450,700))

# title and icon 
pygame.display.set_caption("Diamonds")
icon = pygame.image.load('icon1.jpg')
pygame.display.set_icon(icon)


def image(imagename, imageX, imageY):
        k = pygame.image.load(imagename)
        screen.blit(k, (imageX, imageY))

def button1(picture, position, surface):
    image = pygame.image.load(picture)
    imagerect = image.get_rect()
    imagerect.topright = position
    surface.blit(image,imagerect)
    return (image,imagerect)

#music
bg_music = pygame.mixer.music.load('MUSIC.wav')	
pygame.mixer.music.play(-1)

flag = 0

# game loop
running = True 
while running:
	# background(R,G,B)
	screen.fill((0,200,0))
	bg_music = button1('music1.png', (50, 10), screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		if  pygame.mouse.get_pressed()[0] == 1:
			mouse = pygame.mouse.get_pos()
			
			if bg_music[1].collidepoint(mouse):
				flag += 1
				pygame.mixer.music.stop()

 	# mute icon
	if flag > 0:
           image('mute1.png',8,10)
	pygame.display.update()



