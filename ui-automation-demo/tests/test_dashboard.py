import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.ui
def test_positive_login(driver):
    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем, что мы на Dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )
    assert "dashboard" in driver.current_url.lower()

@pytest.mark.ui
def test_negative_login(driver):
    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.NAME, "username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидаем сообщение об ошибке
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_message.is_displayed()
    except TimeoutException:
        pytest.fail("Сообщение об ошибке при неверном логине не появилось")

@pytest.mark.ui
def test_dashboard(driver):
    """
    Позитивный тест Dashboard:
    1. Логинимся
    2. Проверяем меню и таблицу
    """
    driver.get("http://127.0.0.1:5000/login")

    # Логинимся
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем меню
    try:
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main-menu"))
        )
        assert menu.is_displayed()
    except TimeoutException:
        pytest.fail("Меню Dashboard не появилось после логина")

    # Проверяем таблицу
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        assert table.is_displayed()
    except TimeoutException:
        pytest.fail("Таблица на Dashboard не появилась")

@pytest.mark.ui
def test_dashboard_menu(driver):
    """
    Тест Dashboard:
    Проверка отображения меню после логина
    """
    # 1. Открываем страницу логина
    driver.get("http://127.0.0.1:5000/login")

    # 2. Вводим логин и пароль
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 3. Ждём появления меню
    try:
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main-menu"))
        )
        # 4. Проверяем, что меню отображается
        assert menu.is_displayed()
    except TimeoutException:
        pytest.fail("Меню Dashboard не появилось после логина")


@pytest.mark.ui
def test_dashboard_table(driver):
    """
    Тест Dashboard — проверка таблицы после логина:
    1. Открываем страницу логина
    2. Логинимся верным пользователем
    3. Проверяем, что таблица на Dashboard появилась и видна
    """
    driver.get("http://127.0.0.1:5000/login")

    # Логинимся
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидаем таблицу
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        assert table.is_displayed(), "Таблица на Dashboard не видна"

        # Опционально: проверяем, что есть хотя бы одна строка
        rows = table.find_elements(By.TAG_NAME, "tr")
        assert len(rows) > 0, "Таблица пустая, нет строк"
    except TimeoutException:
        pytest.fail("Таблица на Dashboard не появилась после логина")


