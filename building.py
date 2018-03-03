# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Building(object):
    count = 0
    def __init__(self, frame):
        self.index = Building.count
        Building.count = Building.count + 1
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 4
        self.resize()
        self.x = self.start_x
        self.y = 4
        self.randomizeGap()
        self.setUML()
        self.img_building = QtGui.QImage("building0.png")
        self.img_window = QtGui.QImage("inner1.png")
        self.img_lobby = QtGui.QImage("inner0.png")
        
    def w(self):
        return self.frame.geometry().width()
    
    def h(self):
        return self.frame.geometry().height()

    def lb(self):
        return self.ub + self.h() - 2*4

    def randomizeGap(self):
        self.gapIndex = random.randint(0,3)
        self.gapHeight = self.gapIndex*(self.h()-10)/4.0
    
    def update(self):
        self.x += self.vx/self.scaleFactor
        if self.x < -self.width:
            self.x = self.w()
            self.randomizeGap()
    
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
        elif mode == "Medium":
            self.scaleFactor = 8.0
        elif mode == "Hard":
            self.scaleFactor = 6.0
    
    def setUML(self):
        self.upper_x = self.x
        self.upper_y = self.y
        self.upper_h = self.gapHeight
        self.middle_x = self.x
        self.middle_y = self.gapHeight + self.y
        self.middle_h = self.gapSize
        self.lower_x = self.x
        self.lower_y = self.y + self.gapHeight + self.gapSize
        self.lower_h = self.lb() - self.lower_y
    
    def paintBuilding(self, painter):
        self.setUML()
        painter.drawImage(self.upper_x, self.upper_y, self.img_building.scaled(self.width,self.lb()-self.ub),
                          sx = 0, sy = 0, sw = -1, sh = -1)
        if self.gapIndex < 3:
            painter.drawImage(self.middle_x, self.middle_y, self.img_window.scaled(self.width,self.middle_h),
                              sx = 0, sy = 0, sw = -1, sh = -1)
        else:
            painter.drawImage(self.middle_x, self.middle_y, self.img_lobby.scaled(self.width,self.middle_h+2),
                              sx = 0, sy = 0, sw = -1, sh = -1)
         
    
    def resize(self):
        self.gapSize = (self.h()-2*5)/4
        self.width = self.w()/(2*(Building.count+1))
        self.interval = (self.w() + self.width)/Building.count
        self.start_x = self.w() + self.index*self.interval
        self.vx = -0.015*self.w()
        
    def resetPos(self):
        self.resize()
        self.x = self.start_x
        self.randomizeGap()