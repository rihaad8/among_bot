class User(object):
    """docstrin(g forUser."""

    name = ''
    color_wish1 = ''
    color_wish2 = ''
    color_wish3 = ''
    playCount = 0

    def __init__(self, name, color_wish1, color_wish2, color_wish3, playCount):
        super(User, self).__init__()
        self.name = name
        self.color_wish1 = color_wish1
        self.color_wish2 = color_wish2
        self.color_wish3 = color_wish3
        self.playCount = playCount

    def toList(self):
        attrList = [self.name, self.color_wish1, self.color_wish2, self.color_wish3, self.playCount]
        return attrList
