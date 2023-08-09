import os

def get_contacts(user_os, app):


def more_similar_pearson(user_os, human, app):
    list_sch = []
    contacts = get_contacts(user_os, app)
    for pearson in contacts:
        sch = 0
        for i in range(max(len(human), len(pearson))):
            if human[i] == pearson[i]:
                sch += 1
        list_sch.append(sch)
    return contacts[list_sch.index(max(list_sch))]
def call_on_linux(user_os, app, human):
    if app == 'telegram':
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by telegram
    else:
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by what's app

def call_on_mac(user_os, app, human):
    if app == 'telegram':
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by telegram
    else:
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by what's app

def call_on_win(user_os, app, human):
    if app == 'telegram':
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by telegram
    else:
        call = more_similar_pearson(user_os, human, app)
        os.system() # call by what's app
def calling(user_os, application, pearson):
    if user_os == 'linux':
        call_on_linux(user_os, application, pearson)

    elif user_os == 'macos':
        call_on_mac(user_os, application, pearson)

    else:
        call_on_win(user_os, application, pearson)