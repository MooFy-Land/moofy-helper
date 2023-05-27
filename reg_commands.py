import SECRET
import twelve
from doing_commands import go_on

def input_just_voice():
    voice_command = ''#stream voice for 5 seconds
    return voice_command


def give_voice_command(kit):
    if kit == True:
        print("please say how are you going to call this command\n")
        while True:
            print("i'm listening...")
            command = input_just_voice()
            SECRET.clear()
            print(f"cool.now let's check. are you going to call it like {command}?(y/n)\n")
            answer = input().lower()
            if "y" in answer:
                SECRET.clear()
                break
            else:
                SECRET.clear()
                print("fine let's try it again then\n")
        return command
    else:
        SECRET.clear()
        return ''



def reg1(kit):
    voice = give_voice_command(kit)

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
            SECRET.clear()

    put_to_database_of_commands(type='open', kit=kit, name = voice, app = path)
    print("great we've done it!")
    SECRET.clear()

    return


def reg2(kit):
    print('in fact it is almoast the same with first option, so then just think that "app" its an "tool"')
    reg1(kit)
    return

def reg3(kit):
    voice = give_voice_command(kit)

    while True:
        print('secondly i need the name of platfrom, artist and the name of track what you want to start with this command\nplatfrom:')
        platform = input('\nartist:')
        artist = input('\ntrack:')
        track = input()

        try:
            get_track_id(platform, artist, track)
            SECRET.clear()
            break
        except:
            print(f'you put something wrong. i cant finde this track on {platform}\ncheck your options and try it again please')
            SECRET.clear()

    put_to_database_of_commands(type='song', kit=kit, name=voice, platform=platform, artist=artist, track=track)
    print("great we've done it!")
    SECRET.clear()

    return


def reg4(kit):
    voice = give_voice_command(kit)
    print('in this command thats all what i need from you')

    put_to_database_of_commands(type='exit', kit=kit, name=voice)
    SECRET.clear()
    return


def reg5(kit):
    voice = give_voice_command(kit)

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
            SECRET.clear()

    put_to_database_of_commands(type='kill', kit=kit, name=voice, app=path)
    print("great we've done it!")
    SECRET.clear()

    return


def reg6(kit):
    voice = give_voice_command(kit)
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
            put_to_database_of_commands(type='site', kit=kit, name=voice, browser=browser, link=link)
            SECRET.clear()
            return

        except:
            print('you input smth wrong, try again please')
            SECRET.clear()

def reg7(kit):
    voice = give_voice_command(kit)
    print('command done, cool')
    put_to_database_of_commands(type='off', kit=kit, name=voice)
    SECRET.clear()
    return

def reg8(kit):
    voice = give_voice_command(kit)
    print('in this command, thats all what i need from you')
    put_to_database_of_commands(type='reboot', kit=kit, name=voice)
    SECRET.clear()
    return

def reg9(kit):
    voice = give_voice_command(kit)
    print('in this command, thats all what i need from you')
    put_to_database_of_commands(type='lock', kit=kit, name=voice)
    SECRET.clear()
    return

def reg10(kit):
    if take_from_database(1) in 'linux macos':
        voice = give_voice_command(kit)
        print('in this command, thats all what i need from you')
        put_to_database_of_commands(type='lock', kit=kit, name=voice)
    else:
        print('your os dont avalible for this command')

    SECRET.clear()
    return

def reg11(kit):
    print('comming soon...')
    SECRET.clear()
    return

def reg12(kit):
    voice = give_voice_command(kit)
    print('now i need an app by wich you want to call')
    while True:
        try:
            print("i can call only in telegram or whatsapp")
            app = input('>>>')
            if 'teleg' in app:
                app = 'telegram'
                break
            elif 'what' in app:
                app = 'whatsapp'
                break
            else:
                print('u put smth unreadable, please try again')
        except:
            print('i dk how did u do it but please try to type something more understandable')
        SECRET.clear()

    contacts = twelve.get_contacts(take_from_database(1), app)
    while True:
        try:
            print("now i need a the nickname of the person you want to call")
            nick = input('>>>')
            if nick in contacts:
                print('good, i see him in ur contacts')
                break
            else:
                print('i dont see this nick name in ur list of contacts, please check it and try again')
        except:
            print('i dk how did u do it but please try to type something more understandable')
        SECRET.clear()

    print("that's all what i need in this command")
    put_in_database_of_commands(type='call', kit=kit, application=app, who_we_call=nick)
    SECRET.clear()
    return

def reg13(kit):
    print('comming soon...')
    return