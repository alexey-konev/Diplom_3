import allure
import pytest
import data
from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ждем, что пропадет элемент modal_modal")
    def wait_until_modal_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_SECTION)
        self.wait_until_element_disappears(LoginPageLocators.MODAL_DIV)

    @allure.step("Логинимся в UI пользователем, который был создан в API")
    def login_new_user(self, user_data):
        login = user_data[0]
        password = user_data[1]
        self.open_url(data.LOGIN_PAGE_URL)  # открыли страницу логина
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, login)  # ввели эмейл
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)  # ввели пароль
        self.wait_and_click_element(LoginPageLocators.LOGIN_BUTTON)  # нажали Войти

    @allure.step("Нажимаем Восстановить пароль на странице логина")
    def click_reset_password_link(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(LoginPageLocators.RESET_PASSWORD_LINK)

    def wait_for_login_button(self):
        self.wait_and_find_element(LoginPageLocators.LOGIN_BUTTON)  # без ожидания тест падает

