from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome()

driver.get("https://vk.com/")

#вход
email = driver.find_element_by_id("index_email")
password = driver.find_element_by_id("index_pass")

email.click()
email.send_keys("")
time.sleep(1)

password.click()
password.send_keys("")
time.sleep(1)

button = driver.find_element_by_id("index_login_button")
button.click()

time.sleep(5)

#переходим в сообщения
button = driver.find_element_by_css_selector("#l_msg > a > span > span.left_label.inl_bl")
button.click()

time.sleep(5)


pyautogui.click(x=499, y=252)
time.sleep(2)
#выделяем 10 последних сообщений 
pyautogui.moveTo(721, 600, 1)
y=600
i=0
for i in range (10):
    pyautogui.click(x=721, y=y)
    time.sleep(2)
    y=y-30
    
time.sleep(2)
driver.close()