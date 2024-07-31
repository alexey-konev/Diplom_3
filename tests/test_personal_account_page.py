import pytest
import allure
import data
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage


class TestPersonalAccountPage:

    @allure.title("GoogleChrome - Проверка перехода в раздел История заказов")
    def test_click_order_history_chrome(self, driver_chrome, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data

        login_page.login_new_user(user_data)  # регистрация и логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.click_order_history()  # нажимаем История заказов

        assert personal_account_page.opened_page_url() == data.ORDER_HISTORY_URL

    @allure.title("GoogleChrome - Проверка кнопки Выход")
    def test_click_exit_button_chrome(self, driver_chrome, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data

        login_page.login_new_user(user_data)  # регистрация и логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.click_exit_button()  # нажимаем Выход
        login_page.wait_for_login_button()  # ждем загрузки страницы

        assert personal_account_page.opened_page_url() == data.LOGIN_PAGE_URL

    @allure.title("Firefox - Проверка перехода в раздел История заказов")
    def test_click_order_history_firefox(self, driver_firefox, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data

        login_page.login_new_user(user_data)  # регистрация и логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.click_order_history()  # нажимаем История заказов

        assert personal_account_page.opened_page_url() == data.ORDER_HISTORY_URL

    @allure.title("Firefox - Проверка кнопки Выход")
    def test_click_exit_button_firefox(self, driver_firefox, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data

        login_page.login_new_user(user_data)  # регистрация и логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.click_exit_button()  # нажимаем Выход
        login_page.wait_for_login_button()  # ждем загрузки страницы

        assert personal_account_page.opened_page_url() == data.LOGIN_PAGE_URL
