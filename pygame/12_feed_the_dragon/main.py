import pygame, random

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Knight")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


#set game values
PLAYER_STARTING_LIVES = 10
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


#set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


#set fonts
font = pygame.font.Font("KingthingsWillowless-8ZR2.ttf", 32)


#set text
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Knight", True, YELLOW, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#set sounds and music
coin_sound = pygame.mixer.Sound("coin.wav")
miss_sound = pygame.mixer.Sound("miss.wav")
miss_sound.set_volume(.7)
#loading background music
pygame.mixer.music.load("music.wav")

#set images
player_image = pygame.image.load("dragon_center.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

#main game loop
#with background music
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #check if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check to see if the user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY


    #MOVE THE COIN
    if coin_rect.x < 0:
        #player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        #move the coin
        coin_rect.x -= coin_velocity
    
    #check for collision
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    #UPDATE hud
    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

    #CHECK FOR GAME OVER
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #pause the game untill player presses a key, then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #the player wants to play again:
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                #THE PLAYER WANTS TO QUIT
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #fill the display
    display_surface.fill(BLACK)

    #blit the HUD to the screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

    #draw white line
    pygame.draw.line(display_surface, YELLOW, (0, 64), (WINDOW_WIDTH, 64), 2)

    #bLIT ASSETS TO SCREEN
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    #update display screen adn tick the clock
    pygame.display.update()
    clock.tick(FPS)


#end of the game
pygame.quit()
