# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageProcessnKxdhu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(780, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(780, 600))
        MainWindow.setMaximumSize(QSize(780, 600))
        icon = QIcon()
        iconThemeName = u"icon"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"border-color: rgb(170, 0, 255);\n"
"\n"
"background-color: rgb(77, 77, 77);\n"
"selection-color: rgb(107, 36, 0);\n"
"color: rgb(225, 225, 225);\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionOwner = QAction(MainWindow)
        self.actionOwner.setObjectName(u"actionOwner")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 721, 61))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 140, 161, 71))
        font1 = QFont()
        font1.setFamily(u"Eras Demi ITC")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 260, 161, 71))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 140, 161, 71))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.pushButton_3.clicked.connect(pushButton_3_clicked)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 260, 161, 71))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(500, 370, 161, 71))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(50, 370, 161, 71))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        self.mic = QPushButton(self.centralwidget)
        self.mic.setObjectName(u"mic")
        self.mic.setGeometry(QRect(330, 299, 81, 111))
        font2 = QFont()
        font2.setFamily(u"Eras Demi ITC")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.mic.setFont(font2)
        self.mic.setCursor(QCursor(Qt.OpenHandCursor))
        self.mic.setAutoFillBackground(False)
        self.mic.setStyleSheet(u"font: 12pt \"Eras Demi ITC\";")
        icon1 = QIcon()
        icon1.addFile(u"../Project_image/mic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mic.setIcon(icon1)
        self.mic.setIconSize(QSize(50, 50))
        self.mic.setCheckable(True)
        self.mic.setAutoRepeatInterval(107)
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(540, 490, 221, 71))
        self.buttonBox.setMaximumSize(QSize(16777214, 16777215))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(710, 490, 51, 21))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(240, 500, 101, 41))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(390, 500, 101, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 21))
        self.menuHello = QMenu(self.menubar)
        self.menuHello.setObjectName(u"menuHello")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHello.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHello.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionOwner)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()

        self.retranslateUi(MainWindow)

        self.mic.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Process", None))
        self.actionOwner.setText(QCoreApplication.translate("MainWindow", u"Owner", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHOOSE YOUR IMAGE PROCESSING TOOL", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Image to Text", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Image to\n"
" Handwriting", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Image to Sketch", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Gesture Control", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Image to Text", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Image to Text", None))
        self.mic.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.menuHello.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

def pushButton_3_clicked():
    print("Opening Image to Sketch")
    command="python mediagesture.py"
    subprocess.Popen(command)
