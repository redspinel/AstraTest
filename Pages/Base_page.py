import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import allure
from datetime import datetime



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=15):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator, timeout: int = 15) -> str:
        try:
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            raise TimeoutException(f"Не удалось найти элемент за {timeout} секунд. Локатор: {locator}")

    def element_is_not_visible(self, locator, timeout=15):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def get_hidden_element_text(self, locator, timeout=15):
        element = wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element.get_attribute("value")

    def text_to_be_present_in_element(self, locator, text, timeout=15):
        return wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def element_clickable(self, locator: object, timeout: object = 20) -> object:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element_by_text(self, text, timeout=15):
        xpath = f"//*[contains(text(), '{text}')]"
        return wait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return element

    def get_screenshots(self, duration):
        end_time = time.time() + duration
        screenshot_paths = []

        # Определяем путь к папке screenshots относительно текущего файла
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        screenshots_dir = os.path.join(project_root, "Screenshots")  # Путь к папке screenshots

        # Создаем папку screenshots, если ее нет
        os.makedirs(screenshots_dir, exist_ok=True)

        while time.time() < end_time:
            now_date = datetime.now().strftime("%Y.%m.%d.%H.%M.%S.%f")
            unique_id = str(uuid.uuid4())  # Генерация уникального идентификатора
            name_screenshot = f'screenshot_{now_date}_{unique_id}.png'
            screenshot_path = os.path.join(screenshots_dir, name_screenshot)  # Полный путь к скриншоту
            self.driver.save_screenshot(screenshot_path)
            screenshot_paths.append(screenshot_path)
            time.sleep(0.1) # пауза между скриншотами

        # Прикрепление всех скриншотов к отчету Allure
        for path in screenshot_paths:
            allure.attach.file(path, name=f"Скриншот {os.path.basename(path)}",
                               attachment_type=allure.attachment_type.PNG)

        return screenshot_paths

