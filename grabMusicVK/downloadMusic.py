#!/usr/bin/env python
#coding=utf-8


"""
@author: akanoi
@license GNU LESSER GENERAL PUBLIC LICENSE v3
Copyright (C) 2016
"""


import sys
import os
import requestllib.request
import grabMusicVK.authorization
import grabMusicVK.flagsControl


def downloadMusic(songs, flag_conflict, flag_show):
    """
    Download song in songs list and return log downloading.
    songs: list song;
    flag_conflict: string variable, "n" or "y";
    flag_show: varible 'show' module flagsControl
    """

    log = {
        'done': 0,
        'error': 0
    }

    for song in songs:
        file_name = '%s.mp3' % song
        rewriteFile = os.path.exists(r'%s/%s' % (path, file_name))
        if check_conflict != 'y' and rewriteFile:
            answer = input('File already exists! Rewrite?(y/n): ')
            if answer != 'y':
                continue

        try:
            request.requestlretrieve(songs[song], filename=file_name)  # Downloading music
        except Exception as exception:
            log['error'] += 1

            if not flag_show: 
                print('%s not downloaded!' % song)
                print(exception)
            continue
        else:
            log['done'] += 1

            if not flag_show: 
                print('%s downloaded! %d of %d' % (song, log['done'], count_songs))

    return log


def getPath(flag_directory):
    while True:
        path = r'%s/MusicVK' % os.getcwd()

        if not flag_directory:
            path = os.path.expanduser(input('Enter path' +
                        '(leave blank to install in the crequestrent folder): '))

        if os.path.exists(path):
            break

        print('This folder does not exist or has an invalid path!')

    return path


def getSongs(flag_invisible):
    user = input('Tel. number or e-mail: ')
    password = input('Password: ')

    songs = authorization.getMusicList(user, password, flag_invisible)

    if not songs:
        print('No connection to Internet or incorrect login/password,' \
               'try again later!')
        print('Exiting the program ...')
        sys.exit()

    return song


def main():
    flags = flagsControl.getFlags(sys.argv)
    flagsControl.activateFlags(flags)

    songs = getSongs(flagsControl.invisible)

    count_songs = len(songs)
    if not flagsControl.answer:
        answer = input('You have %s songs. Start download?(y/n): ' % count_songs)
        if answer != 'y':
            print('Exiting the program ...')
            sys.exit()

    path = getPath(flagsControl.directory)
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)  # Moving to correct directory

    print('Start downloading!')
    check_conflict = ['n', 'y'] [flagsControl.answer]
    log = downloadMusic(songs, check_conflict, flagsControl.show)

    print('Load complete.')
    print('Downloaded %d of the %d, with an error - %d' % (log['done'], \
                                                    count_songs, log['error']))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

