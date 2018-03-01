# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Building(object):
    count = 0
    def __init__(self, frame, n):
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 5
        self.width = 200
        self.interval = (self.w()+self.width)/n
        print self.w(), self.width
        self.start_x = self.w() + Building.count*self.interval
        self.x = self.start_x
        self.y = 5
        self.vx = -15.0
        self.gapSize = (self.h()-10)/3
        self.randomizeGap()
        Building.count = Building.count + 1
    
    def w(self):
        return self.frame.geometry().width()
    
    def h(self):
        return self.frame.geometry().height()

    def lb(self):
        return self.ub + self.h() - 2*5

    def randomizeGap(self):
        self.gapHeight = random.randint(5, self.h() - 5 - self.gapSize)
    
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
        elif mode == "Insane":
            self.scaleFactor = 4.0
    
    def paintBuilding(self, painter):
        self.upper_x = self.x
        self.upper_y = self.y
        self.upper_w = 50
        self.upper_h = self.gapHeight
        self.upper = painter.fillRect(self.upper_x, self.upper_y, self.width, 
                                      self.upper_h, QtCore.Qt.red)
        self.lower_x = self.x
        self.lower_y = self.y+self.gapHeight+self.gapSize
        self.lower_h = self.lb() - self.lower_y
        if self.lower_y < self.h() - 5:
            self.lower = painter.fillRect(self.lower_x, self.lower_y, self.width, 
                                          self.lower_h, QtCore.Qt.red)
        
    def resetPos(self):
        self.x = self.start_x
        self.randomizeGap()