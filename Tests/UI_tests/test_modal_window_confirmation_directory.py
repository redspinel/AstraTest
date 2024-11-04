import time
from random import random

import pytest
import allure
import random
from selenium.common import TimeoutException

from Classes.Authorization import Authorization
from Classes.FileManager import FileManager
from Locators.dashboard_locators import DashboardLocators
from Pages.Base_page import BasePage
from Pages.Dashboard_page import DashboardPage

from Utils.config import files_path

@pytest.mark.order(2)
@pytest.mark.parametrize("instance", ["vanilla", "astradisk"])
def test_modal_window_confirmation_directory(driver, instance):
    allure.dynamic.title(f"Проверка модального окна подтверждения после удаления директорий в {instance}")
    auth = Authorization(driver, instance=instance)
    auth.login()

    base_page = BasePage(driver)
    DP = DashboardPage(driver)
    file_manager = FileManager(driver, base_page, DP, files_path)

    with allure.step("Проверка наличия объектов"):
        try:
            base_page.element_is_visible(DashboardLocators.NO_FILES)
        except TimeoutException:
            file_manager.delete_all_objects_ui()
            base_page.element_is_visible(DashboardLocators.NO_FILES)

    with allure.step("Добавление тестового каталога и далее открытие модального окна подтверждения"):
        num_dirs_to_create = random.randint(1, 5)
        created_directories = []

        # Создание директорий
        for _ in range(num_dirs_to_create):
            directory_name_list = file_manager.create_directory()
            created_directories.append(directory_name_list)

        num_dir = len(created_directories)
        if num_dir == 1:
            row_index = DP.find_row_by_obj_name(created_directories[0])
            time.sleep(5)
            base_page.element_is_visible(DashboardLocators.CHECKBOX_IN_ROW(row_index))
            base_page.element_clickable(DashboardLocators.CHECKBOX_IN_ROW(row_index)).click()
            base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE)
            base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()
            base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()
        else:
            # Проверка наличия всех созданных директорий на странице
            time.sleep(5)
            base_page.element_is_visible(DashboardLocators.SELECT_ALL_FILES_CHECKBOX)
            base_page.element_clickable(DashboardLocators.SELECT_ALL_FILES_CHECKBOX).click()
            base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE)
            base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()
            base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()


    with allure.step("Проверка модального окна подтверждения"):
        try:
            base_page.get_screenshots(duration=1)
            base_page.element_is_visible(DashboardLocators.APPROVE_MODAL)
        except TimeoutException:
            pytest.fail("Функционал модального окна подтверждения отсутствует, тест завершен с ошибкой.")
            file_manager.delete_all_objects_ui()
            base_page.element_is_visible(DashboardLocators.NO_FILES)
            driver.quit()
        base_page.get_screenshots(duration=1)
        output_text_title = base_page.get_element_text(DashboardLocators.DELETE_CONFIRMATION_TITLE)
        expected_text_title = f"Удалить {num_dir} {DP.world_endings(num_dir, 'каталог', 'каталога', 'каталогов')}?"
        assert expected_text_title == output_text_title, (
            "Полученный текст заголовка модального окна не равен ожидаемому."
            f"Получено: '{output_text_title}'. Ожидалось: '{expected_text_title}'")

        modal_text_message_output = base_page.get_element_text(DashboardLocators.DELETE_CONFIRMATION_TEXT)
        expected_modal_text_message = f"Вы уверены, что хотите удалить {num_dir} {DP.world_endings(num_dir, 'каталог', 'каталога', 'каталогов')}?"
        assert expected_modal_text_message == modal_text_message_output, (
            "Полученный текст сообщения модального окна не равен ожидаемому."
            f" Получено '{modal_text_message_output}'. Ожидалось '{expected_modal_text_message}'")

        close_button = base_page.element_is_visible(DashboardLocators.CLOSE_DIALOG_BUTTON)
        assert close_button is not None, "Не найдена кнопка 'Закрыть' в модальном окне подтверждения"

        no_button = base_page.element_is_visible(DashboardLocators.NO_BUTTON)
        assert no_button is not None, "Не найдена кнопка 'НЕТ' в модальном окне подтверждения"

        yes_button = base_page.element_is_visible(DashboardLocators.YES_BUTTON)
        assert yes_button is not None, "Не найдена кнопка 'ДА' в модальном окне подтверждения"

    with allure.step(f"Проверка закрытия модально окна через крестик"):
        time.sleep(1)
        base_page.element_clickable(DashboardLocators.CLOSE_DIALOG_BUTTON).click()
        assert base_page.element_is_not_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE), (
            "Модальное окно выбора действия не закрылось после нажатия на крестик"
        )

    with allure.step(f"Проверка закрытие модально окна через нажатие на кнопку 'НЕТ'"):
        with allure.step(f"Повторное открытие модального окна"):
            if base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE):
                base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()
            base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()
            base_page.element_is_visible(DashboardLocators.APPROVE_MODAL)

        with allure.step(f"Нажатие на кнопку 'НЕТ'"):
            base_page.element_is_visible(DashboardLocators.NO_BUTTON)
            time.sleep(1)
            base_page.element_clickable(DashboardLocators.NO_BUTTON).click()
            assert base_page.element_is_not_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE), (
                "Модальное окно выбора действия не закрылось после нажатия на кнопку'НЕТ'"
            )

    with allure.step(f"Проверка закрытия модально окна через нажатие на кнопку 'ДА'"):
        with allure.step(f"Повторное открытие модального окна"):
            if base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE):
                base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()
            base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()
            base_page.element_is_visible(DashboardLocators.APPROVE_MODAL)

        with allure.step(f"Нажатие на кнопку 'ДА'"):
            base_page.element_is_visible(DashboardLocators.YES_BUTTON)
            time.sleep(1)
            base_page.element_clickable(DashboardLocators.YES_BUTTON).click()
            base_page.get_screenshots(duration=1)
            assert base_page.element_is_not_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE), (
                "Модальное окно выбора действия не закрылось после Нажатие на кнопку 'ДА' "
            )

    with allure.step("Удаление тестовых данных"):
        try:
            base_page.element_is_visible(DashboardLocators.NO_FILES)
        except TimeoutException:
            file_manager.delete_all_objects_ui()
            base_page.element_is_visible(DashboardLocators.NO_FILES)