import os

def lock_comp(user_os):
    if user_os == 'linux':
        os.system('gnome-screensaver-command -l')
    elif user_os == 'macos':
        os.system('sudo pkill loginwindow')
    elif user_os == 'windows':
        os.system('rundll32.exe user32.dll,LockWorkStation')

    return