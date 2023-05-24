from doing_commands import go_on

def input_just_voice():
    voice_command = ''#stream voice for 5 seconds
    return voice_command


def give_voice_command():
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

    return command



def reg1():
    voice = give_voice_command()

    print("cool. now i need the path where is your app which you want to start with this command\n>>>")
    while True:
        user_app_mb = input()
        try:
            go_on('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            go_on('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands(type='open', name = voice, app = path)
    print("great we've done it!")
    clear()

    return


def reg2():
    print('in fact it is almoast the same with first option, so then just think that "app" its an "tool"')
    reg1()
    return

def reg3():
    voice = give_voice_command()

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

    put_to_database_of_commands(type='song', voice, platform, artist, track)
    print("great we've done it!")
    clear()

    return


def reg4():
    print("this command need just you'r voice tag.")
    voice = give_voice_command()

    put_to_database_of_commands(type='exit', voice)
    clear()

    return


def reg5():
    voice = give_voice_command()

    print('now i need a way to app what you\n>>>')

    while True:
        user_app_mb = input()
        try:
            go_on('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            go_on('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands(type='kill', name=voice, app=path)
    print("great we've done it!")
    clear()

    return


def reg6():
    voice = give_voice_command()
    while True:
        print('here i need 2 things: your type of browser(chrome, firefox, ...) and link for site that i will need to open')
        print('type please path to your browser\n>>>')
        try:
            browser = input()
            go_on(type='open', user_os=take_from_database(1), application=browser)
            go_on(type='kill', user_os=take_from_database(1), application=browser)
            print('fine, looks like it is working, now please type link what i will need to open\n>>>')
            link = input()
            go_on(type='site', user_os=take_from_database(1), application=browser, link=link)
            go_on(type='kill', user_os=take_from_database(1), application=browser)
            print("Nice, now I'm convinced that I can definitely open this link, the command is registered")
            put_to_database_of_commands(type='site', name=voice, browser=browser, link=link)
            clear()
            return

        except:
            print('you input smth wrong, try again please')
            clear()

def reg7():
    voice = give_voice_command()
    print('command done, cool')
    clear()
    put_to_database_of_commands(type='off', name=voice)
    return

def reg8():
