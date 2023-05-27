import os


def open_site(user_os, browser, link):

    if user_os == 'linux':
        os.system(f'{browser} {link}')
    elif user_os == 'macos':
        # open on mac os
    elif user_os == 'windows':
        # open on windows