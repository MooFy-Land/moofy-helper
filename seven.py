import os

def off_comp(user_os):
    if user_os == 'linux':
        os.system('sudo poweroff -f')
    elif user_os == 'macos':
        os.system('sudo shutdown -h now')
    elif user_os == 'windows':
        os.system('shutdown /s')

    return