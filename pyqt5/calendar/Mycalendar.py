'''
日历控件
QCalendarWidget
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar,self).__init__()
        self.initUI()

    def initUI(self):
        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showDate)
        self.resize(500,400)
        self.setWindowTitle('日历演示')

        self.label=QLabel(self)
        date=self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)

    def showDate(self,date):
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        print(date.toString('yyyy-MM-dd dddd'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())