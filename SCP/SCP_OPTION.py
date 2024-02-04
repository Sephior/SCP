# flake8: noqa
from PyQt5.QtCore import Qt


class SCP_OPTION():
    def __init__(self):
        pass

    #라이트 모드, 다크 모드 변경
    def darkmode(UI, mode):
        if mode=="light":
            UI.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                color: #333;
                font-family: Arial, sans-serif;
            }

            QTabWidget::pane {
                border: 1px solid #ddd;
            }

            QTabBar::tab {
                background-color: #eee;
                color: #333;
                border: 1px solid #ddd;
                padding: 8px;
            }

            QTabBar::tab:selected, QTabBar::tab:hover {
                background-color: #ddd;
            }

            QPushButton, QTextEdit, QComboBox, QLabel, QCheckBox {
                background-color: #eee;
                color: #333;
                border: 1px solid #ddd;
                padding: 8px;
            }

            QPushButton:hover, QComboBox:hover, QLabel:hover {
                background-color: #ddd;
            }
        """)

        elif mode=="dark":
            UI.setStyleSheet("""
            QWidget {
                background-color: #282c34;
                color: #abb2bf;
                font-family: Arial, sans-serif;
            }

            QTabWidget::pane {
                border: 1px solid #3e4451;
            }

            QTabBar::tab {
                background-color: #2c313a;
                color: #abb2bf;
                border: 1px solid #3e4451;
                padding: 8px;
            }

            QTabBar::tab:selected, QTabBar::tab:hover {
                background-color: #3e4451;
            }

            QPushButton, QTextEdit, QComboBox, QLabel, QCheckBox {
                background-color: #2c313a;
                color: #abb2bf;
                border: 1px solid #3e4451;
                padding: 8px;
            }

            QPushButton:hover, QComboBox:hover, QLabel:hover {
                background-color: #3e4451;
            }
        """)

    #항상 화면 맨 앞에 있게 하는 옵션   
    def ontop(UI, bool):
        if bool:
            UI.setWindowFlags(UI.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            UI.setWindowFlags(UI.windowFlags() & ~Qt.WindowStaysOnTopHint)
        UI.show()

    #소수점 자릿수 설정하기
    def primenumber(num):
        form = f".{int(num)}f"
        return form
    
    #소표본일때 자유도 n-1로 설정
    def small(UI, bool):
        if bool:
            return True
        else:
            return False