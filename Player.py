class Player:
    x = 0
    y = 0

    def moveRight(self, n):
        self.x += n
        return self.x
    
    def moveLeft(self, n):
        self.x -= n
        return self.x
    
    def moveUp(self, n):
        self.y -= n
        return self.x
    
    def moveDown(self, n):
        self.y += n
        return self.x
