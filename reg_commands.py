from doing_commands import do_command

def input_just_voice():
    #stream voice for 5 seconds
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
            do_command('open', take_from_database(1), user_app_mb)
            print("don't scare its just for check")
            do_command('kill', take_from_database(1), user_app_mb)
            path = user_app_mb
            break
        except:
            print('smth wrong.please check your path and try it again')
            clear()

    put_to_database_of_commands('open', name = voice, app = path)
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

    put_to_database_of_commands('track', voice, platform, artist, track)
    print("great we've done it!")
    clear()

    return


def reg4():
    print("this command need just you'r voice tag.")
    voice = give_voice_command()

    put_to_database_of_commands('exit', voice)
    clear()

    return


def reg5():
    voice = give_voice_command()

    print('now i need a way to app what you\n>>>')

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

    put_to_database_of_commands('kill', name=voice, app=path)
    print("great we've done it!")
    clear()

    return


def reg6():

