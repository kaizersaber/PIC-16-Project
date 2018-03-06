# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:18 2018

@author: Tan
"""
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import pygame

# Bruin class creates and updates the score, position of Bruin Player
class Bruin(object):
    def __init__(self, frame):
        self.scaleFactor = 10.0
        self.scoreFactor = 1
        self.frame = frame
        self.ub = 5
        self.reset()
        self.jumpSound = pygame.mixer.Sound('jump.ogg')
        self.graphic = QtGui.QImage("Joe_Bruin.png")
    
    # w gets the current width of the frame
    def w(self):
        return self.frame.geometry().width()
    
    # h gets the current height of the frame
    def h(self):
        return self.frame.geometry().height()
    
    # lb updates the current lower bound for the player
    def lb(self):
        return self.ub + self.h() - 2*5
    
    # reset resets the player's position, speed, size and status
    def reset(self):
        self.x, self.y = self.w()/4, self.h()/2 + self.ub
        self.vx, self.vy = 0,0
        self.ay = 0.015*self.h()
        self.size = self.h()/20 - 1
        self.dead = False
        self.inBuilding = False
        self.score = 0
    
    # buildingCheck updates score when a player exits a building safely
    def buildingCheck(self, bool):
        if self.inBuilding:
            if not bool:
                self.score += 1*self.scoreFactor
        self.inBuilding = bool
    
    # setDiff sets the difficulty factors based on mode
    def setDiff(self, mode):
        if mode == "Easy":
            self.scaleFactor = 10.0
            self.scoreFactor = 1
        elif mode == "Medium":
            self.scaleFactor = 9.0
            self.scoreFactor = 2
        elif mode == "Hard":
            self.scaleFactor = 8.0
            self.scoreFactor = 3
    
    # jump increases upward velocity of player and plays sound
    def jump(self):
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(0).play(self.jumpSound)
        self.vy = -(self.h()-2*5)/20 - (10 - self.scaleFactor)
    
    # update updates the current position and checks for collisions
    def update(self, buildings):
        if (self.y + self.size/2 > self.lb()) | (self.y - self.size/2 < self.ub):
            self.dead = True
        
        buildingChecks = []
        for b in buildings:
            if (b.x <= self.x + self.size/2 - 2) & (self.x - self.size/2 + 2 <= b.x + b.width):
                if (b.collision_ub >= self.y - self.size/2 - 5) | (self.y + self.size/2 - 1 >= b.collision_lb):
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
    
    # paintBruin defines how to paint the player
    def paintBruin(self,painter):
        painter.drawImage(self.x - self.size/2, self.y - self.size/2, 
                          self.graphic.scaled(self.size,self.size))