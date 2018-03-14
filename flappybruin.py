# Imports necessary files
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from bruin import Bruin
from building import Building
import pygame

# FlappyBruinGame implements the interface for our gane
class FlappyBruinGame(QtWidgets.QMainWindow):
    # Initializer
    def __init__(self):
        # Initializes the main window component
        super(FlappyBruinGame, self).__init__()
        # Creates QTimer and connects it to animate function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        # Creates instance variables
        # active: used to track whether game is active
        # focus: used to track whether mouse is currently over the game
        # highscore: used to track high score
        # score: used to track current score
        self.active = False
        self.focus = True
        self.highscore, self.score = 0,0
        # Sets up all GUI elements of the game
        self.setupUi()
        # Initializers player and building to None at first
        self.player = None
        self.buildings = None
        # Stores background image from file
        self.graphic = QtGui.QImage("lasky.png")
        # Sets up audio
        self.setupAudio()
    
    # setupAudio sets up audio for the game
    def setupAudio(self):
        # Initializes mixer object
        pygame.mixer.init()
        # Loads menu music into the mixer
        pygame.mixer.music.load('intro.mp3')
        # Sets volume to 1
        pygame.mixer.music.set_volume(1)
        # Makes music loop repeatedly
        pygame.mixer.music.play(loops = -1)
    
    # setupUI sets up GUI elements for the game
    def setupUi(self):
        # Main Windows sizing
        self.setObjectName("MainWindow")
        self.resize(1600, 900)
        self.setFixedSize(1600, 900)
        
        # Central Widget Layout
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
    
    # setMode implements setting of difficulty
    def setMode(self):
        # Gets current mode from comboBox
        mode = self.comboBox.currentText()
        # Sets focus back to self
        self.focus = True
        # Sets difficulty on the player and buildings
        self.player.setDiff(mode)
        for b in self.buildings:
            b.setDiff(mode)

    # gameStart implements starting the game
    def gameStart(self):
        # Stops current music and loads active game music
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.load('bruinsfight.mp3')
        # Hides center label, button and disables comboBox
        self.label.hide()
        self.toolButton_2.hide()
        self.comboBox.setEnabled(False)
        # Resets positions of buildings and player
        for b in self.buildings:
            b.reset()
        self.player.reset()
        # Resets current score to 0
        self.score = 0
        # Updates score label text to current score
        self.label_2.setText(str(self.score))
        # Updates active to True
        self.active = True
        # Plays active game music with repeated loop
        pygame.mixer.music.play(loops = -1)
        # Starts timer that calls animate every 10ms
        self.timer.start(10)
    
    # gameEnd implements ending the ggame
    def gameEnd(self):
        # Stops the timer
        self.timer.stop()
        # Stops the active game music and loads menu music
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load('intro.mp3')
        # Displays Game Over and Restart button
        self.label.setText("Game Over")
        self.label.show()
        self.toolButton_2.show()
        self.toolButton_2.setText("Restart")
        # Sets active to False
        self.active = False
        # Reactivates the comboBox
        self.comboBox.setEnabled(True)
        # Plays music on repeated loop
        pygame.mixer.music.play(loops = -1)
    
    # framePress returns the current position of the cursor on click
    def framePress(self,event):
        print event.x(), event.y()
    
    # keyPressEvent implements jumping action for player
    def keyPressEvent(self, event):
        # Checks if the game is active
        if self.active:
            # If W is pressed, makes the player jump
            if event.key() == QtCore.Qt.Key_W:
                self.player.jump()
    
    # framePaint is used to paint the player and buildings
    def framePaint(self, event):
        # When called for the first time, instantiates player and 3 buildings
        if self.buildings == None:
            self.buildings = [Building(self.frame) for x in range(3)]
        if self.player == None:
            self.player = Bruin(self.frame)
        # Constructs painter for the central frame
        painter = QtGui.QPainter(self.frame)
        # Sets focus on self whenever focus is True
        if self.focus:
            self.setFocus()
        else:
            self.focus = True
        # If active, calls paintBuilding and paintBruin functions
        if self.active:
            painter.drawImage(5,5,self.graphic.scaled(self.frame.geometry().width()-10,self.frame.geometry().height()-10))
            for b in self.buildings:
                b.paintBuilding(painter)
            self.player.paintBruin(painter)
    
    # eventFilter is used to reset focus from the comboBox to the frame and vice-versa
    def eventFilter(self,source,event):
        # If the mouse is hovering over comboBox, sets focus to comboBox
        # Otherwise, sets focus to self.
        if event.type() == QtCore.QEvent.HoverMove:
            if self.comboBox.underMouse():
                self.comboBox.setFocus()
                self.focus = False
            else:
                self.focus = True
    
    # updateSCore is used to update the score labels
    def updateScore(self):
        # Updates current score and its label
        self.score = self.player.score
        self.label_2.setText(str(self.score))
        # If current score exceeds high score, update high score as well
        if self.score > self.highscore:
            self.highscore = self.score
            self.label_4.setText(str(self.highscore))
        
    # quitgame is used to safely exit the game
    def quitgame(self):
        # Stops music
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        # Stops timer
        self.timer.stop()
        # Closes the window
        self.close()
    
    # animate is used to update the elements of the game constantly
    def animate(self):
        # Calls update functions for player, frame and buildings
        self.player.update(self.buildings)
        self.frame.update()
        for b in self.buildings:
            b.update()
        # If player is dead, ends the game
        # Otherwise, updates the score
        if self.player.dead:
            self.gameEnd()
        else:
            self.updateScore()

# Main function starts the GUI
def main():
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    ui = FlappyBruinGame()
    ui.show()
    sys.exit(app.exec_())

# Runs the main function
if __name__ == "__main__":
    main()