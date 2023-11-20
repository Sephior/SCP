#Smart Calculation Program
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, qApp, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

#UI의 기본형인 SCP 클래스 생성
class SCP(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    #UI 구성
    def initUI(self):
        self.putwithkey=False
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('SCP')
        self.setWindowIcon(QIcon('SCP.png'))
        self.resize(600, 700)
        self.center()
        self.tabs = QTabWidget()
        self.simple()
        self.statistic()
        self.graph()

        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)
        self.show()


    #중앙 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

    def simple(self):
        simple = QWidget()

        label = QLabel('First Label', simple)
        label.setAlignment(Qt.AlignLeft)
        font = label.font()
        font.setFamily('Times New Roman')
        font.setBold(True)
        label.setFont(font)


        if self.putwithkey == False:
            moduler = QPushButton('%')
            CE = QPushButton('CE')
            C = QPushButton('C')
            backspace = QPushButton('<-')
            fraction = QPushButton('1/x')
            square = QPushButton('x²')
            root = QPushButton('√x')
            divide = QPushButton('/')
            b7 = QPushButton('7')
            b8 = QPushButton('8')
            b9 = QPushButton('9')
            multi = QPushButton('*')
            b4 = QPushButton('4')
            b5 = QPushButton('5')
            b6 = QPushButton('6')
            minus = QPushButton('-')
            b1 = QPushButton('1')
            b2 = QPushButton('2')
            b3 = QPushButton('3')
            plus = QPushButton('+')
            p_m = QPushButton('+/-')
            b0 = QPushButton('0')
            decimal_point = QPushButton('.')
            cal = QPushButton('=', simple)
            cal.clicked.connect(self.calculate)

            input1 = QHBoxLayout()
            input1.addStretch(1)
            input1.addWidget(moduler)
            input1.addWidget(CE)
            input1.addWidget(C)
            input1.addWidget(backspace)
            input1.addStretch(1)
            input1.addStretch(4)
            input1.addStretch(1)
            
            input2 = QHBoxLayout()
            input2.addStretch(1)
            input2.addWidget(fraction)
            input2.addWidget(square)
            input2.addWidget(root)
            input2.addWidget(divide)
            input2.addStretch(1)
            input2.addStretch(4)
            input2.addStretch(1)

            input3 = QHBoxLayout()
            input3.addStretch(1)
            input3.addWidget(b7)
            input3.addWidget(b8)
            input3.addWidget(b9)
            input3.addWidget(multi)
            input3.addStretch(1)
            input3.addStretch(4)
            input3.addStretch(1)

            input4 = QHBoxLayout()
            input4.addStretch(1)
            input4.addWidget(b4)
            input4.addWidget(b5)
            input4.addWidget(b6)
            input4.addWidget(minus)
            input4.addStretch(1)
            input4.addStretch(4)
            input4.addStretch(1)

            input4 = QHBoxLayout()
            input4.addStretch(1)
            input4.addWidget(b1)
            input4.addWidget(b2)
            input4.addWidget(b3)
            input4.addWidget(plus)
            input4.addStretch(1)
            input4.addStretch(4)
            input4.addStretch(1)

            input5 = QHBoxLayout()
            input5.addStretch(1)
            input5.addWidget(p_m)
            input5.addWidget(b0)
            input5.addWidget(decimal_point)
            input5.addWidget(cal)
            input5.addStretch(1)
            input5.addStretch(4)
            input5.addStretch(1)

            vbox = QVBoxLayout()
            vbox.addStretch(1)
            vbox.addWidget(label)
            vbox.addStretch(1)
            vbox.addLayout(input1)
            vbox.addLayout(input2)
            vbox.addLayout(input3)
            vbox.addLayout(input4)
            vbox.addLayout(input5)
            simple.setLayout(vbox)

        self.tabs.addTab(simple, '공학용 계산기')


    def statistic(self):
        statistic = QWidget()
        if self.putwithkey == False:

            moduler = QPushButton('%')
            CE = QPushButton('CE')
            C = QPushButton('C')
            backspace = QPushButton('<-')

            b7 = QPushButton('7')
            b8 = QPushButton('8')
            b9 = QPushButton('9')
            b4 = QPushButton('4')
            b5 = QPushButton('5')
            b6 = QPushButton('6')
            b1 = QPushButton('1')
            b2 = QPushButton('2')
            b3 = QPushButton('3')
            p_m = QPushButton('+/-')
            b0 = QPushButton('0')
            decimal_point = QPushButton('.')
            cal = QPushButton('=', statistic)


            

            

        self.tabs.addTab(statistic, '통계학 계산기')


    def graph(self):
        graph = QWidget()
        btn = QPushButton('그래프 작성', graph)
        btn.move(30, 200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.calculate)
        layoutGraph = QVBoxLayout(graph)
        layoutGraph.addWidget(btn)
        self.tabs.addTab(graph, '그래프 작성')


    def option(self):
        option = QWidget()
        btn = QPushButton('그래프 작성', option)
        btn.move(30, 200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.calculate)
        layoutOption = QVBoxLayout(option)
        layoutOption.addWidget(btn)
        self.tabs.addTab(option, '그래프 작성')

    def calculate(self):
        print("0")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = SCP()
   sys.exit(app.exec_())