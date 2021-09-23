class Snake:
    def __init__(self, body: list[tuple], direction):
        self.body = body
        self.direction = direction

    def get_snake(self):
        return self.body

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        pass