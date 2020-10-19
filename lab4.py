
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

sp=[]

f=open('addr.txt')

#считали строки из первого файла 
for line in f.readlines():
    sp.append(line)
    line = f.readline()

sp.reverse()

#записываем в другой файл 
f1= open('addr2.txt', 'w')
for i in range(10):
    f1.write(sp[i])


#открытие вкладок 
i=0
for i in range(10):
    driver.get(sp[i])
    i = i+1
    if i != 10:
        driver.execute_script("window.open('','_blank');")
        # переключиться на новую вкладку (с индексом i)
        driver.switch_to.window(driver.window_handles[i])


#закрываем вкладки в обратном порядке
i=9
while i!=-1:
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[i])
    driver.close()
    i=i-1
        
f.close()
f1.close()
