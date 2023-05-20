from first import app
from chetverka import stop_me
from fifth import stop_app
from third import detect_platform
from six import oepn_site

def do_command(type, user_os, application, track, artist):
    if type == 'open':
        app(user_os, application)

    elif type == 'kill':
        stop_app(user_os, application)

    elif type == 'close':
        stop_me()

    elif type == 'song':
        detect_platform(user_os, track, artist)

    elif type == 'site':
        open_site()
