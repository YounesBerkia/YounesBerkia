import os
import time
import shutil

dir =      input('Enter Directory >> ')
music =     'C:\\Users\\berki\\Music'
school =     'C:\\Users\\berki\\Schule'
python_code = 'C:\\Users\\berki\\Python'
wallpapers =   'C:\\Users\\berki\\Desktop\\Main\\Wallpapers'
downloads =     'C:\\Users\\berki\\Downloads'
programs =       'C:\\Users\\berki\\Desktop\\Main\\Programme'
unknown =         'C:\\Users\\berki\\Desktop\\Main\\Unknown'


if dir == 'music':
    dir = music

if dir == 'school' or dir == 'Schule' or dir == 'schule':
    dir = school

if dir == 'python code' or dir == 'python':
    dir = python_code

if dir == 'wallpapers' or dir == 'wallpaper':
    dir = wallpapers

if dir == 'downloads':
    dir = downloads

if dir == 'programs' or dir == 'programme':
    dir = programs

for file in os.listdir(dir):

    if file.endswith(".mp3") or file.endswith(".wav"):
        shutil.move(f"{dir}/{file}", music)


    if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx"):
        shutil.move(f"{dir}/{file}", school)

    if file.endswith(".py"):
        shutil.move(f"{dir}/{file}", python_code)
    
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        shutil.move(f"{dir}/{file}", wallpapers)

    if file.endswith(".exe"):
        shutil.move(f"{dir}/{file}", programs)

    else:
        shutil.move(f"{dir}/{file}", unknown)
