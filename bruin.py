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
            self.scaleFactor = 7.5
        elif mode == "Hard":
            self.scaleFactor = 5.0
        elif mode == "insane":
            self.scaleFactor = 2.5
        
    def jump(self):
        self.vy = 40
    
    def update(self):
        if self.y < 100:
            self.y = 0
            if self.vy < 0:
                self.vy = 0
            self.dead = True
        if self.y > 706:
            self.dead = True
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    def paintBruin(self,painter):
        painter.fillRect(self.x + 1, 706 - self.y, 20, 20, QtCore.Qt.blue)