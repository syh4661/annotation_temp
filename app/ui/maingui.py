# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainumYcqb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# -*- coding: utf-8 -*-



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1580, 1264)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1221, 1191))
        self.sensors = QVBoxLayout(self.verticalLayoutWidget)
        self.sensors.setObjectName(u"sensors")
        self.sensors.setContentsMargins(0, 0, 0, 0)
        self.rgb_frame = QLabel(self.verticalLayoutWidget)
        self.rgb_frame.setObjectName(u"rgb_frame")

        self.sensors.addWidget(self.rgb_frame)

        self.depth_frame = QLabel(self.verticalLayoutWidget)
        self.depth_frame.setObjectName(u"depth_frame")
        self.depth_frame.setEnabled(True)

        self.sensors.addWidget(self.depth_frame)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1320, 100, 160, 171))
        self.bottons = QVBoxLayout(self.verticalLayoutWidget_2)
        self.bottons.setObjectName(u"bottons")
        self.bottons.setContentsMargins(0, 0, 0, 0)
        self.btn_thebutton = QPushButton(self.verticalLayoutWidget_2)
        self.btn_thebutton.setObjectName(u"btn_thebutton")

        self.bottons.addWidget(self.btn_thebutton)

        self.btn_thebutton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.btn_thebutton_2.setObjectName(u"btn_thebutton_2")

        self.bottons.addWidget(self.btn_thebutton_2)

        self.btn_thebutton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.btn_thebutton_3.setObjectName(u"btn_thebutton_3")

        self.bottons.addWidget(self.btn_thebutton_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1580, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rgb_frame.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.depth_frame.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_thebutton.setText(QCoreApplication.translate("MainWindow", u"capture", None))
        self.btn_thebutton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_thebutton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi





