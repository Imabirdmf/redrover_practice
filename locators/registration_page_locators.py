class RegistrationPageLocators:
    FIRST_NAME_FIELD = ("css selector", "input[id='name']")
    LAST_NAME_FIELD = ("css selector", "input[id='surname']")
    EMAIL_FIELD = ("css selector", "input[id='email']")
    PASSWORD_FIELD = ("css selector", "input[id='password']")
    REPEAT_PASSWORD_FIELD = ("css selector", "input[id='password_repeat']")
    REGISTER_BUTTON = ("xpath", "//button[text()='Зарегистрироваться']")
    SUCCESS_MESSAGE = ("xpath", "//div[contains(@class, 'h3')]")

    ERROR_MESSAGE = ("css selector", "div[class='error-field']")