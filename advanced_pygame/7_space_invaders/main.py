import pygame
import random

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()


#define classes
class Game():
    """A class to help control and update gameplay""" 

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """initialize the game"""

        #Set game values
        self.round_number = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_buller_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        #set sounds and music
        self.new_round_sound = pygame.mixer.Sound("new_round.wav")
        self.breach_sound = pygame.mixer.Sound("breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("ship_hit.wav")

        #seta font
        self.font = pygame.font.Font("Spacepatrol-vK7y.ttf", 32)


    def update(self):
        """Update the game"""

        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self):
        """draw the HUD and other information to display"""

        #defining a color
        WHITE = (255, 255, 255)

        #set text
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH//2
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        #bLITE TEH hud TO THE DISPLAY
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)

        pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)



    def shift_aliens(self):
        """shift the aliens down the screen and reverse direction"""
        
        #determine if alien group has hit an edge
        shift = False
        for alien in (self.alien_group.sprites()):
            if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
                shift = True

        #Shift every alien down, change direction, and check fir a breach
        if shift:
            breach = False
            for alien in (self.alien_group.sprites()):
                #shift down
                alien.rect.y += 10*self.round_number

                #reverse the direction and move the alien off the edge so 'shift' doesnt trigger'
                alien.direction = -1*alien.direction
                alien.rect.x += alien.direction*alien.velocity

                #check if an alien reached the ship
                if alien.rect.bottom >= WINDOW_HEIGHT - 100:
                    breach = True


            #aliens breached the line
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status("Aliens breached the line!", "Press 'ENTER' to continiue")

    def check_collisions(self):
        """check for collisions"""
        
        #see if any bullet in the player bullet group hit an alien in te alien group
        if pygame.sprite.groupcollide(self.player_buller_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100

        #see if the player has collided with any bullet in the alien bullet group
        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player.lives -= 1

            self.check_game_status("You've been hit!", "Press 'ENTER' to continue")

    def check_round_completion(self):
        """check to see if a player has complited a single round"""
        
        #if the alien group is empty, you have completed the round
        if not (self.alien_group):
            self.score += 1000*self.round_number
            self.round_number += 1
            
            self.start_new_round()           


    def start_new_round(self):
        """start new round"""

        #create a grid of Aliens 11 columns and 5 rows
        for i in range(8):
            for j in range(3):
                alien = Alien(64 + i*64, 64 + j*64, self.round_number, self.alien_bullet_group)
                self.alien_group.add(alien)

        #pause the game and prompt user to start
        self.new_round_sound.play()
        self.pause_game("Space Invaders Round: " + str(self.round_number), "Press 'ENTER' to begin")

    def check_game_status(self, main_text, sub_text):
        """check to see a status of the game and how player died"""
        
        #empty the bullets groups (with "empty()" method, and reset player and remainibg aliens
        self.alien_bullet_group.empty()
        self.player_buller_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien.reset()
            
        #check if the game is over or if it is simple round reset
        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)

    def pause_game(self, main_text, sub_text):
        """pauses the game"""
        
        global running

        #set colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #Create main pause text
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        #CREATE A SUB PAUSE TEXT
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #Blit the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        #Paue the game untill te user hits enter
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The user wants to play again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                #The user wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    def reset_game(self):
        """reset the game"""
        self.pause_game("Final Score: " + str(self.score), "Press 'ENTER' to play again")

        #reset game values
        self.score = 0
        self.round_number = 1

        self.player.lives = 10000

        #Empty groups
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_buller_group.empty()

        #Start a new game
        self.start_new_round()


class Player(pygame.sprite.Sprite):
    """a class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 10000
        self.velocity = 8

        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("ship_fire.wav")

    def update(self):
        """update the player"""
        keys = pygame.key.get_pressed()

        #move the player within the bound of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        """fire a bullet"""
        #restrict the number of bullets on screen at a time
        if len(self.bullet_group) < 10:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        """reset the player position"""
        self.rect.centerx = WINDOW_WIDTH//2



class Alien(pygame.sprite.Sprite):
    """a class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()

        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1

        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("alien_fire.wav")

    def update(self):
        """update the alien"""
        self.rect.x += self.direction*self.velocity

        #randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """fire a bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        """reset the alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1
        
    
class PlayerBullet(pygame.sprite.Sprite):
    """a class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        
        self.image = pygame.image.load("ship_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.velocity = 12
        bullet_group.add(self)

    def update(self):
        """update the bullet"""
        self.rect.y -= self.velocity

        #if the bullet is off the screen, kill it
        if self.rect.bottom < 0:
            self.kill() #it will remove sprite from sprite group - here ot will remove bullet from bullet group


class AlienBullet(pygame.sprite.Sprite):
    """a class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """initialize bullet"""
        super().__init__()

        self.image = pygame.image.load("alien_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx =  x
        self.rect.centery = y

        self.velocity = 8
        bullet_group.add(self)

    def update(self):
        """update the bullet"""
        self.rect.y += self.velocity

        #if the bullet is off the screen, kill it
        if self.rect.top > WINDOW_HEIGHT:
            self.kill() #it will remove sprite from sprite group - here ot will remove bullet from bullet group



#creating sprite groups:
#create bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

#create a player group and player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)


#create an alien group. WIll add alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()

#TEst aliens... - only for test purposes
#for i in range(10):
    #alien = Alien(64 + i*64, 100, 1, my_alien_bullet_group)
    #my_alien_group.add(alien)


#create a Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()

#main game loop
running = True
while running:
    #check to see if user wans to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #the player wants to fire(by pressing space bar)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()


    #Fill the display
    display_surface.fill((0, 0, 0))

    #update and display all sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    #update and draw Game object
    my_game.update()
    my_game.draw()

    #update the display and tick the clock:
    pygame.display.update()
    clock.tick(FPS)


#End the game
pygame.quit()