#QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle('让窗口居中')

        self.resize(400, 300)
    def center(self):
        #获取屏幕坐标系
        screen=QDesktopWidget().screenGeometry()
        #获取窗口的坐标系
        size=self.geometry()
        newleft=(screen. width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.center() #调用center
    main.show()


    sys.exit(app.exec_())