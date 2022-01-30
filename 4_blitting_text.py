import pygame
from pygame import display
import colour_constants

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting text")

# see all available system fonts
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)

# define fonts
system_font = pygame.font.SysFont("Calibri", 64)
custom_font = pygame.font.Font("./basic_tutorial_assets/AttackGraffiti.ttf", 32)

# define text
system_text = system_font.render("Dragons Rule!", True, colour_constants.GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("MOVE THE DRAGON SOON", True, colour_constants.RED)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, (WINDOW_HEIGHT//2) + 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) the text surfaces onto the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    pygame.display.update()
        
    

pygame.quit()