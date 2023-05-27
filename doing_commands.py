import eight, fifth, first, fourth, nine, seven, six, ten, third, twelve
def go_on(type, call_type, user_os, application, track, artist, link, call_pearson, app_for_calling):
    if type == 'open':
        first.app(user_os, application)

    elif type == 'kill':
        fifth.stop_app(user_os, application)

    elif type == 'exit':
        fourth.stop_me()

    elif type == 'song':
        third.detect_platform(user_os, track, artist)

    elif type == 'site':
        six.open_site(application, link)

    elif type == 'off':
        seven.off_comp(user_os)

    elif type == 'lock':
        nine.lock_comp(user_os)

    elif type == '!___destroy___!':
        ten.OH_FCK_LETS_DO_IT(user_os)

    elif type == 'reboot':
        eight.reboot_comp(user_os)

    elif type == 'call':
        twelve.calling(user_os, app_for_calling, call_pearson)

