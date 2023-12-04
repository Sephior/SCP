#Smart Calculation Program
import re, math
from SCP_UI import *

#통계학 계산을 수행하고 결과를 저장, 반환하는 SCP_STAT 클래스 생성
class SCP_STAT:
    def __init__(self, UI):
        super().__init__()
        self.initUI()
        self.UI = UI
        self.form = ".2f"

    def initUI(self):
        self.samplelist = []

    def textsplit(self, text, kind, Tab):
            if text[-1] == "\n" and not("\n" in text[0:-1]):
                text = text[0:-1]
            numbers = re.findall(r'\d+', text)
            print(numbers)
            self.cal([int(number) for number in numbers], kind, Tab)
    
    def cal(self, list, kind, Tab):
        if kind == "avg":
            print(list)
            avg = sum(list)/len(list)
            sumall = 0
            for i in list:
                sumall += (i-avg)**2
            var = sumall/len(list)
            std = math.sqrt(var)
            Tab.solve.setVisible(True)
            Tab.solve.setText(f"평균 : {format(avg, self.form)},\n분산 : {format(var, self.form)},\n표준편차 : {format(std, self.form)}")
        elif kind == "middle":
            L = sorted(list)
            q1_index = int(0.25 * (len(L)+ 1))
            q2_index = int(0.5 * (len(L) + 1))
            q3_index = int(0.75 * (len(L) + 1))

            q1 = L[q1_index - 1] if len(L) % 4 == 0 else (L[q1_index - 1] + L[q1_index]) / 2
            q2 = L[q2_index - 1] if len(L) % 4 == 0 else (L[q2_index - 1] + L[q2_index]) / 2
            q3 = L[q3_index - 1] if len(L) % 4 == 0 else (L[q3_index - 1] + L[q3_index]) / 2

            srange = max(L)-min(L)
            iqr = q3 - q1
            Tab.solve.setVisible(True)
            a = "f"
            Tab.solve.setText(f"""제1사분위수 : {format(q1, self.form)},
                              \n제2사분위수(중앙값) : {format(q2, self.form)},
                              \n제3사분위수 : {format(q3, self.form)},
                              \n표본범위 : {format(srange, self.form)},
                              \n표본사분위범위 : {format(iqr, self.form)}""")