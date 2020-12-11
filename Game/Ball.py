class Ball(object):
    """docstring for Ball."""

    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def positionForecast(self):
        return [self.position[0]+self.speed[0], self.position[1]+self.speed[1]]

    def move(self):
        self.position = [self.position[0]+self.speed[0], self.position[1]+self.speed[1]]

    def bounceHorizontal(self):
        self.speed = [self.speed[0],-self.speed[1]]

    def bounceVertical(self):
        self.speed = [-self.speed[0],self.speed[1]]
