#Smart Calculation Program
# flake8: noqa
import re, math
from scipy.stats import norm, t, chi2

#통계학 계산을 수행하고 결과를 저장, 반환하는 SCP_STAT 클래스 생성
class SCP_STAT():
    def __init__(self):
        self.init()

    def init(self):
        self.samplelist = []
        self.form = ".2f"
        self.small = False

    def precal(self, text):
            if isinstance(text, str):
                if text[-1] == "\n" and not("\n" in text[0:-1]):
                    text = text[0:-1]
                numbers = re.findall(r'-?\d+\.\d+|-?\d+', text)
                return [float(number) for number in numbers]
            else:
                return text
    
    

    def cal(self, text, condition, name):
            list = self.precal(text)
            #평균, 분산, 표준편차 계산
            result=""
            L = sorted(list)
            lenL = len(L)
            avg = sum(L)/lenL
            sumall = 0
            for i in L:
                sumall += (i-avg)**2
            #소표본일 때 자유도 n-1로 사용
            if lenL<=30 and lenL>1 and self.small == False:
                var = sumall/(lenL-1)
            else:
                var = sumall/lenL
            std = math.sqrt(var)

        #사분위수, 표본범위 계산
            #표본 개수에 따라 사분위수 계산시 오류 발생 가능성
            if lenL>=4:
                q1_index = int(0.25 * (lenL+ 1))
                q1 = L[q1_index - 1] if lenL % 4 == 0 else (L[q1_index - 1] + L[q1_index]) / 2

                q2_index = int(0.5 * (lenL + 1))
                q2 = L[q2_index - 1] if lenL % 4 == 0 else (L[q2_index - 1] + L[q2_index]) / 2
                
                q3_index = int(0.75 * (lenL + 1))
                q3 = L[q3_index - 1] if lenL % 4 == 0 else (L[q3_index - 1] + L[q3_index]) / 2
                srange = max(L)-min(L)
                iqr = q3 - q1

        #모평균 신뢰구간 계산
            a = condition['a']
            if lenL<=30 and condition['정규분포']==False:
                # 스튜던트 t분포 사용
                t_score = t.ppf(1 - (a) / 2, df=lenL-1)
                avgCinterval = (avg-t_score*std/math.sqrt(lenL), avg+t_score*std/math.sqrt(lenL))
            else:
                # z분포 사용
                z_score = norm.ppf(1 - (a) / 2)
                avgCinterval = (avg-z_score*std/math.sqrt(lenL), avg+z_score*std/math.sqrt(lenL))

        #모분산, 모표준편차 신뢰구간 계산
            varCinterval = ((lenL-1)*var/chi2.ppf(1-a/2, df=lenL-1), (lenL-1)*var/chi2.ppf(a/2, df=lenL-1))
            stdCinterval = (math.sqrt(varCinterval[0]), math.sqrt(varCinterval[1]))

            if name!="대응표본":
                if condition['표본 수']==True:
                    result+=f"{name}의 표본 수 : {format(len(list), self.form)}\n"
                if condition['평균']==True:
                    result+=f"{name}의 평균 : {format(avg, self.form)}\n"
                if condition['분산']==True:
                    result+=f"{name}의 분산 : {format(var, self.form)}\n"
                if condition['표준편차']==True:
                    result+=f"{name}의 표준편차 : {format(std, self.form)}\n"
                if condition['사분위수']==True:
                    result+=f"{name}의 제1사분위수 : {format(q1, self.form)}\n"
                    result+=f"{name}의 제2사분위수(중앙값) : {format(q2, self.form)}\n"
                    result+=f"{name}의 제3사분위수 : {format(q3, self.form)}\n"
                if condition['표본범위']==True:
                    result+=f"{name}의 표본범위 : {format(srange, self.form)}\n"
                    result+=f"{name}의 표본사분위범위 : {format(iqr, self.form)}\n"
            if condition['모평균 신뢰구간']==True:
                result+=f"{name}의 모평균 신뢰구간 : {(format(avgCinterval[0], self.form), format(avgCinterval[1], self.form))}\n"
            if condition['모분산 신뢰구간']==True:
                result+=f"{name}의 모분산 신뢰구간 : {(format(varCinterval[0], self.form), format(varCinterval[1], self.form))}\n"
            if condition['모표준편차 신뢰구간']==True:
                result+=f"{name}의 모표준편차 신뢰구간 : {(format(stdCinterval[0], self.form), format(stdCinterval[1], self.form))}\n"

            return [[list, avg, var, std], result]


    def secondcal(self, A, B, condition):
        # 두 코드의 계산 결과 추출
        first = A[0]
        second = B[0]
        n1 = len(first[0])
        n2 = len(second[0])
        #독립표본에서의 신뢰구간 계산
        if condition['표본']=="독립":
            a = condition['a']
            if n1<=30 and condition['정규분포']==False:
                # 스튜던트 t분포 사용
                t_score = t.ppf(1 - (a) / 2, df=n1+n2-2)
                Sp = (n1-1)*first[2]+(n2-1)*second[2]/(n1+n2-2)
                avgCinterval = (first[1]-second[1]-t_score*math.sqrt(Sp/n1+Sp/n2), first[1]-second[1]-t_score*math.sqrt(Sp/n1+Sp/n2))
            else:
                # z분포 사용
                z_score = norm.ppf(1 - (a) / 2)
                avgCinterval = (first[1]-second[1]-z_score*math.sqrt(first[2]/n1+second[2]/n2), first[1]-second[1]-z_score*math.sqrt(first[2]/n1+second[2]/n2))
            result = f"독립표본의 모평균의 신뢰구간 : {avgCinterval}"

        #대응표본에서의 신뢰구간 계산
        elif condition['표본']=="대응":
            if n2!=n2:
                result = "대응표본의 수는 서로 같아야 합니다."
            else:
                Dl = []
                for i, j in zip(first[0], second[0]):
                    Dl.append(i-j)
                result = self.cal(Dl, condition, "대응표본")[1]

        # 반환할 결과값
        result = A[1] + "\n" + B[1] + "\n" + result
        return result