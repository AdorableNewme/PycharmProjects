# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopern = QtWidgets.QAction(MainWindow)
        self.actionopern.setObjectName("actionopern")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menufile.addAction(self.actionnew)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionopern)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionclose)
        self.menuBar.addAction(self.menufile.menuAction())
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionopern)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionclose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionnew.setToolTip(_translate("MainWindow", "创建新文件"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionopern.setText(_translate("MainWindow", "打开"))
        self.actionclose.setText(_translate("MainWindow", "close"))
