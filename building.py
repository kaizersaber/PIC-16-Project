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
        self.gapIndex = 0
        self.numBlocks = 3
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 4
        self.reset()
        self.y = 4
        self.img_window = QtGui.QImage("inner1.png")
        self.img_lobby = QtGui.QImage("inner0.png")
        self.img_block = QtGui.QImage("upper0.png")
        self.img_door = QtGui.QImage("lower0.png")
        
    def w(self):
        return self.frame.geometry().width()
    
    def h(self):
        return self.frame.geometry().height()

    def lb(self):
        return self.ub + self.h() - 2*4

    def randomizeGap(self):
        adj = 0
        if self.gapIndex == 1 & self.numBlocks == 5:
            adj = -1
        self.gapIndex = random.randint(1,self.numBlocks+adj)
        self.collision_ub = self.upper_y[self.gapIndex]
        self.collision_lb = self.upper_y[self.gapIndex-1]
    
    def update(self):
        self.x += self.vx/self.scaleFactor
        if self.x < -self.width:
            self.x = self.w()
            self.randomizeGap()
    
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 6.0
            self.numBlocks = 3
        elif mode == "Medium":
            self.scaleFactor = 6.0
            self.numBlocks = 4
        elif mode == "Hard":
            self.scaleFactor = 6.0
            self.numBlocks = 5
    
    def paintBuilding(self, painter):
        for i in range(1,self.numBlocks+1):
            self.paintBlock(painter,i)
    
    def paintBlock(self, painter, i):
        img = None
        adj = 1
        if i == 1:
            if i == self.gapIndex: 
                adj = 1.01
                img = self.img_lobby
            else:
                adj = 1.01
                img = self.img_door
        else:
            if i == self.gapIndex:
                img = self.img_window
            else:
                adj = 1.01
                img = self.img_block
        painter.drawImage(self.x, self.upper_y[i], img.scaled(self.width,self.blockSize*adj),
                          sx = 0, sy = 0, sw = 0, sh = 0)
    
    def resize(self):
        self.blockSize = (self.h()-8)/self.numBlocks
        self.upper_y = [self.ub + self.blockSize*i for i in range(self.numBlocks,-1,-1)]
        self.width = self.w()/(2*(Building.count+1))
        self.interval = (self.w() + self.width)/Building.count
        self.start_x = self.w() + self.index*self.interval
        self.vx = -self.w()/100
        
    def reset(self):
        self.resize()
        self.x = self.start_x
        self.randomizeGap()