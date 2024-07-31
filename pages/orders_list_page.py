import allure
import pytest
from locators import MainPageLocators, OrdersListPageLocators
from pages.base_page import BasePage


class OrdersListPage(BasePage):

    @allure.step("Нажимаем на первый заказ в списке")
    def click_first_order(self):
        self.wait_and_click_element(OrdersListPageLocators.FIRST_ORDER_IN_LIST)

    @allure.step("Ждем загрузки заголовка Лента заказов")
    def find_orders_list_title(self):
        self.wait_and_find_element(MainPageLocators.ORDERS_LIST_TITLE)

    @allure.step("Проверяем, что открылось окно с деталями заказа")
    def check_order_details(self):
        return self.wait_and_find_element(OrdersListPageLocators.ORDER_ITEMS_LIST)

    @allure.step("Подставляем ID заказа в локатор и смотрим его наличие в списке заказов")
    def find_order_in_list(self, order_id):
        formatted_locator = self.format_locators(OrdersListPageLocators.ORDER_ID_IN_LIST, order_id)
        return self.wait_and_find_element(formatted_locator)

    @allure.step("Получить число заказов за все время")
    def get_all_orders_counter(self):
        return self.get_text_from_element(OrdersListPageLocators.ALL_ORDER_COUNTER)

    @allure.step("Получить число заказов за сегодня")
    def get_today_orders_counter(self):
        return self.get_text_from_element(OrdersListPageLocators.TODAY_ORDER_COUNTER)

    def find_order_in_getting_ready_list(self, order_id):
        formatted_locator = self.format_locators(OrdersListPageLocators.ORDER_ID_IN_GETTING_READY, order_id)
        return self.wait_and_find_element(formatted_locator)
