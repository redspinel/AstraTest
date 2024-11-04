import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from Locators.dashboard_locators import DashboardLocators
from Pages.Base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_row_by_obj_name(self, obj_name):
        """
        Находит номер строки по имени директории в таблице и возвращает номер строки или None, если директория не найдена.

        :param obj_name: Имя директории для поиска
        :return: Номер строки (int) или None, если директория не найдена
        """
        try:
            time.sleep(5)
            rows = self.elements_are_visible(DashboardLocators.FILE_TABLE_ROWS, timeout=15)

            for index, row in enumerate(rows, start=1):
                try:
                    directory_element = row.find_element(*DashboardLocators.DIRECTORY_NAME_IN_ROW)
                    actual_name = directory_element.get_attribute("title")
                    if actual_name == obj_name:
                        return index
                except NoSuchElementException:
                    continue
            return None
        except Exception as e:
            print(f"Ошибка при поиске: {e}")
            return None

    def world_endings(self, number, one, few, many):
        """
        Возвращает правильную форму слова в зависимости от числа.

        :param number: Число
        :param one: Форма для 1 (например, "каталог")
        :param few: Форма для 2, 3, 4 (например, "каталога")
        :param many: Форма для 5 и больше (например, "каталогов")
        :return: Правильная форма слова
        """
        if number % 10 == 1 and number % 100 != 11:
            return one
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return few
        else:
            return many