# Вход через кнопку войти в аккаунт на главной странице
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators
from conftest import driver

class TestEntranceAccount:
    def test_entrance_account(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.place_an_order))
        header = driver.find_element(*TestLocators.place_an_order)
        assert header.text == 'Оформить заказ'