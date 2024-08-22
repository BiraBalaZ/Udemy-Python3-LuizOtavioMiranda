# QMainWindos e centalWidget
# -> QApplication (app)
#   -> QMainWindow (window -> setCentralWidget)
#   -> CentralWidget (central_widget)
#       -> Layout (layout)
#           -> Widget (botao1)
#           -> Widget (botao2)
#           -> Widget (botao3)
#   -> show
# -> exec
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Functions
def slot_example1():
    print(1)

def slot_example2():
    print(2)

def slot_example3():
    print(3)


# Status bar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem da barra de status')

#### Menu
menu = window.menuBar()

### Opção 1
option1 = menu.addMenu('Opção 1')

## Opção 1.1
first_action  = option1.addAction('print(1)')
first_action.triggered.connect(slot_example1) # type: ignore

## Opção 1.2
second_action = option1.addAction('print(2)')
second_action.triggered.connect(slot_example2) # type: ignore

## Opção 1.3
third_action  = option1.addAction('print(3)')
third_action.triggered.connect(slot_example3) # type: ignore

### Opção 2
option2 = menu.addMenu('Opção 2')

## Opção 2.1
first_action  = option2.addAction('print(1)')
first_action.triggered.connect(slot_example1) # type: ignore

## Opção 2.2
second_action = option2.addAction('print(2)')
second_action.triggered.connect(slot_example2) # type: ignore

## Opção 2.3
third_action  = option2.addAction('print(3)')
third_action.triggered.connect(slot_example3) # type: ignore

### Opção 3
option3 = menu.addMenu('Opção 3')

## Opção 3.1
first_action  = option3.addAction('print(1)')
first_action.triggered.connect(slot_example1) # type: ignore

## Opção 3.2
second_action = option3.addAction('print(2)')
second_action.triggered.connect(slot_example2) # type: ignore

## Opção 3.3
third_action  = option3.addAction('print(3)')
third_action.triggered.connect(slot_example3) # type: ignore

####
window.show()
app.exec() # inicia o loop da aplicação


