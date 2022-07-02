import json

#Game statistics
class Stats():

    def __init__(self, score):
        self._best  = 0#File.readBestScore(File)
        self._score = score

    #Update score every move
    def addScore(self, value):
        self._score += value
        if self._score > self._best: 
            self._best = self._score


    def getBest(self):  return self._best
    def getScore(self): return self._score


#Functions on files
class File():

    #Read JSON with all informations about the game
    def readJSON(self, name) -> str:
        with open("./Costants/"+name+".json") as file:
            return json.load(file)

    #Read JSON with bestScore
    def readBestScore(self) -> int:
        with open("./Costants/BestScore.json") as file:
            data = json.load(file)
            return int(data["BESTSCORE"])

    #Write new BestScore on file JSON
    def writeBestScore(self, value):
        with open("./Costants/BestScore.json", "w") as file:
            data = {"BESTSCORE" : value}
            json.dump(data, file)

#Create new dynamic map constants
class Constants():

    def create(self, const):
        const.update({"LAND_Y" : (const["ARENA_H"]-const["IMAGE_LAND_H"]+const["DELTALAND_H"])})
        const.update({"MOUNTAIN_Y" : (const["LAND_Y"]-const["IMAGE_MOUNTAIN_H"]+const["DELTAMOUN_H"])})
        const.update({"BLUE_Y" : (const["MOUNTAIN_Y"]-const["IMAGE_BlUE_H"]+const["DELTABLUE_H"])})
        const.update({"STATS_Y" : const["BLUE_Y"]})

        const.update({"BG_MATRIX" : [[const["IMAGE_BlUE_X"], const["IMAGE_BlUE_Y"], const["IMAGE_BlUE_W"], const["IMAGE_BlUE_H"], const["BLUE_SPEED"]],
                                    [const["IMAGE_MOUNTAIN_X"], const["IMAGE_MOUNTAIN_Y"], const["IMAGE_MOUNTAIN_W"], const["IMAGE_MOUNTAIN_H"], const["MOUNTAIN_SPEED"]],
                                    [const["IMAGE_LAND_X"], const["IMAGE_LAND_Y"], const["IMAGE_LAND_W"], const["IMAGE_LAND_H"], const["LAND_SPEED"]]]})

        const.update({"BG_MATRIXPOS" : [[const["BLUE_X"], const["BLUE_Y"]], [const["MOUNTAIN_X"], const["MOUNTAIN_Y"]], [const["LAND_X"], const["LAND_Y"]]]})


        const.update({"ARENA_GROUND" : (const["LAND_Y"]+5)})
        const.update({"HOLE_X" : const["ARENA_W"]})
        const.update({"HOLE_Y" : (const["ARENA_GROUND"]-7)})
        const.update({"ROCK_X" : const["ARENA_W"]})
        const.update({"ROCK_Y" : (const["ARENA_GROUND"] - const["IMAGE_ROCK_W"] -10)})

        const.update({"PROPS_SPEED" : const["LAND_SPEED"]})
        const.update({"PROPS_MATRIX" : [[const["IMAGE_HOLE_X"], const["IMAGE_HOLE_Y"], const["IMAGE_HOLE_W"], const["IMAGE_HOLE_H"], const["HOLE_X"], const["HOLE_Y"], const["LIFE_HOLE"], const["PROPS_SPEED"], const["PROPS_DELTA_DIM"]],
                                        [const["IMAGE_HOLE2_X"], const["IMAGE_HOLE2_Y"], const["IMAGE_HOLE2_W"], const["IMAGE_HOLE2_H"], const["HOLE_X"], const["HOLE_Y"], const["LIFE_HOLE"], const["PROPS_SPEED"], const["PROPS_DELTA_DIM"]],
                                        [const["IMAGE_ROCK_X"], const["IMAGE_ROCK_Y"], const["IMAGE_ROCK_W"], const["IMAGE_ROCK_H"], const["ROCK_X"], const["ROCK_Y"], const["LIFE_ROCK"], const["PROPS_SPEED"], const["PROPS_DELTA_DIM"]],
                                        [const["IMAGE_ROCK2_X"], const["IMAGE_ROCK2_Y"], const["IMAGE_HOLE2_W"], const["IMAGE_HOLE2_H"], const["ROCK_X"], const["ROCK_Y"], const["LIFE_ROCK2"], const["PROPS_SPEED"], const["PROPS_DELTA_DIM"]]]})
                                    
        const.update({"ROVER_KEY1": (const["MOVE_UP"] + '-' + const["MOVE_LEFT"] + '-' + const["MOVE_RIGHT"] + '-' + const["MOVE_DOWN"] + '-' + const["SHOOT"])})
        const.update({"ROVER_KEY2": (const["MOVE_UP2"] + '-' + const["MOVE_LEFT2"] + '-' + const["MOVE_RIGHT2"] + '-' + const["MOVE_DOWN2"] + '-' + const["SHOOT2"])})

        const.update({"START_POSITION_CAR_X" : (const["ARENA_H"]/2)})
        const.update({"START_POSITION_CAR_Y" : (const["ARENA_GROUND"] - const["IMAGE_CAR_DIM_H"])})
        const.update({"START_POSITION_CAR_X2" : (const["ARENA_H"]/2 - const["IMAGE_CAR_DIM_W"] - 5)})

        const.update({"ROVER_MATRIX1" : [const["START_POSITION_CAR_X"], const["START_POSITION_CAR_Y"], const["IMAGE_CAR_X1"], const["IMAGE_CAR_Y1"], const["IMAGE_CAR_DIM_W"], const["IMAGE_CAR_DIM_H"], const["CAR_SPEED"]]})
        const.update({"ROVER_MATRIX2" : [const["START_POSITION_CAR_X2"], const["START_POSITION_CAR_Y"], const["IMAGE_CAR_X2"], const["IMAGE_CAR_Y2"], const["IMAGE_CAR_DIM_W"], const["IMAGE_CAR_DIM_H"], const["CAR_SPEED"]]})

        const.update({"BULLET_LIST" : [const["IMAGE_BULLET_X"], const["IMAGE_BULLET_Y"], const["IMAGE_BULLET_W"], const["IMAGE_BULLET_H"]]})

        const.update({"BULLET_SPEED_ROVER_X" : (const["CAR_SPEED"] + 1)})

        const.update({"ALIEN_MATRIX" : [[const["IMAGE_ALIEN_X"], const["IMAGE_ALIEN_Y"], const["IMAGE_ALIEN_W"], const["IMAGE_ALIEN_H"], const["ALIEN_SPEED"], const["ALIEN_LIFE"], const["ALIEN_DELTA"], const["ALIEN_TYPE1"]],
                                        [const["IMAGE_ALIEN_X2"], const["IMAGE_ALIEN_Y2"], const["IMAGE_ALIEN_W2"], const["IMAGE_ALIEN_H2"], const["ALIEN_SPEED2"], const["ALIEN_LIFE"], const["ALIEN_DELTA"], const["ALIEN_TYPE2"]]]})

        const.update({"TANK_MATRIX" : [const["ARENA_W"]-const["IMAGE_TANK_W"]-const["IMAGE_TANK_DELTA"], const["ARENA_GROUND"]-const["IMAGE_TANK_H"]-const["IMAGE_TANK_DELTA"], const["IMAGE_TANK_X"], const["IMAGE_TANK_Y"], const["IMAGE_TANK_W"], const["IMAGE_TANK_H"], const["TANK_SPEED"], const["TANK_LIFE"], const["IMAGE_TANK_DELTA"]]})
        
        const.update({"MENU_TITLE": [const["MENU_TITLE_X"], const["MENU_TITLE_Y"], const["MENU_TITLE_W"], const["MENU_TITLE_H"]]})
        
        return const