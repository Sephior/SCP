#Smart Calculation Program
# flake8: noqa

import re, math
# 공학용 계산기
class SCP_STANDARD():
    def __init__(self):
        self.init()

    def init(self):
        self.regularline = "" #str형식으로 저장\
        self.prev = 0
    
    #입력 파싱
    def add(self, string):
        self.regularline += string
        return self.valueChanged()
        
    def clear(self):
        self.regularline = ""
        return self.valueChanged()
    
    def backspace(self):
        self.regularline = self.regularline[0:-1]
        return self.valueChanged()

    def valueChanged(self):
        return self.regularline


    def cal(self):
        #후위 표기법 변환
        numbers = re.findall(r'-?\d+\.\d+|-?\d+', self.regularline)

        result = "1"

        self.regularline = ""
        self.prev = result
        return self.prev