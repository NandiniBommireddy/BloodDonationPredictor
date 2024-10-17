 	
import pygame
# initialize pygame
pygame.init()

# create screen
screen =  pygame.display.set_mode((800,600))

# title and icon 
pygame.display.set_caption("Diamonds")
icon = pygame.image.load('diamond.jpg')
pygame.display.set_icon(icon)

# music icon
musicImg = pygame.image.load('music2.png')
musicX = 10
musicY = 10

def music():
	screen.blit(musicImg, (musicX, musicY))
#music
bg_music = pygame.mixer.music.load('MUSIC.wav')	
pygame.mixer.music.play(-1)

# game loop
running = True 
while running:
	# background(R,G,B)
	screen.fill((0,150,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
 	# music icon
	music( ) 
	pygame.display.update()



