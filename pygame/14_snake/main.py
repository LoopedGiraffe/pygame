import pygame
import random

#initialize pygame
pygame.init()

#set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

#set FPS and clock
FPS = 10
clock = pygame.time.Clock()

#set game variables
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

#set colors
GREEN = (0, 255, 0, 0)
DARKGREEN = (10, 50, 10)
BLUE = (101,189,217)
DARKBLUE = (6,57,112)
YELLOW = (255,255,0)
ORANGE = (252, 64, 3)
RED = (136,1,2)
PINK = (255, 137, 200)

#set fonts
font = pygame.font.SysFont("gabriola", 48)


#set text
title_text = font.render("~~Snake~~", True, DARKBLUE, BLUE)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("  Score:  " + str(score) + "  ", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("  GAME OVER  ", True, ORANGE, DARKBLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("  Press any key to play again ", True, BLUE, YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#set sounds and music
pick_up_sound = pygame.mixer.Sound("coin.wav")

#set imagesv(in this case use simple rects.. so just create their coordinates)
#for rectangle we need (top-left) x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, YELLOW, head_coord)

body_coords = [] # EMPTY LIST AT THE BEGINNING BECAUSE SNAKE DOESNT HAVE BODY - ONLY HEAD




#the main game loop
running = True
while running:
    #check to see if user wants to quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
            
    #add the head coorinate to the first index of the body coorinate list
    #this will essentially move all of the snakes body by one position in the list          
    body_coords.insert(0, head_coord)
    body_coords.pop()

    #update the x,y position of snake head and make a new coordinate:
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    #check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #pause the game until the player presses a key, then reset the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #the player wants to play again:
                if event.type == pygame.KEYDOWN:
                    score = 0

                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT//2 + 100
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

                    body_coords = []

                    snake_dx = 0
                    snake_dy = 0

                    is_paused = False
                
                #the player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    #check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

    #addning body 
        body_coords.append(head_coord)

    #update HUD
    score_text = font.render("  Score:  " + str(score) + "  ", True, GREEN, DARKGREEN)

    #fill the surface (background collor)
    display_surface.fill(PINK)

    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #Blit assets:

    #the body:
    for body in body_coords:
        pygame.draw.rect(display_surface, ORANGE, body)
    #head:
    head_rect = pygame.draw.rect(display_surface, YELLOW, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    #update display abd tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()
