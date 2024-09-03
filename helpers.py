import random
import string


# Генерация email рандомными буквами и рандомным числом для регистрации
def create_random_email():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    random_email = f'vladimirshutovtroitskiy{random_letters}_{random.randint(100, 999)}@yandex.ru'
    return random_email


# Генерация пароля с рандомными буквами и рандомным числом для регистрации
def create_random_password():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
    random_password = f'qwerty_{random_letters}_{random.randint(10, 99)}'
    return random_password

# Генерация основы email с четырьмя рандомными буквами и рандомным числом от 100 до 999
# для негативных проверок на формат вводимого адреса почты
# def create_email_base():
    # random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    # email_base = f'vladimirshutovtroitskiy{random_letters}_{random.randint(100, 999)}'
    # return email_base

# Генерация пароля с невалидными значениями
def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))
