"""
@author: akanoi
@license GNU LESSER GENERAL PUBLIC LICENSE v3
Copyright (C) 2016
"""
#!/usr/bin/env python
# coding=utf-8
import sys
import os
import urllib.request as ur
import authorization
import supportFunc as sf


def main():
    flags = sf.getFlags(sys.argv)
    sf.activateFlags(flags)

    user = input('Tel. number or e-mail: ')
    pswd = input('Password: ')

    songs = authorization.getMusicList(user, pswd, sf.inv)

    if not songs:
        print('No connection to Internet or incorrect login/password,' \
               'try again later!')
        print('Exiting the program ...')
        sys.exit()

    count_songs = len(songs)
    if not sf.answ:
        answer = input('You have %s songs. Start download?(y/n): ' % count_songs)
        if answer != 'y':
            print('Exiting the program ...')
            sys.exit()

    while True:
        path = r'%s/MusicVK' % os.getcwd()

        if not sf.drc:
            path = os.path.expanduser(input('Enter path' +
                        '(leave blank to install in the current folder): '))

        if os.path.exists(path):
            break

        print('This folder does not exist or has an invalid path!')

    if not os.path.exists(path):
        os.makedirs(path)

    os.chdir(path)  # Moving to correct directory

    check_conflict = ['n', 'y'] [sf.answ]
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
        except Exception:
            if not sf.write: print('%s not downloaded!' % song)
            log['error'] += 1
            continue
        else:
            log['done'] += 1
            if not sf.write: print('%s downloaded! %d из %d' % (song, \
                                                     log['done'], count_songs))

    print('Load complete.')
    print('Downloaded %d of the %d, with an error - %d' % (log['done'], \
                                                    count_songs, log['error']))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
