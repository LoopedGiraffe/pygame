import pygame

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement!")

#load images
dragon_image = pygame.image.load('dragon_left.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)





#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #movement based on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

        #movement following coursor position
       # if event.type == pygame.MOUSEMOTION:
       #     print(event)
       #     mouse_x = event.pos[0]
       #     mouse_y = event.pos[1]
       #     dragon_rect.centerx = mouse_x
       #     dragon_rect.centery = mouse_y

        #drag the object when the mouse button is clicked:
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    #fill the display
    display_surface.fill((0, 0, 0))

    #blit assets
    display_surface.blit(dragon_image, dragon_rect)

    #update the display
    pygame.display.update()


#end of game
pygame.quit()
