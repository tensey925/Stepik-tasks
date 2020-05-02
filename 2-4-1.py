from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from math import sin, log

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.ID, 'book')

optimal_price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
button.click()


def func(value):
    return log(abs(12 * sin(value)))


x_text = browser.find_element(By.ID, 'input_value').text
a = str(func(int(x_text)))
browser.find_element(By.ID, 'answer').send_keys(a)
browser.find_element(By.ID, 'solve').click()

alert = browser.switch_to.alert
print(alert.text)
