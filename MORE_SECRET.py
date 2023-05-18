from commads import reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12, reg13, reg14, reg15, reg16

def reg_new_command(command):
    print("fine let's register your command then")
    if command == 1:
        reg1()
    elif command == 2:
        reg2()
    elif command == 3:
        reg3()
    elif command == 4:
        reg4()
    elif command == 5:
        reg5()
    elif command == 6:
        reg6()
    elif command == 7:
        reg7()
    elif command == 8:
        reg8()
    elif command == 9:
        reg9()
    elif command == 10:
        reg10()
    elif command == 11:
        reg11()
    elif command == 12:
        reg12()
    elif command == 13:
        reg13()
    elif command == 14:
        reg14()
    elif command == 15:
        reg15()
    elif command == 16:
        reg16()


def input_voice_command():
    while True:
        #somehow stream voice
        if more_similar_commad(find) in list_of_commands:
            return find


def add_voice_command(choice):
    clear()
    print("okey know let's do an phrase for starting this command")

    voice = input_voice_command()

    return(voice, choice)