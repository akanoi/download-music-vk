#!/usr/bin/env python
#coding=utf-8


"""
Module with additional functions.
getFlags: return set as flags;
activateFlags: set answer, directory, show, invisible depending on flag;
HELP: str, help manual.
"""


import sys
import os

def getFlags(argv):
    """
    argv: sys.argv;
    return set.
    """

    flags = filter(lambda arg: arg if arg[0] == '-' else '', argv)
    return set(''.join(map(lambda arg: arg[1:], flags)))


def activateFlags(flags):
    """
    flags: list.
    """
    
    global answer, directory, show, invisible
    answer = directory = show = invisible = False
    if 'h' in flags:
        os.system('clear')
        print(HELP)
        sys.exit()
    if 'a' in flags:
        answer = True
    if 'd' in flags:
        directory = True
    if 'w' in flags:
        show = True
    if 'i' in flags:
        invisible = True


HELP = \
    """
    Help manual to grabMusicVK.

    Format a call:
        python main.py [flags]

    Flags:
            -h - print help manual
            -a - do not ask user if conflicts
            -d - use the default folder
            -w - not display the download process (the default output)
            -i - user are offline in the VK
    Other:
        By default the folder "MusicVK" in a program created for downloaded files.
        In a path you can use '~' to refer to home directory.
    """
