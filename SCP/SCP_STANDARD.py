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
        self.form = ".2f"
    
    #입력 파싱
    def add(self, string):
        self.regularline += string
        return self.regularline
        
    def clear(self):
        self.regularline = ""
        return self.regularline
    
    def backspace(self):
        self.regularline = self.regularline[0:-1]
        return self.regularline


    #후위 표기법 변환
    def reverse_poland(self, string):
        #기호를 전부 분리

        formula = re.findall(r'√?\d+\.\d+²?|√?\d+²?|--|[+\-*\/\(\)]', string)
        #각 기호별로 재처리를 거치면서 후위 표기법으로 변환
        print(formula)

        result = [] #결과물을 저장하는 리스트
        sign = [] #연산자를 넣을 리스트
        operators = ['+', '-', '*', '/', '(']
        
        for i in formula:
            #괄호 처리
            if i == ')':
                while (sign[-1]!='('):
                    result.append(sign.pop())
                sign.pop()

            elif i in operators:
                #우선순위가 높은 연산자가 sign 내부에 존재하면 처리
                if ('*' in sign or '/' in sign) and (i=='+' or i == '-' or i == '--'):
                    while (sign[-1]=='+' or sign[-1]=='-'):
                        result.append(sign.pop())
                if i=='--':
                    sign.append('+') 
                else:
                    sign.append(i)

            else:
                #연산자가 아닌 값을 처리
                a = float(re.findall(r'\d+\.\d+|\d+', i)[0])
                if '√' in i:
                    a = math.sqrt(a)
                if '²' in i:
                    a *=a
                result.append(a)

        print(sign, result)
        #sign의 남은 연산자 처리
        for i in sign[::-1]:
            result.append(i)
            sign.pop()

        print(sign, result)
        return result

    def Solve(self, list):
        stack=[]
        operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y if y != 0 else float('inf')}
        
        #regularline이 비었거나, 수식만 존재하는 등의 오류 처리
        try:
            for i in list:
                if type(i) is float:
                    stack.append(i)
                else:
                    operation = operators.get(i, lambda x, y: "Invalid operator")   
                    stack.append(operation(stack.pop(-2), stack.pop()))
            return stack[0]
        except:
            return "error"
                

    def cal(self):
        self.prev = str(self.Solve(self.reverse_poland(self.regularline)))
        if self.prev == "error":
            result = self.regularline + "\n\n" + "error"
        else:
            result = self.regularline + "\n\n" + f"{format(self.prev, self.form)}"
            self.regularline = ""
        return result