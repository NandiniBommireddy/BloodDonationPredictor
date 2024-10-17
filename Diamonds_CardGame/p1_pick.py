def button(picture, position, surface):
    image = imageLoad(picture, 1)
    imagerect = image.get_rect()
    imagerect.topright = position
    surface.blit(image,imagerect)
    return (image,imagerect)

# game loop
running = True 
while running:
    
    # background(R,G,B)
    screen.fill((0,200,0))
    

    
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
