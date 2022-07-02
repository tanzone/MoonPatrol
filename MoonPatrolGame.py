from random import randint
from Background import Background
from Arena import Arena
from Rover import Rover
from Props import Props
from Alien import Alien
from Tank import Tank
from Utility import File, Stats, Constants

class MoonPatrolGame():

    def __init__(self, lvl):
        self._lvl      = lvl
        self._numRole  = 0
        self._arena    = None
        self._constMOB = Constants.create(Constants, File.readJSON(File, "MOB_lvl"+str(lvl)))  

    #Set level of the game and read new constants
    def setLvl(self, imgAll, imgBG, numRole, score, lvl):
        self._lvl      = lvl
        self._constMOB = Constants.create(Constants, File.readJSON(File, "MOB_lvl"+str(self._lvl)))   

        self.startGame(imgAll, imgBG, numRole, score)             

    #Main function, starts the game based on the level
    def startGame(self, imgAll, imgBG, numRole, score):
        self._arena    = Arena((self._constMOB["ARENA_W"], self._constMOB["ARENA_H"]), (imgAll, imgBG), score)
        self._numRole  = numRole
        for i in range(1, self._numRole+1):
            self.addRover("ROVER_MATRIX"+str(i), "ROVER_KEY"+str(i), i) 

        self.addBackground(imgBG)             

    #Add rover on the arena based on the number of players
    def addRover(self, name, key, num):
        Rover(self._arena, self._constMOB[name], self._constMOB[key], num, self._constMOB) 

    #Add background on arena
    def addBackground(self, imgBG):    
        numImage = (self._constMOB["ARENA_W"] // self._constMOB["IMAGE_LAND_W"]) + 2
        for i in range(len(self._constMOB["BG_MATRIX"])):
            for j in range(numImage):
                Background(self._arena, self._constMOB["BG_MATRIX"][i], (self._constMOB["BG_MATRIXPOS"][i][0] + (self._constMOB["IMG_BG_W"]*j), self._constMOB["BG_MATRIXPOS"][i][1]))
    
    #Function that manages the game status
    def logicGame(self):
        if self._arena.canStop() and not self.canLevelUp() and not self.canWin():
            self._arena.moveAll(self._constMOB["MOVE_SCORE"])
            self.createObstacoles()
            return "True"
        elif self.canLevelUp(): return self._constMOB["IS_LVL"]
        elif self.canWin() : return self._constMOB["IS_WIN"]
        return self._constMOB["IS_LOSE"]

    #Control if can level up
    def canLevelUp(self):   return self._arena.getStats().getScore() >= self._constMOB["SCORE_LVL_UP"]
    #Control if the player win the game
    def canWin(self):       return self._arena.getStats().getScore() >= self._constMOB["FINAL_SCORE"]
    #Create obstacoles in arena with spawn percetual and control
    def createObstacoles(self):
        if self._arena.canContinue():
            if self.spawnProps():               #Spawns props
                Props(self._arena, self._constMOB["PROPS_MATRIX"][self.spawnChoice(len(self._constMOB["PROPS_MATRIX"]))], self._constMOB) 
            if self.spawnAlien():               #Spawns aliens
                Alien(self._arena, self._constMOB["ALIEN_MATRIX"][self.spawnChoice(len(self._constMOB["ALIEN_MATRIX"]))], self._constMOB)
            if self.spawnTank():                #Spawns tanks
                Tank(self._arena,  self._constMOB["TANK_MATRIX"], self._constMOB)

    #Return if is possible spawn a Props item
    def spawnProps(self) -> bool:         
        return self.canSpawn(Props, 0, self._constMOB["PROPS_PERCENT_SPAWN"])       

    #Return if is possible spawn an Alien
    def spawnAlien(self) -> bool : 
        return self.canSpawn(Alien, self._constMOB["NUM_MAX_ALIEN"], self._constMOB["ALIEN_PERCENT_SPAWN"])    

    #Return if is possible spawn an Alien
    def spawnTank(self) -> bool : 
        return self.canSpawn(Tank, self._constMOB["NUM_MAX_TANK"], self._constMOB["TANK_PERCENT_SPAWN"])    

    #Control can spwan an object
    def canSpawn(self, type, numCount, percent):   
        count = 0
        for i in self._arena.getActors():
            if isinstance(i, type): count += 1

        if count <= numCount: return randint(0,1000) < percent
        return False  

    #Choose the object category to spawn
    def spawnChoice(self, length) -> int:   return randint(0, length-1)
    def getConstMOB(self) -> str:           return self._constMOB
    def getBackgrounds(self)-> list:        return self._arena.getBackgrounds()
    def getActors(self) -> list:            return self._arena.getActors()
    def getRovers(self) -> list:            return self._arena.getRovers()
    def getBestScore(self) -> int:          return self._arena.getStats().getBest()
    def getScore(self) -> int:              return self._arena.getStats().getScore()
    def getLvl(self) -> int:                return self._lvl             