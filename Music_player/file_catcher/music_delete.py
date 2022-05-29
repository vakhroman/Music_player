import GLOBAL

def delete_file(index):
    playlist_content = get_playlist_content()
    needed_string = playlist_content[index]
    file = open(GLOBAL.CURRENT_PLAYLIST, 'w')
    for line in playlist_content:
        if line != needed_string:
            file.write(line)


def get_playlist_content():
    playlist_content = []
    file = open(GLOBAL.CURRENT_PLAYLIST)
    for line in file:
        playlist_content.append(line)
    return playlist_content
