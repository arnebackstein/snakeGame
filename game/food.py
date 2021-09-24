from game.boardItem import BoardItem
from game.position import Position


class Food(BoardItem):
    def __init__(self, position: Position):
        self.position = position

    def get_position(self):
        return self.position
