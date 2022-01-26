def make_album(singer_name, album_name, song_numbers=None):
    if song_numbers:
        album_information = {'singer_name': singer_name, 'album_name': album_name, 'song_numbers': song_numbers}
    else:
        album_information = {'singer_name': singer_name, 'album_name': album_name}
    return album_information


print(make_album('AAA', 'aaa'))
print(make_album('BBB', 'bbb', 10))
print(make_album('CCC', 'ccc', 20))

while True:
    print("enter 'quit' to quit ")
    singer_name = input("please input singer‘s name:")
    if singer_name == 'quit':
        break
    album_name = input("please input album's name:")
    print(make_album(singer_name, album_name))
