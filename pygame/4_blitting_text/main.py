import pygame

#initializing pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting text!")

#Define colors:
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

#see all available system fonts
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)


#define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('KingthingsWillowless-8ZR2.ttf', 32)

#define text
system_text = system_font.render("Dragon Rules!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move your Dragon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)


#the main game loop
running = True
while running:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False

    #bLIT (COPY ) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    #update the display
    pygame.display.update()



#end the game
pygame.quit()
