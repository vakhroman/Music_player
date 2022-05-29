from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QUrl as QUrl5
from GUI import playlist_model
from file_catcher import music_import, music_delete
import GLOBAL


class MusicWindow:
    def __init__(self):
        self.volume_active = True
        # Инициализируем окно
        self.window_itself = QtWidgets.QMainWindow()
        self.window_itself.setWindowIcon(QtGui.QIcon('GUI/logo.png'))
        self.window_itself.setWindowTitle('Музыкальный проигрыватель')
        self.content_list = QtMultimedia.QMediaPlaylist()
        self.fix_window_size()
        GLOBAL.MUSIC_PLAYER.setPlaylist(self.content_list)
        GLOBAL.MUSIC_PLAYER.currentMediaChanged.connect(self.update_track_name)
        GLOBAL.MUSIC_PLAYER.positionChanged.connect(self.update_position)
        GLOBAL.MUSIC_PLAYER.durationChanged.connect(self.update_duration)
        # Настройки главного макета
        self.central_widget = QtWidgets.QWidget(self.window_itself)
        self.central_widget.setStyleSheet("background-color: white")
        self.central_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.window_itself.setCentralWidget(self.central_widget)

        self.init_track_info_and_control_panel()
        self.init_playlist_content_viewer()

    def init_playlist_content_viewer(self):
        self.playlist_content_viewer = QtWidgets.QListView()
        self.playlist_content_viewer.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.playlist_content_viewer.setStyleSheet("border: 1px solid #f31e39")
        self.update_playlist_content()
        self.playlist_content_viewer.setModel(playlist_model.PlaylistModel(self.content_list))
        self.central_layout.addWidget(self.playlist_content_viewer)
        self.playlist_content_viewer.doubleClicked.connect(self.play_selected_song)
        self.playlist_content_viewer.customContextMenuRequested.connect(self.context_menu_listener_for_music_list)

    def update_playlist_content(self):
        self.content_list.clear()
        try:
            playlist_files = open(GLOBAL.CURRENT_PLAYLIST)
            for file in playlist_files:
                media = QtMultimedia.QMediaContent(QUrl5.fromLocalFile(file[0:len(file) - 1]))
                self.content_list.addMedia(media)
        except FileNotFoundError:
            playlist_files = open(GLOBAL.CURRENT_PLAYLIST, 'w')
            for file in playlist_files:
                media = QtMultimedia.QMediaContent(QUrl5.fromLocalFile(file[0:len(file) - 1]))
                self.content_list.addMedia(media)

    def play_selected_song(self):
        GLOBAL.MUSIC_PLAYER.playlist().setCurrentIndex(self.playlist_content_viewer.currentIndex().row())
        GLOBAL.MUSIC_PLAYER.play()

    def update_duration(self):
        self.total_duration.setText(hhmmss(GLOBAL.MUSIC_PLAYER.duration()))
        self.timeSlider.setMaximum(GLOBAL.MUSIC_PLAYER.duration())

    def update_position(self):
        self.current_duration.setText(hhmmss(GLOBAL.MUSIC_PLAYER.position()))
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(GLOBAL.MUSIC_PLAYER.position())
        self.timeSlider.blockSignals(False)

    def update_track_name(self):
        self.track_name.setText(str(GLOBAL.MUSIC_PLAYER.playlist().currentMedia().canonicalUrl().fileName()))

    def init_track_info_and_control_panel(self):
        self.track_info_and_control_panel_layout = QtWidgets.QVBoxLayout()

        self.track_info = QtWidgets.QVBoxLayout()
        self.track_info.setSpacing(0)

        self.track_icon = QtWidgets.QLabel()
        self.track_icon.setPixmap(QtGui.QPixmap('GUI/logo.png'))

        self.track_name = QtWidgets.QLabel()
        self.track_name.setText(str(GLOBAL.MUSIC_PLAYER.playlist().currentMedia().canonicalUrl().fileName()))

        self.time_info = QtWidgets.QHBoxLayout()
        self.time_info.setSpacing(5)

        self.current_duration = QtWidgets.QLabel()
        self.current_duration.setText('00:00')

        self.timeSlider = QtWidgets.QSlider()
        self.timeSlider.setMaximum(0)
        self.timeSlider.setStyleSheet('QSlider::groove:horizontal {\
            height: 10px;\
            margin: 0px;\
            border-radius: 5px;\
            background: #a5a6a5;\
            } QSlider::handle:horizontal {background: \
            #f31e39;border: 1px none #f31e39;width: 17px;margin: -5px 0;border-radius: 8px}\
            QSlider::sub-page:qlineargradient {background: #f31e39;border-radius: 5px }')
        self.timeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.timeSlider.valueChanged.connect(GLOBAL.MUSIC_PLAYER.setPosition)

        self.total_duration = QtWidgets.QLabel()
        self.total_duration.setText('00:00')

        self.time_info.addWidget(self.current_duration)
        self.time_info.addWidget(self.timeSlider)
        self.time_info.addWidget(self.total_duration)

        self.track_info.addWidget(self.track_icon)
        self.track_info.addWidget(self.track_name)
        self.track_info.addLayout(self.time_info)

        self.button_box = QtWidgets.QHBoxLayout()

        self.previous_button = QtWidgets.QPushButton()
        self.previous_button.setIcon(QtGui.QIcon('GUI/buttons/control-skip-180.png'))
        self.previous_button.clicked.connect(GLOBAL.MUSIC_PLAYER.playlist().previous)
        self.button_box.addWidget(self.previous_button)

        self.play_button = QtWidgets.QPushButton()
        self.play_button.setIcon(QtGui.QIcon('GUI/buttons/control.png'))
        self.play_button.clicked.connect(self.play_selected_song)
        self.button_box.addWidget(self.play_button)

        self.pause_button = QtWidgets.QPushButton()
        self.pause_button.setIcon(QtGui.QIcon('GUI/buttons/control-pause.png'))
        self.pause_button.clicked.connect(GLOBAL.MUSIC_PLAYER.pause)
        self.button_box.addWidget(self.pause_button)

        self.stop_button = QtWidgets.QPushButton()
        self.stop_button.setIcon(QtGui.QIcon('GUI/buttons/control-stop-square.png'))
        self.stop_button.clicked.connect(GLOBAL.MUSIC_PLAYER.stop)
        self.button_box.addWidget(self.stop_button)

        self.next_button = QtWidgets.QPushButton()
        self.next_button.setIcon(QtGui.QIcon('GUI/buttons/control-skip.png'))
        self.next_button.clicked.connect(GLOBAL.MUSIC_PLAYER.playlist().next)
        self.button_box.addWidget(self.next_button)

        self.volume_button = QtWidgets.QPushButton()
        self.volume_button.setIcon(QtGui.QIcon('GUI/buttons/speaker-volume.png'))
        self.volume_button.clicked.connect(self.mute_or_unmute)
        self.volume_button.setFlat(True)
        self.button_box.addWidget(self.volume_button)

        self.volume_slider = QtWidgets.QSlider()
        self.volume_slider.setStyleSheet('QSlider::groove:horizontal {\
            height: 10px;\
            margin: 0px;\
            border-radius: 5px;\
            background: #a5a6a5;\
            } QSlider::handle:horizontal {background: \
            #f31e39;border: 1px none #f31e39;width: 17px;margin: -5px 0;border-radius: 8px}\
            QSlider::sub-page:qlineargradient {background: #f31e39;border-radius: 5px }')
        self.volume_slider.sliderMoved.connect(GLOBAL.MUSIC_PLAYER.setVolume)
        self.volume_slider.setValue(GLOBAL.MUSIC_PLAYER.volume())
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.button_box.addWidget(self.volume_slider)

        self.track_info_and_control_panel_layout.addLayout(self.track_info)
        self.track_info_and_control_panel_layout.addLayout(self.button_box)
        self.central_layout.addLayout(self.track_info_and_control_panel_layout)

    def show(self):
        self.window_itself.show()

    def return_to_main_menu(self):
        self.window_itself.close()

    def fix_window_size(self):
        self.window_itself.setFixedSize(700, 200)

    def mute_or_unmute(self):
        if self.volume_active:
            self.volume_active = False
            self.volume_button.setIcon(QtGui.QIcon('GUI/buttons/speaker-no-volume'))
            GLOBAL.MUSIC_PLAYER.setMuted(True)
        else:
            self.volume_active = True
            self.volume_button.setIcon(QtGui.QIcon('GUI/buttons/speaker-volume'))
            GLOBAL.MUSIC_PLAYER.setMuted(False)

    def context_menu_listener_for_music_list(self, position):
        menu = QtWidgets.QMenu()
        add_file_action = menu.addAction('Добавить файл')
        delete_file_action = menu.addAction('Удалить файл')
        user_action = menu.exec_(self.window_itself.sender().mapToGlobal(position))
        if user_action == add_file_action:
            music_import.add_music_to_current_playlist(music_import.grab_music())
            self.update_playlist_content()
            self.playlist_content_viewer.setModel(playlist_model.PlaylistModel(self.content_list))
        elif user_action == delete_file_action:
            selected_files = self.playlist_content_viewer.selectionModel().selectedIndexes()
            if len(selected_files) > 0:
                music_delete.delete_file(selected_files[0].row())
                self.update_playlist_content()
                self.playlist_content_viewer.setModel(playlist_model.PlaylistModel(self.content_list))


def hhmmss(ms):
    h, r = divmod(ms, 3600000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))
