
#!/usr/bin/env python
# coding=utf-8
import sys
import os
import urllib.request as ur
from authorization import get_music_list

try:
    user, pswd = sys.argv[1], sys.argv[2]
except IndexError:
    user = input('Tel. number or e-mail: ')
    pswd = input('Password: ')

songs = get_music_list(user, pswd)

if not songs:
    print('No connection to Internet, try again later!')
    print('Exiting the program ...')
    sys.exit()

count_songs = len(songs)
answer = input('You have %s songs. Start download?(y/n): ' % count_songs)
if answer != 'y':
    print('Exiting the program ...')
    sys.exit()

while True:
    path = os.path.expanduser(input('Enter path' +
                      '(leave blank to install in the current folder): '))

    if not path:
        path = r'%s/MusicVK' % os.getcwd()
        break

    if os.path.exists(path):
        break

    print('This folder does not exist or has an invalid path!')

if not os.path.exists(path):
    os.makedirs(path)

os.chdir(path)  # Moving to correct directory

check_conflict = input('Ask if there is a conflict?(y/n): ')
print('Start downloading!')
log = {
    'done': 0,
    'error': 0
}
for song in songs:
    file_name = '%s.mp3' % song
    if check_conflict != 'y' and os.path.exists(r'%s/%s' % (path, file_name)):
        answer = input('File already exists! Rewrite?(y/n): ')
        if not answer == 'y':
            continue

    try:
        ur.urlretrieve(songs[song], filename=file_name)  # Downloading music
    except Exception as e:
        raise e
        print('%s not downloaded!' % song)
        log['error'] += 1
        continue
    else:
        log['done'] += 1
        print('%s downloaded! %d из %d' % (song, log['done'], count_songs))

print('Load complete.')
print('Downloaded %d of the %d, with an error - %d' % (log['done'], count_songs, log['error']))
