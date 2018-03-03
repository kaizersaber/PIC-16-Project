#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:50:17 2018

@author: ryangrgurich
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Bruin(object):
    def __init__(self, frame):
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 5
        self.reset()
    
    def w(self):
        return self.frame.geometry().width()
    
    def h(self):
        return self.frame.geometry().height()

    def lb(self):
        return self.ub + self.h() - 2*5
    
    def reset(self):
        self.x, self.y = self.w()/4, self.h()/2 + self.ub
        self.vx, self.vy = 0,0
        self.ay = 9.81
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
            self.scaleFactor = 5.0
        
    def jump(self):
        self.vy = -40 - (10 - self.scaleFactor)
    
    def update(self, buildings):
        if (self.y > self.lb()) | (self.y < self.ub):
            self.dead = True

        for b in buildings:
            c1 = (b.x <= self.x) & (self.x <= b.x + b.width)
            c2 = (b.lower_y <= self.y) | (self.y <= b.upper_y + b.upper_h)
            if (c1 and c2):
                self.dead = True
        
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    def paintBruin(self,painter):
        painter.fillRect(self.x - 5, self.y - 5, 11, 11, QtCore.Qt.blue)
