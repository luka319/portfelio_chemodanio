from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html" # N2 !!!
browser = webdriver.Chrome()
browser.get(link)


required_elements = browser.find_elements_by_css_selector('input[required]')
for element in required_elements:
    element.send_keys('required')

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

# проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

