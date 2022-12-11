import pygame
import random


# initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hungry Cat")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10

STARTING_BOOST_LEVEL = 100
STARTING_FISH_VELOCITY = 2
FISH_ACCELERATION = .25
BUFFER_DISTANCE = 100

score = 0
fish_points = 0
fish_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

fish_velocity = STARTING_FISH_VELOCITY

#set colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#set fonts
font = pygame.font.Font("WeAreInLove-3BRy.ttf", 32)

#set text
points_text = font.render("  Fish Points:  " + str(fish_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render("  Score:  " + str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("  Hungry Cat  ", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

eaten_text = font.render("  Fish eaten:  " + str(fish_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 50

lives_text = font.render("  Lives:  " + str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render("  Boost:  " + str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render("  FINAL SCORE:  " + str(score), True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("  Press any key to play again  ", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#set sounds and music
meow_sound = pygame.mixer.Sound("meow.mp3")
miss_sound = pygame.mixer.Sound("miss.wav")
pygame.mixer.music.load("cat_background.mp3")

#set images
player_image_right = pygame.image.load("cat-right.png")
player_image_left = pygame.image.load("cat-left.png")

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

fish_image = pygame.image.load("fish.png")
fish_rect = fish_image.get_rect()
fish_rect.topleft = (random.randint(0,WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

#The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #check if the user wants to quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    
    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity
    
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    #engage boost
    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    
    #move the fish and update fish points
    fish_rect.y += fish_velocity
    fish_points = int(fish_velocity * (WINDOW_HEIGHT - fish_rect.y + 100))

    #player missed fish
    if fish_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()

        fish_rect.topleft = (random.randint(0,WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        fish_velocity = STARTING_FISH_VELOCITY

        player_rect.centerx = WINDOW_WIDTH//2
        player_rect.bottom = WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL

    #check for collision
    if player_rect.colliderect(fish_rect):
        score += fish_points
        fish_eaten += 1
        meow_sound.play()

        fish_rect.topleft = (random.randint(0,WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        fish_velocity += FISH_ACCELERATION

        boost_level += 25
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL

    #update HUD
    points_text = font.render("  Fish Points:  " + str(fish_points), True, ORANGE)
    score_text = font.render("  Score:  " + str(score), True, ORANGE)
    eaten_text = font.render("  Fish eaten:  " + str(fish_eaten), True, ORANGE)
    lives_text = font.render("  Lives:  " + str(player_lives), True, ORANGE)
    boost_text = font.render("  Boost:  " + str(boost_level), True, ORANGE)

    #FILL surface
    display_surface.fill(BLACK)

    #Blit the HUD
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)

    #check for game over
    if player_lives == 0:
        game_over_text = font.render("  FINAL SCORE:  " + str(score), True, ORANGE)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #pause the game untill a player presses the key then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    fish_eaten = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    fish_velocity = STARTING_FISH_VELOCITY

                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                
                #the player wants to quit:
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False



    #BLIT ASSETS
    display_surface.blit(player_image, player_rect)
    display_surface.blit(fish_image, fish_rect)

    pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH, 100), 3)

    #update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)




#End the game
pygame.quit