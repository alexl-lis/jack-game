class Tip:

    picked = False

    def __init__(self, x, y, title, description):
        self.x = x
        self.y = y
        self.title = title
        self.description = description

    def getText(self):
        return self.text