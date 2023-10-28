#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, QRadioButton
#создание элементов интерфейса
app = QApplication([])

window = QWidget()
window.setWindowTitle('Меню Card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Почему застрелился Гитлер?')

RadioGroupBox = QGroupBox('Варианты ответов')
a = QRadioButton('По приколу')
b = QRadioButton('Дипрессия')
c = QRadioButton('Проиграл войну')
d = QRadioButton('Бог знает')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(a)
layout_ans2.addWidget(b)
layout_ans3.addWidget(c)
layout_ans3.addWidget(d)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)
window.show()
app.exec()