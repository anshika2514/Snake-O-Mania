import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1150, 600
SCREEN = pygame.display.set_mode(SIZE)

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
FONT_FAMILY = "font.otf"
BACKGROUND_MUSIC = "SnakeMusic.mp3"
COIN_SOUND = "coin_sound.wav"
SPLASH_SCREEN = "snake_bg.jpg"

bg_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
bg_music.play()

bg_music.set_volume(0.5)

coin = pygame.mixer.Sound(COIN_SOUND)


snake_w = 50
snake_h = 50

def homeScreen():
    home_bg = pygame.image.load(SPLASH_SCREEN)
    home_bg = pygame.transform.scale(home_bg,(WIDTH, HEIGHT))
    msg_1 = "SNAKE GAME"
    msg_2 = "Press SPACE to Start Game"
    font = pygame.font.Font(FONT_FAMILY, 60)
    text_1 = font.render(msg_1, True, RED)
    text_2 = font.render(msg_2, True, RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # will quit pygame
                quit()  # will quit python

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        SCREEN.blit(home_bg, (0,0))
        SCREEN.blit(text_1, (WIDTH // 2 - 300, HEIGHT // 2 - 60))
        SCREEN.blit(text_2, (100, 100))
        pygame.display.flip()

def gameOver():
    msg = "GAME OVER"
    font = pygame.font.Font(FONT_FAMILY,80)
    text = font.render(msg, True, RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # will quit pygame
                quit()  # will quit python

        SCREEN.blit(text, (WIDTH//2 - 200, HEIGHT//2 - 40))
        pygame.display.flip()

def score(counter):
    msg = "Score : {}".format(counter)
    # font = pygame.font.SysFont(None, 50)
    font = pygame.font.Font(FONT_FAMILY, 50)
    text = font.render(msg, True, RED)
    SCREEN.blit(text, (WIDTH - 300, 10))

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(SCREEN, BLACK, [snakeList[i][0],
                                         snakeList[i][1],
                                         snake_w, snake_h])

def game():
    SPEED = 0
    rect_x = 0
    rect_y = 0
    move_x = SPEED
    move_y = SPEED

    frog_img = pygame.image.load("frog.png")
    frog_w = frog_img.get_width()
    frog_h = frog_img.get_height()
    snakeList = []
    snakeLength = 1

    FPS = 100
    clock = pygame.time.Clock()

    counter = 0

    frog_x = random.randint(0, WIDTH - frog_w)
    frog_y = random.randint(0, HEIGHT - frog_h)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # will quit pygame
                quit()  # will quit python

            if event.type == pygame.KEYDOWN:
                SPEED = 5
                if event.key == pygame.K_RIGHT:
                    move_x = SPEED
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -SPEED
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = SPEED
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -SPEED
                    move_x = 0

        SCREEN.fill(WHITE)

        SCREEN.blit(frog_img, (frog_x, frog_y))
        frog_rect = pygame.Rect(frog_x, frog_y, frog_w, frog_h)
        snake_rect = pygame.draw.rect(SCREEN, BLACK, [rect_x, rect_y, snake_w, snake_h])
        rect_x += move_x
        rect_y += move_y

        snakeHead = []
        snakeHead.append(rect_x)
        snakeHead.append(rect_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        drawSnake(snakeList)

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()
                print("Game Over...")

        if snake_rect.colliderect(frog_rect):
            frog_x = random.randint(0, WIDTH - frog_w)
            frog_y = random.randint(0, HEIGHT - frog_h)
            snakeLength += 20
            counter += 1
            coin.play()

        score(counter)

        if rect_x > WIDTH:
            rect_x = -snake_w
        elif rect_x < -snake_w:
            rect_x = WIDTH

        if rect_y > HEIGHT:
            rect_y = -snake_h
        elif rect_y < -snake_h:
            rect_y = HEIGHT

        pygame.display.update()
        clock.tick(FPS)

homeScreen()