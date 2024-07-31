import allure
import pytest
from pages.base_page import BasePage
from locators import PersonalAccountPageLocators, LoginPageLocators


class PersonalAccountPage(BasePage):

    @allure.step("Ждем, что пропадет элемент div modal_modal")
    def wait_until_modal_div_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_DIV)

    @allure.step("Ждем, что пропадет элемент section modal_modal")
    def wait_until_modal_section_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_SECTION)

    @allure.step("Ждем, что пропадют элементы modal_modal")
    def wait_until_modal_disappears(self):
        self.wait_until_modal_div_disappears()
        self.wait_until_modal_section_disappears()

    @allure.step("Нажатие по кнопке Личный кабинет")
    def find_order_history_tab(self):
        self.wait_and_find_element(PersonalAccountPageLocators.ORDER_HISTORY_TAB)

    @allure.step("Нажатие по табу История заказов в личном кабинете")
    def click_order_history(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(PersonalAccountPageLocators.ORDER_HISTORY_TAB)

    @allure.step("Нажатие по кнопке Выход")
    def click_exit_button(self):
        self.wait_until_modal_disappears()  # без этого падают тесты Firefox
        self.wait_and_click_element(PersonalAccountPageLocators.EXIT_BUTTON)

    @allure.step("Получить ID созданного заказа из истории заказов")
    def get_created_order_id(self):
        self.wait_until_modal_disappears()
        return self.get_text_from_element(PersonalAccountPageLocators.ORDER_ID)
