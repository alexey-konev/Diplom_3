from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    EMAIL_FIELD = By.XPATH, ".//*[@class = 'text input__textfield text_type_main-default']"
    RESET_BUTTON = By.XPATH, ".//*[contains(@class, 'button_button') and text() = 'Восстановить']"
    PASSWORD_FIELD = By.XPATH, ".//*[@name='Введите новый пароль']"
    SHOW_PASSWORD_BUTTON = By.XPATH, ".//*[@class = 'input__icon input__icon-action']"
    ACTIVE_PASSWORD_FIELD = By.XPATH, ".//*[@class='input__container']/*[contains(@class, 'input_status_active')]"
    CODE_FIELD = By.XPATH, ".//*[contains(@class, 'input__placeholder') and text() = 'Введите код из письма']"


class LoginPageLocators:

    EMAIL_FIELD = By.XPATH, ".//*[@type='text']"
    PASSWORD_FIELD = By.XPATH, ".//*[@type='password']"
    LOGIN_BUTTON = By.XPATH, ".//*[contains(@class, 'button_button') and text() = 'Войти']"
    RESET_PASSWORD_LINK = By.XPATH, ".//*[contains(@class, 'Auth_link') and text() = 'Восстановить пароль']"
    MODAL_DIV = By.XPATH, ".//div[contains(@class, 'Modal_modal')]/div[contains(@class, 'Modal_modal_overlay')]"
    MODAL_SECTION = By.XPATH, ".//section[contains(@class, 'Modal_modal')]/div[contains(@class, 'Modal_modal_overlay')]"


class PersonalAccountPageLocators:

    PERSONAL_ACC_BUTTON_MAIN_PAGE = By.XPATH, './/nav/a[contains(@class, "AppHeader_header__link")]'
    ORDER_HISTORY_TAB = By.XPATH, ".//*[contains(@class, 'Account_link') and text() = 'История заказов']"
    EXIT_BUTTON = By.XPATH, ".//*[contains(@class, 'Account_button') and text() = 'Выход']"
    ORDER_ID = By.XPATH, ".//*[contains(@class, 'OrderHistory_listItem')][last()]/a/div/p[contains(@class, 'text text_type_digits-default')]"


class HeaderPageLocators:
    PERSONAL_ACC_BUTTON_HEADER = By.XPATH, ".//nav/a[contains(@class, 'AppHeader_header__link')]"
    CONSTRUCTOR_BUTTON_HEADER = By.XPATH, ".//*[contains(@class, 'AppHeader_header__linkText') and text() = 'Конструктор']"
    ORDERS_LIST_BUTTON_HEADER = By.XPATH, ".//*[contains(@class, 'AppHeader_header__linkText') and text() = 'Лента Заказов']"


class MainPageLocators:

    ORDERS_LIST_TITLE = By.XPATH, ".//*[contains(@class, 'text text_type_main-large') and text() = 'Лента заказов']"
    MAKE_BURGER_TITLE = By.XPATH, ".//*[contains(@class, 'text text_type_main-large') and text() = 'Соберите бургер']"
    INGREDIENT_DETAILS_WINDOW = By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]"  #.//*[contains(@class, 'Modal_modal_opened')]//*[contains(@class, 'Modal_modal__title') and text() = 'Детали ингредиента']
    FIRST_BUN = By.XPATH, ".//*[contains(@class, 'BurgerIngredient_ingredient')]//following::img[@alt='Флюоресцентная булка R2-D3']"
    INGREDIENT_DETAILS_CLOSE_BUTTON = By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]//*[contains(@class, 'Modal_modal__close')]"
    INGREDIENT_BASKET = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    INGREDIENT_COUNTER = By.XPATH, (".//img[@alt='Флюоресцентная булка R2-D3']//parent::*[contains(@class, 'BurgerIngredient_ingredient')]"
                                    "/*[contains(@class, 'counter_counter')]/*[contains(@class, 'counter_counter__num')]")
    CREATE_ORDER_BUTTON = By.XPATH, ".//*[text()='Оформить заказ']"
    ORDER_CREATED_TEXT = By.XPATH, ".//*[text()='Ваш заказ начали готовить']"
    MODAL_LOADING = By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']"
    ORDER_ID = By.XPATH, ".//*[contains(@class, 'Modal_modal__title_shadow')]"
    CREATED_ORDER_CLOSE_BUTTON = By.XPATH, ".//*[contains(@class, 'Modal_modal__close_modified')]"

class OrdersListPageLocators:

    FIRST_ORDER_IN_LIST = By.XPATH, ".//*[contains(@class, 'OrderFeed_list')]/*[1]/*[contains(@class, 'OrderHistory_link')]"
    ORDER_ITEMS_LIST = By.XPATH, ".//*[text()='Cостав']"
    ORDER_ID_IN_LIST = By.XPATH, ".//*[contains(@class, 'OrderHistory_link')]//*[contains(@class, 'text_type_digits') and text()='{}']"
    ALL_ORDER_COUNTER = By.XPATH, ".//*[text()='Выполнено за все время:']//parent::*/*[contains(@class, 'OrderFeed_number')]"
    TODAY_ORDER_COUNTER = By.XPATH, ".//*[text()='Выполнено за сегодня:']//parent::*/*[contains(@class, 'OrderFeed_number')]"
    ORDER_ID_IN_GETTING_READY = By.XPATH, ".//*[contains(@class, 'OrderFeed_orderListReady')]/*[text()='0' and text()='{}']"