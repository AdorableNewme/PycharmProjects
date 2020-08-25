import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')
        layout=QVBoxLayout()

        self.colorButton=QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('设置背景色')
        self.colorButton1.clicked.connect(self.getBGCColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel=QLabel('Hello 测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    def getColor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)


    def getBGCColor(self):
        color=QColorDialog.getColor()

        p=QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p) #无法同时设置字体颜色和窗口背景色


        '''
        p.setColor(QPalette.Background,color) 
        self.setPalette(p) 设置界面背景色
        '''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())