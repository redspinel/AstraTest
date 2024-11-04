import time

from Pages.Base_page import BasePage
from Locators.authorization_locators import AuthorizationLocators
from Utils import config


class Authorization(BasePage):
    def __init__(self, driver, instance):
        super().__init__(driver)
        self.driver = driver
        time.sleep(2)
        self.url_login = config.LOGIN_URL_TEST_VANILLA if instance == "vanilla" else config.LOGIN_URL_TEST_ASTRADISK

    def login(self):
        self.driver.get(self.url_login)
        time.sleep(2)
        self.element_is_visible(AuthorizationLocators.LOGO_IMAGE)
        try:
            self.element_is_visible(AuthorizationLocators.EMAIL_INPUT_INACTIVE)
            self.element_clickable(AuthorizationLocators.EMAIL_INPUT_INACTIVE).click()
        except Exception as e:
                print(e)
        self.element_is_visible(AuthorizationLocators.EMAIL_INPUT_ACTIVE)
        self.element_is_visible(AuthorizationLocators.EMAIL_INPUT_ACTIVE).send_keys(config.EMAIL)

        self.element_is_visible(AuthorizationLocators.PASSWORD_INPUT).send_keys(config.PASSWORD)
        self.element_clickable(AuthorizationLocators.LOGIN_BUTTON).click()
        self.element_is_visible(AuthorizationLocators.DASHBOARD_CHECK)
        self.element_is_not_visible(AuthorizationLocators.LAST_ELEMENT)

    def is_logged_in(self):
        """Проверка, что пользователь авторизован и виден дашборд"""
        try:
            return self.element_is_visible(AuthorizationLocators.DASHBOARD_CHECK) is not None
        except:
            return False