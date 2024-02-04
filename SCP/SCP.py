#-------------프로그램 설명--------------
# 통계학 계산 프로그램
#시작은 문제풀이에 기반을 뒀으니까
#그 방향으로 가고
#출력값을 시각화하는걸 어떻게 표로 하던가 해서
#가시성을 높이는 걸로 타협을 보는건 어떨까요

#텍스트만 처리를 해달라고 한 후에
#받아와서 계산해도 되고
#출력값을 텍스트 파일로 추가하는 기능도 괜찮고
#----------------------------------------

#orange3
# flake8: noqa
import sys
from PyQt5.QtWidgets import QApplication
from SCP_STANDARD import *
from SCP_UI import *
from SCP_STAT import *
from SCP_OPTION import *
from SCP_SOLVE import *

if __name__ == '__main__':
   #SCP.py에서 실행
   app = QApplication(sys.argv)
   SCP_UI(SCP_STAT, SCP_OPTION, SCP_STANDARD, SCP_SOLVE).show()
   sys.exit(app.exec_())