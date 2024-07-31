import pytest
import allure
import data
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("GoogleChrome - Проверка клика на ингредиент")
    def test_click_ingredient_chrome(self, driver_chrome):
        main_page = MainPage(driver_chrome)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.click_first_bun()  # кликаем по первой булке

        assert main_page.find_ingredient_details_window()

    @allure.title("GoogleChrome - Проверка закрытия окна Детали ингредиента")
    def test_close_ingredient_details_chrome(self, driver_chrome):
        main_page = MainPage(driver_chrome)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.click_first_bun()  # кликаем по первой булке
        main_page.find_ingredient_details_window()  # ждем открытия окна Детли ингредиента
        main_page.close_ingredient_details_window()  # нажимаем крестик

        assert main_page.make_sure_ingredient_details_window_closed()  # проверяем, что окно перестало быть видимым

    @allure.title("GoogleChrome - Проверка счетчика игредиентов")
    def test_check_ingredient_count_chrome(self, driver_chrome):
        main_page = MainPage(driver_chrome)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.add_ingredient()  # добавляем булку - их добавляется сразу 2

        assert main_page.get_ingredient_counter() == '2'

    @allure.title("GoogleChrome - Проверка оформления заказа залогиненным пользователем")
    def test_create_order_chrome(self, driver_chrome, register_new_user_and_get_data):
        main_page = MainPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()

        assert main_page.check_order_is_created()

    @allure.title("Firefox - Проверка клика на ингредиент")
    def test_click_ingredient_firefox(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.click_first_bun()

        assert main_page.find_ingredient_details_window()

    @allure.title("Firefox - Проверка закрытия окна Детали ингредиента")
    def test_close_ingredient_details_firefox(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.click_first_bun()  # кликаем по первой булке
        main_page.find_ingredient_details_window()  # ждем открытия окна Детли ингредиента
        main_page.close_ingredient_details_window()  # нажимаем крестик

        assert main_page.make_sure_ingredient_details_window_closed()

    @allure.title("Firefox - Проверка счетчика игредиентов")
    def test_check_ingredient_count_firefox(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open_url(data.MAIN_PAGE_URL)

        main_page.add_ingredient()  # добавляем булку - их добавляется сразу 2

        assert main_page.get_ingredient_counter() == '2'

    @allure.title("Firefox - Проверка оформления заказа залогиненным пользователем")
    def test_create_order_firefox(self, driver_firefox, register_new_user_and_get_data):
        main_page = MainPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()

        assert main_page.check_order_is_created()

