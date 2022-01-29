import models 
from pygame import mixer
from playsound import playsound



def _play(my_mediaList):
    for media in my_mediaList:
#==================play music web================
        if media.location.startswith('https://'):
            print(f"{media.name} in {media.location} is playing by rate {media.rate}")
            playsound(media.location)


#==================play music local================
        elif media.location.startswith('/') or media.location.startswith('c:\\'):
            print(f"{media.name} in {media.location} is playing by rate {media.rate}")
            mixer.init()
            mixer.music.load(media.location)
            mixer.music.set_volume(0.7)
            mixer.music.play()


def play_by_name():
    my_mediaList = sorted(models.mediaList,reverse=True, key=lambda x: x.name)
    _play(my_mediaList)


def play_by_rate():
    my_mediaList = sorted(models.mediaList, key=lambda x: x.rate)
    _play(my_mediaList)
