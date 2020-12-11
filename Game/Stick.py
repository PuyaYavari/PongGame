class Stick(object):
    """docstring for Stick."""

    def __init__(self, size, position, speed, limits):
        self.size = size
        self.position = position
        self.speed = speed
        self.limits = limits

    def moveUp(self):
        if self.position - self.speed > self.limits["min"]:
            self.position -= self.speed
        else:
            self.position = 1

    def moveDown(self):
        if self.position + self.size + self.speed < self.limits["max"]:
            self.position += self.speed
        else:
            self.position = self.limits["max"] - self.size

    def getRange(self):
        return self.position, self.position + self.size
