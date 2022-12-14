import pygame

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#create images... returns a surface object with the image deawn on it.
#we can then get the rect of the surface and use the rect to position the image
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_center_image = pygame.image.load("dragon_center.png")
dragon_center_rect = dragon_center_image.get_rect()
dragon_center_rect.center = (WINDOW_WIDTH//2, 32)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75), 5)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface objects at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_center_image, dragon_center_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)



    #Update the display
    pygame.display.update()


#End the game
pygame.quit()
            