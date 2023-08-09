import os

def stop_app(user_os, name_of_app):
    if user_os == 'macos':
        #NEED TO CONFIGURE
    elif user_os == 'win':
        #NEED TO CONFIGURE
    else:
        os.system(f'pkill {name_of_app}')