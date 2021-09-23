class Snake:
    def __init__(self, body: list(tuple), direction):
        self.body = body
        self.direction = direction

    def getSnake(self):
        return self.body

    def setDirection(self, direction):
        self.direction = direction