from tkinter.constants import S
from selenium import webdriver
import pyautogui
import time


driver = webdriver.Chrome()
driver.get('https://github.com/login')


email = driver.find_element_by_xpath('//*[@id="login_field"]')
email.send_keys('berkiayouness@gmail.com')


passwrd = driver.find_element_by_xpath('//*[@id="password"]')
passwrd.send_keys('ymnp1056')


sign_in = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
sign_in.click()
time.sleep(4)


project = driver.find_element_by_xpath('//*[@id="repos-container"]/ul/li/div/a/span[2]')
project.click()
time.sleep(3)


add_file = driver.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/summary')
add_file.click()


upload_files = driver.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/div/ul/li[3]/a')
upload_files.click()
time.sleep(4)


driver.maximize_window()
time.sleep(1)

pyautogui.leftClick(x=682, y=541)
time.sleep(1)


pyautogui.leftClick(x=78, y=228)
pyautogui.doubleClick(x=291, y=188)


pyautogui.leftClick(x=280, y=338)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('enter')

time.sleep(4)
commit = driver.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/form/button')
commit.click()