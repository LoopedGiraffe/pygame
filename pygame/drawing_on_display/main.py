import pygame

#initialize pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("drawing objects")

#define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)

#give background color to the display
display_surface.fill(BLUE)

#Draw various shaoes on our display
#we need to define as follow:

#DRAWING LINES:
#line(surface where we want to draw (specified earlier), color (defined earlier or can be given as RGB numbers), starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 1)

#DRAWING CIRCLES:
#circle(surface where we want to draw, color, center, radius, thickness... 0 for fill) 
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 195, 0)

#DRAWING RECTANGLES
#rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGNETA, (500, 100, 50, 100))

#the main game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update the display
    pygame.display.update()


#end of the game
pygame.quit()