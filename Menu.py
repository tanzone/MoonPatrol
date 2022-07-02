import g2d
from random import randint
from Utility import File

class Menu():
    
    def __init__(self, arena:(int, int), imgAll, constMOB):
        self._w, self._h = arena
        self._constMOB   = constMOB
        self._imgAll     = imgAll
        self._start      = True
        self._menu       = True
        self._rules      = False
        self._game       = False
        self._numPlayer  = 0

    #Draws the Menu
    def drawMenu(self, bestScore):
        if self._start: 
            self.drawTitle()
        else:
            self.drawButtons(bestScore)
            self.drawCopyright()
            self.drawColorMenu(g2d.mouse_position(), bestScore)

    #Draws the title menu
    def drawTitle(self):
        g2d.set_color((0,0,0))
        g2d.fill_rect((0, 0, self._w, self._h))
        posTitle = [self._w/2-((self._constMOB["MENU_TITLE_W"]+ self._constMOB["MENU_DELTA"])/2), self._h/2-((self._constMOB["MENU_TITLE_W"]+ self._constMOB["MENU_DELTA"])/2), 
                    self._constMOB["MENU_DELTA"]+ self._constMOB["MENU_TITLE_W"], self._constMOB["MENU_TITLE_W"]+ self._constMOB["MENU_DELTA"]]
         
        g2d.draw_image_clip(self._imgAll, self._constMOB["MENU_TITLE"], (posTitle))
        g2d.set_color((255,255,0))
        g2d.draw_text_centered("PRESS SPACEBAR TO CONTINUE", (self._w/2, self._h-45), 25)
        if g2d.key_pressed("Spacebar"): 
            self._start = False
            self.setChoice(True, False, False, 0)

    #Draws the buttons of the menu
    def drawButtons(self, bestScore):
        g2d.clear_canvas()
        g2d.set_color((123,123,123))
        g2d.draw_line((self._w/2, 0), (self._w/2, self._h-20))
        g2d.draw_line((0, self._h/2), (self._w, self._h/2))
        
        g2d.draw_text_centered("1 PLAYER", (self._w/4, self._h/4), self._constMOB["SIZE_TEXT"])
        g2d.draw_text_centered("Best Score: " + str(bestScore), (self._w/4, self._h/4 + (self._constMOB["SIZE_TEXT"])), self._constMOB["SIZE_TEXT"]/2)
        g2d.draw_text_centered("2 PLAYER", (3*self._w/4, self._h/4), self._constMOB["SIZE_TEXT"])
        g2d.draw_text_centered("RULES", (self._w/4, 3*self._h/4), self._constMOB["SIZE_TEXT"])
        g2d.draw_text_centered("EXIT", (3*self._w/4, 3*self._h/4), self._constMOB["SIZE_TEXT"])

    #Draws the copyright line in the menu
    def drawCopyright(self):
        g2d.draw_line((0, self._h-20), (self._w, self._h-20))
        g2d.draw_text_centered("   @Copyright by  :  " + self._constMOB["MATRICOLE"], (self._w/2, self._h-(20/2)), 17)

    #Colors the buttons when your mouse passes over them
    def drawColorMenu(self, pos, bestScore):
        if (0 <= pos[0] < self._w/2) and (0 <= pos[1] < self._h/2): 
            self.drawRect((130, 124, 206), (0,0,self._w/2, self._h/2))
            self.drawText((255,255,255), "1 PLAYER", (self._w/4, self._h/4), self._constMOB["SIZE_TEXT"])
            self.drawText((255,255,255), "Best Score: "  + str(bestScore), (self._w/4, self._h/4 + (self._constMOB["SIZE_TEXT"])), self._constMOB["SIZE_TEXT"]/2)
            if g2d.key_pressed("LeftButton"): self.setChoice(False, False, True, 1)

        elif (self._w/2 <= pos[0] < self._w) and (0 <= pos[1] < self._h/2):
            self.drawRect((255,0,0), (self._w/2, 0, self._w/2, self._h/2))
            self.drawText((255,255,255), "2 PLAYER", (3*self._w/4, self._h/4), self._constMOB["SIZE_TEXT"])
            if g2d.key_pressed("LeftButton"): self.setChoice(False, False, True, 2)

        elif (0 <= pos[0] < self._w/2) and (self._h/2 <= pos[1] < self._h-20):
            self.drawText((0,255,0), "RULES", (self._w/4, 3*self._h/4), self._constMOB["SIZE_TEXT"])
            if g2d.key_pressed("LeftButton"): self.setChoice(False, True, False, 0)

        elif (self._w/2 <= pos[0] < self._w) and (self._h/2 <= pos[1] < self._h-20):
            self.drawText((255,0,0), "EXIT", (3*self._w/4, 3*self._h/4), self._constMOB["SIZE_TEXT"])
            if g2d.key_pressed("LeftButton"): self.closeCanvas(bestScore)


    def drawRect(self, rgb, pos):
        g2d.set_color(rgb)
        g2d.fill_rect(pos)

    def drawText(self, rgb, text, pos, size):
        g2d.set_color(rgb)
        g2d.draw_text_centered(text, pos, size)

    #Draws the rules screen
    def drawRules(self):
        g2d.clear_canvas()
        g2d.set_color((0,200,0))
        g2d.draw_text_centered("RULES:", (self._w/4, self._h/8), self._constMOB["SIZE_TEXT"])
        g2d.draw_text_centered("COMMANDS:", (3*self._w/4, self._h/8), self._constMOB["SIZE_TEXT"])
        g2d.set_color((123,123,123))
        g2d.draw_line((self._w/2, 0), (self._w/2, 3*self._h/4 + self._h/8 - self._constMOB["SIZE_TEXT"]))
        g2d.draw_text("Player 1:", (self._w/2 + self._constMOB["SIZE_TEXT2"], self._h/3), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("[Arrows] to move and [Space] to shoot", (self._w/2 + self._constMOB["SIZE_TEXT2"], self._h/3 + 30), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("Player 2:", (self._w/2 + self._constMOB["SIZE_TEXT2"], self._h/3 + 60), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("[WASD] to move and [e] to shoot", (self._w/2 + self._constMOB["SIZE_TEXT2"], self._h/3 + 90), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("1] Dodge all props on land", (self._constMOB["SIZE_TEXT2"], self._h/3), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("2] Shoot to destroy props", (self._constMOB["SIZE_TEXT2"], self._h/3 + 30), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("3] Gain points killing aliens", (self._constMOB["SIZE_TEXT2"], self._h/3 + 60), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("4] There are 3 level", (self._constMOB["SIZE_TEXT2"], self._h/3 + 90), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text("5] ! Play and have fun !", (self._constMOB["SIZE_TEXT2"], self._h/3 + 120), self._constMOB["SIZE_TEXT2"])
        g2d.draw_text_centered("PRESS [ENTER] TO BACK", (self._w/2, 3*self._h/4 + self._h/8), 2*self._constMOB["SIZE_TEXT"]/3)
        self.drawCopyright()
        if g2d.key_pressed("Enter"): self.setChoice(True, False, False, 0)

    #Sets the choise based on what the player clicks
    def setChoice(self, menu, rules, game, numPlayer):
        self._menu      = menu
        self._rules     = rules
        self._game      = game
        self._numPlayer = numPlayer

    def closeCanvas(self, bestScore):
        File.writeBestScore(File, str(bestScore))
        g2d.close_canvas()

    #Stops the game
    def stopGame(self):             self._game = False

    def getMenu(self)  -> bool:     return self._menu
    def getRules(self) -> bool:     return self._rules
    def getGame(self)  -> bool:     return self._game
    def getPlayer(self)-> bool:     return self._numPlayer
    