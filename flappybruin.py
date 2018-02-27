# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newflappy.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from bruin import Bruin

class FlappyBruinGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(FlappyBruinGame, self).__init__()
        self.player = Bruin()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        self.active = False
        self.setupUi()
        
    def setupUi(self):
        # Layouts
        self.setObjectName("MainWindow")
        self.resize(1026, 715)
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
        
        # Center Frame
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3.paintEvent = self.framePaint
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        
        # Center Text
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setText("FlappyBruin")
        self.label.setStyleSheet("font: 56pt \"Britannic Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        
        # Start Game Button
        self.toolButton_2 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_2.setText("Start Game")
        self.toolButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 75 16pt \"Calisto MT\";")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.gameStart)
        self.verticalLayout_2.addWidget(self.toolButton_2, 0, QtCore.Qt.AlignHCenter)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_3)
        
        # Bottom Frame
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # Mute Button
        self.checkBox = QtWidgets.QCheckBox(self.widget_4)
        self.checkBox.setText("Mute")
        self.checkBox.setStyleSheet("font: 75 16pt \"Calisto MT\";")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        
        # Quit Game Button
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_4)
        self.toolButton_3.setText("Quit Game")
        self.toolButton_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Calisto MT\";")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.quitgame)
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        
        # Difficulty Text
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setText("Difficulty:")
        self.label_5.setStyleSheet("font: 87 16pt \"Calisto MT\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        
        # Difficulty Menu
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 16pt \"Calisto MT\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Easy")
        self.comboBox.addItem("Medium")
        self.comboBox.addItem("Hard")
        self.comboBox.addItem("Insane")
        self.comboBox.currentIndexChanged.connect(self.setMode)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.widget_4)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)
        
    def setMode(self):
        mode = self.comboBox.CurrentText()
        if mode == "Easy":
            self.player.scaleFactor = 10.0
        elif mode == "Medium":
            self.player.scaleFactor = 7.5
        elif mode == "Hard":
            self.player.scaleFactor = 5.0
        elif mode == "insane":
            self.player.scaleFactor = 2.5
    
    def displayRules(self):
        self.label.setText("Press W to jump")

    def gameStart(self):
        self.label.hide()
        self.toolButton_2.hide()
        self.label_2.setText("0")
        self.active = True
        self.timer.start(10)
    
    def gameEnd(self):
        self.timer.stop()
        self.label.setText("Game Over")
        self.label.show()
        self.toolButton_2.show()
        self.toolButton_2.setText("Restart")
        self.active = False
        self.player.reset()

    def keyPressEvent(self, event):
        if self.active:
            if event.key() == QtCore.Qt.Key_W:
                self.incrementScore()
                self.player.jump()
            
    def framePaint(self, event):
        painter = QtGui.QPainter(self.widget_3)
        self.player.paintBruin(painter)
    
    def incrementScore(self):
        i = int(self.label_2.text())
        i = i + 1
        self.label_2.setText(str(i))

    def quitgame(self):
        self.timer.stop()
        self.close()
    
    def animate(self):
        self.player.update()
        self.widget_3.update()
        if self.player.dead:
            self.gameEnd()

def main():
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    ui = FlappyBruinGame()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
