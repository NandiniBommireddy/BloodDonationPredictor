import pygame
import os
import random

from pygame.constants import KEYDOWN

from pygame.font import SysFont
 
# initialize pygame
pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
# create screen
screen =  pygame.display.set_mode((1450,700))

clock = pygame.time.Clock()

#To load an Image
def imageLoad(name, card):
    if card == 1:
        fullname = os.path.join("images/cards/", name)
    else: 
        fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print (f"Cannot load image: {name}")
        raise SystemExit
    
    image.convert()

    return image

#To Load sound
def soundLoad(name):
    fullName = os.path.join('sounds', name)
    try: 
        sound = pygame.mixer.Sound(fullName)
    except pygame.error:
        print (f"Cannot load sound: {name}")
        raise SystemExit
    return sound

#To display text messages
def display_text(sentence, x, y):
    textsurface = myfont.render(sentence, False, (0, 0, 0))
    #displayFont = pygame.font.Font.render(font, sentence, 1, (255,255,255), (0,0,0)) 
    screen.blit(textsurface,(x , y))

#To play click sound
def playClick():
    clickSound = soundLoad("click.wav")
    clickSound.play()

#To play shuffle sound
def playShuffle():
    shuffleSound = soundLoad("shuffle.wav")
    shuffleSound.play()

# title and icon 
pygame.display.set_caption("Diamonds")
icon = imageLoad('main_icon.jpg', 0)
pygame.display.set_icon(icon)

def gamew():

    # create game screen
    screen1 =  pygame.display.set_mode((1450,700))

    # title and icon 
    pygame.display.set_caption("Diamonds")
    icon = pygame.image.load('icon1.jpg')
    pygame.display.set_icon(icon)

    # adding background music
    bg_music = pygame.mixer.music.load('MUSIC.wav')
    pygame.mixer.music.play(-1)

    def image(imagename, imageX, imageY):
        k = pygame.image.load(imagename)
        screen1.blit(k, (imageX, imageY))

    def button1(picture, position, surface):
        image = pygame.image.load(picture)
        imagerect = image.get_rect()
        imagerect.topright = position
        surface.blit(image,imagerect)
        return (image,imagerect)

import random
rankname = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "king", "queen", "jack"]
suits = ["hearts", "spades", "clubs"]

#Deck of shuffled diamond cards
def diamond_deck():
    diamond_deck = []
    for i in range(len(rankname)):
        diamond_deck.append("{}_of_diamonds".format(rankname[i]))
        random.shuffle(diamond_deck)
    return diamond_deck

#Deck of all other shuffled suit cards
def decks():
    deck = []
    for i in range(len(rankname)):
        for j in range(len(suits)):
            deck.append("{}_of_{}".format(rankname[i], suits[j]))
    random.shuffle(deck)
    return deck

diamond_deck = diamond_deck()
p1_cards = decks()[:39:3]
p2_cards = decks()[1:39:3]
p3_cards = decks()[2:39:3]

#Assigning values to cards
card_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "K" : 10, "Q" : 10, "J" : 10, "A" : 11}

#Assigning Points diamond cards
points = {"2" : 3, "3" : 3, "4" : 3, "5" : 3, "6" : 3, "7" : 3, "8" : 3, "9" : 3, "10" : 3, "Ace" : 11, "K" : 10, "Q" : 10, "J" : 10}

def music():
    screen.blit(imageLoad('music.png', 0), (10, 10))

def title():
    image, image_rect = display_text(SysFont, "DIAMONDS")

card_back = imageLoad("card_back.png", 1)

def card_img(img_x,img_y,card):
    screen.blit(card,(img_x,img_y))

imgWidth = 100
imgHeight = 145

def diamond_banker():
    screen.blit(imageLoad('banker.jpg', 1), (100, 10))

def button(picture, position, surface):
    image = imageLoad(picture, 1)
    imagerect = image.get_rect()
    imagerect.topright = position
    surface.blit(image,imagerect)
    return (image,imagerect)

n = 1
# game loop
running = True 
while running and n<=13:
    
    screen.fill((0,200,0))

    # background(R,G,B)
    button1 = button(p1_cards[0] +'.png',(115,400), screen)
    button2 = button(p1_cards[1] +'.png',(225,400),screen)
    button3 = button(p1_cards[2] +'.png',(335,400), screen)
    button4 = button(p1_cards[3] +'.png',(445,400),screen)
    button5 = button(p1_cards[4] +'.png',(555,400), screen)
    button6 = button(p1_cards[5] +'.png',(665,400),screen)
    button7 = button(p1_cards[6] +'.png',(775,400), screen)
    button8 = button(p1_cards[7] +'.png',(885,400),screen)
    button9 = button(p1_cards[8] +'.png',(995,400), screen)
    button10 = button(p1_cards[9] +'.png',(1105,400),screen)
    button11 = button(p1_cards[10] +'.png',(1215,400), screen)
    button12 = button(p1_cards[11] +'.png',(1325,400),screen)
    button13 = button(p1_cards[12] +'.png',(1435,400), screen)

    for event in pygame.event.get():       

        if event.type == pygame.QUIT:
            running = False 
        if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()
            if button1[1].collidepoint(mouse):
                play1_pick = p1_cards[0]
                
            if button2[1].collidepoint(mouse):
                play1_pick = p1_cards[1]

            if button3[1].collidepoint(mouse):
                play1_pick = p1_cards[2]
                
            if button4[1].collidepoint(mouse):
                play1_pick = p1_cards[3]

            if button5[1].collidepoint(mouse):
                play1_pick = p1_cards[4]
                
            if button6[1].collidepoint(mouse):
                play1_pick = p1_cards[5]

            if button7[1].collidepoint(mouse):
                play1_pick = p1_cards[6]
                
            if button8[1].collidepoint(mouse):
                play1_pick = p1_cards[7]
            
            if button9[1].collidepoint(mouse):
                play1_pick = p1_cards[8]

            if button10[1].collidepoint(mouse):
                play1_pick = p1_cards[9]
                
            if button11[1].collidepoint(mouse):
                play1_pick = p1_cards[10]

            if button12[1].collidepoint(mouse):
                play1_pick = p1_cards[11]

            if button13[1].collidepoint(mouse):
                play1_pick = p1_cards[12]
        
            print(play1_pick)

            
        pygame.display.update()




