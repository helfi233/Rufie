from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import SecondWin
     
class MainWin(QWidget):
   def __init__(self):
       
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # старт:
       self.show()


   def initUI(self):
       
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
  
   def next_click(self):
       self.tw = SecondWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   
   def set_appear(self):
       self.setWindowTitle(txt_title)
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
       


app = QApplication([])
mw = MainWin()
app.exec_()