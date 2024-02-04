# flake8: noqa

class SCP_SOLVE():
    def __init__(self):
        self.form = ".2f"
    
    # 확률 문제 계산 함수
    def Pprocess(self, goal, data):
        # 찾으려는 목표가 비어 있다면 오류 반환
        if goal=="":
            return "목표가 입력되지 않았거나 찾을 수 없습니다."
        
        # 재귀 형태로 목표값 계산
        data = self.prob(goal, data)

        # 결과값(확률)이 음수면 정상적이지 않은 결과 반환
        if goal in data.keys():
            if data[goal]<0:
                return "정상적이지 않은 입력입니다."
            return goal + " : " + format(data[goal], self.form)
        else:
            return "제공된 정보로 계산할 수 없습니다."

    # 목표와 주어진 값을 바탕으로 계산을 시도하고 그 결과를 반환하는 함수
    def prob(self, goal, data):

        # 변환 시 
        while ("cc" in goal):
            goal = goal.replace("cc", "")

        #값이 이미 존재하면 계산없이 반환
        if goal in data.keys():
            return data

    # 단일 확률
        if goal=="A":
            data = self.p1("A", "B", data)

        elif goal=="B":
            data = self.p1("B", "A", data)
        
        elif goal=="Ac":
            data = self.p2("A", data)

        elif goal=="Bc":
            data = self.p2("A", data)

    # 교집합
        elif goal=="AxB" or goal=="BxA":
            data = self.p3("A", "B", data)
        
        elif goal=="AcxB" or goal=="BxAc":
            data = self.p3("Ac", "B", data)

        elif goal=="AxBc" or goal=="BcxA":
            data = self.p3("A", "Bc", data)

        elif goal=="AcxBc" or goal=="BcxAc":
            data = self.p3("Ac", "Bc", data)

    # 합집합
        elif goal=="AUB" or goal=="BUA":
            data = self.p4("A", "B", data)

        elif goal=="AcUB" or goal=="BUAc":
            data = self.p4("Ac", "B", data)

        elif goal=="AUBc" or goal=="BcUA":
            data = self.p4("A", "Bc", data)

        elif goal=="AcUBc" or goal=="BcUAc":
            data = self.p4("Ac", "Bc", data)

    # 조건부 확률
        elif goal=="AB":
            data = self.p5("A", "B", data)

        elif goal=="BA":
            data = self.p5("B", "A", data)
        
        elif goal=="AcB":
            data = self.p5("Ac", "B", data)

        elif goal=="BAc":
            data = self.p5("B", "Ac", data)

        elif goal=="ABc":
            data = self.p5("A", "B", data)

        elif goal=="BcA":
            data = self.p5("B", "A", data)

        elif goal=="AcBc":
            data = self.p5("Ac", "Bc", data)

        elif goal=="BcAc":
            data = self.p5("Bc", "Ac", data)

        # 결과 반환
        return data

    # P(A) 와 P(B)를 계산하는 함수
    def p1(self, A, B, data):
        data = self.prob(f"{A}x{B}", data)
        data = self.prob(f"{B}{A}", data)
        if f"{A}x{B}" in data.keys() and f"{B}{A}" in data.keys():
            data[f"{A}"] = data[f"{A}x{B}"]/data[f"{B}{A}"]
        else:
            data = self.prob(f"{B}", data)
            data = self.prob(f"{A}{B}", data)
            data = self.prob(f"{B}c", data)
            data = self.prob(f"{A}{B}c", data)
            if (f"{B}" in data.keys() and f"{A}{B}" in data.keys() and f"{B}c" in data.keys() and f"{A}{B}c" in data.keys()):
                data[f"{A}"] = data[f"{B}"]*data[f"{A}{B}"] + data[f"{B}c"]*data[f"{A}{B}c"]
        return data

    # P(Ac) 와 P(Bc)를 계산하는 함수
    def p2(self, A, data):
        data = self.prob(f"{A}", data)
        if (f"{A}" in data.keys()):
            data[f"{A}c"] = 1-data[f"{A}"]
        return data

    # P(AxB)를 계산하는 함수
    def p3(self, A, B, data):
        data = self.prob(f"{A}", data)
        data = self.prob(f"{B}", data)
        data = self.prob(f"{A}U{B}", data)
        if (f"{A}" in data.keys() and f"{B}" in data.keys() and f"{A}U{B}" in data.keys()):
            data[f"{A}x{B}"] = data[f"{A}"] + data[f"{B}"] - data[f"{A}U{B}"]
            data[f"{B}x{A}"] = data[f"{A}x{B}"]
        return data

    # P(AUB)를 계산하는 함수
    def p4(self, A, B, data):
        data = self.prob(f"{A}", data)
        data = self.prob(f"{B}", data)
        data = self.prob(f"{A}x{B}", data)
        if (f"{A}" in data.keys() and f"{B}" in data.keys() and f"{A}x{B}" in data.keys()):
            data[f"{A}U{B}"] = data[f"{A}"] + data[f"{B}"] - data[f"{A}x{B}"]
            data[f"{B}U{A}"] = data[f"{A}U{B}"]
        return data

    # P(AB)를 계산하는 함수
    def p5(self, A, B, data):
        data = self.prob(f"{A}x{B}", data)
        data = self.prob(f"{B}", data)
        if (f"{A}x{B}" in data.keys() and f"{B}" in data.keys()):
            data[f"{A}{B}"] = data[f"{A}x{B}"]/data[f"{B}"]
        return data
