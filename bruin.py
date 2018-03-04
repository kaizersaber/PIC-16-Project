# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

class Bruin(object):
    jumpsound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("jump.mp3"))
    jumpPlayer = QtMultimedia.QMediaPlayer()
    jumpPlayer.setMedia(jumpsound)
    jumpPlayer.setVolume(100)
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
        self.ay = 0.015*self.h()
        self.dead = False
        self.inBuilding = False
        self.score = 0
    
    def buildingCheck(self, bool):
        if self.inBuilding:
            if not bool:
                self.score += 1
        self.inBuilding = bool
    
    def setPos(self,x,y):
        self.x, self.y = x,y
        
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
        elif mode == "Medium":
            self.scaleFactor = 8.0
        elif mode == "Hard":
            self.scaleFactor = 7.0
        
    def jump(self):
        Bruin.jumpPlayer.stop()
        Bruin.jumpPlayer.play()
        self.vy = -(self.h()-2*5)/16 - (10 - self.scaleFactor)
    
    def update(self, buildings):
        if (self.y > self.lb()) | (self.y < self.ub):
            self.dead = True
        
        buildingChecks = []
        for b in buildings:
            if (b.x <= self.x) & (self.x <= b.x + b.width):
                if (b.lower_y <= self.y) | (self.y <= b.upper_y + b.upper_h):
                    self.dead = True
                else:
                    buildingChecks.append(True)
            else:
                buildingChecks.append(False)
                
        if any(buildingChecks):
            self.buildingCheck(True)
        else:
            self.buildingCheck(False)
        
        self.vy += self.ay / self.scaleFactor
        self.x += self.vx / self.scaleFactor
        self.y += self.vy / self.scaleFactor
    
    def paintBruin(self,painter):
        painter.fillRect(self.x - 5, self.y - 5, 11, 11, QtCore.Qt.blue)