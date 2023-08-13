from time import sleep

def input_just_voice():
    #stream voice for 5 seconds
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
    print('in fact it is almoast the same with first option, so then just think that "app" its an "tool"')
    reg1()
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
            do_command('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            do_command('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands('kill', name=command, app=path)
    print("great we've done it!")
    clear()

    return


def reg6():
    print('hear for first i need to know what browser are you using for it')
    while True:
        print('''
        1. google chrome
        2. firefox
        3. yandex browser
        4. tor browser
        choose from this list please''')
        browser = input('>>>')
        if browser.isdigit() and 1 <= browser <= 4:
            print("cool i also use it, let's go futher")
            break
        else:
            print('only digits from 1 to 4, retry please')

    print('now i need to know what site would you want to open with this command')
    while True:
        site = input('format https:// or http://\n>>>')
        if 'http' in site and '://' in site:
            if check_site():
                print('done')
                break
            else:
                print("this site is'nt working, try another one")
        else:
            print("wrong formart, please try again")

    print("now let's give a voice command")
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
    put_to_database_of_commands('site', name=command, site=site, browser=browser)
    print('command now working you can test it')

    return

def reg7():
    print("here i need only your voice command")
    time.sleep(2)
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
    put_to_database_of_commands('site', name=command, site=site, browser=browser)
    print('command now working you can test it')



