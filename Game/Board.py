import Ball
import Stick

class  Board(object):
    """docstring for  Board."""
    stickMovement = 0

    def __init__(self, width, height, ball, stick):
        self.width = width
        self.height = height
        self.ball = ball
        self.stick = stick

    def evaluate(self):
        if self.stickMovement > 0:
            self.stick.moveUp()
        elif self.stickMovement < 0:
            self.stick.moveDown()
        self.stickMovement = 0
        if self.ball.positionForecast()[0] < 1.0 or \
                    (self.ball.positionForecast()[0] >= self.width and \
                    self.ball.positionForecast()[1] in \
                    range(*self.stick.getRange())):
            self.ball.bounceVertical()
        elif self.ball.positionForecast()[0] >= self.width and \
                    self.ball.positionForecast()[1] not in \
                    range(*self.stick.getRange()):
            return False
        if self.ball.positionForecast()[1] < 1.0 or \
                    self.ball.positionForecast()[1] > self.height:
            self.ball.bounceHorizontal()
        self.ball.move()
        return True

    def render(self):
        print("╔",end=(""))
        print("═" * (self.width-1))
        for l in range(1,self.height):
            print("║", end=(""))
            curr_x = 1
            if l == int(self.ball.position[1]):
                print(" " * (int(self.ball.position[0]-1)), end=("○"))
                curr_x = int(self.ball.position[0]+1)
            if l in range(*self.stick.getRange()):
                print(" " * (int(self.width) - curr_x), end=("|"))
            print("")
        print("╚",end=(""))
        print("═" * (self.width-1))
