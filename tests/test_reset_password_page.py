import pytest
import allure
import data
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage


class TestResetPasswordPage:

    @allure.title("GoogleChrome - Проверка перехода на страницу восстановления пароля со страницы логина")
    def test_go_to_forgot_password_page_chrome(self, driver_chrome):
        login_page = LoginPage(driver_chrome)
        login_page.open_url(data.LOGIN_PAGE_URL)

        login_page.click_reset_password_link()

        assert login_page.opened_page_url() == data.FORGOT_PASSWORD_PAGE_URL

    @allure.title("GoogleChrome - Проверка клика по кнопке 'Восстановить'")
    def test_click_reset_button_chrome(self, driver_chrome):
        reset_password_page = ResetPasswordPage(driver_chrome)
        reset_password_page.open_url(data.FORGOT_PASSWORD_PAGE_URL)

        reset_password_page.fill_in_email(data.EMAIL)
        reset_password_page.click_reset_button()

        assert reset_password_page.opened_page_url() == data.RESET_PASSWORD_PAGE_URL

    @allure.title("GoogleChrome - Проверка клика по кнопке показать пароль")
    def test_click_show_password_button_chrome(self, driver_chrome):
        reset_password_page = ResetPasswordPage(driver_chrome)
        reset_password_page.open_url(data.FORGOT_PASSWORD_PAGE_URL)

        reset_password_page.fill_in_email(data.EMAIL)
        reset_password_page.click_reset_button()

        reset_password_page.show_password()

        assert reset_password_page.check_if_password_filed_is_active()

    @allure.title("Firefox - Проверка перехода на страницу восстановления пароля со страницы логина")
    def test_go_to_forgot_password_page_firefox(self, driver_firefox):
        login_page = LoginPage(driver_firefox)
        login_page.open_url(data.LOGIN_PAGE_URL)

        login_page.click_reset_password_link()

        assert login_page.opened_page_url() == data.FORGOT_PASSWORD_PAGE_URL

    @allure.title("Firefox - Проверка клика по кнопке 'Восстановить'")
    def test_click_reset_button_firefox(self, driver_firefox):
        reset_password_page = ResetPasswordPage(driver_firefox)
        reset_password_page.open_url(data.FORGOT_PASSWORD_PAGE_URL)

        reset_password_page.fill_in_email(data.EMAIL)
        reset_password_page.click_reset_button()

        assert reset_password_page.opened_page_url() == data.RESET_PASSWORD_PAGE_URL

    @allure.title("Firefox - Проверка клика по кнопке показать пароль")
    def test_click_show_password_button_firefox(self, driver_firefox):
        reset_password_page = ResetPasswordPage(driver_firefox)
        reset_password_page.open_url(data.FORGOT_PASSWORD_PAGE_URL)

        reset_password_page.fill_in_email(data.EMAIL)
        reset_password_page.click_reset_button()

        reset_password_page.show_password()

        assert reset_password_page.check_if_password_filed_is_active()

