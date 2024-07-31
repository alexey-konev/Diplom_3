from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

import pytest


class BasePage:

    def __init__(self, driver):  # инициализация драйвера через фикстуру
        self.driver = driver

    def wait_and_find_element(self, locator):  # дождаться видимости и найти
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_click_element(self, locator):  # дождаться кликабельности и нажать
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def wait_until_element_disappears(self, locator):  # дождаться невидимости элемента
        return WebDriverWait(self.driver, 15).until_not(expected_conditions.visibility_of_element_located(locator))

    def add_text_to_element(self, locator, text):  # заполнить поле
        self.wait_and_find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):  # получить текст
        return self.wait_and_find_element(locator).text

    def open_url(self, url):
        self.driver.get(url)

    def opened_page_url(self):
        return self.driver.current_url

    def drag_and_drop(self, drag, drop):
        drag = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(drag))
        drop = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(drop))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def format_locators(self, locator_i, num):  # подставить num в локатор
        method, locator = locator_i
        locator = locator.format(num)
        return method, locator

