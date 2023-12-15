#-------------프로그램 설명--------------
# 통계학 계산 프로그램
#----------------------------------------

#orange3
import sys
from PyQt5.QtWidgets import QApplication
from SCP_UI import *
from SCP_STAT import *
from SCP_OPTION import *

if __name__ == '__main__':
   #SCP.py에서 실행
   app = QApplication(sys.argv)
   SCP_UI(SCP_STAT, SCP_OPTION).show
   sys.exit(app.exec_())
   