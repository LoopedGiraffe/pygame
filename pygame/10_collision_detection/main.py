import pygame, random
#initialize pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection!")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set the game values
VELOCITY = 5

#LOAD IMAGES
knight_image = pygame.image.load("dragon_center.png")
knight_rect = knight_image.get_rect()
knight_rect.topleft = (25, 25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


#The main game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #get list of all keys being pressed down
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and knight_rect.left > 0:
        knight_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and knight_rect.right < WINDOW_WIDTH:
        knight_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and knight_rect.top > 0:
        knight_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and knight_rect.bottom < WINDOW_HEIGHT:
        knight_rect.y += VELOCITY

    #check for collision between two rects
    if knight_rect.colliderect(coin_rect):
        print("HIT !")
        coin_rect.x= random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - 32)






    #FILL DISPLAY SURFACE
    display_surface.fill((0, 0, 0))

    #draw rectangles to represent rect's of each object
    pygame.draw.rect(display_surface, (0, 255, 0), knight_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)


    #blit assets
    display_surface.blit(knight_image, knight_rect)
    display_surface.blit(coin_image, coin_rect)

    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()