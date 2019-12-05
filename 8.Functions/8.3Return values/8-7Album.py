def make_album(singer_name,album_name,music_number=''):
    album_info = {'singer':singer_name,'album':album_name}
    if music_number:
        album_info['music_number'] = music_number
        return album_info
    else:
        return album_info
album = make_album('simger1','album1')
print(album)
album = make_album('singer2','album2',music_number = 8)
print(album)
