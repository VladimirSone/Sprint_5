from selenium.webdriver.common.by import By

class TestLocators:
    # кнопка зарегистрироваться финальная
    button_register = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    # поле login
    login_field = By.XPATH, '//label[text() = "Email"]/following-sibling::input'

    # кнопка регистрации нового пользователя
    new_registration = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # поле ввода имени
    name_field = By.XPATH, '//label[text() = "Имя"]/following-sibling::input'

    # кнопка войти в аккаунт на главной странице
    button_enter = By.XPATH, '//button[text() = "Войти в аккаунт"]'

    # кнопка Войти на странице Вход
    enter = By.XPATH, '//button[text() = "Войти"]'

    # поле email на странице Входа в личный кабинет
    email = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # кнопка "Войти" через форму регистрации
    enter_registration = By.XPATH, '//a[text() = "Войти"]'

    # кнопка "восстановить"
    recover = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # кнопка войти в форме восстановить
    button_enter_recover = By.XPATH, '//a[text()="Войти"]'

    # поле email в форме восстановить
    email_recover = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # кнопка "Личный кабинет"
    personal_account = By.XPATH, '//p[text()="Личный Кабинет"]'

    # кнопка "Конструктор"
    construction = By.XPATH, '//p[text()="Конструктор"]'

    # иконка "Stellar Burgers"
    icon = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'

    # кнопка "Выход" в личном кабинете
    exit = By.XPATH, '//button[text()="Выход"]'

    # Кнопка "Оформить заказ"
    place_an_order = By.XPATH, '//button[text()="Оформить заказ"]'

    # текст "Некорректный пароль"
    invalid_password = By.XPATH, '//p[text()="Некорректный пароль"]'

    # поле пароль
    password = By.XPATH, '//label[text() = "Пароль"]/following-sibling::input'

    # Соусы
    sauce = By.XPATH, '//span[text()="Соусы"]'

    # Булки
    rolls = By.XPATH, '//span[text()="Булки"]'

    # Начинки
    fillings = By.XPATH, '//span[text()="Начинки"]'

    # кнопка Профиль
    account_profile = By.XPATH, '//a[text()="Профиль"]'

    # нажатие кнопки
    button_pressed = By.XPATH, '//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
