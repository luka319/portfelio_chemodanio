
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)


first = browser.find_element_by_class_name("first")


first.send_keys("Моё_Имя")

second = browser.find_element_by_class_name("second")
#<input type="text" class="form-control second" placeholder="Введите фамилию" maxlength="32" required="">
second.send_keys("Моё_Фамилиё")

third = browser.find_element_by_class_name("third")
# <input type="text" class="form-control third" placeholder="Введите Email" maxlength="32" required="">
third.send_keys("my_third@email.ru")

#...

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

