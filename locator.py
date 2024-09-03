from selenium.webdriver.common.by import By

class TestLocators:
    # кнопка зарегистрироваться финальная
    button_register = By.XPATH, '/html/body/div/div/main/div/form/button'

    # поле login
    login_field = By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'

    # кнопка регистрации нового пользователя
    new_registration = By.XPATH, '/html/body/div/div/main/div/div/p[1]/a'

    # поле ввода имени
    name_field = By.TAG_NAME, 'input'

    # кнопка войти в аккаунт на главной странице
    button_enter = By.XPATH, '/html/body/div/div/main/section[2]/div/button'

    # кнопка Войти на странице Вход
    enter = By.XPATH, '/html/body/div/div/main/div/form/button'        # '//*[@id="root"]/div/main/div/form/button'

    # поле email на странице Входа в личный кабинет
    email = By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'

    # кнопка "Войти" через форму регистрации
    enter_registration = By.XPATH, '/html/body/div/div/main/div/div/p/a'

    # кнопка "восстановить"
    recover = By.XPATH, '/html/body/div/div/main/div/div/p[2]/a'    # '/html/body/div/div/main/div/form/button'

    # поле email в форме восстановить
    email_recover = By.XPATH, '/html/body/div/div/main/div/form/fieldset/div/div/input'

    # кнопка "Личный кабинет"
    personal_account = By.XPATH, '/html/body/div/div/header/nav/a/p'

    # кнопка "Конструктор"
    construction = By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p'

    # иконка "Stellar Burgers"
    icon = By.XPATH, '/html/body/div/div/header/nav/div'

    # кнопка "Выход" в личном кабинете
    exit = By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button'

    # Кнопка "Оформить заказ"
    place_an_order = By.XPATH, '//button[text()="Оформить заказ"]'

    # текст "Некорректный пароль"
    invalid_password = By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/p'

    # поле пароль
    password = By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'

    # Соусы
    sauce = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span'

    # Булки
    rolls = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span'

    # Начинки
    fillings = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span'

    # кнопка Профиль
    account_profile = By.XPATH, '/html/body/div/div/main/div/nav/ul/li[1]/a'
