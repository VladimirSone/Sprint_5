from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import create_random_email, create_random_password
from locator import TestLocators

# регистрация на сайте с валидными данными (email, пароль)
class TestSuccessfulRegistration:
    def test_successful_registration(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()
        driver.find_element(*TestLocators.button_enter).click()  # найти кнопку войти на главной странице и нажать её
        driver.find_element(*TestLocators.new_registration).click()  # найти кнопку "Зарегистрироваться" и нажать на него
        driver.find_element(*TestLocators.name_field).send_keys("Vladimir")  # найти поле имя и ввести туда значение
        driver.find_element(*TestLocators.login_field).send_keys(random_email)  # найти поле login и заполнить его
        driver.find_element(*TestLocators.password).send_keys(random_password)  # найти поле пароль и заполнить его
        driver.find_element(*TestLocators.button_register).click()  # найти кнопку Зарегистрироваться и нажать её
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.email))
        assert driver.find_element(*TestLocators.email).is_displayed()


# проверка введен невалидный пароль
class TestErrorPassword:
    def test_error_password_registration(self, driver, randompassword=1111):
        random_email = create_random_email()
        randompassword = randompassword
        driver.find_element(*TestLocators.button_enter).click()  # найти кнопку войти на главной странице и нажать её
        driver.find_element(*TestLocators.new_registration).click()  # найти слово "Зарегистрироваться" и нажать на него
        driver.find_element(*TestLocators.name_field).send_keys("Vladimir")  # найти поле имя и ввести туда значение
        driver.find_element(*TestLocators.login_field).send_keys(random_email)  # найти поле login и заполнить его
        driver.find_element(By.NAME, "Пароль").send_keys(randompassword)  # найти поле пароль и заполнить его
        driver.find_element(*TestLocators.button_register).click()  # найти кнопку Зарегистрироваться и нажать её
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        header = driver.find_element(*TestLocators.invalid_password)  # указываем путь на текст "Некорректный пароль"
        assert header.text == 'Некорректный пароль'  # проверяем, что при указании неверного пароля мы увидим текст "Некорректный пароль"
