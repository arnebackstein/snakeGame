from Directions import Direction


class Snake:
    def __init__(self, body: list[tuple], direction: Direction):
        # Body format = [(pos_x, pos_y)]
        self.body = body
        self.direction = direction

    def get_snake(self):
        return self.body

    def set_direction(self, direction):
        self.direction = direction