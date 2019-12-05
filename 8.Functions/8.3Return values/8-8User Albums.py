def make_album(singer_name,album_name,music_number=''):
    album_info = {'singer':singer_name,'album':album_name}
    if music_number:
        album_info['music_number'] = music_number
        return album_info
    else:
        return album_info
while True:
    print("\nPlease Enter album_information:")
    print("Please entet 'q' to quit" )
    s_name = input("singer_name:")
    a_name = input("album_name:")
    m_name = input("music_number:")
    if s_name == 'q':
        break
    if a_name == 'q':
        break
    to_make_album = make_album(s_name,a_name,m_name)
    print(to_make_album)