from selenium.webdriver.common.by import By

class DashboardLocators:
    SELECT_ALL_FILES_CHECKBOX = (By.XPATH, "//label[@for='select_all_files']")
    USER_INPUT_INACTIVE = (By.XPATH, "//span[@class='selectedActions']/a[@class='actions-selected']")
    SELECT_MENU_MODAL_ACTIVE= (By.XPATH, "//div[contains(@class, 'filesSelectMenu') and contains(@class, 'popovermenu') and contains(@class, 'bubble') and contains(@class, 'menu-center') and contains(@style, 'display: block;')]")
    SELECT_MENU_MODAL_INACTIVE = (By.XPATH, "//div[contains(@class, 'filesSelectMenu') and contains(@class, 'popovermenu') and contains(@class, 'bubble') and contains(@class, 'menu-center') and contains(@style, 'display: none;')]")
    DELETE_ACTION = (By.XPATH, "//a[@class='menuitem action delete permanent' and @data-action='delete']/span[@class='icon icon-delete']")
    APPROVE_MODAL = (By.XPATH, "//div[@class='oc-dialog' and @role='dialog']")
    DELETE_CONFIRMATION_TITLE = (By.XPATH, "//h2[@class='oc-dialog-title']")
    DELETE_CONFIRMATION_TEXT = (By.XPATH, "//div[@class='oc-dialog-content']/p")
    CLOSE_DIALOG_BUTTON = (By.XPATH, "//button[@class='oc-dialog-close']")
    NO_BUTTON = (By.XPATH, "//div[@class='oc-dialog-buttonrow twobuttons']/button[text()='Нет']")
    YES_BUTTON = (By.XPATH, "//div[@class='oc-dialog-buttonrow twobuttons']/button[@class='primary' and text()='Да']")
    NO_FILES = (By.CLASS_NAME, "emptyfilelist")
    DASHBOARD_CHECK = (By.XPATH, "//a[contains(@class, 'button') and contains(@class, 'new')]")
    NEW_FOLDER_NAME = (By.XPATH, "//a[@class='menuitem' and @data-filetype='folder' and @data-action='folder']/span[@class='displayname' and text()='Новая папка']")
    NEW_FOLDER_INPUT = (By.XPATH, "//input[@id='view7-input-folder' and @type='text' and @value='Новая папка']")
    CREATE_FOLDER_SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit' and @class='icon-confirm' and @aria-label='Создать папку']")
    FILE_TABLE_ROWS = (By.CSS_SELECTOR, "tbody.files-fileList tr")
    DIRECTORY_NAME_IN_ROW = (By.CSS_SELECTOR, "span.innernametext")
    CHECKBOX_IN_ROW = lambda row_index: (By.XPATH, f"//tbody[@class='files-fileList']/tr[{row_index}]/td[@class='selection']/label")















