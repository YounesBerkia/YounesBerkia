import os
import time
import shutil


dir =                      input('Enter Directory >> ')
print()


#Input your own directorys
music =               'C:\\Users\\berki\\Desktop\\Main\\Music\\'
school =        'C:\\Users\\berki\\Desktop\\Main\\Schule\\'
python_code = 'C:\\Users\\berki\\Desktop\\Main\\Python\\'
wallpapers =   'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\'
downloads =         'C:\\Users\\berki\\Downloads\\'
programs =              'C:\\Users\\berki\\Desktop\\Main\\Programme\\'
unknown =                   'C:\\Users\\berki\\Desktop\\Main\\Unknown\\'


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

                if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx"):
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

            if file.endswith(".exe"):
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
