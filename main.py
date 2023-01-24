# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:07:31 2022

@author: marek
"""

import literki as literki
#from main_window_ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLineEdit, QButtonGroup, QRadioButton)
from PyQt5 import QtCore, QtWidgets, QtGui


def literki_app():
    pass

class Window(QMainWindow):
    active_row=1
    word_length=5
    num_of_tries=6
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.new_game()
        
        self.connect()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Literki")
        MainWindow.resize(310, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("central_widget")
        self.widgets=[[0 for x in range(self.word_length)] for y in range(self.num_of_tries)]           
        font = QtGui.QFont()
        font.setPointSize(14)
        left_margin = 60-20*(self.word_length-5)
        for y in range(0, self.num_of_tries):
            for x in range(0, self.word_length):
                self.widgets[y][x]=QtWidgets.QLineEdit(self.centralwidget)
                self.widgets[y][x].setGeometry(QtCore.QRect(left_margin+x*40, 40+y*40, 31, 31))
                self.widgets[y][x].setFont(font)
                self.widgets[y][x].setText("")
                self.widgets[y][x].setMaxLength(1)
                self.widgets[y][x].setAlignment(QtCore.Qt.AlignCenter)
                self.widgets[y][x].setReadOnly(True)
                self.widgets[y][x].setObjectName("lineEdit"+str(x))
                self.widgets[y][x].installEventFilter(self)
                #print(x,y)
                
                
        self.level1 = QRadioButton('5',self.centralwidget)
        self.level1.setGeometry(QtCore.QRect(60, 390, 81, 41))
        self.level2 = QRadioButton('6',self.centralwidget)
        self.level2.setGeometry(QtCore.QRect(120, 390, 81, 41))
        #self.level3 = QRadioButton('7',self.centralwidget)
        #self.level3.setGeometry(QtCore.QRect(180, 390, 81, 41))
        self.levels = QButtonGroup()
        self.levels.addButton(self.level1)
        self.levels.addButton(self.level2)
        #self.levels.addButton(self.level3)
        if self.word_length == 6:
            self.level2.toggle()
        #elif self.word_length == 7:
        #    self.level3.toggle()
        else:
            self.level1.toggle()
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 330, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.new_game)
        self.pushButton.setCheckable(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 330, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.guess)
        self.pushButton_2.setCheckable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gra w słowa"))
        self.pushButton.setText(_translate("MainWindow", "Nowa Gra"))
        self.pushButton_2.setText(_translate("MainWindow", "Zgaduj"))
        
    def connect(self):
        for widget in self.centralwidget.children():
            #print(widget)
            if isinstance(widget, QLineEdit): 
                widget.textChanged.connect(self.next_letter)
                
   
        
    def lock_all(self):
        for y in range(0, self.num_of_tries):
            for x in range(0, self.word_length):
                self.widgets[y][x].setReadOnly(True)
        

    
    def lock_row(self, row):
            for x in range(0, self.word_length):
                self.widgets[row][x].setReadOnly(True)
        

            
    def unlock_row(self, row):
            for x in range(0, self.word_length):
                self.widgets[row][x].setReadOnly(False)
            self.widgets[row][0].setFocus()
            
    def row2string(self, row):
        string = ""
        for x in range(0, self.word_length):
            string+=self.widgets[row][x].displayText()
            
        return string
    
    def color_row(self, row, feedback):
        print(feedback)
        for x in range(0, self.word_length):
            if(feedback[x]==0):
                self.widgets[row][x].setStyleSheet("background-color: gray;")
            elif(feedback[x]==1):
                self.widgets[row][x].setStyleSheet("background-color: yellow;")
            elif(feedback[x]==2):
                self.widgets[row][x].setStyleSheet("background-color: green;")
                

   
    def reset_color(self):   
        for y in range(0, self.num_of_tries):
            for x in range(0, self.word_length):
                self.widgets[y][x].setStyleSheet("background-color: white;")
 

    def clear_all(self):     
        for y in range(0, self.num_of_tries):
            for x in range(0, self.word_length):
                self.widgets[y][x].setText("")
        

    def new_game(self):
      if self.pushButton.isChecked():
         print("New game pressed")
         #for y in range(0, self.num_of_tries):
         #    for x in range(0, self.word_length):
         #           self.widgets[y][x].setParent(None)
                 
         if self.level1.isChecked():
             self.word_length = 5
             self.num_of_tries = 6
         if self.level2.isChecked():
             self.word_length = 6
             self.num_of_tries = 7
         #if self.level3.isChecked():
         #    self.word_length = 7
         #    self.num_of_tries = 8
             
         
            
         self.setupUi(self)
         self.connect()
         self.game=literki.literki(self.num_of_tries, self.word_length)
         self.active_row=0
         self.lock_all()
         self.unlock_row(self.active_row)
         self.reset_color()
         self.clear_all()
         
    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_Return:
            self.guess()

        
        #print(e) 
        
        
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and event.key()== QtCore.Qt.Key_Backspace):
            #print('key press:', (event.key(), event.text()))
            self.prev_letter()
        return False
        
    def next_letter(self):      
            self.focusNextPrevChild(True)
        #if self.widgets[row][x].displayText() == '' and self.nextInFocusChain() == self.widgets[0][1]:

    def prev_letter(self):      
            self.focusNextPrevChild(False)



         
         
    def guess(self):
        print("Guess pressed")
        try:
            if(self.game.num_of_tries>0 and self.game.win==0):
                string=self.row2string(self.active_row)
                string=string.lower()
                print(string)
                if(self.game.check_word(string)):
                    feedback=self.game.guess(string)
                    print(feedback)
                    self.color_row(self.active_row, feedback)
                    self.lock_row(self.active_row)
                    if(self.active_row<self.num_of_tries-1):
                        self.active_row+=1
                        self.unlock_row(self.active_row)
                else: 
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Błąd!")
                    dlg.setText("Brak słowa w słowniku")
                    button = dlg.exec()
                    if button == QMessageBox.Ok:
                        print("OK!")
                        self.prev_letter()
            else: pass
            if(self.game.win==0 and self.game.num_of_tries==0):
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Słabo!")
                dlg.setText(f"Przegrales, chodzilo o slowo {self.game.word}.")
                button = dlg.exec()
                if button == QMessageBox.Ok:
                    print("OK!")
                    del self.game
            if(self.game.win==1):
                self.lock_all()
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Brawo!")
                dlg.setText("Wygrałes!!!")
                button = dlg.exec()
                if button == QMessageBox.Ok:
                    print("OK!")
                    del self.game
        except AttributeError:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Uwaga!")
            dlg.setText("Przed zgadywaniem rozpocznij nową grę.")
            button = dlg.exec()
            if button == QMessageBox.Ok:
                print("OK!")    
                
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    
