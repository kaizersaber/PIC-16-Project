#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:38:34 2018

@author: ryangrgurich
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget
from PyQt5.QtGui import QIcon, QPainter, QImage, QColor, QFont, QPainterPath
from PyQt5.QtCore import QCoreApplication, Qt, QTimer
from PyQt5 import QtCore

import numpy as np
from random import randint

class Building(object):
    count = 0
    def __init__(self, frame, n):
        self.scaleFactor = 10.0
        self.frame = frame
        self.ub = 4
        self.width = self.w()*0.18
        self.interval = (self.w()+self.width)/n
        print self.w(), self.width
        self.start_x = self.w() + Building.count*self.interval
        self.x = self.start_x
        self.y = self.h()*0.005
        self.vx = -15.0
        self.gapSize = (self.h()-10)/3
        self.gapHeights=np.linspace(0,1,4,endpoint=False)*self.h()
        self.randomizeGap()
        self.img_building_upper = (QImage("imgfiles/upper0.png"), 
                                   QImage("imgfiles/upper1.png"), 
                                   QImage("imgfiles/upper2.png"))
        self.img_building_middle = (QImage("imgfiles/inner1.png"), 
                                   QImage("imgfiles/inner1.png"), 
                                   QImage("imgfiles/inner1.png"),
                                   QImage("imgfiles/inner0.png"))
        self.img_building_lower = (QImage("imgfiles/lower1.png"), 
                                   QImage("imgfiles/lower0.png"), 
                                   QImage("imgfiles/lower2.png"))
        Building.count = Building.count + 1
    
    def w(self):
        return self.frame.geometry().width()
    
    def h(self):
        return self.frame.geometry().height()

    def lb(self):
        return self.ub + self.h() - 2*4

    def randomizeGap(self):
        self.gapHeight = randint(0,3)
    
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
        self.upper_h = self.gapHeights[self.gapHeight]
        if self.gapHeight>0:
            self.upper = painter.drawImage(self.upper_x, self.upper_y,
                                   self.img_building_upper[self.gapHeight-1].scaled(self.width,
                                                              self.upper_h+2),
                                   sx=0,sy=0, sw=-1, sh=-1)
        
        self.middle_x = self.x
        self.middle_y = self.gapHeights[self.gapHeight]+self.y
        self.middle_h = self.h()*0.25
        if self.gapHeight<3:
            self.middle = painter.drawImage(self.middle_x, self.middle_y,
                                    self.img_building_middle[self.gapHeight].scaled(self.width,
                                                            self.middle_h),
                                       sx=0,sy=0, sw=-1, sh=-1)
        else:
            self.middle = painter.drawImage(self.middle_x, self.middle_y-6,
                        self.img_building_middle[self.gapHeight].scaled(self.width,
                                                self.middle_h),
                           sx=0,sy=0, sw=-1, sh=-1)
        
        self.lower_x = self.x
        self.lower_y = self.y+self.gapHeights[self.gapHeight]+self.h()*0.25
        self.lower_h = self.lb() - self.lower_y
        if self.lower_y < self.h() - 5:
            self.lower = painter.drawImage(self.lower_x, self.lower_y,
                                   self.img_building_lower[self.gapHeight-1].scaled(self.width,
                                                              self.lower_h),
                                   sx=0,sy=0, sw=-1, sh=-1)
        
        
    def resetPos(self):
        self.x = self.start_x
        self.randomizeGap()
