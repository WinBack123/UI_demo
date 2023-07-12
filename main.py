from PyQt5 import uic
from PyQt5 import QtWidgets
import qdarkstyle
import sys

class Stats:
    def __init__(self):
        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = uic.loadUi('main.ui')



app = QtWidgets.QApplication(sys.argv)
#app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
stats = Stats()
stats.ui.show()
app.exec_()






