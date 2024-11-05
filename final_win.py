from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *


class FinalWidget(QWidget):
    def __init__(self,heart,index):


        super().__init__()
        self.index = index
        self.heart = heart


        # создаём и настраиваем графические элементы:
        self.initUI()





        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()


        # старт:
        self.show()





    def initUI(self):
        self.indx = QLabel(str(self.index))
        self.hrt = QLabel(self.heart)

        self.layout_line = QVBoxLayout()

        self.layout_line.addWidget(self.indx, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.hrt, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    
    
    def set_appear(self):
        self.setWindowTitle(txt_title2)
        self.resize(win_width, win_height)
        self.setStyleSheet('''
       QWidget {
        font-size: 22px;
        color: #E0E0E0; /* Светло-серый текст */
        background-color: #212121; /* Очень темный фон */
    }
   
  
    
    
    
    QPushButton {
        background-color: #2A2A2A; /* Темно-серая кнопка */
        color: #FFFFFF;
        border: 1px solid #2C2C2C; /* Еще более темный бордюр */
        padding: 5px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #3D3D3D; /* Светло-серый при наведении */
    }
    QLineEdit {
        border: 1px solid #2C2C2C;
        border-radius: 5px;
        background-color: #2A2A2A; /* Очень темный фон для полей */
        color: #FFFFFF; /* Светло-серый текст */
    }
QLabel {
        font-weight: bold;
        font-size: 15px;
        color: #E0E0E0; /* Светло-серый текст для меток */
        text-align: center;
    }''')