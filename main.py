from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint

app = QApplication([])
win = QWidget()
win.setWindowTitle('Лотерея')
win.resize(400,400)

button = QPushButton(win)
button.setText('Випробувати удачу')
button.move(150,300)

lb_1 = QLabel(win)
lb_2 = QLabel(win)
lb_3 = QLabel(win)
lb_1.setText('Натисніть,щоб взяти участь')
lb_2.setText('?')
lb_3.setText('?')
lb_1.move(130,100)
lb_2.move(200,150)
lb_3.move(200,200)

def random():
    number1 = randint(0,9)
    number2 = randint(0,9)
    lb_2.setText(str(number1))
    lb_3.setText(str(number2))
    if number1 == number2:
        lb_1.setText('Ви виграли')
    else:
        lb_1.setText('Ви програли')

button.clicked.connect(random)

win.show()
app.exec_()
