import random
import pygame
 
pygame.init()
pygame.font.init()

font = pygame.font.SysFont("ArialCEItalic.ttf", 45)

screen =  pygame.display.set_mode((1450,700))

rankname = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "king", "queen", "jack"]
suits = ["hearts", "spades", "clubs"]
 
def title_icon(caption, image):
    pygame.display.set_caption(caption)
    icon = pygame.image.load(image)
    pygame.display.set_icon(icon)

def image(imagename, imageX, imageY):
    k = pygame.image.load(imagename)
    screen.blit(k, (imageX, imageY))

def buttons(picture, position, surface):
    image = pygame.image.load(picture)
    imagerect = image.get_rect()
    imagerect.topright = position
    surface.blit(image,imagerect)
    return (image,imagerect)

def music(sound):
    bg_music = pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

def diamond_deck():
    diamond_deck = []
    for i in range(len(rankname)):
        diamond_deck.append("{}_of_diamonds.png".format(rankname[i]))
        random.shuffle(diamond_deck)
    return diamond_deck

def decks():
    deck = []
    for i in range(len(rankname)):
        for j in range(len(suits)):
            deck.append("{}_of_{}.png".format(rankname[i], suits[j]))
            random.shuffle(deck)
    return deck

def card_value(rank):
    value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "1" : 10, "k" : 10, "q" : 10, "j" : 10, "a" : 11}
    return value[rank]

def diamond_points(rank):
    points = {"2" : 3, "3" : 3, "4" : 3, "5" : 3, "6" : 3, "7" : 3, "8" : 3, "9" : 3, "1" : 3, "a" : 20, "k" : 10, "q" : 10, "j" : 10}
    return points[rank]

def display_names():
    diamond = font.render("Diamond card", True, (0,0,0))
    player1 = font.render("Player 1", True, (0,0,0))
    player2 = font.render("Player 2", True, (0,0,0))
    player3 = font.render("Player 3", True, (0,0,0))
    screen.blit(diamond, (950,270))
    screen.blit(player1, (627, 400))
    screen.blit(player2, (122, 270))
    screen.blit(player3, (292,270))
 
def score(sco1, sco2, sco3):   
    s1 = font.render("Score1: "+str(sco1), True, (0,0,0))
    s2 = font.render("Score2: "+str(sco2), True, (0,0,0))
    s3 = font.render("Score3: "+str(sco3), True, (0,0,0))
    screen.blit(s1, (1260, 60))
    screen.blit(s2, (1260, 110))
    screen.blit(s3, (1260, 160))

def winner(s1, s2, s3):
    if max(s1, s2, s3) == s1 and max(s1, s2, s3) == s2 and max(s1, s2, s3) == s3:
        w = font.render("Yay! player 1, player 2 and player 3 are the winners", True, (0, 0, 0))
        screen.blit(w, (350, 40))
    elif max(s1, s2, s3) == s1 and max(s1, s2, s3) == s2:
        w = font.render("Yay! player 1 and player 2 are the winners", True, (0, 0, 0))
        screen.blit(w, (410, 40))
    
    elif max(s1, s2, s3) == s2 and max(s1, s2, s3) == s3:
        w = font.render("Yay! player 2 and player 3 are the winners", True, (0, 0, 0))
        screen.blit(w, (410, 40))
       
    elif max(s1, s2, s3) == s1 and max(s1, s2, s3) == s3:
        w = font.render("Yay! player 1  and player 3 are the winners", True, (0, 0, 0))
        screen.blit(w, (410, 40))
        
    elif max(s1, s2, s3) == s1:
        w = font.render("Yay! player 1 is the winner", True, (0, 0, 0))
        screen.blit(w, (500, 40))
        
    elif max(s1, s2, s3) == s2:
        w = font.render("Yay! player 2 is the winner", True, (0, 0, 0))
        screen.blit(w, (500, 40))
         
    elif max(s1, s2, s3) == s3:
        w = font.render("Yay! player 3 is the winner", True, (0, 0, 0))
        screen.blit(w, (500, 40))
        

diamondcards = diamond_deck()
p1_cards = decks()[:40:3]
p2_cards = decks()[1:40:3]
p3_cards = decks()[2:40:3]
score1, score2, score3 = 0, 0, 0

def quitwindow():
    screen2 =  pygame.display.set_mode((1450,700))

    pygame.display.set_caption("Diamonds")
    icon = pygame.image.load('icon1.jpg')
    pygame.display.set_icon(icon)

    running = True 
    while running:
        screen.fill((200,220,240))

        playagain = buttons("PLAYAGAIN2.PNG", (600,330), screen)
        quit = buttons("QUIT2.png", (1100,330), screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if  pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                
                if quit[1].collidepoint(mouse):
                    running = False
                    pygame.quit()
                if playagain[1].collidepoint(mouse):
                    gamewindow()

        pygame.display.update()


def gamewindow():
    screen1 =  pygame.display.set_mode((1450,700))
    title_icon("Diamonds", "icon1.jpg")

    music('MUSIC.wav')
 
    diamond_pick = random.choice(diamondcards)
    print("Diamond card picked by banker: ",diamond_pick)

    play1_pick = p1_cards[0]
    play2_pick = random.choice(p2_cards)
    play3_pick = random.choice(p3_cards)
    print("card picked by player2:",play2_pick)
    print("card picked by player3:",play3_pick)

    flag, flag1 = 0, 0

    running = True 
    while running:
    
        screen1.fill((0,200,0))
        bgmusic = buttons('music1.png', (50, 10), screen1)
        score(" "," "," ")

        display_names()
        
        p1_card1 = buttons(p1_cards[0], (115, 470), screen1)
        p1_card2 = buttons(p1_cards[1], (225, 470), screen1)
        p1_card3 = buttons(p1_cards[2], (335, 470), screen1)
        p1_card4 = buttons(p1_cards[3], (445, 470), screen1)
        p1_card5 = buttons(p1_cards[4], (555, 470), screen1)
        p1_card6 = buttons(p1_cards[5], (665, 470), screen1)
        p1_card7 = buttons(p1_cards[6], (775, 470), screen1)
        p1_card8 = buttons(p1_cards[7], (885, 470), screen1)
        p1_card9 = buttons(p1_cards[8], (995, 470), screen1)
        p1_card10 = buttons(p1_cards[9], (1105, 470), screen1)
        p1_card11 = buttons(p1_cards[10], (1215, 470), screen1)
        p1_card12 = buttons(p1_cards[11], (1325, 470), screen1)
        p1_card13 = buttons(p1_cards[12], (1435, 470), screen1)
        
        d_card = image('card_back.png', 1000, 100)
        p2card = image('card_back.png', 130, 100)
        p3card = image('card_back.png', 300, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quitwindow()

        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()
            if bgmusic[1].collidepoint(mouse):
                pygame.mixer.music.stop()
                flag = 1
                
            
            if p1_card1[1].collidepoint(mouse):
                play1_pick = p1_cards[0]
                flag1 += 1
            
            if p1_card2[1].collidepoint(mouse):
                play1_pick = p1_cards[1]
                flag1 += 1
            
            if p1_card3[1].collidepoint(mouse):
                play1_pick = p1_cards[2]
                flag1 += 1
            
            if p1_card4[1].collidepoint(mouse):
                play1_pick = p1_cards[3]
                flag1 += 1
            
            if p1_card5[1].collidepoint(mouse):
                play1_pick = p1_cards[4]
                flag1 += 1
            
            if p1_card6[1].collidepoint(mouse):
                play1_pick = p1_cards[5]
                flag1 += 1
            
            if p1_card7[1].collidepoint(mouse):
                play1_pick = p1_cards[6]
                flag1 += 1
            
            if p1_card8[1].collidepoint(mouse):
                play1_pick = p1_cards[7]
                flag1 += 1
            
            if p1_card9[1].collidepoint(mouse):
                play1_pick = p1_cards[8]
                flag1 += 1
               
            if p1_card10[1].collidepoint(mouse):
                play1_pick = p1_cards[9]
                flag1 += 1
            
            if p1_card11[1].collidepoint(mouse):
                play1_pick = p1_cards[10]
                flag1 += 1
            
            if p1_card12[1].collidepoint(mouse):
                play1_pick = p1_cards[11]
                flag1 += 1
            
            if p1_card13[1].collidepoint(mouse):
                play1_pick = p1_cards[12]
                flag1 += 1
            
        if flag == 1:
            image('mute1.png', 8, 10)

        d_front = image(diamond_pick, 1025, 96)
        
        if flag1 > 0:
            p1_front = image(play1_pick, 635, 240)
            p2_front = image(play2_pick, 155, 96)
            p3_front = image(play3_pick, 325, 96)

            p1_value = card_value(play1_pick[0])
            p2_value = card_value(play2_pick[0])
            p3_value = card_value(play3_pick[0])
            p = diamond_points(diamond_pick[0])

            if max(p1_value, p2_value, p3_value) == p1_value and max(p1_value, p2_value, p3_value) == p2_value and max(p1_value, p2_value, p3_value) == p3_value:
                score(score1+(p/3), score2+(p/3), score3+(p/3))
                winner(score1+(p/3), score2+(p/3), score3+(p/3)) 
            elif max(p1_value, p2_value, p3_value) == p1_value and max(p1_value, p2_value, p3_value) == p2_value:
                score(score1+(p/2), score2+(p/2), score3)
                winner(score1+(p/2), score2+(p/2), score3) 
            elif max(p1_value, p2_value, p3_value) == p2_value and max(p1_value, p2_value, p3_value) == p3_value:
                score(score1, score2+(p/2), score3+(p/2))
                winner(score1, score2+(p/2), score3+(p/2))
            elif max(p1_value, p2_value, p3_value) == p3_value and max(p1_value, p2_value, p3_value) == p1_value:  
                score(score1+(p/2), score2, score3+(p/2))
                winner(score1+(p/2), score2, score3+(p/2))   
            elif max(p1_value, p2_value, p3_value) == p1_value:
                score(score1+p, score2, score3)
                winner(score1+p, score2, score3)  
            elif max(p1_value, p2_value, p3_value) == p2_value:
                score(score1, score2+p, score3)
                winner(score1, score2+p, score3)
            elif max(p1_value, p2_value, p3_value) == p3_value: 
                score(score1, score2, score3+p)
                winner(score1, score2, score3+p)

        pygame.display.update()
    print("card picked by player1:",play1_pick)

running = True 
while running:
    # background(R,G,B)
    screen.fill((200,220,240))
    title_icon("Diamonds", "icon1.jpg")

    start = buttons('start1.png',(600,270), screen)
    exit = buttons('exit1.png',(1100, 270),screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()
            
            if start[1].collidepoint(mouse):
                gamewindow()
                running = False
                    
            if exit[1].collidepoint(mouse):
                running = False

    pygame.display.update()