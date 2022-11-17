import pygame

#initialize pygame
pygame.init()

#create our display SURFACE
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete keyboard movements!")

#set game values
VELOCITY = 30

#LOAD IN IMAGES
dragon_image = pygame.image.load('dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT


#main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


        #check for discreete movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
    
    #fill the surface to cover old images
    display_surface.fill((0, 0, 0))

    #Blit (copy) assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    #update our display
    pygame.display.update()


#end of game
pygame.quit()