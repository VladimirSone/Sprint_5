# Проверь выход по кнопке «Выйти» в личном кабинете
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators

class TestAccountLogout:
    def test_account_logout(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))  # оформить заказ
        assert driver.find_element(*TestLocators.place_an_order).is_displayed()  # проверка появления кнопки оформить заказ
        driver.quit()
