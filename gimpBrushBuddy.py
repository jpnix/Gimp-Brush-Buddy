#!/usr/bin/env python

#Author: Matt Permenter
#Date: 6/3/2012
#Program Name: Gimp Brush Helper
#Build: Python version 2.6, PyQt4
#Tested: only on Linux Mint 13 with Gimp 2.6

#This is my first ever GUI program, I created it because I got tired of
#manually moving all of the gimp brushes I downloaded into the  hidden gimp brush folder.
#I thought I could create a more efficient method of doing it with just 
#a single button click. So here it is!


import os,shutil
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):


    #this function takes input from the text form of the gui, concatenates it to the file directory strings
    #looks up to see if the directory exists with the os module, and moves files with the specified file type
    #to the gimp brush folder.   
    def installBrush(self):
        self.name = self.lineEdit.text()
        fileSource = ('/home/' + str(self.name) + '/Desktop/')
        fileTarget = ('/home/' + str(self.name) + '/.gimp-2.6/brushes/')
        fileType = ('.gbr','.gih','.vbr')
        for destination in os.listdir(fileSource):
            if destination.endswith(fileType):
                shutil.move(fileSource+destination,fileTarget)
                
                

    # This is the widow set up by the QT Editor, Just plugged in functions here.
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 326)
        Form.setWindowTitle(QtGui.QApplication.translate("Gimp Brush Install", "Gimp Brush Install", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(105, 60, 210, 28))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 290, 169, 28))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Install Gimp Brushes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 211, 191))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("gimp.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 361, 20))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Download Gimp Brushes to Desktop directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 221, 18))
        self.label.setText(QtGui.QApplication.translate("Form", "Type your system username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.pushButton.click)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ui.installBrush)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass
    

#the main stuff that happens
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

