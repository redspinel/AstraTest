import pytest
import allure
from selenium.common import TimeoutException

from Classes.Authorization import Authorization
from Classes.FileManager import FileManager
from Locators.dashboard_locators import DashboardLocators
from Pages.Base_page import BasePage
import time

from Pages.Dashboard_page import DashboardPage
from Utils.config import files_path

@pytest.mark.order(1)
@pytest.mark.parametrize("instance", ["vanilla", "astradisk"])
def test_modal_window_confirmation_files(driver, instance, base_page=None):
    allure.dynamic.title(f"Проверка модального окна подтверждения после удаления файлов в {instance}")
    auth = Authorization(driver, instance=instance)
    auth.login()
    DP = DashboardPage(driver)
    file_manager = FileManager(driver, base_page, DP, files_path)
    base_page = BasePage(driver)

    with allure.step("Загрузка тестовых файлов"):
        #file_manager.upload_files_ui(file_list)
        # На данный момент ручная загрузка файлов, следует указать кол-во файлов, которое было загружено
        # num_files = len(file_manager.file_list)
        """Временная реализация загрузки"""
        num_files = 1
        # Автоматическая проверка загрузки файлов
        pass

    with allure.step("Проверка модального окна подтверждения"):
        # Временная проверка
        try:
            base_page.element_is_not_visible(DashboardLocators.NO_FILES)
        except TimeoutException:
            pytest.fail("Нет тестовых файлов. Следует загрузить файлы и указать их количество в num_files")
            driver.quit()

        with allure.step(f"Нажатие на чек-бокс Выбрать все файлы {num_files}"):
            if base_page.element_is_visible(DashboardLocators.SELECT_ALL_FILES_CHECKBOX):
                base_page.element_clickable(DashboardLocators.SELECT_ALL_FILES_CHECKBOX).click()

        with allure.step(f"Нажатие на кнопку Действия"):
            if base_page.element_is_visible(DashboardLocators.USER_INPUT_INACTIVE):
                base_page.element_clickable(DashboardLocators.USER_INPUT_INACTIVE).click()

        with allure.step(f"Проверка видимости модального окна выбора действия"):
            modal_actions = base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            assert modal_actions is not None, "Модальное окно выбора действия не открылось"

        with allure.step(f"Нажатие на крестик"):
            modal_actions = base_page.element_is_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE)
            assert modal_actions is not None, "Модальное окно выбора действия не открылось"

        with allure.step(f"Нажатие на кнопку Удалить"):
            base_page.element_is_visible(DashboardLocators.DELETE_ACTION)
            base_page.element_clickable(DashboardLocators.DELETE_ACTION).click()

        with allure.step("Проверка модального окна подтверждения"):
            base_page.get_screenshots(duration=1)
            try:
                base_page.element_is_visible(DashboardLocators.APPROVE_MODAL)
            except TimeoutException:
                pytest.fail("Функционал модального окна подтверждения отсутствует, тест завершен с ошибкой.")
                driver.quit()

            output_text_title = base_page.get_element_text(DashboardLocators.DELETE_CONFIRMATION_TITLE)
            if num_files == 1:
                expected_text_title = f"Удалить {num_files} файл?"
            else:
                expected_text_title = f"Удалить {num_files} файла?"
            assert expected_text_title == output_text_title, (
                "Полученный текст заголовка модального окна не равен ожидаемому."
                f"Получено: '{output_text_title}'. Ожидалось: '{expected_text_title}'")

            modal_text_message_output = base_page.get_element_text(DashboardLocators.DELETE_CONFIRMATION_TEXT)
            if num_files == 1:
                expected_modal_text_message = f"Вы уверены, что хотите удалить {num_files} файл?"
            else:
                expected_modal_text_message = f"Вы уверены, что хотите удалить {num_files} файла?"
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
            base_page.get_screenshots(duration=1)
            assert base_page.element_is_not_visible(DashboardLocators.SELECT_MENU_MODAL_ACTIVE), (
                "Модальное окно выбора действия не закрылось после нажатия на крестик"
            )


        with allure.step(f"Проверка закрытия модально окна через нажатие на кнопку 'НЕТ'"):
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

    with allure.step("Проверка что объекты после нажатия на кнопку 'ДА' удалились"):
        try:
            base_page.element_is_visible(DashboardLocators.NO_FILES)
        except TimeoutException:
            file_manager.delete_all_objects_ui()
            base_page.element_is_visible(DashboardLocators.NO_FILES)



