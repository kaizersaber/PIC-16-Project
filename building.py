# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Building(object):
    def __init__(self, start_x=1000, start_y=5):
        self.scaleFactor = 10.0
        self.start_x = start_x
        self.x = start_x
        self.y = start_y
        self.v_x = -15.0
        self.v_y = 0.0
        self.gapHeightList = [50*i for i in range(10)]
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
        gapSize = 200
        self.upper_x = self.x
        self.upper_y = self.y
        self.upper_w = 50
        self.upper_h = self.gapHeight
        self.upper = painter.fillRect(self.upper_x, 
                                      self.upper_y, 
                                      self.upper_w,
                                      self.upper_h, 
                                      QtCore.Qt.red)
        self.lower_x = self.x
        self.lower_y = self.y+self.gapHeight+gapSize
        self.lower_w = 50
        self.lower_h = 706-(self.y+self.gapHeight+gapSize)
        self.lower = painter.fillRect(self.lower_x, 
                                      self.lower_y, 
                                      self.lower_w, 
                                      self.lower_h, 
                                      QtCore.Qt.red)
        
    def resetPos(self):
        self.x = self.start_x