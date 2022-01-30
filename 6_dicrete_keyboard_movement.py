import pygame
from pygame import display
from pygame.constants import K_LEFT

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement!")

# set game values
VELOCITY = 40

# load the image(s)
dragon_image = pygame.image.load("./basic_tutorial_assets/dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # check for discrete (not continuous!) movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
    
    # clear the screen
    display_surface.fill((0,0,0))

    # blit the image
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()



pygame.quit()