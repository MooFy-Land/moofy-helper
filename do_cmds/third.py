import os

def track_for_spotify(track, artist, user_os):
    if user_os == 'macos':
        # NEED TO DO IT FOR MAC
    elif user_os == 'win':
        # NEED TO DO IT FOR WIN
    else:
        os.system(
            f'(spotify 1>/dev/null 2>&1 &) && sleep 3 && qdbus org.mpris.MediaPlayer2.spotify / org.freedesktop.MediaPlayer2.OpenUri spotify:album:{track}')

def track_for_ya_muisic(track, artist, user_os):
    if user_os == 'macos':
        # NEED TO DO IT FOR MAC
    elif user_os == 'win':
        # NEED TO DO IT FOR MAC
    else:
        # NEED TO DO IT FOR MAC

def detect_platform(user_os, platform, track, artist):
    if platform == 'spotify':
        track_for_spotify(track, artist, user_os)
    else:
        track_for_ya_muisic(track, artist, user_os)
