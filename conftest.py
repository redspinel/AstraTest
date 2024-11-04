import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Utils import config
import os

@pytest.fixture(scope="function")
def driver():
    print("Chrome Driver Path:", config.chrome_driver_path)
    print("Chrome Binary Path:", config.chrome_binary_path)
    print("Download Directory:", config.download_dir)

    if not os.path.isfile(config.chrome_driver_path):
        raise FileNotFoundError(f"Chrome driver not found at {config.chrome_driver_path}")
    if not os.path.isfile(config.chrome_binary_path):
        raise FileNotFoundError(f"Chrome binary not found at {config.chrome_binary_path}")

    service = Service(config.chrome_driver_path)
    options = Options()
    options.binary_location = config.chrome_binary_path

    prefs = {
        "download.default_directory": config.download_dir,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)

    # Оптимизация Chrome для снижения нагрузки
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--force-device-scale-factor=1")  # Зум браузера
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
