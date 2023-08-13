import os, time
from main import menu
from MORE_SECRET import reg_new_command, input_voice_command, say, do_command, take_from_database, add_to_database, take_from_list_of_commands

list_of_able_os = ['macOS, Windows, linux']

pages = ["""                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |1. open some app             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |2. open some tool|for linux  |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |3. maybe start some song?    |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |4. stop me                   |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                                WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |5. stop some app             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |6. open some site            |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |7. turn off my computer      |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |8. reboot my computer        |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |9. lock my computer          |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |10. destroy my comp|dangerous|MooFyMooFyMooFyMooFyMooFyMooFy| VERY DANGEROUS| NO WAY TO BACK IT
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |11. fill in card details     |MooFyMooFyMooFyMooFyMooFyMooFy| (CREDIT CARD) NOT AVALIBALE AT THE MOMENT
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |12.do a call by available app|MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |13. connect with alisa stance|MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |14. connect with some stuff  |MooFyMooFyMooFyMooFyMooFyMooFy| it may be a smart desk or maybe 
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |15. tell a joke              |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |16. kit of available options |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------"""]

def detect_fist_time():
    if take_from_database(4) == None:
        return(True)
    else:
        return(False)


def register():
    global list_of_able_os
    print('hello how do you do?')
    mood = input()
    print("fine i think you are not here for this\nlet's register you")
    sleep(3)
    while True:
        clear()
        print("first what i need it's your os\n>>>")
        try:
            user_os = more_similar_os(input().lower())
            if user_os == False:
                print(f"i don't know this os\n i work only with such os as\n{list_of_able_os}")
            else:
                yes_no = input(f'well your os is {user_os} isnt it?(yes/no)').lower()
                while True:
                    if yes_no in ['yes', 'no']:
                        if yes_no == 'yes':
                            break
                        else:
                            print("fine let's try it again")
                            break
                    else:
                        yes_no = input('yes/no only').lower()
                if yes_no == 'yes':
                    print("fine let's go further")
                    break
        except:
            print('man how did you do an erorr. please type your os')

    add_to_database(user_os, 1)

    print('second what i need it is how you want to call me\n>>>')

    add_to_database(input(), 2)

    print('and last what i need it is how can I call you?')

    add_to_database(input(), 3)

    return

def menu():
    print("""MooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFy
                                                                   here we go again""")
    if detect_fist_time() == True:
        print("                                         my official name is MooFy\nbut you can rename me in register step")
        register()
    print("""                                 MENU
             ______________________________________________________________
             | 1. log new command          |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             | 2. re-register your voice   |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             | 3.clear screen and start    |MooFyMooFyMooFyMooFyMooFyMooFy|
             |         working             |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             | 4. stop me                  |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             | 5. write an review          |MooFyMooFyMooFyMooFyMooFyMooFy|
             |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
             | 6. delete me for ever       |MooFyMooFyMooFyMooFyMooFyMooFy|
             --------------------------------------------------------------""")
    print('what do you want?\n>>>')
    while True:
        try:
            n = int(input())
            if n < 7 and n > 0:
                return(n)
            else:
                print('only digit 1-6')
        except:
            print('seems like you put not digit here, try it again')

def delete_all_files(path):
    os.system(f'rm -r {path}')


def sleep(long):
    time.sleep(long)

def clear():
    sleep(1)
    os.system('clear')


def log_new_command():
    page = 0
    print(pages[page])
    n = input('what do you want?\n>>>')

    while n == 'next' or n == 'return':
        clear()
        if n == 'return':
            return('menu')
        print(pages[page + 1])
        page += 1
        n = input('\n>>>')

    while True:
        try:
            n = int(n)
            if n < 17 and n > 0:
                return (n)
            else:
                print('only digit 1-16')
        except:
            print('seems like you put not digit here, try it again')
            n = input('>>>')




def more_similar_os(user_os):
    list_of_len_sim = []
    list_of_able_os = ['macos, windows, linux']
    for i in list_of_able_os:
        count = 0
        for j in range(len(user_os)):
            if user_os[j] == i[j]:
                count += 1
        list_of_len_sim.append(count)

    if max(list_of_len_sim) < 2:
        return(False)
    else:
        return(list_of_able_os[list_of_len_sim.index(max(list_of_len_sim))])


def find_more_similar_command(cmd):
    list_of_len_sim = []
    list_of_commads = take_from_database('list_of_commands')
    for i in list_of_commads:
        count = 0
        for j in range(len(cmd)):
            if cmd[j] == i[j]:
                count += 1
        list_of_len_sim.append(count)

    return(list_of_commads[count.index(max(count))])

def check_values(values):
    for value in values:
        if  not (1 <= value <= 16):
            return False
    return True


def start():
    while True:
        command = input_voice_command()
        if take_from_list_of_commands(2) in command:
            try:
                do_command(command)
            except:
                say('smth went wrong, sorry, try it again')

def do_it(choice):

    while True:
        while True:
            try:
                n = input('ur choice?\n>>>')
                if n.isdigit() and 0 < int(n) < 7:
                    choice = int(n)
                    break

                else:
                    print('looks like u put not a digit from 1 to 6, try it again')

            except:
                print('smth went wrong, please try it again')

        if choice == 1:
            what_is_new_command = log_new_command()
            if what_is_new_command != 'menu':
                if what_is_new_command == 16:  #new
                    kit = True
                    while True:
                        try:
                            what_is_new_command = list(map(int, input('please enter the command number you would like to include in this protocol in the part provided').split()))
                            if check_values(what_is_new_command):
                                print('cool, lets register it all now')
                                break
                            else:
                                print('you wrote a number of command that i dont have, try again')
                        except:
                            print('only digits are allowed')

                else:
                    kit = False
                reg_new_command(what_is_new_command, kit)
            clear()
            menu()

        elif choice == 2:
            print("i just kidding. i don't need to reg your voice")
            sleep(3)
            clear()
            menu()

        elif choice == 3:
            clear()
            start()

        elif choice == 4:
            clear()
            exit(0)

        elif choice == 5:
            print("if you really want to write an review you can go to my official git repo\nhere it is: https://github.com/dima228132/moofy-helper\nor my tg channel: https://t.me/MooFy_chan")
            sleep(15)
            clear()
            menu()

        elif choice == 6:
            try:
                print("it was great to meet you. i hope i helped you.goodbye")
                delete_all_files('./')
            except:
                print('smth went wrong please try it again')
                sleep(2)
                clear()
                menu()