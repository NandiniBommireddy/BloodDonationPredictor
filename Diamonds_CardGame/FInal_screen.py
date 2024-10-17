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

# game loop 
running = True 
while running:
    # background(R,G,B)
    screen.fill((200,220,240))

    playagain = button("PLAYAGAIN2.PNG", (600,330), screen)
    quit = button("QUIT2.png", (1100,330), screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()
            
            if quit[1].collidepoint(mouse):
                running = False
    pygame.display.update()