#Smart Calculation Program
import sys, math, re
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, qApp, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

from SCP_STAT import *

#UI를 생성하는 SCP_UI 클래스
class SCP_UI(QWidget):

    def __init__(self, STAT):
        super().__init__()
        self.STAT = STAT
        self.initUI()
        

    #UI 구성
    def initUI(self):
        self.kind=None
        self.txt = "error"
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('SCP')
        self.setWindowIcon(QIcon("SCP.png"))
        self.resize(537, 750)
        self.center()
        #각 탭 생성
        self.tabs = QTabWidget()
        self.simpleTab = QWidget()
        self.statisticTab = QWidget()
        self.graphTab = QWidget()
        self.optionTab = QWidget()
        self.simple(self.simpleTab)
        self.statistic(self.statisticTab)
        self.graph(self.graphTab)
        self.option(self.optionTab)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)
        self.show()



    #중앙 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #버튼 생성 함수
    def create_button(self, text, size, callback=None):
        button = QPushButton(text)
        button.setFixedSize(size)
        if callback:
            button.clicked.connect(callback)
        return button

    #라벨 생성 함수
    def create_label(self, text, alignment=Qt.AlignLeft, font='Times New Roman', Bold=True, color="black", bgcolor="#87CEFA", border="dashed"):
        label = QLabel(text)
        label.setAlignment(alignment)
        lfont = label.font()
        lfont.setFamily(font)
        lfont.setBold(Bold)
        label.setFont(lfont)
        label.setStyleSheet(f"color: {color};"
                            f"background-color: {bgcolor};"
                            f"border-style: {border};")
        return label
        
    #기본 계산기 UI
    def simple(self, simple):

        label = QLabel('', simple)
        label.setAlignment(Qt.AlignLeft)
        font = label.font()
        font.setFamily('Times New Roman')
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        #계산기 버튼 구성
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
        cal = QPushButton('=')
        cal.clicked.connect(calculate)

        button_size = QSize(110, 75)  # 원하는 크기로 수정
        moduler.setFixedSize(button_size)
        CE.setFixedSize(button_size)
        C.setFixedSize(button_size)
        backspace.setFixedSize(button_size)
        fraction.setFixedSize(button_size)
        square.setFixedSize(button_size)
        root.setFixedSize(button_size)
        divide.setFixedSize(button_size)
        b7.setFixedSize(button_size)
        b8.setFixedSize(button_size)
        b9.setFixedSize(button_size)
        multi.setFixedSize(button_size)
        b4.setFixedSize(button_size)
        b5.setFixedSize(button_size)
        b6.setFixedSize(button_size)
        minus.setFixedSize(button_size)
        b1.setFixedSize(button_size)
        b2.setFixedSize(button_size)
        b3.setFixedSize(button_size)
        plus.setFixedSize(button_size)
        p_m.setFixedSize(button_size)
        b0.setFixedSize(button_size)
        decimal_point.setFixedSize(button_size)
        cal.setFixedSize(button_size)

        input1 = QHBoxLayout()
        input1.addWidget(moduler)
        input1.addWidget(CE)
        input1.addWidget(C)
        input1.addWidget(backspace)
        input1.addStretch(1)
        input1.addStretch(4)
        input1.addStretch(1)
        
        input2 = QHBoxLayout()
        input2.addWidget(fraction)
        input2.addWidget(square)
        input2.addWidget(root)
        input2.addWidget(divide)
        input2.addStretch(1)
        input2.addStretch(4)
        input2.addStretch(1)

        input3 = QHBoxLayout()
        input3.addWidget(b7)
        input3.addWidget(b8)
        input3.addWidget(b9)
        input3.addWidget(multi)
        input3.addStretch(1)
        input3.addStretch(4)
        input3.addStretch(1)

        input4 = QHBoxLayout()
        input4.addWidget(b4)
        input4.addWidget(b5)
        input4.addWidget(b6)
        input4.addWidget(minus)
        input4.addStretch(1)
        input4.addStretch(4)
        input4.addStretch(1)

        input5 = QHBoxLayout()
        input5.addWidget(b1)
        input5.addWidget(b2)
        input5.addWidget(b3)
        input5.addWidget(plus)
        input5.addStretch(1)
        input5.addStretch(4)
        input5.addStretch(1)

        input6 = QHBoxLayout()
        input6.addWidget(p_m)
        input6.addWidget(b0)
        input6.addWidget(decimal_point)
        input6.addWidget(cal)
        input6.addStretch(1)
        input6.addStretch(4)
        input6.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addSpacing(3)
        vbox.addWidget(label)
        vbox.addSpacing(1)
        vbox.addLayout(input1)
        vbox.addLayout(input2)
        vbox.addLayout(input3)
        vbox.addLayout(input4)
        vbox.addLayout(input5)
        vbox.addLayout(input6)
        simple.setLayout(vbox)

        self.tabs.addTab(simple, '공학용 계산기')

    #통계학 계산 UI 구성
    def statistic(self, statistic):

        txt1 = self.create_label('계산할 수치 선택', color="black", bgcolor="white", border="None")
        txt1.setToolTip('구할 수치를 알고 있다면 점선 위의 수치를,\n수치에서 알 수 있는 값을 알아보려면 점선 아래에서 대응하는 수치를 선택해주세요.')

        kind = QComboBox(statistic)
        kind.setToolTip('구할 수치를 알고 있다면 점선 위의 수치를,\n수치에서 알 수 있는 값을 알아보려면 점선 아래에서 대응하는 수치를 선택해주세요.')
        kind.addItem('--------선택--------')
        kind.addItem('평균, 분산, 표준편차')
        kind.addItem('중앙값, 표본범위')

        kind.activated[str].connect(self.kindonActivated) #콤보상자 입력변수1

        select = QHBoxLayout()
        select.addSpacing(1)
        select.addWidget(txt1)
        select.addWidget(kind)
        select.addSpacing(1)

        explain = QLabel('', statistic)
        statistic.explain = explain


        txt2 = QLabel('표본 입력 : ', statistic)
        txt2.setToolTip('구할 수치를 알고 있다면 점선 위의 수치를,\n수치에서 알 수 있는 값을 알아보려면 점선 아래에서 대응하는 수치를 선택해주세요.')
        txt2.setAlignment(Qt.AlignLeft)
        font = txt1.font()
        font.setFamily('Times New Roman')
        font.setBold(True)
        txt2.setFont(font)
        statistic.txt2 = txt2

        data = QTextEdit(statistic)
        data.setToolTip('')
        data.setAcceptRichText(False)
        data.textChanged.connect(lambda : setattr(self, 'txt', self.statisticTab.data.toPlainText()))
        statistic.data = data

        btn1 = QPushButton('OK', statistic)
        btn1.clicked.connect(lambda : self.STAT.textsplit(self.txt, self.kind, self.statisticTab))
        statistic.btn1 = btn1

        header = QVBoxLayout()
        header.addWidget(txt2)
        header.addWidget(btn1)

        specimen = QHBoxLayout()
        specimen.addLayout(header)
        specimen.addWidget(data)

        solve = QTextEdit(statistic)
        solve.setAcceptRichText(False)
        solve.setReadOnly(True)
        data.textChanged.connect(lambda : setattr(self, 'txt', self.statisticTab.data.toPlainText()))
        statistic.solve = solve

        vbox = QVBoxLayout()
        vbox.addSpacing(3)
        vbox.addLayout(select)
        vbox.addSpacing(3)
        vbox.addWidget(explain)
        vbox.addSpacing(3)
        vbox.addLayout(specimen)
        vbox.addSpacing(3)
        vbox.addWidget(solve)
        vbox.addStretch(1)


        txt2.setVisible(False)
        btn1.setVisible(False)
        data.setVisible(False)
        solve.setVisible(False)
        statistic.setLayout(vbox)
        self.tabs.addTab(statistic, '통계학 계산기')



    def graph(self, graph):
        btn = QPushButton('그래프 작성', graph)
        btn.move(30, 200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(calculate)
        layoutGraph = QVBoxLayout(graph)
        layoutGraph.addWidget(btn)
        graph.setLayout(layoutGraph)
        self.tabs.addTab(graph, '그래프 작성')



    def option(self, option):
        #소수점 자리 수
        self.tabs.addTab(option, '옵션')


    # 통계학 계산기에서 각 단계를 진행할 때마다 레이아웃 갱신
    def sTabphaze(self, Tab):
        if self.kind=="wait":
            Tab.txt2.setVisible(False)
            Tab.btn1.setVisible(False)
            Tab.data.setVisible(False)
            Tab.solve.setVisible(False)
            Tab.explain.setText("")
        elif self.kind=="avg" or self.kind=="middle":
            Tab.txt2.setVisible(True)
            Tab.btn1.setVisible(True)
            Tab.data.setVisible(True)
            Tab.explain.setText("계산을 위해 표본의 데이터를 입력해주십시오.")


    #콤보상자 입력변수
    def kindonActivated(self, text):
        if text=='--------선택--------':
            self.kind = "wait"
        elif text=='평균, 분산, 표준편차':
            self.kind = "avg"
        elif text=="중앙값, 표본범위":
            self.kind = "middle"
        self.sTabphaze(self.statisticTab)


    #textedit의 데이터가 변경되면 txt에 저장
    def text_changed(self):
        self.txt = self.statisticTab.data.toPlainText()

    
    


def calculate(self):
    print("0")

# def Scalculate(list):
#     if ex.kind == "avg":
#         print(list)
#         avg = sum(list)/len(list)
#         sumall = 0
#         for i in list:
#             sumall += (i-avg)**2
#         var = sumall/len(list)
#         std = math.sqrt(var)
#         ex.statisticTab.solve.setVisible(True)
#         ex.statisticTab.solve.setText(f"평균 : {avg},\n분산 : {var},\n표준편차 : {std}")
#     elif ex.kind == "middle":
#         L = sorted(list)
#         q1_index = int(0.25 * (len(L)+ 1))
#         q2_index = int(0.5 * (len(L) + 1))
#         q3_index = int(0.75 * (len(L) + 1))

#         q1 = L[q1_index - 1] if len(L) % 4 == 0 else (L[q1_index - 1] + L[q1_index]) / 2
#         q2 = L[q2_index - 1] if len(L) % 4 == 0 else (L[q2_index - 1] + L[q2_index]) / 2
#         q3 = L[q3_index - 1] if len(L) % 4 == 0 else (L[q3_index - 1] + L[q3_index]) / 2

#         srange = max(L)-min(L)
#         iqr = q3 - q1
#         ex.statisticTab.solve.setVisible(True)
#         ex.statisticTab.solve.setText(f"제1사분위수 : {q1},\n제2사분위수(중앙값) : {q2},\n제3사분위수 : {q3},\n표본범위 : {srange},\n표본사분위범위 : {iqr}")


