#Smart Calculation Program
# flake8: noqa
from PyQt5.QtWidgets import QPushButton, QToolTip, QCheckBox, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QSpinBox, QGroupBox, QDialog, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

#UI를 생성하는 SCP_UI 클래스
class SCP_UI(QWidget):

    def __init__(self, STAT, OPTION, STANDARD):
        super().__init__()
        self.STAT = STAT()
        self.OPTION = OPTION
        self.STANDARD = STANDARD()
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
        self.standardTab = QWidget()
        self.statisticTab = QWidget()
        self.graphTab = QWidget()
        self.optionTab = QWidget()
        self.standard(self.standardTab)
        self.statistic(self.statisticTab)
        self.graph(self.graphTab)
        self.option(self.optionTab)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.OPTION.darkmode(self, "light")
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
        
    #기본 계산기 UI
    def standard(self, standard):
        
        #계산기 디스플레이 라벨 생성
        display = QLabel('0', standard)
        display.setAlignment(Qt.AlignLeft)
        font = display.font()
        font.setFamily('Times New Roman')
        font.setBold(True)
        font.setPointSize(20)
        display.setFont(font)
        display.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        #계산기 버튼 구성
        button_size = QSize(110, 75)

        modular = self.create_button('(', button_size, lambda: display.setText(self.STANDARD.add('(')))
        CE = self.create_button(')', button_size, lambda: display.setText(self.STANDARD.add(')')))
        C = self.create_button('AC', button_size, lambda: display.setText(self.STANDARD.clear()))
        backspace = self.create_button('DEL', button_size, lambda: display.setText(self.STANDARD.backspace()))

        fraction = self.create_button('1/x', button_size, lambda: display.setText(self.STANDARD.add('(1/')))
        square = self.create_button('x²', button_size, lambda: display.setText(self.STANDARD.add('²')))
        root = self.create_button('√x', button_size, lambda: display.setText(self.STANDARD.add('√')))
        divide = self.create_button('/', button_size, lambda: display.setText(self.STANDARD.add('/')))

        b7 = self.create_button('7', button_size, lambda: display.setText(self.STANDARD.add('7')))
        b8 = self.create_button('8', button_size, lambda: display.setText(self.STANDARD.add('8')))
        b9 = self.create_button('9', button_size, lambda: display.setText(self.STANDARD.add('9')))
        multi = self.create_button('*', button_size, lambda: display.setText(self.STANDARD.add('*')))

        b4 = self.create_button('4', button_size, lambda: display.setText(self.STANDARD.add('4')))
        b5 = self.create_button('5', button_size, lambda: display.setText(self.STANDARD.add('5')))
        b6 = self.create_button('6', button_size, lambda: display.setText(self.STANDARD.add('6')))
        minus = self.create_button('-', button_size, lambda: display.setText(self.STANDARD.add('-')))

        b1 = self.create_button('1', button_size, lambda: display.setText(self.STANDARD.add('1')))
        b2 = self.create_button('2', button_size, lambda: display.setText(self.STANDARD.add('2')))
        b3 = self.create_button('3', button_size, lambda: display.setText(self.STANDARD.add('3')))
        plus = self.create_button('+', button_size, lambda: display.setText(self.STANDARD.add('+')))

        p_m = self.create_button('ANS', button_size, lambda: display.setText(self.STANDARD.add(self.STANDARD.prev)))
        b0 = self.create_button('0', button_size, lambda: display.setText(self.STANDARD.add('0')))
        decimal_point = self.create_button('.', button_size, lambda: display.setText(self.STANDARD.add('.')))
        cal = self.create_button('=', button_size, lambda: display.setText(self.STANDARD.cal()))

        input1 = QHBoxLayout()
        input1.addWidget(modular)
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
        vbox.addWidget(display)
        vbox.addSpacing(1)
        vbox.addLayout(input1)
        vbox.addLayout(input2)
        vbox.addLayout(input3)
        vbox.addLayout(input4)
        vbox.addLayout(input5)
        vbox.addLayout(input6)
        standard.setLayout(vbox)

        self.tabs.addTab(standard, '공학 계산기')

    #통계학 계산 UI 구성
    def statistic(self, statistic):

        #계산할 값을 선택하는 레이아웃
        txt1 = QLabel('계산할 수치 선택', statistic)
        
        kind = QComboBox(statistic)
        kind.addItem('--------선택--------')
        kind.addItem('1표본 분석')
        kind.addItem('2표본 분석 (독립)')
        kind.addItem('2표본 분석 (대응)')
        kind.activated[str].connect(self.kindActivated) #콤보상자 입력변수1

        select = QHBoxLayout()
        select.addSpacing(1)
        select.addWidget(txt1)
        select.addWidget(kind)
        select.addSpacing(1)

        #구체적으로 할 일을 알려주는 라벨
        explain = QLabel('', statistic)
        statistic.explain = explain

        #표본 입력
        txt2 = QLabel('표본 입력 : ', statistic)
        txt2.setAlignment(Qt.AlignLeft)
        statistic.txt2 = txt2

        #표본 입력창
        data1 = QTextEdit(statistic)
        data1.setAcceptRichText(False)
        statistic.data1 = data1

        data2 = QTextEdit(statistic)
        data2.setAcceptRichText(False)
        statistic.data2 = data2

        #입력 버튼
        btn1 = QPushButton('OK', statistic)
        btn1.clicked.connect(self.cal)
        statistic.btn1 = btn1

        header = QVBoxLayout()
        header.addWidget(txt2)
        header.addWidget(btn1)

        sample = QHBoxLayout()
        sample.addLayout(header)
        sample.addWidget(data1)
        sample.addWidget(data2)

        #결과값 출력창
        solve = QTextEdit(statistic)
        solve.setAcceptRichText(False)
        solve.setReadOnly(True)
        statistic.solve = solve

        #레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addSpacing(3)
        vbox.addLayout(select)
        vbox.addSpacing(3)
        vbox.addWidget(explain)
        vbox.addSpacing(3)
        vbox.addLayout(sample)
        vbox.addSpacing(3)
        vbox.addWidget(solve)
        vbox.addStretch(1)

        explain.setVisible(False)
        txt2.setVisible(False)
        btn1.setVisible(False)
        data1.setVisible(False)
        data2.setVisible(False)
        solve.setVisible(False)
        statistic.setLayout(vbox)
        self.tabs.addTab(statistic, '통계학 계산기')

    #콤보상자 입력변수 1
    def kindActivated(self, text):
        if text=='--------선택--------':
            self.kind = "wait"
        elif text=='1표본 분석':
            self.kind = "1"
        elif text=="2표본 분석 (독립)":
            self.kind = "2ind"
        elif text=="2표본 분석 (대응)":
            self.kind = "2mat"
        self.sTabphaze(self.statisticTab)
        return

    # 통계학 계산기에서 각 단계를 진행할 때마다 레이아웃 갱신
    def sTabphaze(self, Tab):
        if self.kind=="wait":
            Tab.explain.setVisible(False)
            Tab.txt2.setVisible(False)
            Tab.btn1.setVisible(False)
            Tab.data1.setVisible(False)
            Tab.data2.setVisible(False)
            Tab.solve.setVisible(False)
            Tab.explain.setText("")
        elif self.kind=="1":
            Tab.explain.setVisible(True)
            Tab.txt2.setVisible(True)
            Tab.btn1.setVisible(True)
            Tab.data1.setVisible(True)
            Tab.data2.setVisible(False)
            Tab.explain.setText("계산을 위해 표본의 데이터를 입력해주십시오.")
        elif self.kind=="2mat" or self.kind=="2ind":
            Tab.explain.setVisible(True)
            Tab.txt2.setVisible(True)
            Tab.btn1.setVisible(True)
            Tab.data1.setVisible(True)
            Tab.data2.setVisible(True)
            Tab.explain.setText("계산을 위해 표본의 데이터를 입력해주십시오.")
        return


    def cal(self):
        if self.kind=="1":
            A = self.STAT.textsplit(self.statisticTab.data1.toPlainText(), self.kind)
            print(A)
            self.statisticTab.solve.setText(A)
        elif self.kind=="2ind" or self.kind=="2mat":
            A = self.STAT.textsplit(text = self.statisticTab.data1.toPlainText(), kind = self.kind)
            B = self.STAT.textsplit(text = self.statisticTab.data2.toPlainText(), kind = self.kind)
            #표본 A, B, 유의수준이나 가설 등을 받아오는 condition
            condition = self.condition()
            self.statisticTab.solve.setText(self.STAT.indcal(A, B, condition))
        self.statisticTab.solve.setVisible(True)

    
    def condition(self):
        condition = QDialog()
        condition.setWindowTitle('계산할 속성을 선택하세요')

        # 확인 버튼 추가
        button = QPushButton('확인')
        button.clicked.connect(condition.accept)  # 다이얼로그 종료

        #신뢰구간과 가설검정 내용을 입력받는 UI
        groupbox = QGroupBox('신뢰구간과 가설검정')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        #유의수준
        alpha = QTextEdit()

        #모평균, 모비율, 모분산 추정

        vbox = QVBoxLayout()

        groupbox.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox)
        hbox.addWidget(button)
        condition.setLayout(hbox)

        condition.setWindowTitle('Box Layout')
        condition.setGeometry(300, 300, 480, 320)
        result = condition.exec_()  # 다이얼로그를 모달로 실행

        if result == QDialog.Accepted:
            if checkbox.isChecked():
                print('사용자가 옵션을 선택했습니다.')
            else:
                print('사용자가 옵션을 선택하지 않았습니다.')
        else:
            print('사용자가 창을 닫았습니다.')

        return 0


    def graph(self, graph):
        btn = QPushButton('그래프 작성', graph)
        btn.move(30, 200)
        btn.resize(btn.sizeHint())
        #btn.clicked.connect(calculate)
        layoutGraph = QVBoxLayout(graph)
        layoutGraph.addWidget(btn)
        graph.setLayout(layoutGraph)
        self.tabs.addTab(graph, ' 그래프 작성 ')
        return


    def option(self, option):
        self.tabs.addTab(option, '       옵션      ')

        #다크모드 UI
        darkmode= QComboBox(option)
        darkmode.addItem('라이트 모드')
        darkmode.addItem('다크 모드')
        option.darkmode = darkmode
        darkmode.activated[str].connect(self.darkmode)

        #항상 맨 앞에 창 띄우기 UI
        cb = QCheckBox('창을 항상 화면의 맨 앞으로', option)
        cb.clicked.connect(lambda : self.OPTION.ontop(self, cb.isChecked()))
        option.cb = cb

        #출력하는 소수점 자릿수 설정
        prime = QSpinBox()
        prime.setRange(0, 30)
        prime.setValue(2)
        prime.valueChanged.connect(lambda : setattr(self.STAT, 'form', self.OPTION.primenumber(prime.value())))
        prime.valueChanged.connect(lambda : setattr(self.STANDARD, 'form', self.OPTION.primenumber(prime.value())))
        option.prime = prime
        
        label = QLabel('공학용/통계학 계산기 출력값의 소수점 자리수를 설정합니다.')

        # 소표본일 때 자유도 n-1 값 사용하지 않음
        cb2 = QCheckBox('소표본일 때 자유도 n-1 값 사용하지 않음', option)
        cb2.clicked.connect(lambda : setattr(self.STAT, 'small', self.OPTION.small(self, cb2.isChecked())))
        option.cb2 = cb2

        layoutOption = QVBoxLayout(option)
        layoutOption.addWidget(darkmode)
        layoutOption.addWidget(cb)

        primelayout = QHBoxLayout()
        primelayout.addWidget(label)
        primelayout.addWidget(prime)

        layoutOption.addLayout(primelayout)
        layoutOption.addWidget(cb2)
        layoutOption.addStretch(1)
        return

    #옵션의 라이트, 다크 모드가 변경되면 실행
    def darkmode(self, text):
        if text=='라이트 모드':
            self.OPTION.darkmode(self, "light")
        elif text=="다크 모드":
            self.OPTION.darkmode(self, "dark")