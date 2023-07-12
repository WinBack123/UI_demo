import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('简单绘图')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.pix = QPixmap(600, 500)  # 设置画布大小
        self.pix.fill(Qt.white)  # 设置画布背景颜色为白色

    # 绘图
    def paintEvent(self, event):
        p = QPainter(self.pix)
        p.drawLine(self.lastPoint, self.endPoint)  # 根据鼠标指针前后两个位置绘制直线
        self.lastPoint = self.endPoint  # 让前一个坐标值等于后一个坐标值，就能画出连续的线
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    #当鼠标左键按下时触发该函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    #当鼠标左键移动时触发该函数
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()#调用paintEvent函数，重新绘制

    #当鼠标左键释放时触发该函数
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()  # 调用paintEvent函数，重新绘制

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Demo()
    form.show()
    sys.exit(app.exec_())
