# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseline.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time, os, json, indyTracks
class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, parent, trackname):
        super(Ui_Dialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(222, 116)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.trackname = trackname
        self.parent = parent
        self.weight = 0
        self.front  = 0
        self.rear   = 0
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 70, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.baselineLabel = QtWidgets.QLabel(self)
        self.baselineLabel.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.baselineLabel.setObjectName("baselineLabel")
        self.weightInput = QtWidgets.QLineEdit(self)
        self.weightInput.setGeometry(QtCore.QRect(20, 30, 31, 20))
        self.weightInput.setObjectName("weightInput")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label.setObjectName("label")
        self.frontInput = QtWidgets.QLineEdit(self)
        self.frontInput.setGeometry(QtCore.QRect(90, 30, 31, 20))
        self.frontInput.setObjectName("frontInput")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.rearInput = QtWidgets.QLineEdit(self)
        self.rearInput.setGeometry(QtCore.QRect(150, 30, 31, 20))
        self.rearInput.setObjectName("rearInput")

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.ReturnBaseLine)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.baselineLabel.setText(_translate("Dialog", "<html><head/><body><p>Baseline for :</p></body></html>"))
        self.label.setText(_translate("Dialog", "Weight Jacker"))
        self.label_2.setText(_translate("Dialog", "Front ARB"))
        self.label_3.setText(_translate("Dialog", "Rear ARB"))
    def ReturnBaseLine(self):
        self.weight = self.weightInput.text()
        self.front  = self.frontInput.text()
        self.rear   = self.rearInput.text()
        fail   = False
        if not self.weight.isnumeric():
            fail = True
        else:
            self.weight = int(self.weight)
        if not self.front.isnumeric():
            fail = True
        elif int(self.front) > 6 or int(self.front) < 0:
            fail = True
        else:
            self.front = int(self.front)
        if not self.rear.isnumeric():
            fail = True
        elif int(self.rear) > 6 or int(self.rear) < 0:
            fail = True
        else:
            self.rear = int(self.rear)
        if not fail:
            data = {}
            data["lap"] = []
            x = 0
            while x in range(0,33):
                data["lap"].append({
                    'lap': x,
                    'weight': self.weight,
                    'front': self.front,
                    'rear': self.rear
                })
                x += 1
            with open("../indycar/{}.json".format(self.trackname), 'w') as file:
                json.dump(data, file)
            self.accept()

        else:
            print("failed")
