import pygame, random

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Mouse")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 5
MOUSE_STARTING_VELOCITY = 1
MOUSE_ACCELERATION = 0.25

score = 0
player_lives = PLAYER_STARTING_LIVES

mouse_velocity = MOUSE_STARTING_VELOCITY
mouse_dx = random.choice([-1, 1]) #-1 is left; 1 is right
mouse_dy = random.choice([-1, 1]) #-1 is down; 1 is up

#set game colours
BLUE = (153, 217, 234)
DARKBLUE = (2, 162, 232)
PINK = (255, 174, 201)
RED = (216, 99, 69)

#set fonts
font = pygame.font.Font("WeAreInLove-3BRy.ttf", 32)

#set text
title_text = font.render("  Catch the Mouse  ", True, RED, PINK)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("  Score: " + str(score) + "  ", True, DARKBLUE, BLUE)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("  Lives: " + str(player_lives) + "  ", True, DARKBLUE, BLUE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render("  GAME OVER  ", True, DARKBLUE, BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("  Click anywhere to play again  ", True, RED, PINK)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#set sound and music
click_sound = pygame.mixer.Sound("click.wav")
miss_sound = pygame.mixer.Sound("click_miss.wav")
pygame.mixer.music.load("mouse.wav")

#set images
background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

mouse_image = pygame.image.load("mouse.png")
mouse_rect = mouse_image.get_rect()
mouse_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#the main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #check to see if the User wants to quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #a click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord_x = event.pos[0]
            coord_y = event.pos[1]

            #clown was clicked
            if mouse_rect.collidepoint(coord_x, coord_y):
                click_sound.play()
                score += 1
                mouse_velocity += MOUSE_ACCELERATION

                #MOVE MOUSE IN A NEW DIRECTION
                previous_dx = mouse_dx
                previous_dy = mouse_dy
                #to avoid choosing the same direction
                while(previous_dx == mouse_dx and previous_dy == mouse_dy):
                    mouse_dx = random.choice([-1, 1])
                    mouse_dy = random.choice([-1, 1])

            #we missed the mouse
            else:
                miss_sound.play()
                player_lives -= 1


    #move the mouse
    mouse_rect.x += mouse_dx * mouse_velocity
    mouse_rect.y += mouse_dy * mouse_velocity

    #bounce the mouse off the edges of the display
    if mouse_rect.left <= 0 or mouse_rect.right >= WINDOW_WIDTH:
        mouse_dx = -1 * mouse_dx
    if mouse_rect.top <= 0 or mouse_rect.bottom >= WINDOW_HEIGHT:
        mouse_dy = -1 * mouse_dy


    #update HUD
    score_text = font.render("  Score: " + str(score) + "  ", True, DARKBLUE, BLUE)
    lives_text = font.render("  Lives: " + str(player_lives) + "  ", True, DARKBLUE, BLUE)

    #check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #pause the game untill player clicks then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #the player wants to play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    mouse_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    mouse_velocity = MOUSE_STARTING_VELOCITY
                    mouse_dx = random.choice([-1, 1])
                    mouse_dy = random.choice([-1, 1])

                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False

                #player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #bLIT THE BACKGROUND
    display_surface.blit(background_image, background_rect)

    #blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    #blit assets
    display_surface.blit(mouse_image, mouse_rect)

    #update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

    
#end the game
pygame.quit()
