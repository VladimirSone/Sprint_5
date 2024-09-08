# переход по клику на «Личный кабинет»
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators
from conftest import driver
from conftest import login

class TestPersonalAccount:
    def test_to_your_personal_account(self,driver, login):
        driver.find_element(*TestLocators.personal_account).click()  # нажать на кнопку личный кабинет
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.account_profile))
        assert driver.find_element(*TestLocators.account_profile).is_displayed()
