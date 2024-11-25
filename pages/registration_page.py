from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage
from data.dataclasses.registration_data import RegistrationData

class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    def fill_form(self, data: RegistrationData):
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(data.first_name)
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(data.last_name)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(data.email)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(data.password)
        self.element_is_visible(self.locators.REPEAT_PASSWORD_FIELD).send_keys(data.repeated_password)
        self.element_is_clickable(self.locators.REGISTER_BUTTON).click()

    def get_success_message(self):
        text = self.element_is_visible(self.locators.SUCCESS_MESSAGE).text
        return text

    def get_error_message(self):
        text = self.element_is_visible(self.locators.ERROR_MESSAGE).text
        return text
