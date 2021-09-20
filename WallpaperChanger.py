import os
import ctypes
import time
import cv2
import urllib
import shutil
import random
from pynput import keyboard
import requests
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup


keyboard = keyboard.Controller()

URL = 'https://apod.nasa.gov/apod/astropix.html'
headers = {"User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
wallpapers = [
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\BigSurclone.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\Citrons.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\Fruits.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\IMacBlueDark.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\IMacBlueLight.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\Oranges.jpg',
        'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\Pinapples.jpg'
    ]

def get_source():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    image = soup.find_all('img')

    for img in image:
        image_url = 'https://apod.nasa.gov/apod/' + img['src']
        
        ranint = str(random.randint(1, 999))
        filename = 'Nasa_Picture' + ranint + '.jpg'
        
        src = 'C:\\Users\\berki\\Desktop\\Main\\Python\\' + filename
        dest = 'C:\\Users\\berki\\Desktop\\Main\\Wallpapers\\' + filename

        urllib.request.urlretrieve(image_url, filename)
        
        print()

        time.sleep(5)

        im = cv2.imread('C:\\Users\\berki\\Desktop\\Main\\Python\\' + filename)
        imsize = str(im.shape)
        
        if imsize >= '1366, 768, 3':
            print('Size of Image is : ' + imsize + '    min. requierment : 1366x768')
            shutil.move(src, dest)
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, src , 0)
            time.sleep(6)
            print("Image doesn't meet the resolution requierments!" + '    min. requierment : 1366x768')
            print("Image Size :" + imsize)
            os.remove('C:\\Users\\berki\\Desktop\\Main\\Python\\' + filename)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, random.choice(wallpapers) , 0)

def set_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, random.choice(wallpapers) , 0)

print('[1] Change Wallpaper randomly')
print('[2] Download Wallpaper of the Day from NASA')
print('[3] Both')
print()
option = input('>> ')

if option == '1':
    while True:
        set_wallpaper()
if option == '2':
    get_source()
if option == '3':
    get_source()
    set_wallpaper()