from Actor import Actor
import Bullet
from random import randint, choice

class Alien(Actor):

    def __init__(self, arena, matrix:(int, int, int, int, int, int, int, int), constMOB):
        self._image                 = arena.getImgCar()
        self._imageX, self._imageY  = matrix[0], matrix[1]
        self._imageW, self._imageH  = matrix[2], matrix[3]
        self._x, self._y            = randint(0, arena.size()[0]/2), randint(constMOB["STATS_Y"], int(arena.size()[1]/2))
        self._speed, self._life     = matrix[4], matrix[5]
        self._imageWH_delta         = matrix[6]
        self._type                  = matrix[7]
        self._constMOB              = constMOB
        self._arena                 = arena
        arena.addActor(self)

    #Method that allows the movement of the self object 
    def move(self):
        self.moveMe()
        if self.canShoot():
            Bullet.Bullet(self._arena, (self._x +(self._imageW/2), self._y + self._imageH, self._constMOB["BULLET_ALIEN_Y"]), self._constMOB["BULLET_LIST"], self._constMOB["BULLET_SPEED_ALIEN_Y"], self._constMOB)
    
    #Moves within the arena the self object of a delta movement
    def moveMe(self):
        if self._type == self._constMOB["ALIEN_TYPE1"]:
            delta = choice([-self._speed, 0, self._speed])
            self._x = (self._x + delta) 
            self._y = (self._y + delta) 
            self.controlMovesType1()

        elif self._type == self._constMOB["ALIEN_TYPE2"]:
            self._x += self._speed
            self.controlMovesType2()

    #Check if the movements of type 1 made comply with the regulations
    def controlMovesType1(self):
        if self._x < 0:        self._x = 0
        if self._y < self._constMOB["STATS_Y"] : self._y = self._constMOB["STATS_Y"]
        if self._x+self._imageW > self._arena.size()[0]   : self._x = self._arena.size()[0]   - self._imageW
        if self._y+self._imageH > self._arena.size()[1]/2 : self._y = self._arena.size()[1]/2 - self._imageH

    #Check if the movements made  of type 2 comply with the regulations
    def controlMovesType2(self):
        if self._x < 0 or self._x > self._arena.size()[0] - self._imageW:        
            self._speed = (self._speed * (-1))
            self._x += self._speed 
            self._y += self._imageH

        if self._y < self._constMOB["STATS_Y"] : self._y = self._constMOB["STATS_Y"]
        if self._y+self._imageH > self._arena.size()[1]/2 : self._y = self._arena.size()[1]/2 - self._imageH

    #Return if itself can shoot 
    def canShoot(self) -> bool:
        return randint(0, 1000) < self._constMOB["ALIEN_PERCENT_SHOOT"]

    #Action to do if the self object do collide with an other object
    def collide(self, other):
        if isinstance(other, Bullet.Bullet):
            if other.getType() == self._constMOB["BULLET_ROVER_Y"]:
                #self._arena.removeActor(other)
                self._life -= 1
                if self._life == 0:
                    self._arena.getStats().addScore(self._constMOB["ALIEN_SCORE"])
                    self._arena.removeActor(self)
    
    #Return the image associated with the object itself
    def getImage(self):     return self._image

    #Return the position associated with the object itself
    def position(self):     return self._x, self._y, self._imageW + self._imageWH_delta, self._imageH + self._imageWH_delta

    #Return the symbol associated with the object
    def symbol(self):       return self._imageX, self._imageY, self._imageW, self._imageH