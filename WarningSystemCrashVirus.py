from os import access
from pynput import keyboard
from pynput.keyboard import Key, Controller
from selenium import webdriver
import pyautogui
import time

keyboard = Controller()
password = 'nassimnein'
password_input = input()

if password_input == password:
    ph = webdriver.Chrome()
    ph.get('https://youtube.com')

    ph.maximize_window()
    ph.get('https://pornhub.com')
    
    time.sleep(2)

    accept = ph.find_element_by_xpath('//*[@id="modalWrapMTubes"]/div/div/button')
    accept.click()

    search = ph.find_element_by_xpath('//*[@id="searchInput"]')
    search.send_keys('good luck bro! Und hoffentlich kommst du schnell')

    regis = ph.find_element_by_xpath('//*[@id="headerLoginLink"]')
    regis.click()

    user = ph.find_element_by_xpath('//*[@id="usernameModal"]')
    user.send_keys('nainsadjguefsdf')

    passw = ph.find_element_by_xpath('//*[@id="passwordModal"]')
    passw.send_keys('sjgkjdfgkdenmvcnvsdfjoesclkjdsf')

    login = ph.find_element_by_xpath('//*[@id="signinSubmit"]')
    login.click()

    hamster = webdriver.Chrome()
    hamster.get('https://xhamster.com')

    time.sleep(2)

    hamster.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/button')
    hamster.click()

    