import pygame
import colour_constants

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing objects")

# give a background colour to the display
display_surface.fill(colour_constants.MAGENTA)


# draw various shapes in display
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, colour_constants.RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, colour_constants.CYAN, (100,100), (200,300), 5)

#Circle(surface, color, centre, radius, thickness ...0 for fill)
pygame.draw.circle(display_surface, colour_constants.BLUE, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2), 100, 5)
pygame.draw.circle(display_surface, colour_constants.YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 0)

#Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, colour_constants.CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, colour_constants.RED, (500, 100, 100, 200))

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update the display
    pygame.display.update()


# end the game
pygame.quit()