# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# ==============
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==============

import sys
import time

print("Попытка #1 === try #1")

# diver1 = webdriver.Firefox()
diver1 = webdriver.Chrome()
 
diver1.get("http://127.0.0.1:8000/index/")

diver1.maximize_window()

b = 5

def my_sleep(b):

    for a in xrange(b):  # только для 2-го питона

          time.sleep(1)
          sys.stdout.write(' sleep = %s \r' % (b-a))


# diver1.implicitly_wait(b) # seconds


'''
elem1 = diver1.find_element_by_xpath('//*[@id="two"]') # 
elem1.click()

print(' ====== elem1 ========')

# отработал хорошо, но дальше нужно нажимать 
# на окно алерта, а то оно останавливается
'''

iframe1 = diver1.find_elements_by_tag_name('iframe')[0]

# diver1.switch_to.default_content()

diver1.switch_to.frame(iframe1)


elem2 = diver1.find_element_by_xpath('//*[@id="one"]') # 
elem2.click()

alert = diver1.switch_to_alert() # Переключаемся на окно алерта. switch_to_alert возвращает класс Alert:
print('alert = ', alert.text)  # Возвращает текст алерта.
# alert.dismiss() # Выполняет действие "отказаться" от алерта.


my_sleep(b)
# diver1.implicitly_wait(b) # 5 seconds если нет, если да то сразу !!!

alert.accept() # Выполняет действие "принять" алерт.

# alert.send_keys() # Выполняет действие "напечатать" в окне алерта.

print('\n iframe1 ok \n======================================\n')


# ===================  iframe N2 ============================

# diver1.switch_to.default_content()   # вернулись в основное окно
# оба варианта сверху и снизу - работают нормально 

diver1.switch_to_default_content() # вернулись в основное окно

iframe2 = diver1.find_elements_by_tag_name('iframe')[1]

# diver1.switch_to.default_content()

diver1.switch_to.frame(iframe2)

elem3 = diver1.find_element_by_xpath('//*[@id="one"]') # 
elem3.click()

alert = diver1.switch_to_alert() # Переключаемся на окно алерта. switch_to_alert возвращает класс Alert:
print('alert = ', alert.text)  # Возвращает текст алерта.


my_sleep(b)
# diver1.implicitly_wait(b) # 5 seconds если нет, если да то сразу !!!

alert.dismiss() # Выполняет действие "отказаться" от алерта.
# alert.accept() # Выполняет действие "принять" алерт.


print('\n iframe2 ok \n======================================\n')
print('----------------------------')


diver1.switch_to_default_content() # вернулись в основное окно


# diver1.close()