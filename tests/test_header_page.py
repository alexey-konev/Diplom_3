import pytest
import allure
import data
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from pages.orders_list_page import OrdersListPage


class TestHeaderPage:

    @allure.title("GoogleChrome - Проверка перехода по клику Личный кабинет в хэдере авторизированного пользователя")
    def test_click_personal_account_button_auth_chrome(self, driver_chrome, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_chrome)  # создаем нужные объекты-страницы
        login_page = LoginPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.find_order_history_tab()  # ждем загрузки страницы

        assert personal_account_page.opened_page_url() == data.PERSONAL_ACCOUNT_URL

    @allure.title("GoogleChrome - Проверка перехода по клику Личный кабинет в хэдере НЕавторизированного пользователя")
    def test_click_personal_account_button_unauth_chrome(self, driver_chrome):
        header_page = HeaderPage(driver_chrome)
        header_page.open_url(data.MAIN_PAGE_URL)  # открываем главную страницу

        header_page.click_personal_account_button()  # нажимаем Личный кабинет

        assert header_page.opened_page_url() == data.LOGIN_PAGE_URL

    @allure.title("GoogleChrome - Проверка перехода по клику Лента заказов в хэдере")
    def test_click_orders_list_button_chrome(self, driver_chrome):
        header_page = HeaderPage(driver_chrome)
        order_list_page = OrdersListPage(driver_chrome)

        header_page.open_url(data.MAIN_PAGE_URL)  # открываем главную страницу
        header_page.click_orders_list_button()  # нажимаем Лента заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert header_page.opened_page_url() == data.ORDER_LIST_URL

    @allure.title("GoogleChrome - Проверка перехода по клику Конструктор в хэдере")
    def test_click_constructor_button_chrome(self, driver_chrome):
        header_page = HeaderPage(driver_chrome)
        main_page = MainPage(driver_chrome)

        header_page.open_url(data.ORDER_LIST_URL)  # открываем страницу Ленты заказов
        header_page.click_constructor_button()  # нажимаем Конструктор
        main_page.find_make_burger_title()  # ждем загрузки страницы

        assert header_page.opened_page_url() == data.MAIN_PAGE_URL

    @allure.title("Firefox - Проверка перехода по клику Личный кабинет в хэдере авторизированного пользователя")
    def test_click_personal_account_button_auth_firefox(self, driver_firefox, register_new_user_and_get_data):
        personal_account_page = PersonalAccountPage(driver_firefox)  # создаем нужные объекты-страницы
        login_page = LoginPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_personal_account_button()  # нажимаем Личный кабинет
        personal_account_page.find_order_history_tab()  # ждем загрузки страницы

        assert personal_account_page.opened_page_url() == data.PERSONAL_ACCOUNT_URL

    @allure.title("GoogleChrome - Проверка перехода по клику Личный кабинет в хэдере НЕавторизированного пользователя")
    def test_click_personal_account_button_unauth_firefox(self, driver_firefox):
        header_page = HeaderPage(driver_firefox)
        header_page.open_url(data.MAIN_PAGE_URL)  # открываем главную страницу

        header_page.click_personal_account_button()  # нажимаем Личный кабинет

        assert header_page.opened_page_url() == data.LOGIN_PAGE_URL

    @allure.title("Firefox - Проверка перехода по клику Лента заказов в хэдере")
    def test_click_orders_list_button_firefox(self, driver_firefox):
        header_page = HeaderPage(driver_firefox)
        order_list_page = OrdersListPage(driver_firefox)

        header_page.open_url(data.MAIN_PAGE_URL)  # открываем главную страницу
        header_page.click_orders_list_button()  # нажимаем Лента заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert header_page.opened_page_url() == data.ORDER_LIST_URL

    @allure.title("Firefox - Проверка перехода по клику Конструктор в хэдере")
    def test_click_constructor_button_firefox(self, driver_firefox):
        header_page = HeaderPage(driver_firefox)
        main_page = MainPage(driver_firefox)

        header_page.open_url(data.ORDER_LIST_URL)  # открываем страницу Ленты заказов
        header_page.click_constructor_button()  # нажимаем Конструктор
        main_page.find_make_burger_title()  # ждем загрузки страницы

        assert header_page.opened_page_url() == data.MAIN_PAGE_URL
