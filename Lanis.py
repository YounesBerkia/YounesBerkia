from selenium import webdriver
import time

def clear_win():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

def options():
    print('OPTIONS')
    print('[1] Unterricht')
    print('[2] Nachrichten')
    print('[3] Vertretungen')
    print('--------------------')
    print()

options()
option = input('>> ')

if option == '1':
    driver = webdriver.Chrome()
    driver.get('https://start.schulportal.hessen.de/?i=6063')
    driver.minimize_window()


    time.sleep(2)

    username = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    username.send_keys('Younes.Berkia')


    password = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password.send_keys('21.12.2005')


    login = driver.find_element_by_xpath('//*[@id="alllogin"]')
    login.click()

    time.sleep(4)

    lessons = driver.find_element_by_xpath('//*[@id="sortablestart"]/li[2]')
    lessons.click()

    driver.maximize_window()
    clear_win()


if option == '2':
    driver = webdriver.Chrome()
    driver.get('https://start.schulportal.hessen.de/?i=6063')
    driver.minimize_window()


    username = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    username.send_keys('Younes.Berkia')


    password = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password.send_keys('21.12.2005')


    login = driver.find_element_by_xpath('//*[@id="alllogin"]')
    login.click()

    time.sleep(4)

    messages = driver.find_element_by_xpath('//*[@id="sortablestart"]/li[2]/div/div[2]/a/h3')
    messages.click()

    website = driver.title
    print(website)
    driver.maximize_window()
    clear_win()


if option == '3':
    driver = webdriver.Chrome()
    driver.get('https://start.schulportal.hessen.de/?i=6063')
    driver.minimize_window()


    username = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    username.send_keys('Younes.Berkia')


    password = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password.send_keys('21.12.2005')


    login = driver.find_element_by_xpath('//*[@id="alllogin"]')
    login.click()

    time.sleep(4)

    missing = driver.find_element_by_xpath('//*[@id="sortablestart"]/li[5]/div/div[2]/a/h3')
    missing.click()
    driver.maximize_window()
    clear_win()