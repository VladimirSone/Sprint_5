# Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators


# переход по клику на конструктор
class TestTransitionAccountToConstruction:
    def test_transition_account_to_construction(self, driver, login):
        driver.find_element(*TestLocators.personal_account).click()  # кнопка личный кабинет + нажать на кнопку
        driver.find_element(*TestLocators.personal_account).click()  # нажать клик на кнопку личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.personal_account))
        driver.find_element(*TestLocators.construction).click()  # нажать на кнопку "Конструктор"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.construction))
        assert driver.find_element(*TestLocators.construction).is_displayed()

# переход по клику на логотип Stellar Burgers
class TestTransitionAccountToIcon:
    def test_transition_account_to_icon(self, driver):
        driver.find_element(*TestLocators.personal_account).click()  # нажать клик на кнопку личный кабинет
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.personal_account))
        driver.find_element(*TestLocators.icon).click()  # нажать на иконку "Stellar Burgers"
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.icon))
        assert driver.find_element(*TestLocators.icon).is_displayed()
