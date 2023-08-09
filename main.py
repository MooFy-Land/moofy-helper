from SECRET import *

list_of_able_os = ['macOS, Windows, linux']

def detect_first_time():
    if take_from_database(4) == None:
        return(True)
    else:
        return(False)


def register():
    global list_of_able_os
    print('hello how do you do?')
    mood = input()
    print("fine i think you are not here for this\nlet's register you")
    sleep(1)
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






def menu():
    print("""MooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFyMooFYMooFyMooFyMooFyMooFy
                                                                   here we go again""")
    if detect_fist_time() == True:
        print("                                         my official name is MooFy-helper\nbut you can rename me in register step")
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


def main():
    choice = menu()
    do_it(choice)




if __name__ == '__main__':
    while True:
        main()
