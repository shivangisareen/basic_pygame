import pygame
from pygame.constants import MOUSEMOTION

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse movement!")


# load images
dragon_image = pygame.image.load("./basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        
        # drag the object when the mouse button is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        if event.type == pygame.QUIT:
            running = False
        

    # clear the display
    display_surface.fill((0,0,0))

    # blit the image
    display_surface.blit(dragon_image, dragon_rect)

    # update the display
    pygame.display.update()


pygame.quit()