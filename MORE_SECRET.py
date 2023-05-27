from reg_commands import reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12, reg13, reg14, reg15, reg16

def reg_new_command(command, kit):
    print("fine let's register your command then")
    if command == 1:
        reg1(kit)
    elif command == 2:
        reg2(kit)
    elif command == 3:
        reg3(kit)
    elif command == 4:
        reg4(kit)
    elif command == 5:
        reg5(kit)
    elif command == 6:
        reg6(kit)
    elif command == 7:
        reg7(kit)
    elif command == 8:
        reg8(kit)
    elif command == 9:
        reg9(kit)
    elif command == 10:
        reg10(kit)
    elif command == 11:
        reg11(kit)
    elif command == 12:
        reg12(kit)
    elif command == 13:
        reg13(kit)
    elif command == 14:
        reg14(kit)
    elif command == 15:
        reg15(kit)
    elif command == 16:
        reg16()


def input_voice_command():
    while True:
        find = ''#somehow stream voice
        if more_similar_commad(find) in list_of_commands:
            return find
        else:
            say('did not hear. please repeat')
def do_command(command):
    if command == ''