# Imports necessary files
from PyQt5 import QtGui
import random

class Building(object):
    """
    This class draws and animates the buildings used in the Flappy Bruin
    game. It also holds the function that set's the game difficulty, setDiff(),
    increasing the number of builing floors, through the changing the numBlocks
    variable.
    
    Dependencies:
        upper0.png: Wall image used in __init__()
        inner0.png: Lobby image used in __init__()
        inner1.png: Window image used in __init__()
        lower0.png: Door image used in __init__()
    
    Attributes:
    Set by __init__():
        count: Global class variable that represents the number of building 
                objects called. Import to insure ratio of gaps between buildings is
                able to be resized (see self.interval in resize()).
        index: The building objects index value within a set of building objects
        gapIndex: Where the gap to pass through a building will be placed
        numBlocks: Number of floors a building has changes with game difficulty
        scaleFactor: Scale physics of game play depending on difficulty
        frame: The current QFrame
        upper_half: Represent the starting block of the upper_half of the
                    building, with the gap as the divider.
        y: y cordinate of the building
        img_window: Any but the first floor, this is a block the player can 
                    pass through.
        img_lobby: The first floor image that can be passed through by the 
                    player.
        img_block: Any but the first floor, represents the outside of building
                    this is a block the player cannot pass through.
        img_door: represents the outer lower floor that the player cannot pass through.
                
    Set by randomizeGap():
        collision_ub: the y cordinate to inform the upper half of the collision
                        zone which is detected in the bruin class.
        collision_lb: the y cordinate to inform the lower half of the collision
                        zone which is detected in the bruin class.
            
    Set by resize():
        blockSize: size of building block to painted relative to frame
        upper_y: stores cordinates of y indexes for each block to be drawn from.
        width: width of each block created in ratio to frame and number of 
                buildings
        interval: gap between buidlings
        start_x: intitial x cordinate of the building.
        vx: velocity at which the building moves.
    
    Functions:
        __init__(): Initializer
        frame_width(): Gets frame width
        frame_height(): Gets frame height
        randomizeGap(): Shuffles gapIndex of building
        update(): Updates building position for animation
        setDiff(): Implements difficulty level for building
        paintBuilding(): Calls paintBlock at specified indices
        paintBlock(): Paints a specified floor of building
        resize(): Resizes building based on frame size
        reset(): Calls resize(), resets position and calls randomizeGap()
    """
    count = 0
    # Initializer
    def __init__(self, frame):
        self.index = Building.count
        Building.count = Building.count + 1
        self.gapIndex = 0
        self.numBlocks = 3
        self.scaleFactor = 6.0
        self.frame = frame
        self.ub = 4
        self.reset()
        self.y = 4
        self.img_window = QtGui.QImage("inner1.png")
        self.img_lobby = QtGui.QImage("inner0.png")
        self.img_block = QtGui.QImage("upper0.png")
        self.img_door = QtGui.QImage("lower0.png")
    
    # frame_width() gets the width of the frame
    def frame_width(self):
        return self.frame.geometry().width()
    
    # frame_height() gets the height of the frame
    def frame_height(self):
        return self.frame.geometry().height()

    # randomizeGap() generates a random value for gapIndex
    def randomizeGap(self):
        self.gapIndex = random.randint(1,self.numBlocks)
        # Sets values for bruin class to detect collision bounds of building
        self.collision_ub = self.upper_y[self.gapIndex]
        self.collision_lb = self.upper_y[self.gapIndex-1]
    
    # update() reinitializes the building whenever necessary
    def update(self):
        self.x += self.vx/self.scaleFactor
        if self.x < -self.width:
            self.x = self.frame_width()
            self.randomizeGap()
    
    # setDiff() sets game difficulty
    def setDiff(self, mode):
        # Easy: 3 floors, Medium: 4 floors, Hard: 5 floors
        if mode == "Easy":
            self.numBlocks = 3
        elif mode == "Medium":
            self.numBlocks = 4
        elif mode == "Hard":
            self.numBlocks = 5
            
    # paintBuilding() paints building in pieces using paintBlock
    def paintBuilding(self, painter):
        for i in range(1,self.numBlocks+1):
            self.paintBlock(painter,i)
            
    # paintBlock() paints floor of a building
    def paintBlock(self, painter, floor):
        img = None
        adj = 1
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
    
    # resize() resets building coordinates to paint
    def resize(self):
        self.blockSize = (self.frame_height()-8)/self.numBlocks
        self.upper_y = [self.ub + self.blockSize*i for i in range(self.numBlocks,-1,-1)]
        self.width = self.frame_width()/(2*(Building.count+1))
        self.interval = (self.frame_width() + self.width)/Building.count
        self.start_x = self.frame_width() + self.index*self.interval
        self.vx = -self.frame_width()/100
    
    # reset() calls resize(), resets position and calls randomizeGap()
    def reset(self):
        self.resize()
        self.x = self.start_x
        self.randomizeGap()