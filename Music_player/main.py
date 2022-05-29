from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from GUI import main_menu


if __name__ == '__main__':
    import sys
    import os
    # Исправление ошибки с длительностью аудиодорожки QtMediaPlayer
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon('GUI/logo.png'))
    mm = main_menu.MainMenu()
    mm.window_itself.show()
    sys.exit(app.exec_())


