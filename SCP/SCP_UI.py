#Smart Calculation Program
# flake8: noqa
from PyQt5.QtWidgets import QPushButton, QToolTip, QCheckBox, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextEdit, QSpinBox, QGroupBox, QDialog, QLineEdit, QRadioButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize



# 통계학 계산 시의 옵션 레이아웃 클래스
class OptionDialog(QDialog):
    def __init__(self, kind):
        super(OptionDialog, self).__init__()
        self.initUI()
        if kind=='1':
            self.rbtn5.setVisible(False)
            self.rbtn6.setVisible(False)
        elif kind=='2':
            self.rbtn5.setVisible(True)
            self.rbtn6.setVisible(True)
    
    def setcheckbox(self, name, checked=False):
        checkbox = QCheckBox(name)
        checkbox.setChecked(checked)
        return checkbox

    def initUI(self):
        # 그룹박스 생성
        groupBox1 = QGroupBox()

        # 체크박스 생성
        self.checkbox = self.setcheckbox('표본 수', True)
        self.checkbox1 = self.setcheckbox('평균', True)
        self.checkbox2 = self.setcheckbox('분산', True)
        self.checkbox3 = self.setcheckbox('표준편차', True)
        self.checkbox4 = self.setcheckbox('중앙값')
        self.checkbox5 = self.setcheckbox('사분위수')
        self.checkbox6 = self.setcheckbox('표본범위')

        # 왼쪽 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.checkbox)
        vbox.addWidget(self.checkbox1)
        vbox.addWidget(self.checkbox2)
        vbox.addWidget(self.checkbox3)
        vbox.addWidget(self.checkbox4)
        vbox.addWidget(self.checkbox5)
        vbox.addWidget(self.checkbox6)
        groupBox1.setLayout(vbox)


        # 그룹박스 생성
        self.groupBox2 = QGroupBox('정규분포를 따르는 표본')
        self.groupBox2.setCheckable(True)
        self.groupBox2.setChecked(True)
        self.groupBox2.setEnabled(False)

        # 체크박스 생성
        self.checkbox7 = self.setcheckbox('모평균 신뢰구간', True)
        self.checkbox8 = self.setcheckbox('모분산 신뢰구간')
        self.checkbox9 = self.setcheckbox('모표준편차 신뢰구간')


        # 신뢰계수 입력을 위한 버튼 생성
        self.rbtn1 = QRadioButton('0.1', self)
        self.rbtn2 = QRadioButton('0.05', self)
        self.rbtn3 = QRadioButton('0.025', self)
        self.rbtn4 = QRadioButton('사용자 지정', self)
        self.qle = QLineEdit(self)
        self.qle.setEnabled(False)

        # 독립, 대응표본 입력을 위한 버튼
        self.rbtn5 = QRadioButton('독립표본', self)
        self.rbtn6 = QRadioButton('대응표본', self)

        # 신뢰계수 입력 레이아웃
        hbox = QHBoxLayout()
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.rbtn1)
        self.button_group.addButton(self.rbtn2)
        self.button_group.addButton(self.rbtn3)
        self.button_group.addButton(self.rbtn4)
        hbox.addWidget(self.rbtn1)
        hbox.addWidget(self.rbtn2)
        hbox.addWidget(self.rbtn3)
        hbox.addWidget(self.rbtn4)
        hbox.addWidget(self.qle)
        self.button_group.buttonClicked.connect(lambda: (self.groupBox2.setEnabled(True), self.qle.setEnabled(self.rbtn4.isChecked())))

        # 독립, 대응표본 입력 레이아웃
        self.hbox2 = QHBoxLayout()
        self.button_group2 = QButtonGroup(self)
        self.button_group2.addButton(self.rbtn5)
        self.button_group2.addButton(self.rbtn6)
        self.hbox2.addWidget(self.rbtn5)
        self.hbox2.addWidget(self.rbtn6)

        #오른쪽 레이아웃 설정
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.checkbox7)
        vbox2.addWidget(self.checkbox8)
        vbox2.addWidget(self.checkbox9)
        self.groupBox2.setLayout(vbox2)
        rightlayout = QVBoxLayout()
        rightlayout.addLayout(hbox)
        rightlayout.addLayout(self.hbox2)
        rightlayout.addWidget(self.groupBox2)
        
        # 다이얼로그 버튼
        okButton = QPushButton('확인')
        okButton.clicked.connect(self.accept)

        # 전체 레이아웃 설정
        sublayout = QHBoxLayout()
        sublayout.addWidget(groupBox1)
        sublayout.addLayout(rightlayout)
        
        layout = QVBoxLayout()
        layout.addLayout(sublayout)
        layout.addWidget(okButton)

        # 다이얼로그 윈도우 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('옵션 설정')

    def getCheckboxStates(self):
        # 체크박스 상태 반환
        if self.rbtn1.isChecked():
            a = 0.1
        elif self.rbtn2.isChecked():
            a = 0.05
        elif self.rbtn3.isChecked():
            a = 0.025
        elif self.rbtn4.isChecked():
            a = float(self.qle.text())
        else:
            a = -1

        # 독립, 대응표본 반환
        if self.rbtn5.isChecked():
            mode = '독립'
        elif self.rbtn6.isChecked():
            mode = '대응'
        else:
            mode = None

        return {
            '표본 수': self.checkbox.isChecked(),
            '평균': self.checkbox1.isChecked(),
            '분산': self.checkbox2.isChecked(),
            '표준편차': self.checkbox3.isChecked(),
            '중앙값': self.checkbox4.isChecked(),
            '사분위수': self.checkbox5.isChecked(),
            '표본범위': self.checkbox6.isChecked(),
            'a' : a,
            '표본' : mode,
            '정규분포': self.groupBox2.isChecked(),
            '모평균 신뢰구간' : self.checkbox7.isChecked(),
            '모분산 신뢰구간' : self.checkbox8.isChecked(),
            '모표준편차 신뢰구간' : self.checkbox9.isChecked()
        }

# 확률 문제 계산 시의 옵션 레이아웃 클래스
class OptionDialog2(QDialog):
    def __init__(self):
        super(OptionDialog2, self).__init__()
        self.initUI()

    def initUI(self):
        # 확률 입력 시 가독성을 위한 그룹박스 생성
        self.groupBox1 = QGroupBox() # 단일
        self.groupBox2 = QGroupBox() # 교집합
        self.groupBox3 = QGroupBox() # 합집합
        self.groupBox4 = QGroupBox() # 조건부 확률

        # 확률 입력을 위한 라인 생성
        # 단일 확률
        self.text11 = QLabel('P(A)  ', self)
        self.line11 = QLineEdit("", self)
        self.text12 = QLabel('P(B)  ', self)
        self.line12 = QLineEdit("", self)
        self.text13 = QLabel('P(Ac)', self)
        self.line13 = QLineEdit("", self)
        self.text14 = QLabel('P(Bc)', self)
        self.line14 = QLineEdit("", self)

        # 교집합 확률
        self.text21 = QLabel('P(AxB) ', self)
        self.line21 = QLineEdit("", self)
        self.text22 = QLabel('P(AcxB) ', self)
        self.line22 = QLineEdit("", self)
        self.text23 = QLabel('P(AxBc)', self)
        self.line23 = QLineEdit("", self)
        self.text24 = QLabel('P(AcxBc)', self)
        self.line24 = QLineEdit("", self)

        # 합집합 확률
        self.text31 = QLabel('P(AUB) ', self)
        self.line31 = QLineEdit("", self)
        self.text32 = QLabel('P(AcUB) ', self)
        self.line32 = QLineEdit("", self)
        self.text33 = QLabel('P(AUBc)', self)
        self.line33 = QLineEdit("", self)
        self.text34 = QLabel('P(AcUBc)', self)
        self.line34 = QLineEdit("", self)

        # 조건부 확률
        self.text41 = QLabel('P(A|B) ', self)
        self.line41 = QLineEdit("", self)
        self.text42 = QLabel('P(Ac|B) ', self)
        self.line42 = QLineEdit("", self)
        self.text43 = QLabel('P(A|Bc)', self)
        self.line43 = QLineEdit("", self)
        self.text44 = QLabel('P(Ac|Bc)', self)
        self.line44 = QLineEdit("", self)
        self.text45 = QLabel('P(B|A) ', self)
        self.line45 = QLineEdit("", self)
        self.text46 = QLabel('P(B|Ac) ', self)
        self.line46 = QLineEdit("", self)
        self.text47 = QLabel('P(Bc|A)', self)
        self.line47 = QLineEdit("", self)
        self.text48 = QLabel('P(Bc|Ac)', self)
        self.line48 = QLineEdit("", self)

        # 다이얼로그 버튼
        okButton = QPushButton('확인')
        okButton.clicked.connect(self.accept)

        # 목표 입력을 위한 라벨 생성
        self.text = QLabel('찾으려는 목표를 입력 \nex) AxB(교집합), Ac|B 등', self)
        self.line = QLineEdit("", self)

        # 전체 레이아웃 설정
        l11 = QHBoxLayout()
        l11.addWidget(self.text11)
        l11.addWidget(self.line11)

        l12 = QHBoxLayout()
        l12.addWidget(self.text12)
        l12.addWidget(self.line12)

        l13 = QHBoxLayout()
        l13.addWidget(self.text13)
        l13.addWidget(self.line13)

        l14 = QHBoxLayout()
        l14.addWidget(self.text14)
        l14.addWidget(self.line14)

        l21 = QHBoxLayout()
        l21.addWidget(self.text21)
        l21.addWidget(self.line21)

        l22 = QHBoxLayout()
        l22.addWidget(self.text22)
        l22.addWidget(self.line22)

        l23 = QHBoxLayout()
        l23.addWidget(self.text23)
        l23.addWidget(self.line23)

        l24 = QHBoxLayout()
        l24.addWidget(self.text24)
        l24.addWidget(self.line24)

        l31 = QHBoxLayout()
        l31.addWidget(self.text31)
        l31.addWidget(self.line31)

        l32 = QHBoxLayout()
        l32.addWidget(self.text32)
        l32.addWidget(self.line32)

        l33 = QHBoxLayout()
        l33.addWidget(self.text33)
        l33.addWidget(self.line33)

        l34 = QHBoxLayout()
        l34.addWidget(self.text34)
        l34.addWidget(self.line34)

        l41 = QHBoxLayout()
        l41.addWidget(self.text41)
        l41.addWidget(self.line41)

        l42 = QHBoxLayout()
        l42.addWidget(self.text42)
        l42.addWidget(self.line42)

        l43 = QHBoxLayout()
        l43.addWidget(self.text43)
        l43.addWidget(self.line43)

        l44 = QHBoxLayout()
        l44.addWidget(self.text44)
        l44.addWidget(self.line44)

        l45 = QHBoxLayout()
        l45.addWidget(self.text45)
        l45.addWidget(self.line45)

        l46 = QHBoxLayout()
        l46.addWidget(self.text46)
        l46.addWidget(self.line46)

        l47 = QHBoxLayout()
        l47.addWidget(self.text47)
        l47.addWidget(self.line47)

        l48 = QHBoxLayout()
        l48.addWidget(self.text48)
        l48.addWidget(self.line48)

        #생성한 레이아웃을 그룹박스에 입력
        vbox1 = QVBoxLayout()
        vbox1.addLayout(l11)
        vbox1.addLayout(l12)
        vbox1.addLayout(l13)
        vbox1.addLayout(l14)
        self.groupBox1.setLayout(vbox1)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(l21)
        vbox2.addLayout(l22)
        vbox2.addLayout(l23)
        vbox2.addLayout(l24)
        self.groupBox2.setLayout(vbox2)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.groupBox1)
        layout1.addWidget(self.groupBox2)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(l31)
        vbox3.addLayout(l32)
        vbox3.addLayout(l33)
        vbox3.addLayout(l34)
        self.groupBox3.setLayout(vbox3)

        vbox4 = QVBoxLayout()
        vbox4.addLayout(l41)
        vbox4.addLayout(l42)
        vbox4.addLayout(l43)
        vbox4.addLayout(l44)
        vbox4.addLayout(l45)
        vbox4.addLayout(l46)
        vbox4.addLayout(l47)
        vbox4.addLayout(l48)
        self.groupBox4.setLayout(vbox4)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.groupBox1)
        layout1.addWidget(self.groupBox2)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.groupBox3)
        layout2.addWidget(self.groupBox4)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addWidget(self.text)
        layout.addWidget(self.line)
        layout.addWidget(okButton)

        # 다이얼로그 윈도우 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('확률 입력')

    def getLineStates(self):
        # 확률 반환
        result = {}
        if self.line11.text()!="":
            result[self.text11.text()] = self.line11.text()
        if self.line12.text()!="":
            result[self.text12.text()] = self.line12.text()
        if self.line13.text()!="":
            result[self.text13.text()] = self.line13.text()
        if self.line14.text()!="":
            result[self.text14.text()] = self.line14.text()

        if self.line21.text()!="":
            result[self.text21.text()] = self.line21.text()
        if self.line22.text()!="":
            result[self.text22.text()] = self.line22.text()
        if self.line23.text()!="":
            result[self.text23.text()] = self.line23.text()
        if self.line24.text()!="":
            result[self.text24.text()] = self.line24.text()

        if self.line31.text()!="":
            result[self.text31.text()] = self.line31.text()
        if self.line32.text()!="":
            result[self.text32.text()] = self.line32.text()
        if self.line33.text()!="":
            result[self.text33.text()] = self.line33.text()
        if self.line34.text()!="":
            result[self.text34.text()] = self.line34.text()

        if self.line41.text()!="":
            result[self.text41.text()] = self.line41.text()
        if self.line42.text()!="":
            result[self.text42.text()] = self.line42.text()
        if self.line43.text()!="":
            result[self.text43.text()] = self.line43.text()
        if self.line44.text()!="":
            result[self.text44.text()] = self.line44.text()
        if self.line45.text()!="":
            result[self.text45.text()] = self.line45.text()
        if self.line46.text()!="":
            result[self.text46.text()] = self.line46.text()
        if self.line47.text()!="":
            result[self.text47.text()] = self.line47.text()
        if self.line48.text()!="":
            result[self.text48.text()] = self.line48.text()

        if self.line.text()=="":
            text = "목표를 알 수 없습니다."
        else:
            text = self.line.text()
            if "|" in text:
                text = text.replace("|", "")
        print(text, result)
        return text, result

#UI를 생성하는 SCP_UI 클래스
class SCP_UI(QWidget):

    def __init__(self, STAT, OPTION, STANDARD, SOLVE):
        super().__init__()
        self.STAT = STAT()
        self.OPTION = OPTION
        self.STANDARD = STANDARD()
        self.SOLVE = SOLVE()
        self.initUI()

    #UI 구성
    def initUI(self):
        self.kind=None
        self.kind2=None
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
        self.solveTab = QWidget()
        self.optionTab = QWidget()
        self.standard(self.standardTab)
        self.statistic(self.statisticTab)
        self.solve(self.solveTab)
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
        kind.addItem('2표본 분석')
        kind.activated[str].connect(self.kindActivated) #콤보상자 입력변수 1

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
        resolve = QTextEdit(statistic)
        resolve.setAcceptRichText(False)
        resolve.setReadOnly(True)
        statistic.resolve = resolve

        #레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addSpacing(3)
        vbox.addLayout(select)
        vbox.addSpacing(3)
        vbox.addWidget(explain)
        vbox.addSpacing(3)
        vbox.addLayout(sample)
        vbox.addSpacing(3)
        vbox.addWidget(resolve)
        vbox.addStretch(1)

        explain.setVisible(False)
        txt2.setVisible(False)
        btn1.setVisible(False)
        data1.setVisible(False)
        data2.setVisible(False)
        resolve.setVisible(False)
        statistic.setLayout(vbox)
        self.tabs.addTab(statistic, '통계학 계산기')

    #콤보상자 입력변수 1
    def kindActivated(self, text):
        if text=='--------선택--------':
            self.kind = "wait"
        elif text=='1표본 분석':
            self.kind = "1"
        elif text=="2표본 분석":
            self.kind = "2"
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
            Tab.resolve.setVisible(False)
            Tab.explain.setText("")
        else:
            Tab.explain.setVisible(True)
            Tab.txt2.setVisible(True)
            Tab.btn1.setVisible(True)
            Tab.data1.setVisible(True)
            Tab.explain.setText("계산을 위해 표본의 데이터를 입력해주십시오.")
            if self.kind=="1":
                Tab.data2.setVisible(False)
            elif self.kind=="2":
                Tab.data2.setVisible(True)
        return

    #확인 버튼을 눌렀을 때 실제로 계산을 진행하는 단계
    def cal(self):
        optionDialog = OptionDialog(self.kind)
        result = optionDialog.exec_()
        if result == QDialog.Accepted:
            condition = optionDialog.getCheckboxStates()
            if self.kind=="1":
                A = self.STAT.cal(self.statisticTab.data1.toPlainText(), condition, "표본")
                self.statisticTab.resolve.setText(A[1])
            elif self.kind=="2":
                A = self.STAT.cal(self.statisticTab.data1.toPlainText(), condition, "A")
                B = self.STAT.cal(self.statisticTab.data2.toPlainText(), condition, "B")
                #표본 A, B, 유의수준이나 가설 등을 받아오는 condition
                self.statisticTab.resolve.setText(self.STAT.secondcal(A, B, condition))
            self.statisticTab.resolve.setVisible(True)

    # 문제 풀이 도우미
    def solve(self, solve):
        txt = QLabel('계산할 문제 선택', solve)

        kind= QComboBox(solve)
        kind.addItem('--------선택--------')
        kind.addItem('확률 문제 {P(A) 등}')
        kind.addItem('확률변수와 기댓값 문제')
        kind.activated[str].connect(self.kindActivated2) #콤보상자 입력변수

        select = QHBoxLayout()
        select.addSpacing(1)
        select.addWidget(txt)
        select.addWidget(kind)
        select.addSpacing(1)

        #구체적으로 할 일을 알려주는 라벨
        explain = QLabel('', solve)
        solve.explain = explain

        #결과 입력
        txt1 = QLabel('버튼을 눌러\n값 변경', solve)
        txt1.setAlignment(Qt.AlignLeft)
        solve.txt1 = txt1

        #입력 버튼
        btn1 = QPushButton('값 변경', solve)
        btn1.clicked.connect(self.cal2)
        solve.btn1 = btn1

        header = QHBoxLayout()
        header.addWidget(txt1)
        header.addWidget(btn1)


        #결과 입력
        txt21 = QLabel('성공 확률 : ', solve)
        txt21.setAlignment(Qt.AlignLeft)
        solve.txt21 = txt21
        line21 = QLineEdit('', solve)
        solve.line21 = line21

        txt22 = QLabel('시행 횟수 : ', solve)
        txt22.setAlignment(Qt.AlignLeft)
        solve.txt22 = txt22
        line22 = QLineEdit('', solve)
        solve.line22 = line22

        spin21 = QSpinBox(solve)
        spin21.setRange(0, 2**31-1)
        spin21.setValue(0)
        solve.spin21 = spin21
        txt23 = QLabel('번 이상, ', solve)
        txt23.setAlignment(Qt.AlignLeft)
        solve.txt23 = txt23
        
        spin22 = QSpinBox(solve)
        spin22.setRange(-1, 2**31-1)
        spin22.setValue(-1)
        solve.spin22 = spin22
        txt24 = QLabel('번 이하로 성공할 확률 (-1이면 최대)', solve)
        txt24.setAlignment(Qt.AlignLeft)
        solve.txt24 = txt24
        
        btn2 = QPushButton('결과 출력')
        btn2.clicked.connect(self.cal2)
        solve.btn2 = btn2

        checkbox2 = QCheckBox('확률 상세보기')
        solve.checkbox2 = checkbox2

        header21 = QHBoxLayout()
        header21.addWidget(txt21)
        header21.addWidget(line21)
        header21.addWidget(txt22)
        header21.addWidget(line22)

        header22 = QHBoxLayout()
        header22.addWidget(spin21)
        header22.addWidget(txt23)
        header22.addWidget(spin22)
        header22.addWidget(txt24)

        header23 = QHBoxLayout()
        header23.addWidget(checkbox2)
        header23.addSpacing(1)
        header23.addWidget(btn2)

        #결과 출력창
        data = QTextEdit(solve)
        data.setAcceptRichText(False)
        data.setReadOnly(True)
        solve.data = data

        #레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addSpacing(3)
        vbox.addLayout(select)
        vbox.addSpacing(3)
        vbox.addWidget(explain)
        vbox.addSpacing(3)
        vbox.addLayout(header)
        vbox.addLayout(header21)
        vbox.addLayout(header22)
        vbox.addLayout(header23)
        vbox.addWidget(data)
        vbox.addStretch(1)

        explain.setVisible(False)
        txt1.setVisible(False)
        btn1.setVisible(False)
        txt21.setVisible(False)
        line21.setVisible(False)
        txt22.setVisible(False)
        line22.setVisible(False)
        txt23.setVisible(False)
        spin21.setVisible(False)
        txt24.setVisible(False)
        spin22.setVisible(False)
        btn2.setVisible(False)
        checkbox2.setVisible(False)
        data.setVisible(False)
        solve.setLayout(vbox)
        self.tabs.addTab(solve, '문제 풀이 도우미')
        

    #콤보상자 입력변수 2
    def kindActivated2(self, text):
        if text=='--------선택--------':
            self.kind2 = "wait"
        elif text=='확률 문제 {P(A) 등}':
            self.kind2 = "prob"
        elif text=='확률변수와 기댓값 문제':
            self.kind2 = "rand"
        self.sTabphaze2(self.solveTab)
        return

    # 문제 도우미에서 각 단계를 진행할 때마다 레이아웃 갱신
    def sTabphaze2(self, Tab):
        if self.kind2=="wait":
            Tab.explain.setVisible(False)
            Tab.txt1.setVisible(False)
            Tab.btn1.setVisible(False)
            Tab.txt21.setVisible(False)
            Tab.line21.setVisible(False)
            Tab.txt22.setVisible(False)
            Tab.line22.setVisible(False)
            Tab.txt23.setVisible(False)
            Tab.spin21.setVisible(False)
            Tab.txt24.setVisible(False)
            Tab.spin22.setVisible(False)
            Tab.btn2.setVisible(False)
            Tab.checkbox2.setVisible(False)
            Tab.data.setVisible(False)
            Tab.explain.setText("")
        elif self.kind2=="prob":
            Tab.explain.setVisible(True)
            Tab.txt1.setVisible(True)
            Tab.btn1.setVisible(True)
            Tab.txt21.setVisible(False)
            Tab.line21.setVisible(False)
            Tab.txt22.setVisible(False)
            Tab.line22.setVisible(False)
            Tab.txt23.setVisible(False)
            Tab.spin21.setVisible(False)
            Tab.txt24.setVisible(False)
            Tab.spin22.setVisible(False)
            Tab.btn2.setVisible(False)
            Tab.checkbox2.setVisible(False)
            Tab.explain.setText("계산을 위해 아래 버튼을 눌러 확률 값을 입력해주십시오.")
        elif self.kind2=="rand":
            Tab.explain.setVisible(True)
            Tab.txt1.setVisible(False)
            Tab.btn1.setVisible(False)
            Tab.txt21.setVisible(True)
            Tab.line21.setVisible(True)
            Tab.txt22.setVisible(True)
            Tab.line22.setVisible(True)
            Tab.txt23.setVisible(True)
            Tab.spin21.setVisible(True)
            Tab.txt24.setVisible(True)
            Tab.spin22.setVisible(True)
            Tab.btn2.setVisible(True)
            Tab.checkbox2.setVisible(True)
            Tab.explain.setText("계산을 위해 조건을 입력해주십시오.")
        return

    # 확인 버튼을 눌렀을 때 실제로 계산을 진행하는 단계
    def cal2(self):
        if self.kind2=="prob":
            optionDialog = OptionDialog2()
            result = optionDialog.exec_()
            if result == QDialog.Accepted:
                goal, data = optionDialog.getLineStates()
                input={}
                for key, value in data.items():
                    # key에서 P()꼴을 제거
                    # 분수 입력이나 연산에도 대응 가능하도록 공학용 계산기의 함수 이용
                    input[key.replace("P(", "").replace(")", "").strip()]=self.STANDARD.cal4SOLVE(value)
                # 주어진 확률 값을 받아오는 딕셔너리 data
                self.solveTab.data.setText(self.SOLVE.Pprocess(goal, input))
                self.solveTab.data.setVisible(True)
        elif self.kind2=="rand":
            try:
                p = self.STANDARD.cal4SOLVE(self.solveTab.line21.text())
                n = int(self.STANDARD.cal4SOLVE(self.solveTab.line22.text()))
                min = int(self.solveTab.spin21.text())
                max = int(self.solveTab.spin22.text())
                detail = self.solveTab.checkbox2.isChecked()
                self.solveTab.data.setText(self.SOLVE.rand_V(p, n, min, max, detail))
                self.solveTab.data.setVisible(True)
            except:
                QMessageBox.question(self, '에러', '정상적이지 않은 입력입니다.')

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
        prime.valueChanged.connect(lambda : setattr(self.SOLVE, 'form', self.OPTION.primenumber(prime.value())))
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