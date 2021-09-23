from bardItem import BoardItem
from position import Position


class Food(BoardItem):
    def __init__(self, position: Position):
        self.position = position

    def get_position(self):
        return self.position
