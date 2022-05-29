from PyQt5 import QtWidgets, QtGui


class InstructionWindow:
    def __init__(self):
        self.window_itself = QtWidgets.QDialog()
        self.window_itself.setStyleSheet("background-color: white;border: 1px solid white; font-size: 15px")
        self.window_itself.setWindowTitle('Как пользоваться')
        self.window_itself.setWindowIcon(QtGui.QIcon('GUI/info.png'))

        self.text_layout = QtWidgets.QVBoxLayout()

        self.text = QtWidgets.QLabel()
        self.text.setText('Для прослушивания музыки ее нужно добавить в плейлист. Ее можно добавить как из\
                          \nглавного меню, так и с помощью контекстного меню в окне прослушивания (там же можно и\
                          \nудалить файлы из плейлиста).')
        self.text_layout.addWidget(self.text)

        self.window_itself.setLayout(self.text_layout)

    def show(self):
        self.window_itself.exec()
