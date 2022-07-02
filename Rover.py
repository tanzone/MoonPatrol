from time import time
from Actor import Actor
from Bullet import Bullet

class Rover(Actor):
    def __init__(self, arena, matrix:(int, int, int, int, int, int, int), keys: str, number: int, constMOB):
        self._image                = arena.getImgCar()
        self._x, self._y           = matrix[0], matrix[1]
        self._imageX, self._imageY = matrix[2], matrix[3]
        self._imageW, self._imageH = matrix[4], matrix[5]
        self._speed                = matrix[6]
        self._keys                 = keys
        self._dx, self._dy         = 0, 0
        self._jump, self._dead     = False, False
        self._type, self._timeDead = str(number),  0
        self._constMOB             = constMOB
        self._arena                = arena
        arena.addActor(self)

    
    # Method that allows the movement of the self object 
    #with additional controls and image changes
    
    def move(self): 
        if not self.isDead(): 
            self.moveMe()       #moves the object in its direction
            self.controlMoves() #control if moves is possible
            self.changeImage()  #if is necessary change image in jump or fall
        else: self.graphicDie()
    
    
    # Moves within the arena the self object of a delta movement
    
    def moveMe(self):
        self._dy += self._constMOB["GRAVITA"]
        self._y  += self._dy
        self._x  += self._dx
    
    #Check if the movements made comply with the regulations
    
    def controlMoves(self):
        arena_w = self._arena.size()[0]

        if self._y > self._constMOB["ARENA_GROUND"] - self._imageH: #esce da sotto
            self._y               = self._constMOB["ARENA_GROUND"] - self._imageH
            self._jump, self._dy  = False, 0

        if self._x < 0: #esce da sinistra
            self._x = 0
        elif self._x > arena_w - self._imageW: #esce da destra
            self._x = arena_w - self._imageW

    #The associated image is changed according to the movement it is making at that moment
    
    def changeImage(self):
        if self._y == self._constMOB["ARENA_GROUND"] - self._imageH: #is normal
            self.setImage(self._constMOB["IMAGE_CAR_X"+self._type], self._constMOB["IMAGE_CAR_Y"+self._type], self._constMOB["IMAGE_CAR_DIM_W"], self._constMOB["IMAGE_CAR_DIM_H"])
        elif self._dy > 0: #is falling
            self.setImage(self._constMOB["IMAGE_CARDOWN_X"+self._type], self._constMOB["IMAGE_CARDOWN_Y"+self._type], self._constMOB["IMAGE_CAR_DIM_W"], self._constMOB["IMAGE_CAR_DIM_H"]) 
        elif self._dy < 0: #is jumping
            self.setImage(self._constMOB["IMAGE_CARUP_X"+self._type], self._constMOB["IMAGE_CARUP_Y"+self._type], self._constMOB["IMAGE_CAR_DIM_W"], self._constMOB["IMAGE_CAR_DIM_H"])

    def setImage(self, imageX: int, imageY: int, imageW: int, imageH: int):
        self._imageX, self._imageY = imageX, imageY
        self._imageW, self._imageH = imageW, imageH

    #Jump
    def go_up(self):
        self.moveDxDy_control(0, -self._constMOB["CAR_JUMP"])
        self._jump = True

    #Turn left 
    def go_left(self):  self.moveDxDy_control(-self._speed, 0)

    #Turn right
    def go_right(self): self.moveDxDy_control(+self._speed, 0)

    #Go down     
    def go_down(self):  self.moveDxDy_control(0, +self._speed)

    #Stay 
    def stay(self):     self.moveDxDy_control(0,0)
    
    #Controls if is possible to keep moving in the same direction
    def moveDxDy_control(self, dx, dy):
        self._dx = dx
        if not self.isJump():
            self._dy = dy

    #Shooting
    def fire(self):
        if not self.isDead(): 
            Bullet(self._arena, (self._x + self._imageW,    self._y + (self._imageH/4), self._constMOB["BULLET_ROVER_X"]), self._constMOB["BULLET_LIST"], self._constMOB["BULLET_SPEED_ROVER_X"], self._constMOB)
            Bullet(self._arena, (self._x +(self._imageW/4), self._y,                    self._constMOB["BULLET_ROVER_Y"]), self._constMOB["BULLET_LIST"], self._constMOB["BULLET_SPEED_ROVER_Y"], self._constMOB)

    #Action to do if the self object do collide with an other object
    
    def collide(self, other):
        if not self.isDead() and isinstance(other, Bullet): 
            if (other.getType() == self._constMOB["BULLET_ALIEN_Y"] or
                other.getType() == self._constMOB["BULLET_TANK_X"]):
                self.dead()
        elif not self.isDead() and not isinstance(other, Rover): 
            self.dead()

    
    #Set dead true and change image to die
    
    def dead(self):
        self._dead     = True
        self._timeDead = time()
    
    #Function that produces the death animation for the Rover

    def graphicDie(self):
        for i in range(0, self._constMOB["STAGE_EXPLOSION"]):
            if time() - self._timeDead > self._constMOB["TIME_EXPLOSION"]*i:
                self.setImage(self._constMOB["IMAGE_CAR_EXPLOSION"+str(i+1)+"_X"], self._constMOB["IMAGE_CAR_EXPLOSION"+str(i+1)+"_Y"], 
                              self._constMOB["IMAGE_CAR_EXPLOSION"+str(i+1)+"_W"], self._constMOB["IMAGE_CAR_EXPLOSION"+str(i+1)+"_H"])
                    
        if time() - self._timeDead > self._constMOB["TIME_EXPLOSION"]*(self._constMOB["STAGE_EXPLOSION"]+1):
            self._arena.removeActor(self)


    #Return the keys for move the object
    def getKeys(self) -> list:  return self._keys.split("-")

    #Control if the self object is jumping
    def isJump(self) -> bool:   return self._jump or self._y != self._constMOB["ARENA_GROUND"] - self._imageH

    #Control if the self object is dead
    def isDead(self) -> bool:   return self._dead

    #Return the image associated with the object itself
    def getImage(self) -> str:  return self._image
    
    #Return the position associated with the object itself
    def position(self):         return self._x, self._y, self._imageW, self._imageH

    #Return the symbol associated with the object
    def symbol(self):           return self._imageX, self._imageY, self._imageW, self._imageH
