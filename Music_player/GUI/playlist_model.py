from PyQt5 import QtCore, QtGui


class PlaylistModel(QtCore.QAbstractListModel):
    def __init__(self, playlist):
        super(PlaylistModel, self).__init__()
        self.playlist = playlist

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.playlist.media(index.row()).canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()
