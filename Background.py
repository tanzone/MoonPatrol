class Background():

    def __init__(self, arena, matrix: (int, int, int, int, int), posizione: int):
        self._image                 = arena.getImgBG()
        self._imageX, self._imageY  = matrix[0], matrix[1]
        self._imageW, self._imageH  = matrix[2], matrix[3]
        self._x, self._y            = posizione
        self._origX, self._origY    = posizione
        self._speed                 = matrix[4]
        self._arena                 = arena
        arena.addBackground(self)

    #Method that allows the movement of the self object 
    def move(self):
        if self._x + self._imageW <= 0:
            origX = self._arena.getBackgrounds()[-1].originalPosition()[0]
            self._x = origX + (self._x + self._imageW)

        self._x -= self._speed

    #Return the image associated with the object itself
    def getImage(self) -> str:                  
        return self._image

    #Return the original positions where itself spawned
    def originalPosition(self) -> (int, int):   
        return self._origX, self._origY
    
    #Return the position associated with the object itself
    def position(self): 
        return self._x, self._y, self._imageW, self._imageH+30

    #Return the symbol associated with the object
    def symbol(self):   
        return self._imageX, self._imageY, self._imageW, self._imageH