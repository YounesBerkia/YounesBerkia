from selenium import webdriver
import pyautogui
import random
import time


#open browser
pyautogui.leftClick(x=202, y=753)
time.sleep(4)

#Incognito
pyautogui.leftClick(x=1344, y=50)
time.sleep(0.6)

pyautogui.leftClick(x=1067, y=129)
time.sleep(3)

#write text
pyautogui.leftClick(x=421, y=51)
time.sleep(0.8)

pyautogui.write('https://www.gmailnator.com/', interval=0.4)
pyautogui.press('enter')

#Gmail setup
time.sleep(10)
pyautogui.press('down', presses=8)

time.sleep(2)
pyautogui.leftClick(x=671, y=443)

time.sleep(15)
pyautogui.leftClick(x=622, y=448)

#minimize browser
time.sleep(5)
pyautogui.leftClick(x=1253, y=15)

#close browser
time.sleep(1)
pyautogui.leftClick(x=1343, y=12)
pyautogui.leftClick(x=202, y=753)

#Incognito
pyautogui.leftClick(x=1344, y=50)
time.sleep(0.6)

pyautogui.leftClick(x=1067, y=129)
time.sleep(3)

#write text
pyautogui.leftClick(x=421, y=51)
time.sleep(0.8)

pyautogui.write('https://id.sonyentertainmentnetwork.com/id/create_account_ca/', interval=0.15)
pyautogui.press('enter')

#create Account
time.sleep(5)
pyautogui.leftClick(x=677, y=506)
time.sleep(5)

#date setup
pyautogui.leftClick(x=526, y=427)
time.sleep(0.6)
for i in range(random.randint(1, 23)):
    pyautogui.press('down', interval=0.25)
    time.sleep(0.7)
pyautogui.press('enter')
time.sleep(1)

pyautogui.leftClick(x=663, y=427)
for i in range(random.randint(1, 12)):
    pyautogui.press('down', interval=0.25)
    time.sleep(0.7)
pyautogui.press('enter')
time.sleep(1.3)

pyautogui.leftClick(x=806, y=427)
for i in range(random.randint(21, 30)):
    pyautogui.press('down', interval=0.25)
    time.sleep(0.7)
pyautogui.press('enter')
time.sleep(1.3)

pyautogui.leftClick(x=835, y=652)
time.sleep(7)

pyautogui.leftClick(x=639, y=447)
pyautogui.press('down', presses=6, interval=0.15)
pyautogui.press('enter')

time.sleep(8)
pyautogui.leftClick(x=639, y=589)
pyautogui.press('down')
pyautogui.press('enter')

time.sleep(1)
pyautogui.moveTo(x=923, y=459)
pyautogui.dragRel(yOffset=659)
pyautogui.leftClick(x=923, y=659)

pyautogui.leftClick(x=841, y=631)
time.sleep(5)

#write email
pyautogui.leftClick(x=630, y=483)
pyautogui.hotkey('ctrl', 'v')

#write password
password = 'Nicht1218'

pyautogui.leftClick(x=559, y=563)
pyautogui.write(password, interval=0.2)

pyautogui.leftClick(x=595, y=629)
pyautogui.write(password, interval=0.2)

pyautogui.leftClick(x=844, y=689)
time.sleep(6)

#create account
pyautogui.moveTo(x=923, y=430)
pyautogui.dragRel(yOffset=663)
pyautogui.leftClick(x=923, y=663)

pyautogui.leftClick(x=760, y=627)
pyautogui.leftClick(x=682, y=438)
time.sleep(2)

pyautogui.leftClick(x=683, y=585)

#minimize browser
pyautogui.leftClick(x=1253, y=15)
pyautogui.leftClick(x=1253, y=15)
pyautogui.leftClick(x=1253, y=15)
pyautogui.leftClick(x=1253, y=15)
pyautogui.leftClick(x=1253, y=15)

#open text document
pyautogui.doubleClick(x=680, y=36)
time.sleep(1)

pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.write(' - nicht1218')

#credentials
driver = webdriver.Chrome()
driver.get('https://namso-gen.com/')

time.sleep(4)

bin = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[1]/label/input')
bin.send_keys('42409400xxxxxxxx')

driver.maximize_window()
time.sleep(1)
pyautogui.leftClick(x=1253, y=278)

for i in range(12):
    pyautogui.press('down')

time.sleep(4)

generate = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[5]/button')

for i in range(500):
    generate.click()

time.sleep(2)
copy = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[2]/div/label/button')
copy.click()

validate = webdriver.Chrome()
validate.get('https://www.mrchecker.net/card-checker/ccn2/')

text = validate.find_element_by_xpath('//*[@id="cc"]')
text.click()

pyautogui.hotkey('ctrl', 'v')

confirm = validate.find_element_by_xpath('//*[@id="form"]/div[2]/div/button[1]')
confirm.click()

driver.minimize_window()
validate.maximize_window()