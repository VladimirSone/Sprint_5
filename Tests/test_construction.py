from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators


# переход из раздела "Булки" в раздел "Начинки"
class TestConstructor:
    def test_rolls_fillings(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        assert driver.find_element(*TestLocators.fillings).text == "Начинки"

# переход из раздела "Булки" в раздел "Соусы"
    def test_rolls_cous(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        assert driver.find_element(*TestLocators.sauce).text == "Соусы"

# переход из раздела "Соусы" в раздел "Начинки"
    def test_cous_fillings(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        driver.find_element(*TestLocators.fillings).click()
        assert driver.find_element(*TestLocators.fillings).text == "Начинки"

# переход из раздела "Начинки" в раздел "Соусы"
    def test_fillings_cous(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        driver.find_element(*TestLocators.sauce).click()
        assert driver.find_element(*TestLocators.sauce).text == "Соусы"

# переход из раздела "Соусы" в раздел "Булки"
    def test_cous_rolls(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        driver.find_element(*TestLocators.rolls).click()
        assert driver.find_element(*TestLocators.rolls).text == "Булки"

# переход из раздела "Начинки" в раздел "Булки"
    def test_fillings_rolls(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        driver.find_element(*TestLocators.rolls).click()
        assert driver.find_element(*TestLocators.rolls).text == "Булки"
