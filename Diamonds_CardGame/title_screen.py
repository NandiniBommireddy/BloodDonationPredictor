import pygame
 
# initialize pygame
pygame.init()

# create title screen
screen =  pygame.display.set_mode((800,600))

# title and icon 
pygame.display.set_caption("Diamonds")
icon = pygame.image.load('icon1.jpg')
pygame.display.set_icon(icon)


# game window
def gamew():

    # create game screen
    screen1 =  pygame.display.set_mode((800,600))

    # title and icon 
    pygame.display.set_caption("Diamonds")
    icon = pygame.image.load('icon1.jpg')
    pygame.display.set_icon(icon)

    # music icon
    musicImg = pygame.image.load('music1.png')
   
    def music():
        screen1.blit(musicImg, (10,10))

    # game loop
    running = True 
    while running:
    
        screen1.fill((0,200,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        music() 
        pygame.display.update()



def Buttonify(picture, position, surface):
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

    start = Buttonify('start1.png',(370,225), screen)
    exit = Buttonify('exit1.png',(700,225),screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()
            
            if start[1].collidepoint(mouse):
                gamew()
                running = False
            if exit[1].collidepoint(mouse):
                running = False

    pygame.display.update()


