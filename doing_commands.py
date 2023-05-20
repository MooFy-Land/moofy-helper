from first import app
from chetverka import stop_me
from fifth import stop_app
from third import detect_platform
from six import open_site
from seven import off_comp
from eight
from nine import lock_comp
from ten import OH_FCK_LETS_DO_IT
def do_command(type, user_os, application, track, artist, link):
    if type == 'open':
        app(user_os, application)

    elif type == 'kill':
        stop_app(user_os, application)

    elif type == 'close':
        stop_me()

    elif type == 'song':
        detect_platform(user_os, track, artist)

    elif type == 'site':
        open_site(application, link)

    elif type == 'off':
        off_comp(user_os)

    elif type == 'lock':
        lock_comp(user_os)

    elif type == '!___destroy___!':
        OH_FCK_LETS_DO_IT(user_os)

