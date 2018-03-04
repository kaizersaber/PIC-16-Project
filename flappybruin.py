# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newflappy.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from bruin import Bruin
from building import Building

class FlappyBruinGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(FlappyBruinGame, self).__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        self.active = False
        self.focus = True
        self.highscore, self.score = 0,0
        self.setupUi()
        self.player = None
        self.buildings = None
        self.setupAudio()
    
    def setupAudio(self):
        pass
    
    def setupUi(self):
        # Layouts
        self.setObjectName("MainWindow")
        self.resize(1000, 715)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        # Background Frame
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Top Frame
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # High Score Text
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setText("High Score:")
        self.label_6.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        
        # High Score Value
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setText("0")
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        # Current Score Text
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setText("Current Score:")
        self.label_3.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        
        # Current Score Value
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setText("0")
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_2)
        
        # Center Frame
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QWidget#frame {border:5px solid rgb(0, 0, 0)}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame.paintEvent = self.framePaint
        self.frame.mousePressEvent = self.framePress

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        
        # Center Text
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("FlappyBruin")
        self.label.setStyleSheet("font: 56pt \"Britannic Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        
        # Start Game Button
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setText("Start Game")
        self.toolButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n" "font: 75 16pt \"Calisto MT\";")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.gameStart)
        self.verticalLayout_2.addWidget(self.toolButton_2, 0, QtCore.Qt.AlignHCenter)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        
        self.verticalLayout.addWidget(self.frame)
        
        # Bottom Frame
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # Mute Button
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setText("Press W to Jump")
        self.label_7.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        
        # Quit Game Button
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_4)
        self.toolButton_3.setText("Quit Game")
        self.toolButton_3.setStyleSheet("background-color: rgb(170, 255, 255);\n" "font: 75 16pt \"Calisto MT\";")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.quitgame)
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        
        # Difficulty Text
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setText("Difficulty:")
        self.label_5.setStyleSheet("font: 87 16pt \"Calisto MT\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        
        # Difficulty Menu
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n" "font: 16pt \"Calisto MT\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Easy")
        self.comboBox.addItem("Medium")
        self.comboBox.addItem("Hard")
        self.comboBox.currentIndexChanged.connect(self.setMode)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.widget_4)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)
        
    def setMode(self):
        mode = self.comboBox.currentText()
        self.focus = True
        self.player.setDiff(mode)
        for b in self.buildings:
            b.setDiff(mode)
    
    def displayRules(self):
        self.label.setText("Press W to jump")

    def gameStart(self):
        self.label.hide()
        self.toolButton_2.hide()
        for b in self.buildings:
            b.resetPos()
        self.player.reset()
        self.score = 0
        self.label_2.setText(str(self.score))
        self.active = True
        self.timer.start(10)
    
    def gameEnd(self):
        self.timer.stop()
        self.label.setText("Game Over")
        self.label.show()
        self.toolButton_2.show()
        self.toolButton_2.setText("Restart")
        self.active = False

    def framePress(self,event):
        print event.x(), event.y()
    
    def keyPressEvent(self, event):
        if self.active:
            if event.key() == QtCore.Qt.Key_W:
                self.player.jump()
            
    def framePaint(self, event):
        if self.buildings == None:
            self.buildings = [Building(self.frame) for x in range(3)]
        if self.player == None:
            self.player = Bruin(self.frame)
        painter = QtGui.QPainter(self.frame)
        if self.focus:
            self.setFocus()
        else:
            self.focus = True
        if self.active:
            for b in self.buildings:
                b.paintBuilding(painter)
            self.player.paintBruin(painter)
            
    
    def eventFilter(self,source,event):
        if event.type() == QtCore.QEvent.HoverMove:
            if self.comboBox.underMouse():
                self.comboBox.setFocus()
                self.focus = False
            else:
                self.focus = True
    
    def updateScore(self):
        self.score = self.player.score
        self.label_2.setText(str(self.score))
        if self.score > self.highscore:
            self.highscore = self.score
            self.label_4.setText(str(self.highscore))

    def quitgame(self):
        self.timer.stop()
        self.close()
    
    def animate(self):
        self.player.update(self.buildings)
        self.frame.update()
        for b in self.buildings:
            b.update()
        if self.player.dead:
            self.gameEnd()
        else:
            self.updateScore()

def main():
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    ui = FlappyBruinGame()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()