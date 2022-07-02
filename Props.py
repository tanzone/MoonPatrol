from Actor import Actor
import Bullet

class Props(Actor):

    def __init__(self, arena, matrix: (int, int, int, int, int, int, int, int, int), constMOB):
        self._image                 = arena.getImgCar()
        self._imageX, self._imageY  = matrix[0], matrix[1]
        self._imageW, self._imageH  = matrix[2], matrix[3]
        self._x, self._y            = matrix[4], matrix[5]
        self._life, self._speed     = matrix[6], matrix[7]
        self._imageWH_delta         = matrix[8]
        self._constMOB              = constMOB
        self._arena                 = arena
        arena.addActor(self)

    #Method that allows the movement of the self object 
    def move(self):
        if self._x + self._imageW <= 0:
            self._arena.removeActor(self)

        self._x -= self._speed        

    #Action to do if the self object do collide with an other object
    def collide(self, other):
        if isinstance(other, Bullet.Bullet):
            if other.getType() == self._constMOB["BULLET_ROVER_X"]:
                #self._arena.removeActor(other)
                self._life -= 1
                if self._life == 0:
                    self._arena.getStats().addScore(self._constMOB["PROPS_SCORE"])
                    self._arena.removeActor(self)

    #Return the image associated with the object itself
    def getImage(self):     return self._image

    #Return the position associated with the object itself
    def position(self):     return self._x, self._y, self._imageW + self._imageWH_delta, self._imageH + self._imageWH_delta

    #Return the symbol associated with the object
    def symbol(self):       return self._imageX, self._imageY, self._imageW, self._imageH