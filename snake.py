from directions import Direction
from position import Position


class Snake(object):
    def __init__(self, body: list[Position], direction: Direction):
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
        next_position = self.body[0]
        if self.direction == Direction.UP:
            next_position.y -= 10
        elif self.direction == Direction.RIGHT:
            next_position.x += 10
        elif self.direction == Direction.DOWN:
            next_position.y += 10
        elif self.direction == Direction.LEFT:
            next_position.x -= 10

        self.body.insert(0, next_position)
        self.body.pop(-1)
