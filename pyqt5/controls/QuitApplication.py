import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QMainWindow, QApplication,QWidget

class QuiApplication(QMainWindow):
    def __init__(self):
        super(QuiApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        #添加Button

        self.button1=QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainFram=QWidget()
        mainFram.setLayout(layout)

        self.setCentralWidget(mainFram)

    #按钮单击事件的方法(自定义的槽)
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'被按下')
        app=QApplication.instance()
        #退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuiApplication()
    main.show()
    sys.exit(app.exec_())