#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Main(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.initUI()


    def initUI(self):
        # set window tool tip
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # resize button
        btn1 = QPushButton('Button', self)
        btn1.setToolTip('resize')
        btn1.clicked.connect(lambda: self.resize(btn1))
        btn1.move(50, 50)

        #exit button
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def resize(self, btn):
        btn.resize(200, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main('Image Handler Main')
    sys.exit(app.exec_())
