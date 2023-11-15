#Smart Calculation Program
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

#UI의 기본형인 SCP 클래스 생성
class SCP(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    #UI 구성
    def initUI(self):
        self.setWindowTitle('SCP')
        self.setWindowIcon(QIcon('SCP.png'))
        self.setGeometry(300, 300, 600, 800) #x, y, width, height
        self.quit()
        self.show()
    #종료 버튼 구성
    def quit(self):
        btn = QPushButton('Quit', self)
        btn.move(250, 750)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = SCP()
   sys.exit(app.exec_())