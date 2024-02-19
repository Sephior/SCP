#Smart Calculation Program
# flake8: noqa
import re, math

# 공학용 계산기
class SCP_STANDARD():
    def __init__(self):
        self.init()

    def init(self):
        self.regularline = "" #str형식으로 저장\
        self.prev = "0"
        self.form = ".2f"
    
    #입력
    def add(self, string):
        self.regularline += string
        return self.regularline
    
    #초기화
    def clear(self):
        self.regularline = ""
        return self.regularline
    
    #한 글자 지우기
    def backspace(self):
        self.regularline = self.regularline[0:-1]
        return self.regularline


    #후위 표기법 변환
    def reverse_poland(self, string):
        #기호를 전부 분리
        formula = re.findall(r'√?\d+\.\d+²?|√?\d+²?|--|[+\-*/()]', string)

        #각 기호별로 재처리를 거치면서 후위 표기법으로 변환
        result = [] #결과물을 저장하는 리스트
        sign = [] #연산자를 넣을 리스트
        operators = {'+': 1, '-': 1, '*': 2, '/': 2}

        for i in formula:
            #괄호 처리
            if i == ')':
                while sign[-1] != '(':
                    result.append(sign.pop())
                sign.pop()  # '(' 제거

            elif i in operators:
                # 우선순위가 높은 연산자가 sign 내부에 존재하면 처리
                while (sign and sign[-1] != '(' and operators.get(sign[-1], 0) >= operators[i]):
                    result.append(sign.pop())
                sign.append(i)

            else:
                #연산자가 아닌 값을 처리
                a = float(re.findall(r'\d+\.\d+|\d+', i)[0])
                if '√' in i:
                    a = math.sqrt(a)
                if '²' in i:
                    a *= a
                result.append(a)

        # 남은 연산자 처리
        while sign:
            result.append(sign.pop())
        return result

    def Solve(self, list):
        stack=[]
        operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y if y != 0 else float('inf')}
        
        #regularline이 비었거나, 연산자만 존재하거나, 괄호가 안 닫히는 등의 오류 처리
        try:
            for i in list:
                if type(i) is float:
                    stack.append(i)
                else:
                    operation = operators.get(i, lambda x, y: "Invalid operator")   
                    stack.append(operation(stack.pop(-2), stack.pop()))
                    print(stack)
            return stack[0]
        except:
            return "error"
                
    #실제로 호출되는 함수 cal
    def cal(self):
        self.prev = self.Solve(self.reverse_poland(self.regularline))
        # 결과값을 문자열 형태로 가공 및 반환
        if self.prev == "error":
            result = self.regularline + "\n\n" + "error"
        else:
            result = self.regularline + "\n\n" + str(format(self.prev, self.form))
            self.regularline = ""
        return result
    
    #SOLVE의 입력시에 연산이 필요한 경우 연산해서 반환
    def cal4SOLVE(self, text):
        return self.Solve(self.reverse_poland(text))