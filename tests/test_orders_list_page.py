import pytest
import allure
import data
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.orders_list_page import OrdersListPage


class TestOrdersListPage:

    @allure.title("GoogleChrome - Проверка клика по заказу в ленте заказов")
    def test_click_order_chrome(self, driver_chrome, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_chrome)
        order_list_page.open_url(data.ORDER_LIST_URL)

        order_list_page.click_first_order()

        assert order_list_page.check_order_details()

    @allure.title("GoogleChrome - Проверка, что заказ из раздела «История заказов» отображается "
                  "на странице «Лента заказов»")
    def test_check_order_in_orders_list_chrome(self, driver_chrome, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        main_page = MainPage(driver_chrome)
        personal_account_page = PersonalAccountPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_personal_account_button()  # переходим в личный кабинет
        personal_account_page.click_order_history()  # переходим в историю заказов
        order_id = personal_account_page.get_created_order_id()  # запоминаем id заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert order_list_page.find_order_in_list(order_id)  # ищем заказ в ленте

    @allure.title("GoogleChrome - Проверка, при создании нового заказа счётчик Выполнено за всё время увеличивается»")
    def test_all_orders_counter_chrome(self, driver_chrome, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        main_page = MainPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы
        order_counter = int(order_list_page.get_all_orders_counter())
        header_page.click_constructor_button()  # переходим в коснтруктор
        main_page.find_make_burger_title()  # ждем загрузки страницы
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert int(order_list_page.get_all_orders_counter()) == (order_counter + 1)

    @allure.title("GoogleChrome - Проверка, при создании нового заказа счётчик Выполнено за сегодня увеличивается»")
    def test_today_orders_counter_chrome(self, driver_chrome, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        main_page = MainPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы
        order_counter = int(order_list_page.get_today_orders_counter())
        header_page.click_constructor_button()  # переходим в коснтруктор
        main_page.find_make_burger_title()  # ждем загрузки страницы
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert int(order_list_page.get_today_orders_counter()) == (order_counter + 1)

    @allure.title("GoogleChrome - Проверка, что после оформления заказа его номер появляется в разделе В работе")
    def test_check_order_in_getting_ready_list_chrome(self, driver_chrome, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_chrome)
        login_page = LoginPage(driver_chrome)
        main_page = MainPage(driver_chrome)
        header_page = HeaderPage(driver_chrome)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        order_id = main_page.get_created_order_id()  # получаем id созданного заказа
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert order_list_page.find_order_in_getting_ready_list(order_id)

    @allure.title("Firefox - Проверка клика по заказу в ленте заказов")
    def test_click_order_firefox(self, driver_firefox, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_firefox)
        order_list_page.open_url(data.ORDER_LIST_URL)

        order_list_page.click_first_order()

        assert order_list_page.check_order_details()

    @allure.title("Firefox - Проверка, что заказ из раздела «История заказов» отображается "
                  "на странице «Лента заказов»")
    def test_check_order_in_orders_list_firefox(self, driver_firefox, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        main_page = MainPage(driver_firefox)
        personal_account_page = PersonalAccountPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_personal_account_button()  # переходим в личный кабинет
        personal_account_page.click_order_history()  # переходим в историю заказов
        order_id = personal_account_page.get_created_order_id()  # запоминаем id заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert order_list_page.find_order_in_list(order_id)  # ищем заказ в ленте

    @allure.title("Firefox - Проверка, при создании нового заказа счётчик Выполнено за всё время увеличивается»")
    def test_all_orders_counter_firefox(self, driver_firefox, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        main_page = MainPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы
        order_counter = int(order_list_page.get_all_orders_counter())
        header_page.click_constructor_button()  # переходим в коснтруктор
        main_page.find_make_burger_title()  # ждем загрузки страницы
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert int(order_list_page.get_all_orders_counter()) == (order_counter + 1)

    @allure.title("Firefox - Проверка, при создании нового заказа счётчик Выполнено за сегодня увеличивается»")
    def test_today_orders_counter_firefox(self, driver_firefox, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        main_page = MainPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы
        order_counter = int(order_list_page.get_today_orders_counter())
        header_page.click_constructor_button()  # переходим в коснтруктор
        main_page.find_make_burger_title()  # ждем загрузки страницы
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert int(order_list_page.get_today_orders_counter()) == (order_counter + 1)

    @allure.title("Firefox - Проверка, что после оформления заказа его номер появляется в разделе В работе")
    def test_check_order_in_getting_ready_list_firefox(self, driver_firefox, register_new_user_and_get_data):
        order_list_page = OrdersListPage(driver_firefox)
        login_page = LoginPage(driver_firefox)
        main_page = MainPage(driver_firefox)
        header_page = HeaderPage(driver_firefox)
        user_data = register_new_user_and_get_data  # регистрируем нового пользователя, получаем данные для входа

        login_page.login_new_user(user_data)  # логин
        main_page.add_ingredient()  # добавляем булку
        main_page.click_create_order()  # создаем заказ
        order_id = main_page.get_created_order_id()  # получаем id созданного заказа
        main_page.close_created_order()  # закрываем окно созданного заказа
        header_page.click_orders_list_button()  # переходим в ленту заказов
        order_list_page.find_orders_list_title()  # ждем загрузки страницы

        assert order_list_page.find_order_in_getting_ready_list(order_id)
