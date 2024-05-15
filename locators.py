from selenium.webdriver.common.by import By


class StellarLocators:
    NAME_FIELD_REG = (By.XPATH, ".//label[text()='Имя']/../input")   # Поле "Имя" формы регистрации
    EMAIL_FIELD_REG = (By.XPATH, ".//label[text()='Email']/../input")   # Поле "Email" формы регистрации
    PASSWORD_FIELD_REG = (By.XPATH, ".//input[@type='password']")   # Поле "Пароль" формы регистрации
    BUTTON_REGISTRATION = (
        By.XPATH,
        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    )   # Кнопка "Зарегистрироваться" формы регистрации

    PAGE_INPUT = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']")   # Страница с формой "Вход"
    EMAIL_FIELD_IN = (By.XPATH, ".//label[text()='Email']/../input")  # Поле "Email" формы "Вход"
    PASSWORD_FIELD_IN = (By.XPATH, ".//input[@type='password']")  # Поле "Пароль" формы "Вход"
    BUTTON_ENTER_IN = (
        By.XPATH,
        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    )  # Кнопка "Войти" формы "Вход"
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[@href='/forgot-password']")  # Кнопка "Восстановить пароль" формы "Вход"
    BUTTON_ENTER = (By.XPATH, ".//a[@href='/login']")  # Кнопка "Войти"
    BUTTON_RECOVER = (By.XPATH, ".//button[text()='Восстановить']")  # Кнопка "Восстановить" на странице
    # "Восстановление пароля"

    INVALID_PASSWORD = (
        By.XPATH, ".//p[@class='input__error text_type_main-default']")   # Сообщение о некорректном пароле

    BUTTON_LOG_IN_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")   # Кнопка "Войти в аккаунт" на главной
    # странице
    BUTTON_PLACE_AN_ORDER = (
        By.XPATH,
        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    )   # Кнопка "Оформить заказ" на главной странице

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")   # Кнопка "Личный кабинет"
    BUTTON_SAVE = (By.XPATH, ".//button[text()='Сохранить']")   # Кнопка "Сохранить" в профиле

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")   # Кнопка "Конструктор"
    BUTTON_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")   # Кнопка-логотип "Stellar Burgers"
    BUTTON_OUTPUT = (By.XPATH, ".//button[text()='Выход']")   # Кнопка "Выход" в личном кабинете

    SECTION_BREAD = (By.XPATH, ".//span[text()='Булки']")   # Раздел "Булки" в "Конструкторе"
    LIST_BREAD = (By.XPATH, ".//h2[text()='Булки']")   # Список продуктов раздела "Булки"
    SECTION_SAUCES = (By.XPATH, ".//span[text()='Соусы']")   # Раздел "Соусы" в "Конструкторе"
    LIST_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")  # Список продуктов раздела "Соусы"
    SECTION_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")   # Раздел "Начинки" в "Конструкторе"
    LIST_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")  # Список продуктов раздела "Начинки"
