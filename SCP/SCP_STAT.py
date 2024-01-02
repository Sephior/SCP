#Smart Calculation Program
# flake8: noqa
import re, math

#통계학 계산을 수행하고 결과를 저장, 반환하는 SCP_STAT 클래스 생성
class SCP_STAT():
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.samplelist = []
        self.form = ".2f"
        self.small = False

    def textsplit(self, text, kind):
            if text[-1] == "\n" and not("\n" in text[0:-1]):
                text = text[0:-1]
            numbers = re.findall(r'-?\d+\.\d+|-?\d+', text)
            return self.basical([float(number) for number in numbers], kind)
    
    

    def basical(self, list, kind):
            print(list)
            result=""
            result+=f"표본 수 : {format(len(list), self.form)}\n"
            avg = sum(list)/len(list)
            sumall = 0
            for i in list:
                sumall += (i-avg)**2
            #소표본일 때 자유도 n-1로 사용
            if self.small==True:
                var = sumall/(len(list)-1)
            else:
                var = sumall/len(list)
            std = math.sqrt(var)

            result+=f"평균 : {format(avg, self.form)}\n"
            result+=f"분산 : {format(var, self.form)}\n"
            result+=f"표준편차 : {format(std, self.form)}\n"

            L = sorted(list)
            #표본 개수에 따라 사분위수 계산시 오류 발생 가능성
            if len(L)>=4:
                q1_index = int(0.25 * (len(L)+ 1))
                q1 = L[q1_index - 1] if len(L) % 4 == 0 else (L[q1_index - 1] + L[q1_index]) / 2

                q2_index = int(0.5 * (len(L) + 1))
                q2 = L[q2_index - 1] if len(L) % 4 == 0 else (L[q2_index - 1] + L[q2_index]) / 2
                
                q3_index = int(0.75 * (len(L) + 1))
                q3 = L[q3_index - 1] if len(L) % 4 == 0 else (L[q3_index - 1] + L[q3_index]) / 2
                srange = max(L)-min(L)
                iqr = q3 - q1

                result+=f"제1사분위수 : {format(q1, self.form)}\n"
                result+=f"제2사분위수(중앙값) : {format(q2, self.form)}\n"
                result+=f"제3사분위수 : {format(q3, self.form)}\n"
                result+=f"표본범위 : {format(srange, self.form)}\n"
                result+=f"표본사분위범위 : {format(iqr, self.form)}\n"

            if kind=="sample1":
                return result
            
            elif kind[7]=="2":
                return [[len(list), avg, var, std, q1, q2, q3, srange, iqr], result]


    def indcal(self, A, B, condition):
        result ="asdf"
        return result