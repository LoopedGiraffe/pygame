import pygame

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding sounds!")

#load sounds
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#play the sound effects
sound_1.play()
pygame.time.delay(2000) #delay in miliseconds
sound_2.play()
pygame.time.delay(2000)

#change the volume of soundeffect
sound_2.set_volume(0.5)
sound_2.play()

#load background music
pygame.mixer.music.load('music.wav')

#play and stopthe music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

#the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#ending game
pygame.quit()


