# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flappybird.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Bruin(object):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.x, self.y = 150, 350
        self.vx, self.vy = 0,0
        self.ay = -9.81
        self.dead = False
    
    def setPos(self,x,y):
        self.x, self.y = x,y
        
    def jump(self):
        self.vy = 50
    
    def update(self):
        if self.y < 1:
            self.y = 0
            if self.vy < 0:
                self.vy = 0
            self.dead = True
        if self.y > 650:
            self.dead = True
        self.vy += self.ay / 7.5
        self.x += self.vx / 7.5
        self.y += self.vy / 7.5

class FlappyBruinGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(FlappyBruinGame, self).__init__()
        self.player = Bruin()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 706)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color:yellow;")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 220, 971, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.frame)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.verticalLayout.addWidget(self.newButton)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setEnabled(True)
        self.quitButton.setAutoDefault(True)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flappy Bruin"))
        self.label.setText(_translate("MainWindow", "Score:"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "FlappyBruin"))
        self.newButton.setText(_translate("MainWindow", "New Game"))
        self.quitButton.setText(_translate("MainWindow", "Quit Game"))
        self.newButton.clicked.connect(self.gameStart)
        self.quitButton.clicked.connect(self.quitgame)
        self.frame.paintEvent = self.framePaint

    def gameStart(self):
        self.label_3.hide()
        self.label_2.setText("0")
        self.timer.start(10)
    
    def gameEnd(self):
        self.timer.stop()
        self.label_3.setText("Game Over")
        self.label_3.show()
        self.player.reset()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.incrementScore()
            self.player.jump()
        if event.key() == QtCore.Qt.Key_O:
            self.gameEnd()
            
    def framePaint(self, event):
        painter = QtGui.QPainter(self.frame)
        painter.fillRect(self.player.x + 1, 600 - self.player.y, 20, 20, QtCore.Qt.blue)

    def incrementScore(self):
        i = int(self.label_2.text())
        i = i + 1
        self.label_2.setText(str(i))

    def quitgame(self):
        self.timer.stop()
        self.close()
    
    def animate(self):
        self.player.update()
        self.frame.update()
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

#%%
QtCore.Qt.blue