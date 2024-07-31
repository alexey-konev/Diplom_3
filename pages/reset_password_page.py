import allure
import pytest
from pages.base_page import BasePage
from locators import ResetPasswordPageLocators, LoginPageLocators


class ResetPasswordPage(BasePage):
    @allure.step("Ждем, что пропадет элемент modal_modal")
    def wait_until_modal_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_SECTION)
        self.wait_until_element_disappears(LoginPageLocators.MODAL_DIV)

    @allure.step("Заполняем эмейл на странице Забыли пароль")
    def fill_in_email(self, email):
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Нажимаем Восстановить на странице Забыли пароль")
    def click_reset_button(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(ResetPasswordPageLocators.RESET_BUTTON)
        self.wait_and_find_element(ResetPasswordPageLocators.CODE_FIELD)  # без ожидания падает тест

    @allure.step("Нажимаем 'глаз', чтобы показать пароль")
    def show_password(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверяем, что поле подсвечивается")
    def check_if_password_filed_is_active(self):
        return self.wait_and_find_element(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
