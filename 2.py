import os

def tool_for_mac(path, type, tool_name):

def tool_for_win(path, type, tool_name):
'''

        NEED TO BE INICILIZED

'''

def tool_for_linux(path, type, tool_name):
    os.system(f'cd {path}')

    if type == 'py':
        os.system(f'python3 {tool_name}')
    elif type == 'bash':
        os.system(f'bash ./{tool_name}')
    else:
        '''
            NEED TO UNDERSTAND WHAT WILL THE THIRD TYPE
        '''



def tool(user_os, path, type, tool_name):
    if user_os == 'macos':
        tool_for_mac(path, type, tool_name)
    elif user_os == 'win'
        tool_for_win(path, type, tool_name)
    else:
        tool_for_linux(path, type, tool_name)