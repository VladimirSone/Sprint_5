import pytest
from selenium import webdriver
from locator import TestLocators
from data import UsersTestData

#  фикстура веб-драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.window('--window-size=1920,1080')
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*TestLocators.button_enter).click()
    driver.find_element(*TestLocators.email).send_keys(UsersTestData.email)
    driver.find_element(*TestLocators.password).send_keys(UsersTestData.password)
    driver.find_element(*TestLocators.enter).click()
