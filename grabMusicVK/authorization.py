"""
Authorization module.
checkConnection: try open google.com;
getMusicList: return list musics user if data is correct, else empty dict.
"""
import vk
import urllib.request


def checkConnection():
    """ Return True or False. """
    return urllib.request.urlopen('http://google.com', timeout=1)


def getMusicList(name, password, inv):
    """
    name: str;
    password: str;
    inv: boolean, True if set invisible user else False;
    return dict.
    """
    if not checkConnection():
        return False

    session = vk.AuthSession(app_id='5566502', user_login=name,
                             user_password=password, scope='audio')
    api = vk.API(session)

    if inv: api.account.setOffline()

    musics = api.audio.get() or {}
    try:
        return {'%s - %s' % (s['artist'], s['title']): s['url'] for s in musics}
    except Exception:
        return {}
