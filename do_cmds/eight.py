import os

def reboot_comp(user_os):
    if user_os in 'linux macos':
        os.system('sudo reboot')
    else:
        os.system('shutdown /r')
    return