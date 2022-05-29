from PyQt5 import QtCore, QtWidgets, QtGui


class AboutAppWindow:
    def __init__(self):
        self.window_itself = QtWidgets.QDialog()
        self.window_itself.setStyleSheet("background-color: white;border: 1px solid white; font-size: 15px")
        self.window_itself.setWindowTitle('О приложении')
        self.window_itself.setWindowIcon(QtGui.QIcon('GUI/info.png'))

        self.text_layout = QtWidgets.QVBoxLayout()

        self.text = QtWidgets.QLabel()
        self.text.setText('Данное приложение было разработано Вахрушевым Романом Андреевичем ИСПк-203-52-00 в ходе учебной практики УП 05.\
        \nОно используется для воспроизведения аудио-файлов различных форматов.')
        self.text_layout.addWidget(self.text)

        self.window_itself.setLayout(self.text_layout)

    def show(self):
        self.window_itself.exec()
