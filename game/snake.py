from game.enums.directions import Direction
from game.enums.position import Position
from game.snakeBodyPart import SnakeBodyPart


class Snake(object):
    def __init__(self, body: list[SnakeBodyPart], direction: Direction):
        self.body = body
        self.direction = direction

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
        next_position = self.body[0].get_position()
        if self.direction == Direction.UP:
            next_position.y -= 1
        elif self.direction == Direction.RIGHT:
            next_position.x += 1
        elif self.direction == Direction.DOWN:
            next_position.y += 1
        elif self.direction == Direction.LEFT:
            next_position.x -= 1

        self.body.insert(0, SnakeBodyPart(next_position))
        self.body.pop(-1)
