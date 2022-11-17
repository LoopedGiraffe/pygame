import pygame

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOE_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOE_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello Worls!")
#the main game loop

running = True
while running:
    #loop through a list of event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

#end the game
pygame.quit()
