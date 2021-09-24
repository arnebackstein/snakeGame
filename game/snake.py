import config
from game.enums.directions import Direction
from game.position import Position
from game.snakeBodyPart import SnakeBodyPart


class Snake(object):
    def __init__(self, body: list[SnakeBodyPart], direction: Direction):
        self.body = body
        self.direction = direction
        self.grow_next_move = False

    def get_snake(self):
        return self.body

    def set_direction(self, direction):
        if (self.direction == Direction.UP and direction == Direction.DOWN or
                self.direction == Direction.LEFT and direction == Direction.RIGHT or
                self.direction == Direction.DOWN and direction == Direction.UP or
                self.direction == Direction.RIGHT and direction == Direction.LEFT):
            return
        self.direction = direction

    def move(self):
        next_position = Position(self.body[0].get_position().x, self.body[0].get_position().y)
        if self.direction == Direction.UP:
            next_position.y = (next_position.y - 1) % config.board['height']
        elif self.direction == Direction.RIGHT:
            next_position.x = (next_position.x + 1) % config.board['width']
        elif self.direction == Direction.DOWN:
            next_position.y = (next_position.y + 1) % config.board['height']
        elif self.direction == Direction.LEFT:
            next_position.x = (next_position.x - 1) % config.board['width']

        self.body.insert(0, SnakeBodyPart(next_position))
        if not self.grow_next_move:
            self.body.pop(-1)
        else:
            self.grow_next_move = False

    def grow(self):
        self.grow_next_move = True
        pass
