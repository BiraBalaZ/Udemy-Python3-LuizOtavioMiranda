import sys

from styles import setupTheme
from info import Info
from display import Display
from main_window import MainWindow
from buttons import ButtonsGrid
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget,
                               QLabel)

def temp_label(texto, font_size = 150):
    label = QLabel(texto)
    label.setStyleSheet(f'font-size: {font_size}px')
    return label

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Info
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    # Display da Calculadora
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vertical_layout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFizedSize()
    window.show()
    app.exec()


