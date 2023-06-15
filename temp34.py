import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


msg = QMessageBox()
msg.setWindowTitle("Tutorial on PyQt5")
msg.setText("This is the main text!")
x = msg.exec_()