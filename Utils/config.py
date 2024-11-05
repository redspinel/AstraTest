import os
import platform

# Данные для входа
LOGIN_URL_TEST_VANILLA = "https://test-vanilla.promo.astradisk.ru/"
LOGIN_URL_TEST_ASTRADISK = "https://test-disk.promo.astradisk.ru/"

EMAIL = ""
PASSWORD = ""

# Переход на уровень выше, чтобы получить корневую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Пути к драйверу и браузеру
if platform.system() == "Windows":
    chrome_driver_path = os.path.join(BASE_DIR, 'Drivers', 'chromedriver-win64', 'chromedriver.exe')
    chrome_binary_path = os.path.join(BASE_DIR, 'Browsers', 'chrome-win64', 'chrome.exe')
else:  # Для Linux
    chrome_driver_path = os.path.join(BASE_DIR, 'Drivers', 'chromedriver-linux64', 'chromedriver')
    chrome_binary_path = os.path.join(BASE_DIR, 'Browsers', 'chrome-linux64', 'chrome')

# Папка для загрузки файлов
download_dir = os.path.join(BASE_DIR, 'ASTRADISK')
files_path = os.path.join(BASE_DIR, 'Payload_data', 'Files')
