from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.psychicscience.org/random.aspx")

#выбираем одно случайное число
textbox = driver.find_element_by_id("num")
textbox.click()
textbox.send_keys("1")

textbox = driver.find_element_by_id("st")
textbox.click()
textbox.send_keys("1")

textbox = driver.find_element_by_id("en")
textbox.click()
textbox.send_keys("10")

button = driver.find_element_by_id("go")
button.click()
time.sleep(3)

driver.refresh()#обновляем страницу

#выбираем несколько случайных чисел
textbox = driver.find_element_by_id("num")
textbox.click()
textbox.send_keys("10")

textbox = driver.find_element_by_id("st")
textbox.click()
textbox.send_keys("1")

textbox = driver.find_element_by_id("en")
textbox.click()
textbox.send_keys("100")

button = driver.find_element_by_id("go")
button.click()

time.sleep(3)

driver.refresh()#обновляем страницу

#генерация большого количества чисел
textbox = driver.find_element_by_id("num")
textbox.click()
textbox.send_keys("1000")

textbox = driver.find_element_by_id("st")
textbox.click()
textbox.send_keys("10")

textbox = driver.find_element_by_id("en")
textbox.click()
textbox.send_keys("1000000")

button = driver.find_element_by_id("go")
button.click()

time.sleep(5)

driver.refresh()#обновляем страницу

#меняем режим генерации
textbox = driver.find_element_by_id("num")
textbox.click()
textbox.send_keys("36")

textbox = driver.find_element_by_id("st")
textbox.click()
textbox.send_keys("10")

textbox = driver.find_element_by_id("en")
textbox.click()
textbox.send_keys("1000")

button = driver.find_element_by_id("rpt")
button.click()
button = driver.find_element_by_css_selector("#rpt > option:nth-child(3)")
button.click()

button = driver.find_element_by_id("go")
button.click()

time.sleep(5)
driver.close()
