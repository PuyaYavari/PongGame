import msvcrt

class InputHandler(object):
    """docstring for InputHandler."""

    def __init__(self, board):
        self.board = board

    def evaluate(self):
        input = False
        if msvcrt.kbhit():
            input = msvcrt.getwch()
        if input in ('w','W'):
            self.board.stickMovement = 1
        elif input in ('s','S'):
            self.board.stickMovement = -1
