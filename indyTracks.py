## -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indyTracls.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os, json, time
import baseline
class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, Dialog, trackname=None, fromOverlay=False):
        super(Ui_Dialog, self).__init__()
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 412)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.trackname = trackname
        self.Dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.indyInfoGrid = QtWidgets.QTableWidget(Dialog)
        self.indyInfoGrid.setGeometry(QtCore.QRect(10, 50, 371, 301))
        self.indyInfoGrid.setObjectName("indyInfoGrid")
        self.indyInfoGrid.setColumnCount(3)
        self.indyInfoGrid.setRowCount(33)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.indyInfoGrid.setHorizontalHeaderItem(2, item)
        self.lap0_weight = QtWidgets.QTableWidgetItem()
        self.lap0_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(0, 0, self.lap0_weight)
        self.lap0_front = QtWidgets.QTableWidgetItem()
        self.lap0_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(0, 1, self.lap0_front)
        self.lap0_rear = QtWidgets.QTableWidgetItem()
        self.lap0_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(0, 2, self.lap0_rear)
        self.lap1_weight = QtWidgets.QTableWidgetItem()
        self.lap1_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(1, 0, self.lap1_weight)
        self.lap1_front = QtWidgets.QTableWidgetItem()
        self.lap1_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(1, 1, self.lap1_front)
        self.lap1_rear = QtWidgets.QTableWidgetItem()
        self.lap1_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(1, 2, self.lap1_rear)
        self.lap2_weight = QtWidgets.QTableWidgetItem()
        self.lap2_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(2, 0, self.lap2_weight)
        self.lap2_front = QtWidgets.QTableWidgetItem()
        self.lap2_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(2, 1, self.lap2_front)
        self.lap2_rear = QtWidgets.QTableWidgetItem()
        self.lap2_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(2, 2, self.lap2_rear)
        self.lap3_weight = QtWidgets.QTableWidgetItem()
        self.lap3_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(3, 0, self.lap3_weight)
        self.lap3_front = QtWidgets.QTableWidgetItem()
        self.lap3_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(3, 1, self.lap3_front)
        self.lap3_rear = QtWidgets.QTableWidgetItem()
        self.lap3_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(3, 2, self.lap3_rear)
        self.lap4_weight = QtWidgets.QTableWidgetItem()
        self.lap4_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(4, 0, self.lap4_weight)
        self.lap4_front = QtWidgets.QTableWidgetItem()
        self.lap4_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(4, 1, self.lap4_front)
        self.lap4_rear = QtWidgets.QTableWidgetItem()
        self.lap4_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(4, 2, self.lap4_rear)
        self.lap5_weight = QtWidgets.QTableWidgetItem()
        self.lap5_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(5, 0, self.lap5_weight)
        self.lap5_front = QtWidgets.QTableWidgetItem()
        self.lap5_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(5, 1, self.lap5_front)
        self.lap5_rear = QtWidgets.QTableWidgetItem()
        self.lap5_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(5, 2, self.lap5_rear)
        self.lap6_weight = QtWidgets.QTableWidgetItem()
        self.lap6_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(6, 0, self.lap6_weight)
        self.lap6_front = QtWidgets.QTableWidgetItem()
        self.lap6_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(6, 1, self.lap6_front)
        self.lap6_rear = QtWidgets.QTableWidgetItem()
        self.lap6_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(6, 2, self.lap6_rear)
        self.lap7_weight = QtWidgets.QTableWidgetItem()
        self.lap7_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(7, 0, self.lap7_weight)
        self.lap7_front = QtWidgets.QTableWidgetItem()
        self.lap7_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(7, 1, self.lap7_front)
        self.lap7_rear = QtWidgets.QTableWidgetItem()
        self.lap7_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(7, 2, self.lap7_rear)
        self.lap8_weight = QtWidgets.QTableWidgetItem()
        self.lap8_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(8, 0, self.lap8_weight)
        self.lap8_front = QtWidgets.QTableWidgetItem()
        self.lap8_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(8, 1, self.lap8_front)
        self.lap8_rear = QtWidgets.QTableWidgetItem()
        self.lap8_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(8, 2, self.lap8_rear)
        self.lap9_weight = QtWidgets.QTableWidgetItem()
        self.lap9_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(9, 0, self.lap9_weight)
        self.lap9_front = QtWidgets.QTableWidgetItem()
        self.lap9_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(9, 1, self.lap9_front)
        self.lap9_rear = QtWidgets.QTableWidgetItem()
        self.lap9_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(9, 2, self.lap9_rear)
        self.lap10_weight = QtWidgets.QTableWidgetItem()
        self.lap10_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(10, 0, self.lap10_weight)
        self.lap10_front = QtWidgets.QTableWidgetItem()
        self.lap10_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(10, 1, self.lap10_front)
        self.lap10_rear = QtWidgets.QTableWidgetItem()
        self.lap10_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(10, 2, self.lap10_rear)
        self.lap11_weight = QtWidgets.QTableWidgetItem()
        self.lap11_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(11, 0, self.lap11_weight)
        self.lap11_front = QtWidgets.QTableWidgetItem()
        self.lap11_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(11, 1, self.lap11_front)
        self.lap11_rear = QtWidgets.QTableWidgetItem()
        self.lap11_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(11, 2, self.lap11_rear)
        self.lap12_weight = QtWidgets.QTableWidgetItem()
        self.lap12_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(12, 0, self.lap12_weight)
        self.lap12_front = QtWidgets.QTableWidgetItem()
        self.lap12_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(12, 1, self.lap12_front)
        self.lap12_rear = QtWidgets.QTableWidgetItem()
        self.lap12_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(12, 2, self.lap12_rear)
        self.lap13_weight = QtWidgets.QTableWidgetItem()
        self.lap13_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(13, 0, self.lap13_weight)
        self.lap13_front = QtWidgets.QTableWidgetItem()
        self.lap13_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(13, 1, self.lap13_front)
        self.lap13_rear = QtWidgets.QTableWidgetItem()
        self.lap13_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(13, 2, self.lap13_rear)
        self.lap14_weight = QtWidgets.QTableWidgetItem()
        self.lap14_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(14, 0, self.lap14_weight)
        self.lap14_front = QtWidgets.QTableWidgetItem()
        self.lap14_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(14, 1, self.lap14_front)
        self.lap14_rear = QtWidgets.QTableWidgetItem()
        self.lap14_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(14, 2, self.lap14_rear)
        self.lap15_weight = QtWidgets.QTableWidgetItem()
        self.lap15_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(15, 0, self.lap15_weight)
        self.lap15_front = QtWidgets.QTableWidgetItem()
        self.lap15_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(15, 1, self.lap15_front)
        self.lap15_rear = QtWidgets.QTableWidgetItem()
        self.lap15_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(15, 2, self.lap15_rear)
        self.lap16_weight = QtWidgets.QTableWidgetItem()
        self.lap16_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(16, 0, self.lap16_weight)
        self.lap16_front = QtWidgets.QTableWidgetItem()
        self.lap16_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(16, 1, self.lap16_front)
        self.lap16_rear = QtWidgets.QTableWidgetItem()
        self.lap16_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(16, 2, self.lap16_rear)
        self.lap17_weight = QtWidgets.QTableWidgetItem()
        self.lap17_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(17, 0, self.lap17_weight)
        self.lap17_front = QtWidgets.QTableWidgetItem()
        self.lap17_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(17, 1, self.lap17_front)
        self.lap17_rear = QtWidgets.QTableWidgetItem()
        self.lap17_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(17, 2, self.lap17_rear)
        self.lap18_weight = QtWidgets.QTableWidgetItem()
        self.lap18_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(18, 0, self.lap18_weight)
        self.lap18_front = QtWidgets.QTableWidgetItem()
        self.lap18_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(18, 1, self.lap18_front)
        self.lap18_rear = QtWidgets.QTableWidgetItem()
        self.lap18_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(18, 2, self.lap18_rear)
        self.lap19_weight = QtWidgets.QTableWidgetItem()
        self.lap19_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(19, 0, self.lap19_weight)
        self.lap19_front = QtWidgets.QTableWidgetItem()
        self.lap19_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(19, 1, self.lap19_front)
        self.lap19_rear = QtWidgets.QTableWidgetItem()
        self.lap19_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(19, 2, self.lap19_rear)
        self.lap20_weight = QtWidgets.QTableWidgetItem()
        self.lap20_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(20, 0, self.lap20_weight)
        self.lap20_front = QtWidgets.QTableWidgetItem()
        self.lap20_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(20, 1, self.lap20_front)
        self.lap20_rear = QtWidgets.QTableWidgetItem()
        self.lap20_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(20, 2, self.lap20_rear)
        self.lap21_weight = QtWidgets.QTableWidgetItem()
        self.lap21_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(21, 0, self.lap21_weight)
        self.lap21_front = QtWidgets.QTableWidgetItem()
        self.lap21_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(21, 1, self.lap21_front)
        self.lap21_rear = QtWidgets.QTableWidgetItem()
        self.lap21_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(21, 2, self.lap21_rear)
        self.lap22_weight = QtWidgets.QTableWidgetItem()
        self.lap22_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(22, 0, self.lap22_weight)
        self.lap22_front = QtWidgets.QTableWidgetItem()
        self.lap22_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(22, 1, self.lap22_front)
        self.lap22_rear = QtWidgets.QTableWidgetItem()
        self.lap22_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(22, 2, self.lap22_rear)
        self.lap23_weight = QtWidgets.QTableWidgetItem()
        self.lap23_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(23, 0, self.lap23_weight)
        self.lap23_front = QtWidgets.QTableWidgetItem()
        self.lap23_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(23, 1, self.lap23_front)
        self.lap23_rear = QtWidgets.QTableWidgetItem()
        self.lap23_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(23, 2, self.lap23_rear)
        self.lap24_weight = QtWidgets.QTableWidgetItem()
        self.lap24_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(24, 0, self.lap24_weight)
        self.lap24_front = QtWidgets.QTableWidgetItem()
        self.lap24_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(24, 1, self.lap24_front)
        self.lap24_rear = QtWidgets.QTableWidgetItem()
        self.lap24_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(24, 2, self.lap24_rear)
        self.lap25_weight = QtWidgets.QTableWidgetItem()
        self.lap25_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(25, 0, self.lap25_weight)
        self.lap25_front = QtWidgets.QTableWidgetItem()
        self.lap25_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(25, 1, self.lap25_front)
        self.lap25_rear = QtWidgets.QTableWidgetItem()
        self.lap25_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(25, 2, self.lap25_rear)
        self.lap26_weight = QtWidgets.QTableWidgetItem()
        self.lap26_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(26, 0, self.lap26_weight)
        self.lap26_front = QtWidgets.QTableWidgetItem()
        self.lap26_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(26, 1, self.lap26_front)
        self.lap26_rear = QtWidgets.QTableWidgetItem()
        self.lap26_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(26, 2, self.lap26_rear)
        self.lap27_weight = QtWidgets.QTableWidgetItem()
        self.lap27_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(27, 0, self.lap27_weight)
        self.lap27_front = QtWidgets.QTableWidgetItem()
        self.lap27_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(27, 1, self.lap27_front)
        self.lap27_rear = QtWidgets.QTableWidgetItem()
        self.lap27_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(27, 2, self.lap27_rear)
        self.lap28_weight = QtWidgets.QTableWidgetItem()
        self.lap28_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(28, 0, self.lap28_weight)
        self.lap28_front = QtWidgets.QTableWidgetItem()
        self.lap28_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(28, 1, self.lap28_front)
        self.lap28_rear = QtWidgets.QTableWidgetItem()
        self.lap28_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(28, 2, self.lap28_rear)
        self.lap29_weight = QtWidgets.QTableWidgetItem()
        self.lap29_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(29, 0, self.lap29_weight)
        self.lap29_front = QtWidgets.QTableWidgetItem()
        self.lap29_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(29, 1, self.lap29_front)
        self.lap29_rear = QtWidgets.QTableWidgetItem()
        self.lap29_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(29, 2, self.lap29_rear)
        self.lap30_weight = QtWidgets.QTableWidgetItem()
        self.lap30_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(30, 0, self.lap30_weight)
        self.lap30_front = QtWidgets.QTableWidgetItem()
        self.lap30_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(30, 1, self.lap30_front)
        self.lap30_rear = QtWidgets.QTableWidgetItem()
        self.lap30_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(30, 2, self.lap30_rear)
        self.lap31_weight = QtWidgets.QTableWidgetItem()
        self.lap31_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(31, 0, self.lap31_weight)
        self.lap31_front = QtWidgets.QTableWidgetItem()
        self.lap31_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(31, 1, self.lap31_front)
        self.lap31_rear = QtWidgets.QTableWidgetItem()
        self.lap31_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(31, 2, self.lap31_rear)
        self.lap32_weight = QtWidgets.QTableWidgetItem()
        self.lap32_weight.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(32, 0, self.lap32_weight)
        self.lap32_front = QtWidgets.QTableWidgetItem()
        self.lap32_front.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(32, 1, self.lap32_front)
        self.lap32_rear = QtWidgets.QTableWidgetItem()
        self.lap32_rear.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.indyInfoGrid.setItem(32, 2, self.lap32_rear)
        self.indyInfoGrid.horizontalHeader().setDefaultSectionSize(100)
        self.indyInfoGrid.verticalHeader().setDefaultSectionSize(10)
        self.trackNameCombo = QtWidgets.QComboBox(Dialog)
        self.trackNameCombo.setGeometry(QtCore.QRect(20, 20, 201, 22))
        self.trackNameCombo.setObjectName("trackNameCombo")
        self.loadTracks()
        self.loadIndyTrack = QtWidgets.QPushButton(Dialog)
        self.loadIndyTrack.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.loadIndyTrack.setObjectName("loadIndyTrack")
        self.loadIndyTrack.setCheckable(True)
        self.loadIndyTrack.clicked.connect(self.btnstate)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        if self.trackname and not os.path.exists("indycar/{}.json".format(self.trackname)):
            self.callOtherDialog(Dialog)
        elif self.trackname and not fromOverlay:
            self.setTrack(self.trackname)
            self.btnstate(True)
        elif fromOverlay:
            self.close()

    def callOtherDialog(self, Dialog):
        Dialog.hide()
        self.baselineDialog = baseline.Ui_Dialog(self, self.trackname)
        self.baselineDialog.exec_()
        self.setTrack(self.trackname)
        Dialog.show()
        self.btnstate(True)

    def accept(self):
        file = self.trackname.lower()
        file = "indycar/{}.json".format(file)
        x = 0
        data = {}
        data["lap"] = []
        hasFailed = False
        while x in range(0, 33):
            weight = self.indyInfoGrid.item(x, 0).text()
            front  = self.indyInfoGrid.item(x, 1).text()
            rear   = self.indyInfoGrid.item(x, 2).text()
            fail = False
            if not weight.replace("-", "").isnumeric() or int(weight) >= 20 or int(weight) <= -20:
                fail = True
                print("Weight failed lap {}".format(x))
            if not front.isnumeric() or int(front) > 6 or int(front) < 1:
                fail = True
                print("Front failed lap {}".format(x))
            if not rear.isnumeric() or int(rear) > 6 or int(rear) < 1:
                fail = True
                print("Rear failed lap {}".format(x))
            if not fail:
                data["lap"].append({
                    'lap': x,
                    'weight': int(weight),
                    'front': int(front),
                    'rear': int(rear)
                })
            else:
                hasFailed = True
            x += 1
        if hasFailed == False:
            print("has not failed")
            with open(file, "w") as track_file:
                json.dump(data, track_file)
            self.Dialog.close()
        else:
            print("has failed")
            hasFailed = False
            pass
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.indyInfoGrid.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Lap 0"))
        item = self.indyInfoGrid.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Lap 1"))
        item = self.indyInfoGrid.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Lap 2"))
        item = self.indyInfoGrid.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Lap 3"))
        item = self.indyInfoGrid.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Lap 4"))
        item = self.indyInfoGrid.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "Lap 5"))
        item = self.indyInfoGrid.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "Lap 6"))
        item = self.indyInfoGrid.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "Lap 7"))
        item = self.indyInfoGrid.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "Lap 8"))
        item = self.indyInfoGrid.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "Lap 9"))
        item = self.indyInfoGrid.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "Lap 10"))
        item = self.indyInfoGrid.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "Lap 11"))
        item = self.indyInfoGrid.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "Lap 12"))
        item = self.indyInfoGrid.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "Lap 13"))
        item = self.indyInfoGrid.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "Lap 14"))
        item = self.indyInfoGrid.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "Lap 15"))
        item = self.indyInfoGrid.verticalHeaderItem(16)
        item.setText(_translate("Dialog", "Lap 16"))
        item = self.indyInfoGrid.verticalHeaderItem(17)
        item.setText(_translate("Dialog", "Lap 17"))
        item = self.indyInfoGrid.verticalHeaderItem(18)
        item.setText(_translate("Dialog", "Lap 18"))
        item = self.indyInfoGrid.verticalHeaderItem(19)
        item.setText(_translate("Dialog", "Lap 19"))
        item = self.indyInfoGrid.verticalHeaderItem(20)
        item.setText(_translate("Dialog", "Lap 20"))
        item = self.indyInfoGrid.verticalHeaderItem(21)
        item.setText(_translate("Dialog", "Lap 21"))
        item = self.indyInfoGrid.verticalHeaderItem(22)
        item.setText(_translate("Dialog", "Lap 22"))
        item = self.indyInfoGrid.verticalHeaderItem(23)
        item.setText(_translate("Dialog", "Lap 23"))
        item = self.indyInfoGrid.verticalHeaderItem(24)
        item.setText(_translate("Dialog", "Lap 24"))
        item = self.indyInfoGrid.verticalHeaderItem(25)
        item.setText(_translate("Dialog", "Lap 25"))
        item = self.indyInfoGrid.verticalHeaderItem(26)
        item.setText(_translate("Dialog", "Lap 26"))
        item = self.indyInfoGrid.verticalHeaderItem(27)
        item.setText(_translate("Dialog", "Lap 27"))
        item = self.indyInfoGrid.verticalHeaderItem(28)
        item.setText(_translate("Dialog", "Lap 28"))
        item = self.indyInfoGrid.verticalHeaderItem(29)
        item.setText(_translate("Dialog", "Lap 29"))
        item = self.indyInfoGrid.verticalHeaderItem(30)
        item.setText(_translate("Dialog", "Lap 30"))
        item = self.indyInfoGrid.verticalHeaderItem(31)
        item.setText(_translate("Dialog", "Lap 31"))
        item = self.indyInfoGrid.verticalHeaderItem(32)
        item.setText(_translate("Dialog", "Lap 32"))
        item = self.indyInfoGrid.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Weight Jacker"))
        item = self.indyInfoGrid.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Front ARB"))
        item = self.indyInfoGrid.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Rear ARB"))
        __sortingEnabled = self.indyInfoGrid.isSortingEnabled()
        self.indyInfoGrid.setSortingEnabled(False)
        self.indyInfoGrid.setSortingEnabled(__sortingEnabled)
        self.loadIndyTrack.setText(_translate("Dialog", "Load"))

    def btnstate(self, override=False):
        if self.loadIndyTrack.isChecked() or override == True:
            self.trackname = self.trackNameCombo.currentText()
            file = self.trackname.lower()
            file = file
            file = "indycar/{}.json".format(file)
            with open(file, "r") as track_file:
                data = json.load(track_file)
            x = 0
            for p in data['lap']:
                weight =  p["weight"]
                w_table = self.indyInfoGrid.item(x, 0)
                w_table.setText("{}".format(weight))
                front = p["front"]
                f_table = self.indyInfoGrid.item(x, 1)
                f_table.setText("{}".format(front))
                rear = p["rear"]
                r_table = self.indyInfoGrid.item(x, 2)
                r_table.setText("{}".format(rear))
                x += 1

    def loadTracks(self):
        for files in os.listdir("indycar/"):
            track = files.replace(".json", "")
            track = track.title()
            self.trackNameCombo.addItem(track)

    def setTrack(self, trackname):
        index = self.trackNameCombo.findText(self.trackname, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.trackNameCombo.setCurrentIndex(index)
        else:
            self.trackNameCombo.addItem(self.trackname)
            index = self.trackNameCombo.findText(self.trackname, QtCore.Qt.MatchFixedString)
            self.trackNameCombo.setCurrentIndex(index)

def start(trackname=None, fromOverlay=False):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDialog = QtWidgets.QDialog()
    main = Ui_Dialog(mainDialog, trackname, fromOverlay)
    return mainDialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDialog = QtWidgets.QDialog()
    main = Ui_Dialog(mainDialog, "jonathans")
    sys.exit(mainDialog.exec_())
