import pygame
import random

#initiaize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite groups!")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#define classes

class Player(pygame.sprite.Sprite):
    """A simple class to represent a player fights monsters"""
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5

        self.monster_group = monster_group

    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()

    def move(self):
        """move the player continiously"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        """check for collision between player (self) and the monster group"""
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))


class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster ;)"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Blue-Monster-icon.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity



#create a monster group and add 10 monsters
my_monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

#create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, my_monster_group)
player_group.add(player)

#the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the display
    display_surface.fill((0, 0, 0))

    #Update and Draw assets
    player_group.update()
    player_group.draw(display_surface)
    
    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #update the pygame and tick the clock
    pygame.display.update()
    clock.tick(FPS)
    

#End the game
pygame.quit()