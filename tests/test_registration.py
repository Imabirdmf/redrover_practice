import time

import pytest

from data.data.registration_data import RegistrationData
from data.urls import Urls
from pages.registration_page import RegistrationPage
from data.generator.registartion_generator import RegistrationGenerator


class TestRegistration:
    url = Urls()
    registration_generator = RegistrationGenerator()
    registration_data = RegistrationData()

    def test_success_registration(self, driver):
        info = next(self.registration_generator.generate_registration_data())
        page = RegistrationPage(driver, self.url.reg_url)
        page.open()
        page.fill_form(info)
        time.sleep(5)
        success_message = page.get_success_message()
        assert success_message == self.registration_data.success_reg_message

    @pytest.mark.parametrize('value', [('', 'Заполните поле корректно'),
                                       ('hello', 'Заполните поле корректно')])
    def test_registration_invalid_email(self, driver, value):
        info = next(self.registration_generator.generate_registration_data(email=value[0]))
        page = RegistrationPage(driver, self.url.reg_url)
        page.open()
        page.fill_form(info)
        time.sleep(2)
        error_message = page.get_error_message()
        assert error_message == value[1]