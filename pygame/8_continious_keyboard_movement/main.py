import pygame

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("continious Keyboard Movement")

#SET fps AND CLOCK
FPS = 60
clock = pygame.time.Clock()


#set game values
VELOCITY = 5

#load images
knight_image = pygame.image.load("dragon_center.png")
knight_rect = knight_image.get_rect()
knight_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #get a list of all keys being pressed down (held)
    keys = pygame.key.get_pressed()
    print(keys)

    #move knight continiously
    if keys[pygame.K_LEFT]:
        knight_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        knight_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        knight_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        knight_rect.y += VELOCITY


    #FILL THE DISPLAY
    display_surface.fill((0, 0, 0))

    #blit the display
    display_surface.blit(knight_image, knight_rect)

    #update the display
    pygame.display.update()

    #thick the clock
    clock.tick(FPS)


#End the game
pygame.quit()
