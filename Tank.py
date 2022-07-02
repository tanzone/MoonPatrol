from Actor import Actor
import Bullet
from random import randint

class Tank(Actor):

    def __init__(self, arena, matrix:(int, int, int, int, int, int, int), constMob):
        self._image                     = arena.getImgCar()
        self._x, self._y                = matrix[0], matrix[1]
        self._imageX, self._imageY      = matrix[2], matrix[3]
        self._imageW, self._imageH      = matrix[4], matrix[5]
        self._imageDelta                = matrix[8]
        self._speed, self._life         = matrix[6], matrix[7]
        self._constMOB                  = constMob 
        self._arena                     = arena
        arena.addActor(self)

    #Function that Moves the tank

    def move(self):
        self.moveMe()
        self.controlMoves()
        if self.canShoot():
            Bullet.Bullet(self._arena, (self._x,self._y + self._imageH/3 , self._constMOB["BULLET_TANK_X"]), self._constMOB["BULLET_LIST"], self._constMOB["BULLET_SPEED_TANK_X"], self._constMOB)

    #Function that changes the x position of the tank to move it

    def moveMe(self):
        self._x -= self._speed
    
    #Function that checks if the tank can move
  
    def controlMoves(self):
        arena_w = self._arena.size()[0]

        if self._x < 2*arena_w/3:            self._speed *= -1 
        if self._x > arena_w - self._imageW: self._speed *= -1 
    
    #Function that returns true if the tank can shoot, it is based on the probability set in the constants
    
    def canShoot(self):
        return randint(0, 1000) < self._constMOB["TANK_PERCENT_SHOOT"]
    
    #Function manages tanks collisions

    def collide(self, other):
        if isinstance(other, Bullet.Bullet):
            if other.getType() == self._constMOB["BULLET_ROVER_X"]:
                self._life -= 1
                if self._life == 0:
                    self._arena.getStats().addScore(self._constMOB["TANK_SCORE"])
                    self._arena.removeActor(self)

    def getImage(self):     return self._image
    def position(self):     return self._x, self._y, self._imageW+self._imageDelta, self._imageH+self._imageDelta 
    def symbol(self):       return self._imageX, self._imageY, self._imageW, self._imageH
