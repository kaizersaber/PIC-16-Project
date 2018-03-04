# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018
@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets

# Bruin class creates and updates the score, position, and life of the bruin player
class Bruin(object):
    def __init__(self, frame):
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 5 # upperbound
        self.reset()
    
    # width of the frame
    def w(self):
        return self.frame.geometry().width()
    
    # height of the frame
    def h(self):
        return self.frame.geometry().height()

    # lowerbound
    def lb(self):
        return self.ub + self.h() - 2*5
    
    # updates position of the square as well as survival status
    def reset(self):
        self.x, self.y = self.w()/4, self.h()/2 + self.ub
        self.vx, self.vy = 0,0
        self.ay = 0.015*self.h()
        self.dead = False
        self.inBuilding = False
        self.score = 0
    
    # runs list of bools; contains a True for clean passage through building
    def buildingCheck(self, bool):
        if self.inBuilding:
            print "In Building: ", self.inBuilding, "bool: ", bool
            if not bool:
                self.score += 1
        self.inBuilding = bool
    
    # SetsPosition of Bruin
    def setPos(self,x,y):
        self.x, self.y = x,y
    
    # Sets new Scalar Factor depending on difficulty level (lower value is harder level)
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
        elif mode == "Medium":
            self.scaleFactor = 8.0
        elif mode == "Hard":
            self.scaleFactor = 7.0
    
    # adjust Bruin Velocity based on frame height and scal
    def jump(self):
        self.vy = -(self.h()-2*5)/16 - (10 - self.scaleFactor)
    
    # Updates to check if bruin has hit building or frame edge
    def update(self, buildings):
        # checks edge of frame
        if (self.y > self.lb()) | (self.y < self.ub):
            self.dead = True
        checklist = []
        # checks for edge of buildings
        for b in buildings:
            if (b.x <= self.x) & (self.x <= b.x + b.width):
                if (b.lower_y <= self.y) | (self.y <= b.upper_y + b.upper_h):
                    self.dead = True # if hit edge; bruin dead and game over
                else: # exiting safe area
                    checklist.append(True)
        # Once bruin exits clear door area, if not dead then update score via buildingCheck
        if not self.dead:
            if any(checklist):
                self.buildingCheck(True) # for 
            else:
                self.buildingCheck(False)
        
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    # fill square unit with Bruin Blue
    def paintBruin(self,painter):
        painter.fillRect(self.x - 5, self.y - 5, 11, 11, QtCore.Qt.blue)
