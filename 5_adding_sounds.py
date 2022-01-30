import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding sounds!")

# load sound effects
sound_1 = pygame.mixer.Sound("./basic_tutorial_assets/sound_1.wav")
sound_2 = pygame.mixer.Sound("./basic_tutorial_assets/sound_2.wav")

# play the sound effects
sound_1.play()
pygame.time.delay(2000)
# sound_2.play()
# pygame.time.delay(2000)

# change the volume of the sound effect
sound_2.set_volume(.1)
sound_2.play()

# load background music
pygame.mixer.music.load("./basic_tutorial_assets/music.wav")

# play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

pygame.quit()
