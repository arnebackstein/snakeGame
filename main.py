import pygame

from Directions import Direction
from snake import Snake

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('SUPER CRAZY SHIT')

# colors
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

game_over = False

clock = pygame.time.Clock()

snake = Snake();

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.setDirection(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.setDirection(Direction.RIGHT)
            elif event.key == pygame.K_UP:
                snake.setDirection(Direction.UP)
            elif event.key == pygame.K_DOWN:
                snake.setDirection(Direction.DOWN)

    dis.fill(white)

    for part in snake.getSnake():
        pygame.draw.rect(dis, black, [part[0], part[1], 10, 10])

    pygame.display.update()

    snake.move();

    clock.tick(30)
# Hallo
pygame.quit()
quit()
