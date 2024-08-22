# QWidget e QLaout de PySide6.Qtidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros wodgets
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 20px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 20px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 20px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show() # Central widget entra na hierarquia e mostra sua janela
app.exec() # inicia o loop da aplicação
