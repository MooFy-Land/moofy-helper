import take_from_database from MORE_SECRET

def input_just_voice():
    '''
            phrase = somehow stream voice for 5 sec
            print(phrase, 'am i correctly heard you?(y/n)')
            if 'y' in input().lower():
            print('cool, phrase done then')

            return phrase

    '''
    return voice_command
def reg1():
    print("please say how are you going to call this command\n")
    while True:
        print("i'm listening...")
        command = input_just_voice()
        clear()
        print(f"cool.now let's check. are you going to call it like {command}?(y/n)\n")
        answer = input().lower()
        if "y" in answer:
            clear()
            break
        else:
            clear()
            print("fine let's try it again then\n")

    print("cool. now i need the path where is your app which you want to start with this command\n>>>")
    while True:
        user_app_mb = input()
        try:
            print('now i will test this app for correctly working')
            do_command('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            do_command('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands('open', name = command, app = path)
    print("great we've done it!")
    clear()

    return


def reg2():
    if take_from_database(1) in 'linux, macOS':
        print('in fact it is almoast the same with first option, so then just think that "app" its an "tool"')
        reg1()
    else:
        print('your os is not allowed for this option(sorry)')
    return

def reg3():
    print("please say how are you going to call this command\n")
    while True:
        print("i'm listening...")
        command = input_just_voice()
        clear()
        print(f"cool.now let's check. are you going to call it like {command}?(y/n)\n")
        answer = input().lower()
        if "y" in answer:
            clear()
            break
        else:
            clear()
            print("fine let's try it again then\n")
    while True:
        print('secondly i need the name of platfrom, artist and the name of track what you want to start with this command\nplatfrom:')
        platform = input('\nartist:')
        artist = input('\ntrack:')
        track = input()

        try:
            get_track_id(platform, artist, track)
            clear()
            break
        except:
            print(f'you put something wrong. i cant finde this track on {platform}\ncheck your options and try it again please')
            clear()

    put_to_database_of_commands('track', command, platform, artist, track)
    print("great we've done it!")
    clear()

    return


def reg4():
    print("this command need just you'r voice tag. so say it")
    while True:
        print("i'm listening...")
        command = input_just_voice()
        clear()
        print(f"cool.now let's check. are you going to call it like {command}?(y/n)\n")
        answer = input().lower()
        if "y" in answer:
            clear()
            break
        else:
            clear()
            print("fine let's try it again then\n")

    put_to_database_of_commands('exit', command)
    clear()

    return


def reg5():
    print("please say how are you going to call this command\n")
    while True:
        print("i'm listening...")
        command = input_just_voice()
        clear()
        print(f"cool.now let's check. are you going to call it like {command}?(y/n)\n")
        answer = input().lower()
        if "y" in answer:
            clear()
            break
        else:
            clear()
            print("fine let's try it again then\n")

    print("cool. now i need the path where is your app which you want to start with this command\n>>>")
    while True:
        user_app_mb = input()
        try:
            print('now i will test this app for correctly working')
            do_command('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            do_command('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands('close', name=command, app=path)
    print("great we've done it!")
    clear()

    return


