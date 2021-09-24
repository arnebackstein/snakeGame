import random

import pygame

import config
from game.boardItem import BoardItem
from game.enums.directions import Direction
from game.enums.position import Position
from game.food import Food
from game.snake import Snake
from game.snakeBodyPart import SnakeBodyPart


class Board(object):
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((config.board['width'] * config.board['scaling'],
                                                config.board['height'] * config.board['scaling']))
        pygame.display.update()
        pygame.display.set_caption('SUPER CRAZY SHIT')

        self.clock = pygame.time.Clock()
        self.snake = Snake([SnakeBodyPart(Position(30, 30))], Direction.UP)
        self.board = {}

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
                self.add_to_board(part)

            for key in self.board:
                if isinstance(self.board[key], BoardItem):
                    x = self.board[key].get_position().x
                    y = self.board[key].get_position().y

                    if isinstance(self.board[key], Food):
                        pygame.draw.rect(self.display, config.colors['green'],
                                         [x * config.board['scaling'], y * config.board['scaling'],
                                          config.board['scaling'], config.board['scaling']])

                    elif isinstance(self.board[key], SnakeBodyPart):
                        pygame.draw.rect(self.display, config.colors['black'],
                                         [x * config.board['scaling'], y * config.board['scaling'],
                                          config.board['scaling'], config.board['scaling']])

            pygame.display.update()
            self.snake.move()
            self.spawn_food()
            self.clock.tick(10)

    def add_to_board(self, item: BoardItem) -> bool:
        x = int(item.get_position().x)
        y = int(item.get_position().y)
        self.board[x, y] = item
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
