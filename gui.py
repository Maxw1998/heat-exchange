# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'

# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(883, 610)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 550, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 550, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 100, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.textEdited[str].connect(lambda: self.onChange())  ##
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 111, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(580, 100, 111, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 100, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 360, 71, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(470, 160, 91, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 230, 71, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 300, 111, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 160, 51, 41))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 230, 111, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(470, 300, 91, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(470, 350, 91, 41))
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 160, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 160, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 300, 111, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 360, 111, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(580, 300, 111, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(580, 360, 111, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 430, 81, 41))
        self.label_11.setObjectName("label_11")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 430, 111, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(370, 430, 111, 41))
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 430, 111, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.show()

        self.pushButton.clicked.connect(self.addNum)

    def addNum(self,Dialog):
        reliutiG = self.lineEdit.text()
        feidian = self.lineEdit_2.text()
        rukouC1 = self.lineEdit_6.text()
        chukouC1 = self.lineEdit_3.text()
        lengliutiG = self.lineEdit_4.text()
        lingjiedian = self.lineEdit_5.text()
        rukouC2 = self.lineEdit_7.text()
        chukouC2 = self.lineEdit_8.text()
        huanreA = self.lineEdit_9.text()
        #su = sum([reliutiG,feidian,rukouC1,chukouC1,lengliutiG,lingjiedian,rukouC2,chukouC2,huanreA])
        #print(u'计算结果为: %s' %su)
        print(u'热流体流量: %s 沸点：%s 入口温度：%s 出口温度：%s 冷流体流量：%s 凝结点：%s 入口温度2：%s 出口温度2：%s 换热面积：%s' %(reliutiG,feidian,rukouC1,chukouC1,lengliutiG,lingjiedian,rukouC2,chukouC2,huanreA))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "传热计算"))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.pushButton_2.setText(_translate("Dialog", "清零"))
        self.comboBox.setItemText(0, _translate("Dialog", "水"))
        self.comboBox.setItemText(1, _translate("Dialog", "空气"))
        self.comboBox.setItemText(2, _translate("Dialog", "硫化氢"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">热流体</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">热流体流量</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">入口温度</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">临界点</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">出口温度</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">冷流体</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">冷流体流量</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">沸点</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "水"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "空气"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">入口温度</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">出口温度</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">通道类型</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">换热面积</span></p></body></html>"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    win = Ui_Dialog()
    win.setupUi(form)
    form.show()
    sys.exit(app.exec_())