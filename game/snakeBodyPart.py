from game.boardItem import BoardItem
from game.enums.position import Position


class SnakeBodyPart(BoardItem):

    def __init__(self, position):
        super().__init__(position)

