from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOGO_IMAGE = (By.XPATH, "//form[@name='login' and @class='login-form']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='user' and @name='user' and @class='input-field__input']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password' and @name='password' and @class='input-field__input input-field__input--trailing-icon']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='button-vue__text' and text()='Войти']")
    DASHBOARD_CHECK = (By.XPATH, "//a[@href='#' and @class='button new' and @aria-label='Меню создания файла или папки']/span[text()='Новый']")
    LAST_ELEMENT = (By.XPATH, "//div[@class='mask icon-loading']")
    EMAIL_INPUT_INACTIVE= (By.XPATH, "//input[@id='user' and @class='input-field__input']")
    EMAIL_INPUT_ACTIVE = (By.XPATH, "//input[@id='user' and contains(@class, 'input-field__input') and contains(@class, 'focus-visible')]")



