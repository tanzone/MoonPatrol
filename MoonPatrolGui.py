import g2d
from MoonPatrolGame import MoonPatrolGame
from Menu import Menu
from Utility import File

class MoonPatrolGui():
    def __init__(self, game: MoonPatrolGame):
        self._game     = game
        self._constMOB = game.getConstMOB()
        #self._songMenu = g2d.load_audio(self._constMOB["AUDIO_LOAD_MENU"])
        #self._songGame = g2d.load_audio(self._constMOB["AUDIO_LOAD_GAME"])
        self._imgAll   = g2d.load_image(self._constMOB["IMAGES_MOON_PATROL"])
        self._imgBG    = g2d.load_image(self._constMOB["IMAGES_MOON_PATROL_BG"])
        self._menu     = Menu(( self._constMOB["ARENA_W"],  self._constMOB["ARENA_H"]), self._imgAll, self._constMOB)
        
        self.startMenu()

    #Shows the menu
    def startMenu(self):
        g2d.init_canvas((self._constMOB["ARENA_W"], self._constMOB["ARENA_H"]))
        g2d.main_loop(self.tick,  self._constMOB["FPS"])

    #Starts the game
    def startGame(self):
        #g2d.pause_audio(self._songMenu)
        #g2d.play_audio(self._songGame, True)
        self._menu.stopGame()
        self._game.setLvl(self._imgAll, self._imgBG, self._menu.getPlayer(), 0, 1)

    #Function that is called repeatedly
    def tick(self):
        if   self._menu.getMenu()   : self._menu.drawMenu(self.getBestScore())      # Draw menu
        elif self._menu.getRules()  : self._menu.drawRules()  # Draws the rules of the game
        elif self._menu.getGame()   : self.startGame()
        else: self.controlGame(self._game.logicGame())

    #Gets the best score from the BestScore file
    def getBestScore(self):
        try:     return self._game.getBestScore()
        except : return File.readBestScore(File)
    
    #Main function that manages the game progress
    def controlGame(self, value):
        if value == "True":     # Game Logic 
            self.keyControl()   # Control key pressed or released Player 1
            self.drawGame()     # Game design
        elif value == self._constMOB["IS_WIN"] : self.drawResult(self._constMOB["GAME_WIN"], (0,255,0), self._game.getScore(), self._game.getBestScore(), 1)
        elif value == self._constMOB["IS_LVL"] : self.drawResult(self._constMOB["GAME_LVL"], (150,255,150), self._game.getScore(), self._game.getBestScore(), 0)
        elif value == self._constMOB["IS_LOSE"]: self.drawResult(self._constMOB["GAME_LOSE"], (255,0,0),    self._game.getScore(), self._game.getBestScore(), -1)

    #Control what key i pressed or released
    def keyControl(self):
        for obj in self._game.getRovers():
            command = obj.getKeys()
            if g2d.key_pressed(command[0]):     obj.go_up()
            elif g2d.key_pressed(command[1]):   obj.go_left()
            elif g2d.key_pressed(command[2]):   obj.go_right()
            elif g2d.key_pressed(command[3]):   obj.go_down()
    
            elif (g2d.key_released(command[0])  or
                  g2d.key_released(command[1])  or 
                  g2d.key_released(command[2])  or 
                  g2d.key_released(command[3])):
                obj.stay()

            if g2d.key_pressed(command[4]):     obj.fire()

    #Draw all item in arena
    def drawGame(self):
        g2d.clear_canvas() 
        g2d.set_color((0,0,0)) 
        g2d.fill_rect((0,0, self._constMOB["ARENA_W"], self._constMOB["ARENA_H"])) 
        self.drawStats(self._game.getScore(), self._game.getBestScore())        
        self.drawSigleList(self._game.getBackgrounds())
        self.drawSigleList(self._game.getActors())

    #Draws the statistics of your game while you play
    def drawStats(self, score, best):
        g2d.set_color((123,123,123))
        g2d.fill_rect((0,0,  self._constMOB["ARENA_W"], self._constMOB["STATS_Y"]))
        g2d.set_color((255,0,0))
        g2d.draw_line((0, self._constMOB["STATS_Y"]), (self._constMOB["ARENA_W"], self._constMOB["STATS_Y"]))
        g2d.draw_line(( self._constMOB["ARENA_W"]/2, 0), (self._constMOB["ARENA_W"]/2, self._constMOB["STATS_Y"]))
        g2d.draw_text("SCORE     -> " + str(self._game.getScore()), (20, 20), self._constMOB["SIZE_STAT"])
        g2d.draw_text("BESTSCORE -> " + str(self._game.getBestScore()), (20, 70), self._constMOB["SIZE_STAT"])
        g2d.draw_text("LEVEL -> " + str(self._game.getLvl()), (self._constMOB["ARENA_W"]/2 +20, 30), self._constMOB["SIZE_STAT"])

    #Draws only the objects from the given list
    def drawSigleList(self, objects: list):     
        for obj in objects:
            g2d.draw_image_clip(obj.getImage(), obj.symbol(), obj.position())

    #Draws the result screen with the endgame text based on your performance
    def drawResult(self, result, rgb, score, bestScore, count):
        g2d.clear_canvas()
        g2d.set_color(rgb)
        g2d.draw_text_centered(result, (self._constMOB["ARENA_W"]/2, self._constMOB["ARENA_H"]/5), 3*self._constMOB["SIZE_TEXT2"])
        g2d.set_color((123,123,123))
        g2d.draw_text_centered("YOUR SCORE : " +'% 6.0f'%(self._game.getScore()), (self._constMOB["ARENA_W"]/2, self._constMOB["ARENA_H"]/3 + 4*self._constMOB["SIZE_TEXT2"]), 2*self._constMOB["SIZE_TEXT2"])
        g2d.draw_text_centered("BESTSCORE : " +'% 6.0f'%(self._game.getBestScore()), (self._constMOB["ARENA_W"]/2, self._constMOB["ARENA_H"]/3 + 8*self._constMOB["SIZE_TEXT2"]), 2*self._constMOB["SIZE_TEXT2"])
        g2d.set_color((123,123,123))
        g2d.draw_text_centered("PRESS [ENTER] TO CONTINUE", (self._constMOB["ARENA_W"]/2, 3*self._constMOB["ARENA_H"]/4 + self._constMOB["ARENA_H"]/8), 2*self._constMOB["SIZE_TEXT"]/3)
        if g2d.key_pressed("Enter"):
            if count == 0:
                self._game.setLvl(self._imgAll, self._imgBG, self._menu.getPlayer(), score, self._game.getLvl()+1)
            elif abs(count) == 1:
                #g2d.pause_audio(self._songGame)
                #g2d.play_audio(self._songMenu, True)
                self._menu.setChoice(True, False, False, 0)    # Make the menu reappear

