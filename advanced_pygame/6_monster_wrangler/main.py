import pygame
import random

#initialize pygame
pygame.init()

#set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    """A class to control gameplay"""

    def __init__(self, player, monster_group):
        """initialize the game object"""

        #set game values
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        #set sounds and music
        self.next_level_sound = pygame.mixer.Sound("next_level.wav")

        #set font
        self.font = pygame.font.Font("RonysiswadiArchitect2-x3POK.ttf", 24)

        #set images
        blue_image = pygame.image.load("Blue-Monster-icon.png")
        green_image = pygame.image.load("Green-Monster-icon.png")
        purple_image = pygame.image.load("Purple-Monster-icon.png")
        yellow_image = pygame.image.load("Orange-Monster-icon.png")

        #this list corresponds to the monster type attribute (0 -> blue, 1 -> green, 2 -> purple, 3 - > yellow):
        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0,3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect() #all monster images have the same dimentions so only one rect is needen :)
        self.target_monster_rect.centerx = WINDOW_WIDTH//2
        self.target_monster_rect.top = 30


    def update(self):
        """Update our game object"""

        # assuring that time round is measured in seconds - we are using for that our FPS which we have set to 60 - which means 60 frames per second
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        #check for collisions
        self.check_collisions()


    def draw(self):
        """draw the HUD and other to the display"""
        #set collors
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)

        #add the monster colors to a list where the index of the color matches target_monster_images
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        #set text
        catch_text = self.font.render("Current catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH//2
        catch_rect.top = 5

        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render("Current Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render("Round Time: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render("Warps: " + str(self.player.warps), True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)


        #blit the HUD
        display_surface.blit(catch_text, catch_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(time_text, time_rect)
        display_surface.blit(warp_text, warp_rect)
        display_surface.blit(self.target_monster_image, self.target_monster_rect)

        pygame.draw.rect(display_surface, colors[self.target_monster_type], (WINDOW_WIDTH//2 - 32, 30, 64, 64), 2)
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT -200), 4)


    def check_collisions(self):
        """Check for collisions between player and monsters"""
        
        #check for collision between a player and an individual monster (specific color type)
        #we must test the type of the monster to see if ot matches the type of our target monster
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)

        #we collided with a monster
        if collided_monster:
            #caught correct monster
            if collided_monster.type == self.target_monster_type:
                #incerase the score (100 points multiplied by round number)
                self.score += 100*self.round_number
                #remove caught monster from screen (by removing colllided monster from its monster_group)
                collided_monster.remove(self.monster_group)

                if (self.monster_group):
                    #there are more monsters to catch
                    self.player.catch_sound.play()
                    self.choose_new_target()
                else:
                    #the round is complete
                    self.player.reset()
                    self.start_new_round()
            #caught the wrong monster
            else:
                self.player.die_sound.play()
                self.player.lives -= 1

                #check for game over
                if self.player.lives <= 0:
                #pause the game
                    self.pause_game("Final score: " + str(self.score), "Press 'Enter' to play again")
                    self.reset_game()
                self.player.reset()


    def start_new_round(self):
        """populate board with new monsters"""
        #bonus - bigger when quicker round was finnished
        self.score += int(10000*self.round_number/(1 + self.round_time))

        #reset round values:
        self.round_time = 0
        self.frame_count = 0
        self.round_number += 1
        self.player.warps += 1

        #remove any remaining monsters frim a game reset
        for monster in self.monster_group:
            self.monster_group.remove(monster)

        #add monsters to the monster group
        #for each round adding 4 monsters (in each collor)
        for i in range(self.round_number):
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[0], 0))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[1], 1))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[2], 2))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[3], 3))
    
        #choose new target monster
        self.choose_new_target()

        #play a soun of new level
        self.next_level_sound.play()

    
    def choose_new_target(self):
        """choose a new target monster for the play"""
        target_monster = random.choice(self.monster_group.sprites())
        #update type and image of target monster:
        self.target_monster_type = target_monster.type
        self.target_monster_image = target_monster.image

    def pause_game(self, main_text, sub_text):
        """pause game"""
        global running
        #set a color
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #create the main pause text:
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        #CREATE THE SUP PAUSE TEXT
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #Display pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        #pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  #ENTER is K_RETURN
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    def reset_game(self):
        """reset the game"""

        self.score = 0
        self.round_number = 0

        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()

        self.start_new_round()


class Player(pygame.sprite.Sprite):
    """player class that the user can control"""

    def __init__(self):

        """initialize player"""
        super().__init__()

        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("coin.wav")
        self.die_sound = pygame.mixer.Sound("miss.wav")
        self.warp_sound = pygame.mixer.Sound("click.wav")

    def update(self):
        """update player"""
        keys = pygame.key.get_pressed()

        #move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity


    def warp(self):
        """warp the player to the bottom safe zone"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        """resre the players position"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT


class Monster(pygame.sprite.Sprite):
    """a class to create enemy monster objects"""

    def __init__(self, x, y, image, monster_type):
        """initialize monster"""
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #monster type is an int: 0 -> blue, 1 -> green, 2 -> purple, 3 - > yellow
        self.type = monster_type

        #set random motion
        self.dx = random.choice([-1, 1]) #change in x direction
        self.dy = random.choice([-1, 1]) #change in y direction
        self.velocity = random.randint(1, 5) #random speed 


    def update(self):
        """update the monster"""

        #monster movement
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #bounce the monster off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.dy = -1*self.dy



#create a player group and player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#create a monster group 
my_monster_group = pygame.sprite.Group()

#TEST MONSTERS
#monster = Monster(500, 500, pygame.image.load("Green-Monster-icon.png"), 1)
#my_monster_group.add(monster)
#monster = Monster(500, 500, pygame.image.load("Blue-Monster-icon.png"), 0)
#my_monster_group.add(monster)

#create a game object
my_game = Game(my_player, my_monster_group)
my_game.pause_game("Monster Wrangler", "Press ENTER to begin")
my_game.start_new_round()

#the main game loop
running = True
while running:
    #check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #player wants to warp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()


    #fill the display
    display_surface.fill((0, 0, 0))

    #update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #update and draw the Game
    my_game.update()
    my_game.draw()


    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

