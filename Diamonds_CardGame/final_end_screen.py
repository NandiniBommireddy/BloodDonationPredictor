import random
import pygame
# initialize pygame
pygame.init()

# create title screen
screen =  pygame.display.set_mode((1450,700))

# title and icon 
pygame.display.set_caption("Diamonds")
icon = pygame.image.load('diamond.jpg')
pygame.display.set_icon(icon)

def button(picture, position, surface):
    image = pygame.image.load(picture)
    imagerect = image.get_rect()
    imagerect.topright = position
    surface.blit(image,imagerect)
    return (image,imagerect)


def gamew(): 

    # create screen
    screen =  pygame.display.set_mode((1450,700))

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

# game loop 
running = True 
while running:
    # background(R,G,B)
    screen.fill((200,220,240))

    playagain = button("PLAYAGAIN2.PNG", (600,300), screen)
    quit = button("QUIT2.png", (1100,300), screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()

            if playagain[1].collidepoint(mouse):
                gamew()
                running = False
            
            if quit[1].collidepoint(mouse):
                running = False
    pygame.display.update()