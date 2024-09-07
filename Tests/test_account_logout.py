# Проверь выход по кнопке «Выйти» в личном кабинете
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators

class TestAccountLogout:
    def test_account_logout(self, driver, login):
        WebDriverWait(driver,6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.personal_account).click()
        WebDriverWait(driver,6).until(expected_conditions.visibility_of_element_located(TestLocators.account_profile))
        driver.find_element(*TestLocators.exit).click()
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.enter))  # оформить заказ
        assert driver.find_element(*TestLocators.enter).is_displayed()  # кнопка Войти на странице Вход
