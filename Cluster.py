class Cluster:
    def __init__(self, loc_x, loc_y, size):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.size = size

    def getX(self):
        return self.loc_x

    def getY(self):
        return self.loc_y

    def getSize(self):
        return self.size