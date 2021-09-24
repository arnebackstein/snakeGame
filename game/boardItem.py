from game.enums.position import Position


class BoardItem(object):
    def __init__(self, position: Position):
        self.position = position

    def get_position(self) -> Position:
        """Get the position of an item on the board"""
        return self.position
