import json
import codecs


with open('data/Lyrics_MFDOOM.json', 'r') as read_file:
    data = json.load(read_file)
    lyrics = []
    # print(len(data['songs']))
    for song in data['songs']:
        lyrics.append(song['lyrics'])
    # test = data['songs'][203]['lyrics']
    # print([test])
    # print(lyrics[203])

with codecs.open('data/Lyrics_MFDOOM.txt', 'w', encoding='utf8') as f:
    for item in lyrics:
        # if '[' not in item:
        item.replace('[Instrumental]\n','')
        item += '\n'
        f.write(item)