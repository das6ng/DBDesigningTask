#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *

class MainWin(object):
    def __init__(self):
        # Create an PyQT4 application object.
        self.app = QApplication(sys.argv)
 
        # The QWidget widget is the base class of all user interface objects in PyQt4.
        self.widg = QWidget()

        # Set window size.
        self.widg.resize(320, 240)
         
        # Set window title
        self.widg.setWindowTitle("Hello World!")
 
        # Add a button
        btn = QPushButton('Hello World!', self.widg)
        btn.setToolTip('Click to quit!')
        btn.clicked.connect(self.conStr)
        btn.resize(btn.sizeHint())
        btn.move(100, 80)

    def show(self):
        # Show window
        self.widg.show()
    
    def conStr(self):
        print "> Hello!"

if __name__ == "__main__":
    main = MainWin()
    main.show()
    sys.exit(main.app.exec_())
