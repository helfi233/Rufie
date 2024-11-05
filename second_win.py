from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel,
    QPushButton, QLineEdit
)

from instr import *  
from final_win import FinalWidget


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()

        # Таймер
        self.timer = QTimer()
        self.time_left = 0

        # создаём и настраиваем графические элементы:
        self.initUI()

        # устанавливает связи между элементами
        self.connects()

        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()

    def initUI(self):
        self.name_text = QLabel(txt_name)
        self.age_text = QLabel(txt_age)
        self.test1_text = QLabel(txt_1test)
        self.test2_text = QLabel(txt_2test)
        self.test3_text = QLabel(txt_3test)
        self.timer_label = QLabel(txt_timer)

        self.test1_button = QPushButton(txt_1tst, self)
        self.test2_button = QPushButton(txt_2tst, self)
        self.test3_button = QPushButton(txt_3tst, self)
        self.result_button = QPushButton(txt_results, self)

        self.name = QLineEdit('ФИО')
        self.age = QLineEdit('0')
        self.pulse1 = QLineEdit('0')
        self.pulse2 = QLineEdit('0')
        self.pulse3 = QLineEdit('0')

      
        self.layout_line = QVBoxLayout()

        self.layout_line.addWidget(self.name_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.name, alignment=Qt.AlignLeft)

     
        self.layout_line.addWidget(self.age_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.age, alignment=Qt.AlignLeft)

  
        self.layout_line.addWidget(self.test1_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.test1_button, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.pulse1, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.test2_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.test2_button, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.test3_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.test3_button, alignment=Qt.AlignLeft)

      
        self.layout_line.addWidget(self.result_button, alignment=Qt.AlignLeft)

  
        
        self.layout_line.addWidget(self.pulse2, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.pulse3, alignment=Qt.AlignLeft)


        self.layout_right = QVBoxLayout()
        self.layout_right.addWidget(self.timer_label, alignment=Qt.AlignRight)

       
        self.layout_main = QHBoxLayout()
        self.layout_main.addLayout(self.layout_line)
        self.layout_main.addLayout(self.layout_right)
        self.setLayout(self.layout_main)

      
        self.timer.timeout.connect(self.update_timer)

    def next_click(self): 
        try:
            index = (((int(self.pulse1.text())+int(self.pulse2.text())+int(self.pulse3.text()))-200)/10)
            
            if (int(self.age.text())== 7 or int(self.age.text()) == 8):
                if (index >= 21):
                    score = 'Низкий'
                    Whishes = 'Ваше способность сердца очень плохая,обратитесь к врачу'
                elif(index >= 17 and index <= 20.9):
                    score ='Удовлетворительный'
                    Whishes ='ваше работа сердце в норме но стоит наблюдать или обследоваться у врача пожеланию '
                elif (index >= 12 and index<=16.9):
                    score ='Средний'
                    Whishes ='ваша работоспособность сердца в норме не стоит беспокоится'
                elif (index >= 6.5 and index<=11.9):
                    score ='Выше среднего'
                    Whishes ='ваша работоспособность сердца в хорошем состояние'
                elif (index <=6.4):
                    score ='Высокий'
                    Whishes ='ваша работоспособность сердца отличное,это повод радоваться'
            elif (int(self.age.text())== 9 or int(self.age.text()) == 10):
                if (index >= 19.5):
                    score = 'Низкий'
                    Whishes = 'Ваше способность сердца очень плохая,обратитесь к врачу'
                elif (index >= 15.5 and index<=19.4):
                    score ='Удовлетворительный'
                    Whishes ='ваше работа сердце в норме но стоит наблюдать или обследоваться у врача пожеланию '
                elif (index >= 10.5 and index<=15.4):
                    score ='Средний'
                    Whishes ='ваша работоспособность сердца в норме не стоит беспокоится'
                elif (index >= 5 and index<= 10.4):
                    score ='Выше среднего'
                    Whishes ='ваша работоспособность сердца в хорошем состояние'
                elif(index <=4.9):
                    score ='Высокий'
                    Whishes ='ваша работоспособность сердца отличное,это повод радоваться'
            elif (int(self.age.text())== 11 or int(self.age.text()) == 12):
                if (index >= 18):
                    score = 'Низкий'
                    Whishes = 'Ваше способность сердца очень плохая,обратитесь к врачу'
                elif (index >= 14 and index <=17.9):
                    score ='Удовлетворительный'
                    Whishes ='ваше работа сердце в норме но стоит наблюдать или обследоваться у врача пожеланию '
                elif (index >= 9 and index<=13.9):
                    score ='Средний'
                    Whishes ='ваша работоспособность сердца в норме не стоит беспокоится'
                elif index >= 3.5 and index<= 8.9:
                    score ='Выше среднего'
                    Whishes ='ваша работоспособность сердца в хорошем состояние'
                elif (index <=3.4):
                    score ='Высокий'
                    Whishes ='ваша работоспособность сердца отличное,это повод радоваться' 
            elif (int(self.age.text())== 13 or int(self.age.text()) == 14):
                if (index >= 16.5):
                    score = 'Низкий'
                    Whishes = 'Ваше способность сердца очень плохая,обратитесь к врачу'
                elif (index >= 12.5 and index<=16.4):
                    score ='Удовлетворительный'
                    Whishes ='ваше работа сердце в норме но стоит наблюдать или обследоваться у врача пожеланию '
                elif (index >= 7.5 and index<=12.4):
                    score ='Средний'
                    Whishes ='ваша работоспособность сердца в норме не стоит беспокоится'
                elif (index >= 2 and index<= 7.4):
                    score ='Выше среднего'
                    Whishes ='ваша работоспособность сердца в хорошем состояние'
                elif (index <=1.4):
                    score ='Высокий'
                    Whishes ='ваша работоспособность сердца отличное,это повод радоваться'
            elif (int(self.age.text()) >= 15 ):
                if (index >= 15):
                    score = 'Низкий'
                    Whishes = 'Ваше способность сердца очень плохая,обратитесь к врачу'
                elif (index >= 11 and index<=14.9):
                    score ='Удовлетворительный'
                    Whishes ='ваше работа сердце в норме но стоит наблюдать или обследоваться у врача пожеланию '
                elif (index >= 6 and index<=10.9):
                    score ='Средний'
                    Whishes ='ваша работоспособность сердца в норме не стоит беспокоится'
                elif (index >= 0.5  and index<= 5.9):
                    score ='Выше среднего'
                    Whishes ='ваша работоспособность сердца в хорошем состояние'
                elif (index <=0.4):
                    score ='Высокий'
                    Whishes ='ваша работоспособность сердца отличное,это повод радоваться'     
            heart = 'ваше оценка сердца'+score+',основаясь на ваш возраст и индекс'+Whishes
        
            self.tw = FinalWidget(heart,index)
            self.hide()
        except:
            print('Неудалось')
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
        border: 1px solid #FF0000;
       
    }
QLabel {
        font-weight: bold;
        font-size: 15px;
        color: #E0E0E0; /* Светло-серый текст для меток */
        text-align: center;
    }''')

            return
       

    def connects(self):
        self.test1_button.clicked.connect(self.start_timer_15)
        self.test2_button.clicked.connect(self.start_timer_45)
        self.test3_button.clicked.connect(self.start_timer_60)
        self.result_button.clicked.connect(self.next_click)

    def start_timer_15(self):
        self.time_left = 15
        self.timer_label.setText(f'Осталось времени: {self.time_left} секунд')
        self.timer.start(1000) 

    def start_timer_45(self):
        self.time_left = 45
        self.timer_label.setText(f'Осталось времени: {self.time_left} секунд')
        self.timer.start(1000)

    def start_timer_60(self):
        self.time_left = 60
        self.timer_label.setText(f'Осталось времени: {self.time_left} секунд')
        self.timer.start(1000)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(f'Осталось времени: {self.time_left} секунд')
        else:
            self.timer.stop()
            self.timer_label.setText('Время истекло!')

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





