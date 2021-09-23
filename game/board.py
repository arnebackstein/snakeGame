import random

import pygame

import config
from game.boardItem import BoardItem
from game.food import Food
from game.enums.directions import Direction
from game.enums.position import Position
from game.snake import Snake


class Board(object):
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((config.board['width'], config.board['height']))
        pygame.display.update()
        pygame.display.set_caption('SUPER CRAZY SHIT')

        self.clock = pygame.time.Clock()
        self.snake = Snake([Position(300, 300)], Direction.UP)
        self.board = [[None] * int(config.board['height'] / 10)] * int(config.board['width'] / 10)

    def start_game_loop(self) -> None:
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.set_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(Direction.RIGHT)
                    elif event.key == pygame.K_UP:
                        self.snake.set_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction(Direction.DOWN)

            self.display.fill(config.colors['white'])

            for part in self.snake.get_snake():
                pygame.draw.rect(self.display, config.colors['black'], [part.x, part.y, 10, 10])

            pygame.display.update()
            self.snake.move()
            self.clock.tick(10)

    def add_to_board(self, item: BoardItem) -> bool:
        # TODO implement
        return False

    def remove_from_board(self, item: BoardItem) -> bool:
        # TODO implement
        return False

    def spawn_food(self):
        x = int(random.uniform(0, config.board['width']))
        y = int(random.uniform(0, config.board['height']))
        self.add_to_board(Food(Position(x, y)))

    def quit(self):
        pygame.quit()