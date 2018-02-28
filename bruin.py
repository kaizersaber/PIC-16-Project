# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Bruin(object):
    def __init__(self):
        self.scaleFactor = 10.0
        self.reset()
    
    def reset(self):
        self.x, self.y = 150, 400
        self.vx, self.vy = 0,0
        self.ay = -9.81
        self.dead = False
    
    def setPos(self,x,y):
        self.x, self.y = x,y
        
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
        elif mode == "Medium":
            self.scaleFactor = 8.0
        elif mode == "Hard":
            self.scaleFactor = 6.0
        elif mode == "Insane":
            self.scaleFactor = 4.0
        
    def jump(self):
        self.vy = 40
    
    def update(self, buildings):
        if self.y < 100:
            self.y = 0
            if self.vy < 0:
                self.vy = 0
            self.dead = True
        if self.y > 706:
            self.dead = True

        for b in buildings:
            c1 = self.x < b.upper_w+b.upper_x
            c2 = self.x > b.upper_x
            c3 = (706-self.y) >= b.upper_y
            c4 = (706-self.y) <= (b.upper_y+b.upper_h)
            c5 = (706-self.y) >= b.lower_y
            if (c1 and c2 and ((c3 and c4) or c5)):
                self.dead = True
        
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    def paintBruin(self,painter):
        painter.fillRect(self.x + 1, 706 - self.y, 20, 20, QtCore.Qt.blue)