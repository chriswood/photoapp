#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Main(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(400, 400, 300, 200)
        self.build_buttons()
        self.show()

    def build_buttons(self):
        #exit button
        #btn1.clicked.connect(lambda: self.resize(btn1))
        qbtn = QPushButton('Close', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(qbtn)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main('RaspConnect')
    sys.exit(app.exec_())
