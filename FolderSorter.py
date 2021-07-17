import os
import time
import shutil


dir =                      input('Enter Directory >> ')
print()


#Input your own directorys
music =       '/Users/younes/Desktop/Main/Music'
school =      '/Users/younes/Desktop/Main/School'
python_code = '/Users/younes/Desktop/Main/Python'
wallpapers =  '/Users/younes/Desktop/Main/Wallpapers'
downloads =   '/Users/younes/Downloads'
programs =    '/Users/younes/Desktop/Main/Programme'
unknown =     '/Users/younes/Desktop/Main/Unknown'


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

running = True

while running == True:
    for file in os.listdir(dir):
        try:

            if file.endswith(".mp3") or file.endswith(".wav"):
                shutil.move(f"{dir}/{file}", music)
                print('[+] Found music file!')
                print('-    ', file)
                print('\n')

                if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".pptx"):
                    shutil.move(f"{dir}/{file}", school)
                    print('[+] Found file for school!')
                    print('-    ', file)
                    print('\n')

            if file.endswith(".py"):
                shutil.move(f"{dir}/{file}", python_code)
                print('[+] Found python file!')
                print('-    ', file)
                print('\n')

            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                shutil.move(f"{dir}/{file}", wallpapers)
                print('[+] Found image!')
                print('-    ', file)
                print('\n')

            if file.endswith(".dmg") or file.endswith(".app"):
                shutil.move(f"{dir}/{file}", programs)
                print('[+] Found exe file!')
                print('-    ', file)
                print('\n')

            else:
                shutil.move(f"{dir}/{file}", unknown)
                print('[+] Found unknown file!')
                print('-    ', file)
                print('\n')

                print('[+] Finished!')
                running = False

        except:
            print('[+] Finished!')
            running = False
            pass

running = False

time.sleep(5)
os.close()
