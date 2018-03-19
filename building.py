# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Tan, Ryan
"""

from PyQt5 import QtGui
import random


class Building(object):
    '''This class draws and animates the buildings used in the Flappy Bruin
    game. It also holds the function that set's the game difficulty, setDiff(),
    incresing the number of builing floors, through the changing the numBlocks
    varible.
    Attributes:
        Set by __init__()
        count: Global class variable that represents the number of building 
            objects called. Import to insure ratio of gaps between buildings is
            able to be resized (see self.interval in resize()).
        index: The building objects index value within a set of building objects
        gapIndex: Where the gap to pass through a building will be placed
        numBlocks: number of floors a building has changes with game difficulty
        scaleFactor: used to scale physics of game play depending on difficulty
        frame: the current qt frame
        upper_half: Represent the starting block of the upper_half of the
            building, with the gap as the divider.
        y: y cordinate of the building
        img_window: Any but the first floor, this is a block the player can 
            pass through.
        img_lobby: The first floor image that can be passed through by the 
            player.
        img_block: Any but the first floor, represents the outside of building
            this is a block the player cannot pass through.
        img_door: represents the outer lower floor that the player cannot pass
            through.
            
        Set by randomizeGap()
        collision_ub: the y cordinate to inform the upper half of the collision
            zone which is detected in the bruin class.
        collision_lb: the y cordinate to inform the lower half of the collision
            zone which is detected in the burin class.
        
        Set by resize()
        blockSize: size of building block to painted relative to frame
        upper_y: stores cordinates of y indexes for each block to be drawn from.
        width: width of each block created in ratio to frame and number of 
            buildings
        interval: gap between buidlings
        start_x: intitial x cordinate of the building.
        vx: velocity at which the building moves.
    '''
    count = 0
    def __init__(self, frame):
        self.index = Building.count
        Building.count = Building.count + 1
        self.gapIndex = 0
        self.numBlocks = 3
        self.scaleFactor = 6.0
        self.frame = frame
        self.upper_half = 4
        self.reset()
        self.y = 4
        self.img_window = QtGui.QImage("inner1.png")
        self.img_lobby = QtGui.QImage("inner0.png")
        self.img_block = QtGui.QImage("upper0.png")
        self.img_door = QtGui.QImage("lower0.png")
        
    def frame_width(self):
        """Gets the width of the frame"""
        return self.frame.geometry().width()
    
    def frame_height(self):
        """Gets the height fo the frame"""
        return self.frame.geometry().height()

    def randomizeGap(self):
        """Generates a random value for gapIndex that is matched to a
        building section that the player can pass through. This also set values
        for self.collision_ub and self.collision_lb used in the bruin class to
        detect when the player collides with the buidling.
        """
        self.gapIndex = random.randint(1,self.numBlocks)
        self.collision_ub = self.upper_y[self.gapIndex]
        self.collision_lb = self.upper_y[self.gapIndex-1]
    
    def update(self):
        """Used to redraw the building when the window size is changed"""
        self.x += self.vx/self.scaleFactor
        if self.x < -self.width:
            self.x = self.frame_width()
            self.randomizeGap()
    
    def setDiff(self, mode):
        """Sets the game diffaculty by changing the number of building sections"""
        if mode == "Easy":
            self.scaleFactor = 6.0
            self.numBlocks = 3
        elif mode == "Medium":
            self.scaleFactor = 6.0
            self.numBlocks = 4
        elif mode == "Hard":
            self.scaleFactor = 6.0
            self.numBlocks = 5
    
    def paintBuilding(self, painter):
        """paints building in pieces using paintBlock()"""
        for floor in range(1,self.numBlocks+1):
            self.paintBlock(painter,floor)
    
    def paintBlock(self, painter, floor):
        """Paints a floor of the builiding"""
        img = None
        adj = 1
        #conditional used to deremine whether a pass throgh component is drawn
        #or an image representing the outside of the building is drawn
        if floor == 1:
            if floor == self.gapIndex: 
                adj = 1.01
                img = self.img_lobby
            else:
                adj = 1.01
                img = self.img_door
        else:
            if floor == self.gapIndex:
                img = self.img_window
            else:
                adj = 1.01
                img = self.img_block
        painter.drawImage(self.x, self.upper_y[floor], img.scaled(self.width,self.blockSize*adj),
                          sx = 0, sy = 0, sw = 0, sh = 0)
    
    def resize(self):
        """Redraws building cordinates for painter"""
        self.blockSize = (self.frame_height()-8)/self.numBlocks
        self.upper_y = [self.upper_half + self.blockSize*i for i in range(self.numBlocks,-1,-1)]
        self.width = self.frame_width()/(2*(Building.count+1))
        self.interval = (self.frame_width() + self.width)/Building.count
        self.start_x = self.frame_width() + self.index*self.interval
        self.vx = -self.frame_width()/100
        
    def reset(self):
        """resets building attributes"""
        self.resize()
        self.x = self.start_x
        self.randomizeGap()