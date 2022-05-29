from PyQt5 import QtCore, QtWidgets, QtGui

import GUI.music_window
from GUI import mm_buttons, about_app_window, instruction_window
from file_catcher.music_import import *


class MainMenu:
    def __init__(self):
        # Инициализируем окно
        self.window_itself = QtWidgets.QMainWindow()
        self.window_itself.setStyleSheet("background-color: white;border: 1px solid white; font-size: 15px")
        self.window_itself.setWindowTitle('Музыкальный проигрыватель')
        self.window_itself.setWindowIcon(QtGui.QIcon('GUI/logo.png'))
        # Настройки главного макета
        self.central_widget = QtWidgets.QWidget(self.window_itself)
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.window_itself.setCentralWidget(self.central_widget)
        # Настройки приветственного текста
        self.starting_text = QtWidgets.QLabel('Добро пожаловать в музыкальный проигрыватель')
        self.central_layout.addWidget(self.starting_text)
        # Настройки логотипа
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap('GUI/logo.png'))
        # Настройки суб-макета
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.central_layout.addLayout(self.sub_layout)
        self.sub_layout.setSpacing(0)
        self.sub_layout.addWidget(self.logo)
        self.sub_layout.addLayout(mm_buttons.MMButtons().get_central_layout())

        # Вызовы под-окон
        self.sub_layout.itemAt(1).layout().itemAt(0).widget().clicked.connect(self.change_window_to_listener)
        self.sub_layout.itemAt(1).layout().itemAt(1).widget().clicked.connect(
            lambda: add_music_to_current_playlist(grab_music()))
        self.sub_layout.itemAt(1).layout().itemAt(2).widget().clicked.connect(self.change_window_to_instruction)
        self.sub_layout.itemAt(1).layout().itemAt(3).widget().clicked.connect(self.change_window_to_about_app)
        # Вызов функции закрепления размера окна
        self.fix_window_size()

    def fix_window_size(self):
        self.window_itself.setFixedSize(400, 170)

    def change_window_to_listener(self):
        self.window_itself.close()
        self.music_listener = GUI.music_window.MusicWindow()
        self.music_listener.show()

    def change_window_to_instruction(self):
        self.instruction_window = GUI.instruction_window.InstructionWindow()
        self.instruction_window.show()

    def change_window_to_about_app(self):
        self.about_app_window = GUI.about_app_window.AboutAppWindow()
        self.about_app_window.show()

