# flake8: noqa

class SCP_SOLVE():
    def __init__(self):
        self.form = ".2f"
        self.data = {}
        self.prevdata = {}
        self.count = 0
    
    # 확률 문제 계산 함수
    def Pprocess(self, goal, data):
        # 찾으려는 목표가 비어 있다면 오류 반환
        if goal=="":
            return "목표가 입력되지 않았거나 찾을 수 없습니다."
        
        # 재귀 형태로 목표값 계산
        self.data = data
        self.count = 50
        self.data = self.prob(goal)

        # 결과를 계산할 수 없으면 계산 불가능 반환
        if isinstance(self.data, str):
            return self.data
        # 결과값(확률)이 음수면 정상적이지 않은 결과 반환
        elif self.data[goal]<0:
            return "정상적이지 않은 입력입니다."
        else: 
            return "P("+ goal + ") : " + format(self.data[goal], self.form)

    # 목표와 주어진 값을 바탕으로 계산을 시도하고 그 결과를 반환하는 함수
    def prob(self, goal):
        # 변환 시 여집합이 중복이면 원래 값으로 변경
        #for key, value in self.data.items():
        #    if "cc" in key:
        #        self.data[key.replace("cc", "")]=value
        #        del self.data[key]
            

    # 확률 계산
        self.data = self.p2("A")
        self.data = self.p2("B")
        self.data = self.p2("Ac")
        self.data = self.p2("Bc")
        for i, j in [("A", "B"), ("B", "A"), ("Ac", "B"), ("B", "Ac"), ("A", "Bc"), ("Bc", "A"), ("Ac", "Bc"), ("Bc", "Ac")]:
            self.data = self.p1(i, j) # 단일 확률
            self.data = self.p3(i, j) # 교집합
            self.data = self.p4(i, j) # 합집합
            self.data = self.p5(i, j) # 조건부 확률

        # 결과가 기존 데이터와 같으면 : 더 이상 계산할 수 없으면 반환
        if self.count==0:
            return "제공된 정보로 계산할 수 없습니다."

        #목표 값이 있으면 결과값 반환
        if goal not in self.data.keys():
            self.count -=1
            self.data = self.prob(goal)
        return self.data

    # P(A) 와 P(B)를 계산하는 함수
    def p1(self, A, B):
        #중복 확인
        if f"{A}" in self.data.keys():
            return self.data
        
        if f"{A}x{B}" in self.data.keys() and f"{B}{A}" in self.data.keys():
            self.data[f"{A}"] = self.data[f"{A}x{B}"] / self.data[f"{B}{A}"]
        elif (f"{B}" in self.data.keys() and f"{A}{B}" in self.data.keys() and f"{B}c" in self.data.keys() and f"{A}{B}c" in self.data.keys()):
            self.data[f"{A}"] = self.data[f"{B}"] * self.data[f"{A}{B}"] + self.data[f"{B}c"] * self.data[f"{A}{B}c"]
        elif (f"{A}x{B}" in self.data.keys() and f"{A}x{B}c" in self.data.keys()):
            self.data[f"{A}"] = self.data[f"{A}x{B}"] + self.data[f"{A}x{B}c"]
        return self.data
    
    # P(Ac) 와 P(Bc)를 계산하는 함수
    def p2(self, A):
        #중복 확인
        if f"{A}c" in self.data.keys():
            return self.data
        
        if (f"{A}" in self.data.keys()):
            self.data[f"{A}c"] = 1 - self.data[f"{A}"]
        return self.data
    
    # P(AxB)를 계산하는 함수
    def p3(self, A, B):
        #중복 확인
        if f"{A}x{B}" in self.data.keys():
            return self.data
        
        if f"{B}x{A}" in self.data.keys():
            self.data[f"{A}x{B}"] = self.data[f"{B}x{A}"]
        elif (f"{A}" in self.data.keys() and f"{B}" in self.data.keys() and f"{A}U{B}" in self.data.keys()):
            self.data[f"{A}x{B}"] = self.data[f"{A}"] + self.data[f"{B}"] - self.data[f"{A}U{B}"]
            self.data[f"{B}x{A}"] = self.data[f"{A}x{B}"]
        return self.data
    
    # P(AUB)를 계산하는 함수
    def p4(self, A, B):
        #중복 확인
        if f"{A}U{B}" in self.data.keys():
            return self.data
        
        if f"{B}U{A}" in self.data.keys():
            self.data[f"{A}U{B}"] = self.data[f"{B}U{A}"]
        elif (f"{A}" in self.data.keys() and f"{B}" in self.data.keys() and f"{A}x{B}" in self.data.keys()):
            self.data[f"{A}U{B}"] = self.data[f"{A}"] + self.data[f"{B}"] - self.data[f"{A}x{B}"]
            self.data[f"{B}U{A}"] = self.data[f"{A}U{B}"]
        return self.data
    
    # P(AB)를 계산하는 함수
    def p5(self, A, B):
        #중복 확인
        if f"{A}{B}" in self.data.keys():
            return self.data
        
        if (f"{A}x{B}" in self.data.keys() and f"{B}" in self.data.keys()):
            self.data[f"{A}{B}"] = self.data[f"{A}x{B}"] / self.data[f"{B}"]
        return self.data

    # 확률, 횟수, 성공이 적어도 몇 이상일 조건, 몇일 조건을 각각 입력받기
    def rand_V(self, p, n, min, max):
        return