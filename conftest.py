import pytest
from selenium import webdriver
import requests

import data
import helpers

@pytest.fixture()
def driver_firefox(scope='session'):  # инициализация драйвера для firefox
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1366,768')
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def driver_chrome():  # инициализация драйвера для chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1366,768')
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def register_new_user_and_get_data():
    # генерируем рандомные данные и отправляем запрос на регистарцию, получаем логин, пароль и токен
    payload, access_token = helpers.register_new_user_and_return_login_password_token()
    yield payload
    helpers.delete_user(access_token)  # удаляем тестовые данные

