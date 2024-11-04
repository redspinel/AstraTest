import os
import shutil
import subprocess
import getpass

def clean_directory(path):
    if os.path.exists(path):
        print(f"Очистка директории: {path}")
        shutil.rmtree(path)
    os.makedirs(path)
    print(f"Создана директория: {path}")

if __name__ == "__main__":
    current_user = getpass.getuser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    allure_dir = os.path.join(BASE_DIR, 'AllureReports')
    screenshots_dir = os.path.join(BASE_DIR, 'Screenshots')

    print(f"Базовая директория: {BASE_DIR}")
    print(f"Путь для результатов Allure: {allure_dir}")
    print(f"Путь для скриншотов: {screenshots_dir}")

    # Очистка папок для отчетов и скриншотов
    clean_directory(allure_dir)
    clean_directory(screenshots_dir)

    # Запуск всех тестов сразу с указанием директории для результатов Allure
    print("Запуск тестов с использованием pytest...")
    result = subprocess.call(['pytest', '--alluredir', allure_dir])
    if result != 0:
        print("Ошибка при выполнении тестов.")
    else:
        print("Тесты завершены успешно.")

    # Инструкция для ручного открытия Allure отчета
    print("\nДля генерации и открытия отчета Allure вручную выполните следующие команды в консоли:")
    print(f"allure generate {allure_dir} -o {allure_dir}/report --clean")
    print(f"allure open {allure_dir}/report")
