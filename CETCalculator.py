# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re

from Ui_Calculator import Ui_MainWindow

class myIntValidator1(QIntValidator):
    def fixup(self, p_str):
        if len(p_str) == 0 or int(p_str) < 0: 
            print('myIntValidator1 null')         
            return '0'
        elif int(p_str) > 15:
            print(p_str)
            return '15'
            
class myIntValidator2(QIntValidator):
    def fixup(self, p_str):
        if len(p_str) == 0 or int(p_str) < 0: 
            print('myIntValidator2 null')
            return '0'
        elif int(p_str) > 10:
            print(p_str)
            return '10'
                 
class myIntValidator3(QDoubleValidator):
    def fixup(self, p_str):
        print(p_str)
        if len(p_str) == 0 or float(p_str) < 0: 
            print('myIntValidator3 null') 
            return '0'
        elif float(p_str) > 106.5:
            print(p_str)
            return '106.5'

class myValidator(QValidator):
    def validate(self, input_str, pos_type):
        try:
            if float(input_str) <= 106.5 and float(input_str)  >= 0:      
                return(QValidator.Acceptable,input_str,pos_type)
            elif float(input_str) > 106.5 or float(input_str)  < 0:
                return(QValidator.Intermediate,input_str,pos_type)
            else:
                return(QValidator.Invalid,input_str,pos_type)
        except:
            if len(input_str) == 0:
                print('myValidator null')
                return(QValidator.Intermediate,input_str,pos_type)
            return(QValidator.Invalid,input_str,pos_type)

    def fixup(self, p_str):
        try:
            if float(p_str)  < 0:
                return '0'
            elif float(p_str) > 106.5:
                return '106.5'
        except:
            return '0'

class mywin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.InitUi()

    def InitUi(self):
        self.setupUi(self)
        # set Window's location
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()
        print("Your screen's geometry is:",self.width,'X',self.height)
        self.resize(460,315)
        self.Wsize = self.geometry()
        centerX = int((self.width-self.Wsize.width())/2)
        centerY = int((self.height-self.Wsize.height())/2)
        self.move(centerX,centerY)
        self.setWindowTitle('CET_Score')
        self.setWindowIcon(QIcon('./ICON/python.ico'))
        # connect the singal and the slot 
        self.Clear.clicked.connect(self.Clear_Result)
        self.Calculation.clicked.connect(self.GET_Score)
        self.QuitCET.clicked.connect(self.quitWin)
        Article_Validator = myValidator()
        self.PartOne.setValidator(Article_Validator)
        # self.PartFour.setValidator(Article_Validator)
        FloatValidator = myIntValidator3(0,106.5,4)
        self.PartFour.setValidator(FloatValidator)
        Item15_Validator = myIntValidator1(0,15)
        self.PartTwo_SAB.setValidator(Item15_Validator)
        Item10_Validator = myIntValidator2(0,10)
        self.PartTwo_SC.setValidator(Item10_Validator)
        self.PartThree_SA.setValidator(Item10_Validator)
        self.PartThree_SB.setValidator(Item10_Validator)
        self.PartThree_SC.setValidator(Item10_Validator)
         
    def GET_Score(self):     
        score = float(self.PartOne.text()) + float(self.PartTwo_SAB.text())*7.1 + float(self.PartTwo_SC.text()) * 14.2 + float(self.PartThree_SA.text())*3.55 + float(self.PartThree_SB.text())*7.1 + float(self.PartThree_SC.text())*14.2 + float(self.PartFour.text())
        self.Result.setText('%.1f'%score)
        print(score)    
        print("calculation finished")
        
    def Clear_Result(self):
        self.Result.clear()
        self.Result.setText('Try Again')  
        print("clear finished")

    def quitWin(self):
        try:
            print(".........Quiting.........")
            self.close()
        except:
            print("-----Quit went wrong!-----")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    winCET= mywin()
    winCET.show()
    sys.exit(app.exec_())

