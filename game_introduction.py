import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 1500, 700
SCREEN = pygame.display.set_mode(SIZE)

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255

SCREEN.fill(RED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # will quit pygame
            quit()  # will quit python

    # Surface - Screen, Color - White, [x,y,width,height]
    pygame.draw.rect(SCREEN, WHITE, [0,0,100,100])
    pygame.draw.circle(SCREEN, BLACK, [300,300], 100)

    pygame.display.flip()