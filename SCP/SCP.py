#-------------프로그램 설명--------------
# 통계학 계산 프로그램
# 통계학 복습과 파이썬 실력 향상을 위해 시작하게 된 프로젝트
# PyQt5를 이용해 UI 구성
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
from SCP_EXTRACT import *

if __name__ == '__main__':
   #SCP.py에서 실행
   app = QApplication(sys.argv)
   SCP_UI(SCP_STAT, SCP_OPTION, SCP_STANDARD, SCP_SOLVE, SCP_EXTRACT).show()
   sys.exit(app.exec_()) 