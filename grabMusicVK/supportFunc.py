"""
Module with additional functions.
getFlags: return set as flags;
activateFlags: set answ, drc, write, inv depending on flag;
HELP: str, help manual.
"""
import sys
import os

def getFlags(in_args):
    """
    in_args: sys.argv;
    return set.
    """
    _res = filter(lambda arg: arg if arg[0] == '-' else '', in_args)
    return set(''.join(map(lambda arg: arg[1:], _res)))


def activateFlags(flags):
    """
    flags: list.
    """
    global answ, drc, write, inv
    answ = drc = write = inv =False
    if 'h' in flags:
        os.system('clear')
        print(HELP)
        sys.exit()
    if 'a' in flags:
        answ = True
    if 'd' in flags:
        drc = True
    if 'w' in flags:
        write = True
    if 'i' in flags:
        inv = True


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
