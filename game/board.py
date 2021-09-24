import random

import pygame

import config
from game.boardItem import BoardItem
from game.border import Border
from game.enums.directions import Direction
from game.position import Position
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

        self.game_over = False
        self.clock = pygame.time.Clock()
        self.snake = Snake([SnakeBodyPart(Position(15, 15))], Direction.UP)
        self.board = {}

    def start_game_loop(self) -> None:
        self.draw_borders()
        self.spawn_food()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.set_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.set_direction(Direction.RIGHT)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.set_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.set_direction(Direction.DOWN)

            self.display.fill(config.colors['white'])

            self.remove_from_board_by_type(SnakeBodyPart)

            snake_body = self.snake.get_snake()
            for i in range(1, len(snake_body), 1):
                self.add_to_board(snake_body[i])

            self.handle_collision(snake_body[0])
            self.add_to_board(snake_body[0])

            self.draw_board()
            pygame.display.update()
            self.snake.move()
            self.clock.tick(10)

    def handle_collision(self, item):
        item_on_board = self.board.get((item.get_position().x, item.get_position().y))
        if item_on_board:
            if isinstance(item_on_board, Food):
                self.snake.grow()
                self.spawn_food()
                self.remove_from_board(item_on_board)
            elif isinstance(item_on_board, SnakeBodyPart):
                self.game_over = True
            elif isinstance(item_on_board, Border):
                self.game_over = True

    def draw_borders(self):
        for x in range(config.board['width']):
            if x < config.board['width'] * 0.3 or x > config.board['width'] * 0.7:
                self.add_to_board(Border(Position(x, 0)))
                self.add_to_board(Border(Position(x, config.board['height']-1)))

        for y in range(1, config.board['height'] - 1):
            if y < config.board['height'] * 0.3 or y > config.board['height'] * 0.7:
                self.add_to_board(Border(Position(0, y)))
                self.add_to_board(Border(Position(config.board['width']-1, y)))

    def add_to_board(self, item: BoardItem) -> bool:
        x = int(item.get_position().x)
        y = int(item.get_position().y)
        self.board[x, y] = item
        return False

    def remove_from_board(self, item: BoardItem) -> bool:
        # TODO implement
        return False

    def remove_from_board_by_type(self, item_type):
        to_remove_keys = list()
        for key in self.board:
            if type(self.board[key]) is item_type:
                to_remove_keys.append(key)
        for key in to_remove_keys:
            self.board.pop(key)

    def draw_board(self):
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

                elif isinstance(self.board[key], Border):
                    pygame.draw.rect(self.display, config.colors['black'],
                                     [x * config.board['scaling'], y * config.board['scaling'],
                                      config.board['scaling'], config.board['scaling']])

    def spawn_food(self):
        x = int(random.uniform(0, config.board['width']))
        y = int(random.uniform(0, config.board['height']))
        if not (x, y) in self.board:
            self.add_to_board(Food(Position(x, y)))

    def quit(self):
        pygame.quit()
