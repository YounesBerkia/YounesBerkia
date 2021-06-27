import os
import time
import shutil
from typing import MutableSequence

dir =      input('Enter Directory >> ')
music =     '/home/price/Music'
school =     '/home/price/Schule'
python_code = '/home/price/Python Code'
wallpapers =   '/home/price/Wallpapers'
sound_effects = '/home/price/Sound Effects'
downloads = '/home/price/Downloads'


while True:
    if dir == 'music':
        dir = music

    if dir == 'school' or dir == 'Schule' or dir == 'schule':
        dir = school

    if dir == 'python code' or dir == 'python':
        dir = python_code

    if dir == 'wallpapers' or dir == 'wallpaper':
        dir = wallpapers

    if dir == 'sound effect':
        dir = sound_effects

    if dir == 'downloads':
        dir = downloads

    for file in os.listdir(dir):

        if file.endswith(".mp3") or file.endswith(".wav"):
	        shutil.move(f"{dir}/{file}", music)


        if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".odt"):
            shutil.move(f"{dir}/{file}", school)

        if file.endswith(".py"):
	        shutil.move(f"{dir}/{file}", python_code)
        
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".JPG"):
            shutil.move(f"{dir}/{file}", wallpapers)

        if file.endswith(".ogg"):
	        shutil.move(f"{dir}/{file}", sound_effects)
