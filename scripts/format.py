import json
import codecs


with open('data/Lyrics_MFDOOM.json', 'r') as read_file:
    data = json.load(read_file)
    lyrics = []
    for song in data['songs']:
        lyrics.append(song['lyrics'])
    test = data['songs'][0]['lyrics']
    print([test])

with codecs.open('test.txt', 'w', encoding='utf8') as f:
    for item in lyrics:
        if '[' not in item:
            item += '\n'
            f.write(item)