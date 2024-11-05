# Проект для автоматизации тестирования Nextcloud и Astra.Disk


## Описание
Этот проект содержит автотесты для проверки функционала модального окна подтверждения действий при удалении файлов и каталогов в двух инстансах:
- **Ванильный Nextcloud** - без подтверждения действий (модальное окно отсутствует)
- **Astra.Disk** - с подтверждением действий (модальное окно присутствует)


## Структура проекта
- `Classes/Authorization.py`: Авторизация пользователя.
- `Classes/FileManager.py`: Управление файлами (загрузка, удаление и пр.).
- `Pages/BasePage.py`: Базовый класс для всех страниц.
- `Tests/`: Папка с тестами.
- `Utils/`: Папка с вспомогательными файлами и конфигурацией.


## Установка и настройка
git clone https://github.com/your-repo.git


## Установите зависимости:
pip install -r requirements.txt


## Указать login и password
в Utils.config.py


## Примечания
Так как это тестовое задание, в связи с нехваткой времени некоторый функционал не реализован полностью:
1. Перед запуском тестов необходимо вручную загрузить файлы на каждый инстанс, так как автоматическая загрузка не реализована. 
Указать кол-во загруженных файлов в самом коде теста
2. На момент запуска теста test_modal_window_confirmation_files не должно быть создано директорий (только файлы), так как текущий функционал не реализован.
Настройка Allure: Для получения отчёта требуется установленный Allure. Установите его, следуя инструкции ниже.

### Шаги установки проекта на Ubuntu
cd ~/your_directory  # Заменить `your_directory` на нужную папку
git clone https://github.com/redspinel/AstraTest.git
cd AstraTest
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
nano Utils/config.py # Вписать login и pass > Сохранить
скачать 'chrome' файл или весь архив (https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chrome-linux64.zip) и переместить в Browsers>chrome-linux64
wget https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz
tar -zxvf allure-2.32.0.tgz
sudo mv ~/Downloads/allure-2.32.0 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/bin/allure
sudo apt update
sudo apt install -y openjdk-11-jre
java -version
allure --version
запуск тестов: pytest


### Настройка Chrome и ChromeDriver
Страница загрузки https://googlechromelabs.github.io/chrome-for-testing/#stable
1. **Для Windows**: 
   - Поместите Chrome в `Browsers/chrome-win64` и ChromeDriver в `Drivers/chromedriver-win64`.
   - Скачать Chrome https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/win64/chrome-win64.zip.
   - Скачать Driver https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/win64/chromedriver-win64.zip
   - После скачивания извлеките файл `chrome.dll` и переместите его в директорию проекта `Browsers/chrome-win64/` в папке проекта или замените полностью файлы на новые.

2. **Для Ubuntu/Linux**:
   - Поместите Chrome в `Browsers/chrome-linux64` и ChromeDriver в `Drivers/chromedriver-linux64`.
   - Скачать Chrome https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chrome-linux64.zip
   - Скачать Driver https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chromedriver-linux64.zip
   - После скачивания извлеките файл `chrome` и переместите его в директорию проекта `Borwsers/chrome-linux64` в папке проекта или замените полностью файлы на новые.
   - Сделайте файлы исполняемыми:
   - Перейти в папку проекта, далее
     ```bash
     chmod +x /path/to/ASTRA/Browsers/chrome-linux64/chrome
     chmod +x /path/to/ASTRA/Drivers/chromedriver-linux64/chromedriver
     ```


### Установка Allure для генерации отчетов linux
1. **Для Ubuntu/Linux**:
Способ 1: Установка через PPA (рекомендуется для Ubuntu)
    - sudo apt-add-repository ppa:qameta/allure
    - sudo apt update
    - sudo apt install allure

Способ 2: Установка вручную для других дистрибутивов Linux
    - Скачайте последнюю версию Allure:
    wget https://github.com/allure-framework/allure2/releases/download/2.20.1/allure-2.20.1.tgz
    - Распакуйте архив:
    tar -zxvf allure-2.20.1.tgz
    - Переместите файлы в /opt и создайте символическую ссылку:
    sudo mv allure-2.20.1 /opt/allure
    sudo ln -s /opt/allure/bin/allure /usr/bin/allure
    - Запуск тестов
    pytest
    - Генерация и просмотр отчетов Allure
    allure generate AllureReports -o AllureReports/report --clean
    allure open AllureReports/report


### Установка Allure для генерации отчетов на Windows
1. **Скачайте последнюю версию Allure**:
   - Перейдите на [страницу релизов Allure](https://github.com/allure-framework/allure2/releases) и скачайте ZIP-архив последней версии для Windows. В проекте используется `allure-2.32.0.zip`.

2. **Распакуйте архив**:
   - Извлеките содержимое архива (например, в `C:\allure`).

3. **Добавьте Allure в переменные среды PATH**:
   - Откройте «Параметры системы» → «Дополнительные параметры системы».
   - Перейдите в «Переменные среды».
   - В списке «Системные переменные» найдите переменную `Path` и нажмите «Изменить».
   - Добавьте путь к папке `bin` внутри директории Allure, например: `C:\allure\bin`.
   - Сохраните изменения и перезагрузите терминал (или систему, если нужно), чтобы изменения вступили в силу.

4. **Проверьте установку**:
   - Откройте командную строку и выполните команду:
     ```cmd
     allure --version
     ```
   - Если все настроено правильно, вы увидите версию Allure.

5. **Запуск тестов**:
   - Запустите тесты с использованием `run.py`:
     ```cmd
     python run.py
     ```

6. **Генерация и просмотр отчетов Allure**:
   - После выполнения тестов для генерации отчета выполните:
     ```cmd
     allure generate AllureReports -o AllureReports\report --clean
     ```
   - Чтобы открыть отчет:
     ```cmd
     allure open AllureReports\report
     ```

Теперь Allure установлен и готов к использованию на Windows.







