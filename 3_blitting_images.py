import pygame
from pygame import display

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting images")

# create images ... returns a Surface object
dragon_left_image = pygame.image.load("./basic_tutorial_assets/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,20)

dragon_right_image = pygame.image.load("./basic_tutorial_assets/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright=(WINDOW_WIDTH, 20)


# the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 100), (WINDOW_WIDTH, 100), 2)

    pygame.display.update() 


pygame.quit()