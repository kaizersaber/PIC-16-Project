# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018

@author: Tan
"""

class Bruin(object):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.x, self.y = 150, 400
        self.vx, self.vy = 0,0
        self.ay = -9.81
        self.dead = False
        self.scaleFactor = 7.5
    
    def setPos(self,x,y):
        self.x, self.y = x,y
        
    def jump(self):
        self.vy = 50
    
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