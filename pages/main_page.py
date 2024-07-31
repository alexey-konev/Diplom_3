import allure
import pytest
from locators import MainPageLocators, LoginPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ждем, что пропадет элемент modal_modal")
    def wait_until_modal_disappears(self):
        self.wait_until_element_disappears(LoginPageLocators.MODAL_SECTION)

    @allure.step("Ждем, что пропадет элемент modal_loading после оформления заказа")
    def wait_until_modal_loading_disappears(self):
        self.wait_until_element_disappears(MainPageLocators.MODAL_LOADING)

    @allure.step("Ждем загрузки заголовка Соберите бургер")
    def find_make_burger_title(self):
        self.wait_and_find_element(MainPageLocators.MAKE_BURGER_TITLE)

    @allure.step("Ждем загрузки окна Детали ингредиента")
    def find_ingredient_details_window(self):
        return self.wait_and_find_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW)

    @allure.step("Ждем загрузки окна Детали ингредиента")
    def click_first_bun(self):
        self.wait_and_click_element(MainPageLocators.FIRST_BUN)

    @allure.step("Закрываем окно Детали ингредиента по крестику")
    def close_ingredient_details_window(self):
        self.wait_and_click_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step("Проверяем, что окно закрылось")
    def make_sure_ingredient_details_window_closed(self):
        return self.wait_until_element_disappears(MainPageLocators.INGREDIENT_DETAILS_WINDOW)

    @allure.step("Добавляем ингредиент с помощью drag-and-drop")
    def add_ingredient(self):
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.INGREDIENT_BASKET)

    @allure.step("Получить количество ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Нажимаем на кнопку Оформить заказ")
    def click_create_order(self):
        self.wait_and_click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Проверяем, что видно окно Заказ оформлен")
    def check_order_is_created(self):
        return self.wait_and_find_element(MainPageLocators.ORDER_CREATED_TEXT)

    @allure.step("Получаем ID созданного заказа")
    def get_created_order_id(self):
        self.wait_until_modal_loading_disappears()
        return self.get_text_from_element(MainPageLocators.ORDER_ID)

    @allure.step("Нажимаем на кнопку Оформить заказ")
    def close_created_order(self):
        self.wait_until_modal_loading_disappears()
        self.wait_and_click_element(MainPageLocators.CREATED_ORDER_CLOSE_BUTTON)
