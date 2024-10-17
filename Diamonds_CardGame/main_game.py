import random
import pygame
 
# initialize pygame
pygame.init()

# create title screen
screen =  pygame.display.set_mode((1450,700))

# title and icon 
pygame.display.set_caption("Diamonds")
icon = pygame.image.load('icon1.jpg')
pygame.display.set_icon(icon)


# game window
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

    # game code
    rankname = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "king", "queen", "jack"]
    suits = ["hearts", "spades", "clubs"]

    # deck of shuffled diamond cards
    def diamond_deck():
        diamond_deck = []
        for i in range(len(rankname)):
            diamond_deck.append("{}_of_diamonds.png".format(rankname[i]))
        random.shuffle(diamond_deck)
        return diamond_deck

    # deck of all other shuffled suit cards
    def decks():
        deck = []
        for i in range(len(rankname)):
            for j in range(len(suits)):
                deck.append("{}_of_{}.png".format(rankname[i], suits[j]))
        random.shuffle(deck)
        return deck

    #Assigning values to cards
    def card_value(rank):
        value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "1" : 10, "k" : 10, "q" : 10, "j" : 10, "a" : 11}
        return value[rank]

    #Assigning Points diamond cards
    def diamond_points(rank):
        points = {"2" : 3, "3" : 3, "4" : 3, "5" : 3, "6" : 3, "7" : 3, "8" : 3, "9" : 3, "1" : 3, "a" : 11, "k" : 10, "q" : 10, "j" : 10}
        return points[rank]

    #Winner
    def winner(s1, s2, s3):
        if max(s1, s2, s3) == s1 and max(s1, s2, s3) == s2:
            return("yay {} and {} are the winners".format(p1, p2))
        elif max(s1, s2, s3) == s2 and max(s1, s2, s3) == s3:
            return("yay {} and {} are the winners".format(p2, p3))
        elif max(s1, s2, s3) == s1 and max(s1, s2, s3) == s3:
            return("yay {} and {} are the winners".format(p1, p3))
        elif max(s1, s2, s3) == s1 and max(s1, s2, s3) == s2 and max(s1, s2, s3) == s3:
            return("yay {}, {} and {} are the winners".format(p1, p2, p3))
        elif max(s1, s2, s3) == s1:
            return("yay {} is the winner".format(p1))
        elif max(s1, s2, s3) == s2:
            return("yay {} is the winner".format(p2))
        elif max(s1, s2, s3) == s3:
            return("yay {} is the winner".format(p3))

    #print(diamond_deck())
    #print(decks())

    # Player names
    #print("Enter player names\n") 
    #p1 = input("player1:")
    #p2 = input("player2:")
    #p3 = input("player3:")


    # Deck distribution
    d = decks()
    p1_cards = d[0:40:3]
    p2_cards = d[1:40:3]
    p3_cards = d[2:40:3]
    #player_cards1 =  "{} = {}\n".format(p1, p1_cards)
    #player_cards2 =  "{} = {}\n".format(p2, p2_cards)
    #player_cards3 =  "{} = {}\n".format(p3, p3_cards)
    #print(player_cards1)
    #print(player_cards2)
    #print(player_cards3)


    score1, score2, score3 = 0, 0, 0
    d = diamond_deck()
    
    # Comparing card values for different cases
    for _ in range(13):

        # Banker picking diamond card
        diamond_pick = random.choice(d)
        #print("Diamond card picked by banker: ",diamond_pick)
        
        #PLayers picking their cards
        #play1_pick = input("Enter card picked: ") 
        play2_pick = random.choice(p2_cards)
        play3_pick = random.choice(p3_cards)
        #print("card picked by player1:",play1_pick)
        #print("card picked by player2:",play2_pick)
        #print("card picked by player3:",play3_pick)
        #p1_value = card_value(play1_pick[0])
        #p2_value = card_value(play2_pick[0])
        #p3_value = card_value(play3_pick[0])
        #point = diamond_points(diamond_pick[0])

    flag = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0

    # game loop
    running = True 
    while running:
    
        screen1.fill((0,200,0))

        bgmusic = button1('music1.png', (50, 10), screen1)

        dcard = button1('card_back.png', (675,100), screen1)

        # player 1 cards
        p1card1 = button1(p1_cards[0], (115, 400), screen1)
        p1card2 = button1(p1_cards[1], (225, 400), screen1)
        p1card3 = button1(p1_cards[2], (335, 400), screen1)
        p1card4 = button1(p1_cards[3], (445, 400), screen1)
        p1card5 = button1(p1_cards[4], (555, 400), screen1)
        p1card6 = button1(p1_cards[5], (665, 400), screen1)
        p1card7 = button1(p1_cards[6], (775, 400), screen1)
        p1card8 = button1(p1_cards[7], (885, 400), screen1)
        p1card9 = button1(p1_cards[8], (995, 400), screen1)
        p1card10 = button1(p1_cards[9], (1105, 400), screen1)
        p1card11 = button1(p1_cards[10], (1215, 400), screen1)
        p1card12 = button1(p1_cards[11], (1325, 400), screen1)
        p1card13 = button1(p1_cards[12], (1435, 400), screen1)

        # bidding cards of player 2 and player 3
        p2card = button1('card_back.png', (130,100), screen1)
        p3card = button1('card_back.png', (300,100), screen1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if  pygame.mouse.get_pressed()[0] == 1:
            mouse = pygame.mouse.get_pos()

            if bgmusic[1].collidepoint(mouse):
                flag += 1
                pygame.mixer.music.stop()

            if dcard[1].collidepoint(mouse):
                flag1 += 1
            if p2card[1].collidepoint(mouse):
                flag2 += 1
            if p3card[1].collidepoint(mouse):
                flag3 += 1

            if p1card1[1].collidepoint(mouse):
                play1_pick = p1_cards[0]
            if p1card2[1].collidepoint(mouse):
                play1_pick = p1_cards[1]
            if p1card3[1].collidepoint(mouse):
                play1_pick = p1_cards[2]
            if p1card4[1].collidepoint(mouse):
                play1_pick = p1_cards[3]
            if p1card5[1].collidepoint(mouse):
                play1_pick = p1_cards[4]
            if p1card6[1].collidepoint(mouse):
                play1_pick = p1_cards[5]
            if p1card7[1].collidepoint(mouse):
                play1_pick = p1_cards[6]
            if p1card8[1].collidepoint(mouse):
                play1_pick = p1_cards[7]
            if p1card9[1].collidepoint(mouse):
                play1_pick = p1_cards[8]
            if p1card10[1].collidepoint(mouse):
                play1_pick = p1_cards[9]
            if p1card11[1].collidepoint(mouse):
                play1_pick = p1_cards[10]
            if p1card12[1].collidepoint(mouse):
                play1_pick = p1_cards[11]
            if p1card13[1].collidepoint(mouse):
                play1_pick = p1_cards[12]
                print(play1_pick)


        if flag > 0:
            image('mute1.png',8,10)
        if flag1 > 0:
            image(diamond_pick, 620, 96)       
        if flag2 > 0:
            image(play2_pick, 75, 96)
        if flag3 > 0:
            image(play3_pick, 245, 96) 

        pygame.display.update()


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

    start = button('start1.png',(600,270), screen)
    exit = button('exit1.png',(1100,270),screen)
    
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

