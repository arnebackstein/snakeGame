from game.boardItem import BoardItem
from game.position import Position


class Border(BoardItem):

    def __init__(self, position: Position):
        super().__init__(position)

