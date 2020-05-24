import sys

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QLabel,QMessageBox

app = QApplication([])
label = QLabel('This is PyQt5!')
label.show()
app.exec_()
