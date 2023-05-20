import os
def app_for_mac(name_of_app):
'''

            NEED TO BE INICILIZED

'''

def app_for_win(name_of_app):
'''

            NEED TO BE INICILIZED

'''

def app_for_linux(name_of_app):

    os.system(name_of_app)


def app(user_os, name_of_app):
    if user_os == 'macos':
        app_for_mac(name_of_app)
    elif user_os == 'windows':
        app_for_win(name_of_app)
    else:
        app_for_linux(name_of_app)