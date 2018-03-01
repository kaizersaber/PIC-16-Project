# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Ryan, Tan
"""
from PyQt5 import QtCore
import random

class Building(object):
    def __init__(self, start_x=1000, start_y=5, buildingWidth=200):
        self.scaleFactor = 10.0
        self.start_x = start_x
        self.x = start_x
        self.y = start_y
        self.v_x = -15.0
        self.v_y = 0.0
        self.buildingWidth = buildingWidth
        self.gapHeightList = [50, 200, 350]
        self.gapHeight = random.choice(self.gapHeightList)
    
    def update(self):
        self.x += self.v_x/self.scaleFactor
        if self.x < -200:
            self.x = 1000
            self.gapHeight = random.choice(self.gapHeightList)
    
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
        elif mode == "Medium":
            self.scaleFactor = 7.5
        elif mode == "Hard":
            self.scaleFactor = 5.0
        elif mode == "Insane":
            self.scaleFactor = 2.5
    
    def paintBuilding(self, painter):
        gapSize = 150
        self.upper_x = self.x
        self.upper_y = self.y
        self.upper_w = self.buildingWidth
        self.upper_h = self.gapHeight
        self.upper = painter.fillRect(self.upper_x, 
                                      self.upper_y, 
                                      self.upper_w,
                                      self.upper_h, 
                                      QtCore.Qt.darkRed)
        self.middle_x = self.x
        self.middle_y = self.y+self.gapHeight
        self.middle_w = self.buildingWidth
        self.middle_h = gapSize
        self.middle = painter.fillRect(self.middle_x,
                                       self.middle_y,
                                       self.middle_w,
                                       self.middle_h,
                                       QtCore.Qt.lightGray)
        
        self.lower_x = self.x
        self.lower_y = self.y+self.gapHeight+gapSize
        self.lower_w = self.buildingWidth
        self.lower_h = 706-(self.y+self.gapHeight+gapSize)
        self.lower = painter.fillRect(self.lower_x, 
                                      self.lower_y, 
                                      self.lower_w, 
                                      self.lower_h, 
                                      QtCore.Qt.darkRed)    
    def resetPos(self):
        self.x = self.start_x
