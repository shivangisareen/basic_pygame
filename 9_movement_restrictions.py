import pygame
from pygame import display
from pygame.display import set_caption

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Restricted keyboard movement")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# set game values
VELOCITY = 5

# load images
dragon_image = pygame.image.load("./basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get a list of all keys currently being down
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY


    # fill the display_surface
    display_surface.fill((0,0,0))

    # blit assets
    display_surface.blit(dragon_image, dragon_rect)

    # update the display
    pygame.display.update()
    
    # tick the clock
    # loop is running FPS amount
    clock.tick(FPS)
            

pygame.quit()

