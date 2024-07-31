import allure
import pytest
from locators import LoginPageLocators, HeaderPageLocators, PersonalAccountPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Ждем, что пропадет элемент modal_modal")
    def wait_until_modal_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_SECTION)
        self.wait_until_element_disappears(LoginPageLocators.MODAL_DIV)

    @allure.step("Нажатие по кнопке Личный кабинет в хэдере")
    def click_personal_account_button(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(HeaderPageLocators.PERSONAL_ACC_BUTTON_HEADER)

    @allure.step("Нажатие по кнопке Конструктор в хэдере")
    def click_constructor_button(self):
        self.wait_until_modal_disappears()
        self.wait_and_click_element(HeaderPageLocators.CONSTRUCTOR_BUTTON_HEADER)

    @allure.step("Нажатие по кнопке Лента заказов в хэдере")
    def click_orders_list_button(self):
        self.wait_until_modal_disappears()
        self.wait_and_click_element(HeaderPageLocators.ORDERS_LIST_BUTTON_HEADER)

