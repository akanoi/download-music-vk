import vk
import urllib.request


def check_connection():
    return urllib.request.urlopen('http://google.com', timeout=1)


def get_music_list(name, password):
    if not check_connection():
        return False

    session = vk.AuthSession(app_id='5566502', user_login=name,
                             user_password=password, scope='audio')
    api = vk.API(session)

    musics = api.audio.get()
    return {'%s - %s' % (s['artist'], s['title']): s['url'] for s in musics}
