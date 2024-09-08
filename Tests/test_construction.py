from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestLocators


# переход из раздела "Булки" в раздел "Начинки"
class TestConstructor:
    def test_rolls_fillings(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        WebDriverWait(driver,6).until(expected_conditions.presence_of_element_located(TestLocators.fillings))
        assert driver.find_element(*TestLocators.button_pressed).text == "Начинки"

# переход из раздела "Булки" в раздел "Соусы"
    def test_rolls_cous(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        WebDriverWait(driver,6).until(expected_conditions.visibility_of_element_located(TestLocators.sauce))
        assert driver.find_element(*TestLocators.button_pressed).text == "Соусы"

# переход из раздела "Соусы" в раздел "Начинки"
    def test_cous_fillings(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        driver.find_element(*TestLocators.fillings).click()
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.fillings))
        assert driver.find_element(*TestLocators.button_pressed).text == "Начинки"

# переход из раздела "Начинки" в раздел "Соусы"
    def test_fillings_cous(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        driver.find_element(*TestLocators.sauce).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.sauce))
        assert driver.find_element(*TestLocators.button_pressed).text == "Соусы"

# переход из раздела "Соусы" в раздел "Булки"
    def test_cous_rolls(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.sauce).click()
        driver.find_element(*TestLocators.rolls).click()
        WebDriverWait(driver,6).until(expected_conditions.presence_of_element_located(TestLocators.rolls))
        assert driver.find_element(*TestLocators.button_pressed).text == "Булки"

# переход из раздела "Начинки" в раздел "Булки"
    def test_fillings_rolls(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.place_an_order))
        driver.find_element(*TestLocators.fillings).click()
        driver.find_element(*TestLocators.rolls).click()
        WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.rolls))
        assert driver.find_element(*TestLocators.button_pressed).text == "Булки"
