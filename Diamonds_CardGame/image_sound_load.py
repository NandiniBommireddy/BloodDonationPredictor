import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400,300))

def imageLoad(name, card):
    
    if card == 1:
        fullname = os.path.join("images/cards/", name)
    else: 
        fullname = os.path.join('images', name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print (f"Cannot load image: {name}")

    image = image.convert()
    
    return image, image.get_rect()

def soundLoad(name):
    
    fullName = os.path.join('sounds', name)
    try: 
        sound = pygame.mixer.Sound(fullName)
        
    except pygame.error:
        print (f"Cannot load sound: {name}")
    return sound

def display(font, sentence):
    
    displayFont = pygame.font.Font.render(font, sentence, 1, (255,255,255), (0,0,0)) 
    return displayFont

def playClick():
    clickSound = soundLoad("click.wav")
    clickSound.play()

def playShuffle():
    shuffleSound = soundLoad("shuffle.wav")
    shuffleSound.play()


img1, img1_rect = imageLoad("2_of_clubs.png", 1)
'''imageLoad("diamonds_backgroung.jpeg", 0)
soundLoad("click.wav")
soundLoad("shuffle.wav")'''
print(img1,img1_rect)
