#-------------프로그램 설명--------------
# 통계학 계산 프로그램

#텍스트만 처리를 해달라고 한 후에
#받아와서 계산해도 되고
#출력값을 텍스트 파일로 추가하는 기능도 괜찮고
#마지막으로 exe파일로 변환

#위 코드에서는 클릭 시 self.EXTRACT.save_as_txt() 함수를 호출하며, 이때 텍스트 추출은 self.statisticTab.resolve.toPlainText()로 이루어집니다. 람다 함수를 사용함으로써 클릭 이벤트가 발생할 때까지 해당 함수가 실행되지 않습니다. 이 방법을 사용하면 오류가 발생하지 않을 것입니다.
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