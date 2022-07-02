from Actor import Actor
import Props 
import Rover 
import Alien
import Tank
from random import randint

class Bullet(Actor):
    
    def __init__(self, arena, cannonPos: (int, int, int), array:(int, int, int, int), speed, constMOB):
        self._image                 = arena.getImgCar()
        self._imageX, self._imageY  = array[0], array[1]
        self._imageW, self._imageH  = array[2], array[3]
        self._x, self._y            = cannonPos[0], cannonPos[1]
        self._type                  = cannonPos[2]
        self._speed                 = speed
        self._arena                 = arena
        self._constMOB              = constMOB
        arena.addActor(self)
    
    #Method that allows the movement of the self object 
    def move(self):        
        self.moveMe()
        self.controlMoves()

    #Moves within the arena the self object of a delta movement
    def moveMe(self):
        if   self._type == self._constMOB["BULLET_ROVER_X"]: self._x += self._speed #rover X
        elif self._type == self._constMOB["BULLET_ROVER_Y"]: self._y -= self._speed #rover Y
        elif self._type == self._constMOB["BULLET_ALIEN_Y"]: self._y += self._speed #enemy alien
        elif self._type == self._constMOB["BULLET_TANK_X"]: self._x -= self._speed #enemy cannon
    
    #Check if the movements made comply with the regulations
    def controlMoves(self):
        if self._x > self._arena.size()[0] or self._y < self._constMOB["STATS_Y"]: 
            self._arena.removeActor(self)
        
        if self._y + self._imageH > self._constMOB["ARENA_GROUND"] and self._type == self._constMOB["BULLET_ALIEN_Y"]: 
            if self.canProp():
                i = [x for x in self._constMOB["PROPS_MATRIX"][self.spawnChoice(len(self._constMOB["PROPS_MATRIX"])/2)]]
                matrix = [i[0], i[1], i[2], i[3], self._x, i[5], i[6], i[7], i[8]]
                Props.Props(self._arena, matrix,self._constMOB)
            self._arena.removeActor(self)            
    
    #Action to do if the self object do collide with an other object
    def collide(self, other):
        #Control type bullet
        if isinstance(other, Bullet):
            if (other.getType() != self._constMOB["BULLET_ROVER_X"] and
                other.getType() != self._constMOB["BULLET_ROVER_Y"]):
                self._arena.removeActor(self)
        #Control other object
        if  (not (self.getTypeRover() and isinstance(other, Rover.Rover)) and
             not (self.getTypeTank() and isinstance(other, Tank.Tank)) and
             not (self.getTypeAlien() and isinstance(other, Alien.Alien))):
            
            self._arena.removeActor(self)


    #Return if is possible to spawn a Props
    def canProp(self) -> bool:      return randint(0, 1000) < self._constMOB["ALIEN_PERCENT_PROP"]

    #Return what type of item spawn
    def spawnChoice(self, length) -> int:   return randint(0, length-1)

    #Return the type associated with the object itself
    def getType(self):              return self._type

    #Return if self type is rover
    def getTypeRover(self) -> bool: return self._type == self._constMOB["BULLET_ROVER_X"] or self._type == self._constMOB["BULLET_ROVER_Y"]

    #Return if self type is Alien
    def getTypeAlien(self) -> bool: return self._type == self._constMOB["BULLET_ALIEN_Y"]

    #Return if self type is Tank
    def getTypeTank(self) -> bool: return self._type == self._constMOB["BULLET_TANK_X"]

    #Return the image associated with the object itself
    def getImage(self) -> str:      return self._image
    
    #Return the position associated with the object itself
    def position(self):             return self._x, self._y, self._imageW, self._imageH
    
    #Return the symbol associated with the object
    def symbol(self):               return self._imageX, self._imageY, self._imageW, self._imageH

