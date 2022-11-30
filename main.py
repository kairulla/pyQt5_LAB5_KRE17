#!/usr/bin/env python3
# coding=utf-8

import random
import sys
import re

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi

class Launcher(QWidget):

    def __init__(self):
        super(Launcher, self).__init__()
        loadUi('g.ui', self)

        self.setWindowTitle('Лабораторная 5 _ Python3 + PyQt5')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('_MY_PICTURES//logo.png'))

        image = QtGui.QPixmap()
        image.load('_MY_PICTURES//background.png')
        # image = image.scaled(self.width(), self.height())
        image = image.scaledToWidth(round(self.width() / 14))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        self.qPushButtonArrayGenerator.clicked.connect(self.qPushButtonArrayGeneratorOnClick)
        self.qPushButtonClear.clicked.connect(self.qPushButtonClearOnClick)
        self.qPushButtonReadFromFile.clicked.connect(self.qPushButtonReadFromFileOnClick)
        self.qPushButtonSaveToFile.clicked.connect(self.qPushButtonSaveToFileOnClick)
        self.qPushButtonSolver.clicked.connect(self.qPushButtonSolverOnClick)


    def qPushButtonArrayGeneratorOnClick(self):
        self.qPlainTextEditMyArray.clear()
        row = 5
        column = 6
        for i in range(row):
            for j in range(column):
                number = random.randint(-20, 20)
                self.qPlainTextEditMyArray.insertPlainText("%6s" % number)
            self.qPlainTextEditMyArray.appendPlainText("\n")


    def qPushButtonClearOnClick(self):
        self.qPlainTextEditMyArray.clear()
        self.qLabelValues.setText("Максимальный элемент = ")


    def qPushButtonReadFromFileOnClick(self):
        self.qPushButtonClearOnClick()
        try:
            filename = "myFile.txt"

            in_file = open(filename, 'r')
            colList = []
            for line in in_file:
                sub_array = []
                str_nums = line.split(' ')
                for sn in str_nums:
                    if sn:
                        sub_array.append(int(sn))
                colList.append(sub_array)
            in_file.close()

            for i in colList:
                for j in i:
                    self.qPlainTextEditMyArray.insertPlainText("%6s" % str(j))
                self.qPlainTextEditMyArray.appendPlainText("\n")
        except:
            self.qLabelValues.setText("Нет файла")


    def qPushButtonSaveToFileOnClick(self):
        # write_file("myFile.txt", self.global_array)
        # self.qLabelValues.setText("СОХРАНЕНО")

        filename = "myFile.txt"
        text = self.qPlainTextEditMyArray.toPlainText()
        colList = self.qPlainTextEditMyArrayConvertToArray(text)

        out_file = open(filename, 'w')
        for row in colList:
            for num in row:
                out_file.write("%6s" % num)
            out_file.write('\n')
        out_file.close()


    def qPushButtonSolverOnClick(self):
        text = self.qPlainTextEditMyArray.toPlainText()
        colList = self.qPlainTextEditMyArrayConvertToArray(text)
        # print(colList)

        colListMax = colListMin = colList[0][0]
        colListMaxI = colListMinI = colListMaxJ = colListMinJ = 0
        for row, i in enumerate(colList):
            for col, j in enumerate(i):
                if (j > colListMax):
                    colListMax = j
                    colListMaxI = row
                    colListMaxJ = col
                if (j < colListMin):
                    colListMin = j
                    colListMinI = row
                    colListMinJ = col
        self.qLabelValues.setText(
            "Максимальный элемент = %d    i = %d  j = %d\nМинимальный элемент = %d    i = %d  j = %d" % (
                colListMax, colListMaxI, colListMaxJ, colListMin, colListMinI, colListMinJ))

        # for row, i in enumerate(colList):
        #     for col, j in enumerate(i):
        #         print("%6s" % colList[row][col], end="")
        #     print()


    def qPlainTextEditMyArrayConvertToArray(self, text):
        rowListDirty = text.split('\n')

        rowList = []
        for i in rowListDirty:
            if (len(i) != 0):
                rowList.append(i)
        # print(rowList)

        colListDirty = []
        for j in rowList:
            col = re.split(' ', j)
            colListDirty.append(col)
        # print(colListDirty)

        colList = []
        for i in colListDirty:
            sub_array = []
            for j in i:
                if (len(j) != 0):
                    sub_array.append(int(j))
            colList.append(sub_array)
        return colList


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec_())
