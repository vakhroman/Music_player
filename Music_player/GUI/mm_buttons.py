from PyQt5 import QtWidgets, QtCore


class MMButtons:
    def __init__(self):
        self.central_layout = QtWidgets.QVBoxLayout()

        self.listen_music_button = QtWidgets.QPushButton()
        self.listen_music_button.setText('Послушать музыку')
        self.listen_music_button.setStyleSheet("background-color: #fd6f71;border: 1px solid #fd6f71;"
                                               "border-top-left-radius: 10px;border-top-right-radius: 10px;"
                                               "border-bottom-right-radius: 10px; color: white")
        self.central_layout.addWidget(self.listen_music_button)

        self.add_music_button = QtWidgets.QPushButton()
        self.add_music_button.setText('Добавить музыку')
        self.add_music_button.setStyleSheet("background-color: #fb5c63;border: 1px solid #fd6f71;"
                                            "border-top-right-radius: 10px;"
                                            "border-bottom-right-radius: 10px; color: white")
        self.central_layout.addWidget(self.add_music_button)

        self.help_button = QtWidgets.QPushButton()
        self.help_button.setText('Как пользоваться')
        self.help_button.setStyleSheet("background-color: #f74150;border: 1px solid #fd6f71;"
                                            "border-top-right-radius: 10px;"
                                            "border-bottom-right-radius: 10px; color: white")
        self.central_layout.addWidget(self.help_button)

        self.about_app_button = QtWidgets.QPushButton()
        self.about_app_button.setText('О приложении')
        self.about_app_button.setStyleSheet("background-color: #f31e39;border: 1px solid #fd6f71;"
                                               "border-bottom-left-radius: 10px;border-top-right-radius: 10px;"
                                               "border-bottom-right-radius: 10px; color: white")
        self.central_layout.addWidget(self.about_app_button)

    def get_central_layout(self):
        return self.central_layout
