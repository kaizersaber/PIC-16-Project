# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:38:38 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Building(object):
    def __init__(self, start_x=990, start_y=200):
        self.start_x = start_x
        self.x = start_x
        self.y = start_y
        self.v_x = -2.0
        self.v_y = 0.0
    
    def update(self):
        self.x += self.v_x
        if self.x < -200:
            self.x = self.start_x
    
    def paintBuilding(self, painter):
        #gapHeight = randint()
        painter.fillRect(self.x, self.y, 200, 506, QtCore.Qt.red)