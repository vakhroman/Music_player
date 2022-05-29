from PyQt5 import QtWidgets
import GLOBAL


# Функция вызова диалогового окна для получения пути до музыкального файла
def grab_music():
    window = QtWidgets.QFileDialog()
    window.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
    return window.getOpenFileNames(window, 'Выберите файл', filter='Аудио-файлы (*.mp3)')[0]


def add_music_to_current_playlist(music_list):
    playlist_content = get_playlist_content()
    playlist_file = open(GLOBAL.CURRENT_PLAYLIST, 'a')
    for music_file in music_list:
        if music_file+'\n' not in playlist_content:
            playlist_file.write(music_file+'\n')


def get_playlist_content():
    playlist_content = []
    file = open(GLOBAL.CURRENT_PLAYLIST)
    for line in file:
        playlist_content.append(line)
    return playlist_content
