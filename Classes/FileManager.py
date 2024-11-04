import time

import allure
import random
from Locators.dashboard_locators import DashboardLocators


class FileManager:
    def __init__(self, driver, base_page, dash_board_page, files_path):
        self.driver = driver
        self.base_page = base_page
        self.dash_board_page = dash_board_page
        self.file_list = []
        self.files_path = files_path


    def add_file_to_list(self, file_name):
        """Добавление файла в локальный список файлов для отслеживания"""
        self.file_list.append(file_name)

    def upload_file_ui(self, file_name):
        """Метод для загрузки файла через UI"""
        with allure.step("Загрузка файла через UI"):
            pass

    def upload_file_api(self, file_name):
        """Метод для загрузки файла через API"""
        with allure.step("Загрузка через API"):
            pass

    def delete_file_ui(self, file_name):
        """Метод для удаления файла через UI"""
        with allure.step(f"Удаление файла через UI {file_name}"):
            pass

    def delete_all_objects_ui(self):
        """Метод для удаления всех файлов через UI"""
        with allure.step(f"Удаление всех объектов через UI"):
            # Нажатие на чек-бокс "Выбрать все файлы"
            if self.base_page.element_is_visible(DashboardLocators.SELECT_ALL_FILES_CHECKBOX):
                self.base_page.element_clickable(DashboardLocators.SELECT_ALL_FILES_CHECKBOX).click()

            # Нажатие на кнопку "Действия"
            if self.base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE):
                self.base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()

            # Попытка удалить все файлы
            self.base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            self.base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()

            # Подтверждение удаления в модальном окне
            self.base_page.element_clickable(DashboardLocators.YES_BUTTON).click()

    def create_directory(self, directory_name=None):
        """
        Создает новую директорию с заданным именем или случайным, если имя не передано.

        :param directory_name: Имя директории для создания (опционально)
        :return: Имя созданной директории
        """
        # Если имя директории не указано, генерируем случайное имя
        if not directory_name:
            directory_name = str(random.randint(1, 9999999))

        with (allure.step("Создание новой директории")):
            # Открываем меню создания папки
            self.base_page.element_is_not_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            self.base_page.element_is_visible(DashboardLocators.DASHBOARD_CHECK)
            self.base_page.element_clickable(DashboardLocators.DASHBOARD_CHECK).click()
            time.sleep(1.5)

            # Нажимаем кнопку создания новой папки
            self.base_page.element_is_visible(DashboardLocators.NEW_FOLDER_NAME)
            self.base_page.element_clickable(DashboardLocators.NEW_FOLDER_NAME).click()

            # Вводим имя директории
            time.sleep(1.5)
            self.base_page.element_is_visible(DashboardLocators.NEW_FOLDER_INPUT)
            self.base_page.element_is_visible(DashboardLocators.NEW_FOLDER_INPUT).send_keys(directory_name)

            # Подтверждаем создание директории
            time.sleep(1.5)
            self.base_page.element_is_visible(DashboardLocators.CREATE_FOLDER_SUBMIT_BUTTON)
            self.base_page.element_clickable(DashboardLocators.CREATE_FOLDER_SUBMIT_BUTTON).click()

        # Добавляем имя новой директории в список для отслеживания
        self.file_list.append(directory_name)

        return directory_name


    def delete_all_files_api(self, files):
        """Метод для удаления всех файлов через API"""
        with allure.step(f"Удаление всех файлов через API {files}"):
            pass

    def delete_file_api(self, file_name):
        """Метод для удаления файла через API"""
        with allure.step(f"Удаление файла через API {file_name}"):
            pass

    def files_exists_ui(self, files):
        """Проверка, что файл присутствует в UI"""
        with allure.step(f"Проверка, что файл присутствует в UI {files}"):
            pass

    def files_exists_api(self, files):
        """Проверка, что файл присутствует через API"""
        with allure.step(f"Проверка, что файл присутствует через API {files}"):
            pass
