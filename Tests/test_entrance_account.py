from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators
from data import UsersTestData
driver: WebDriver = webdriver.Chrome()

# вход по кнопке «Войти в аккаунт» на главной
class TestEntranceAccount:
    def test_entrance_account(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        assert driver.find_element(*TestLocators.place_an_order).is_displayed()

# вход через кнопку «Личный кабинет»
class TestPersonalAccount:
    def test_personal_account(self, driver):
        driver.find_element(*TestLocators.personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.new_registration))
        driver.find_element(*TestLocators.email).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.password).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.enter).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        assert driver.find_element(*TestLocators.place_an_order).is_displayed()

# вход через кнопку в форме регистрации
class TestFormRegistration:
    def test_form_registration(self, driver):
        driver.find_element(*TestLocators.button_enter).click()  # нажать кнопку войти в аккаунт
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.new_registration))
        driver.find_element(*TestLocators.new_registration).click()  # нажать на Зарегистрировать
        driver.find_element(*TestLocators.enter_registration).click()  # кнопка войти в форме региcтрации
        driver.find_element(*TestLocators.email).send_keys(UsersTestData.email)  # найти поле login и заполнить его
        driver.find_element(*TestLocators.password).send_keys(UsersTestData.password)  # найти поле пароль и заполнить его
        driver.find_element(*TestLocators.enter).click()  # найти кнопку войти и нажать её
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        assert driver.find_element(*TestLocators.place_an_order).is_displayed()


# вход через кнопку в форме восстановления пароля
class TestPasswordRecovery:
    def test_password_recovery(self, driver):
        driver.find_element(*TestLocators.button_enter).click()
        driver.find_element(*TestLocators.recover).click()  # кнопка восстановить
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p/a').click()  # кнопка войти в форме восстановить
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.enter))
        driver.find_element(*TestLocators.email).send_keys(UsersTestData.email)  # найти поле login и заполнить его
        driver.find_element(*TestLocators.password).send_keys(UsersTestData.password)  # найти поле пароль и заполнить его
        driver.find_element(*TestLocators.enter).click()  # найти кнопку войти и нажать её
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        assert driver.find_element(*TestLocators.place_an_order).is_displayed()
