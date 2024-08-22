# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('BUTTON')
botao.setStyleSheet('''
    font-size: 40px;
    font-weight: bold;
    color: red;
    background-color: black;
''')
botao.show() # Adiciona o Widget na hierarquia e exibe a janela

# botao2 = QPushButton('Botão 2')
# botao2.show()

app.exec() # inicia o loop da aplicação
