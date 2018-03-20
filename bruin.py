# Import necessary Files
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import pygame

# Bruin class creates and updates the score, position of Bruin Player
class Bruin(object):
    '''
        This class draws and animates the character Joe the Bruin.

        Dependancies:
            Joe_Bruin.png:  paints the character you play
            jump.oog:       sound associated with a jump / pressing 'W'

        Attributes:
            Set by __init___():
                scaleFactor:    Scale physics of game play depending on difficulty
                scoreFactor:    Store the player's score
                frame:          Screen Frame
                ub:             Upper Boundary for the playing screen
                jumpSound:      Plays the jumping sound
                graphic:        Reads in image of character to later bind to the player
            
            Set by reset():
                x:              Resets x position at 1/4 the width length
                y:              Resets y position at 1/2 the height length
                vx:             Resets horizantal velocity
                vy:             Resets verticle velocity
                ay:             Applies acceleration at the rate of 0.015 unites of the frame's height
                size:           Sets the size of the character at about 1/20th of the height of the frame
                dead:           Resets boolean death status to False
                inBuilding:     Resets boolean touching the building status to False
                score:          Resets score to 0

        Functions:
            __init__():         Initializer
            w():                Returns frame width
            h():                Returns frame height
            lb():               Returns lower bound of playing screen
            reset():            Resets the game to a new game. Keeps High Score
            buildingCheck():    Checks whether or not player is in a building column and then checks whether or not it has hit the building
                                    if it has not hit the building, then it adds a scoreFactor to the score once it exits the building
            setDiff():          Sets scaleFactor and scoreFactor depending on the difficulty setting
            jump():             Implements the jump sound as it adjusts the verticle velocity to simulate a jump
            update():           Updates the current position, velocity, and checks for collisions. If collision occured, changes dead to True.
            paintBruin():       Binds the image of Joe the bruin to the character positon
    '''
    def __init__(self, frame):
        self.scaleFactor = 10.0
        self.scoreFactor = 1
        self.frame = frame
        self.ub = 5
        self.reset()
        self.jumpSound = pygame.mixer.Sound('jump.ogg')
        self.graphic = QtGui.QImage("Joe_Bruin.png")
    
    # w gets the current width of the frame
    def w(self):
        return self.frame.geometry().width()
    
    # h gets the current height of the frame
    def h(self):
        return self.frame.geometry().height()
    
    # lb updates the current lower bound for the player
    def lb(self):
        return self.ub + self.h() - 2*5
    
    # reset resets the player's position, speed, size and status
    def reset(self):
        self.x, self.y = self.w()/4, self.h()/2 + self.ub
        self.vx, self.vy = 0,0
        self.ay = 0.015*self.h()
        self.size = self.h()/20 - 1
        self.dead = False
        self.inBuilding = False
        self.score = 0
    
    # buildingCheck updates score when a player exits a building safely
    def buildingCheck(self, bool):
        if self.inBuilding:
            if not bool:
                self.score += 1*self.scoreFactor
        self.inBuilding = bool
    
    # setDiff sets the difficulty factors based on mode
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
            self.scoreFactor = 1
        elif mode == "Medium":
            self.scaleFactor = 9.0
            self.scoreFactor = 2
        elif mode == "Hard":
            self.scaleFactor = 8.0
            self.scoreFactor = 3
    
    # jump increases upward velocity of player and plays sound
    def jump(self):
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(0).play(self.jumpSound)
        self.vy = -(self.h()-2*5)/20 - (10 - self.scaleFactor)
    
    # update updates the current position and checks for collisions
    def update(self, buildings):
        if (self.y + self.size/2 > self.lb()) | (self.y - self.size/2 < self.ub):
            self.dead = True
        
        buildingChecks = []
        for b in buildings:
            if (b.x <= self.x + self.size/2 - 2) & (self.x - self.size/2 + 2 <= b.x + b.width):
                if (b.collision_ub >= self.y - self.size/2 - 5) | (self.y + self.size/2 - 1 >= b.collision_lb):
                    self.dead = True
                else:
                    buildingChecks.append(True)
            else:
                buildingChecks.append(False)
                
        if any(buildingChecks):
            self.buildingCheck(True)
        else:
            self.buildingCheck(False)
        
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    # paintBruin defines how to paint the player
    def paintBruin(self,painter):
        painter.drawImage(self.x - self.size/2, self.y - self.size/2, 
                          self.graphic.scaled(self.size,self.size))
