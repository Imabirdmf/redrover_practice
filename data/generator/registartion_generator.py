from data.dataclasses.registration_data import RegistrationData
from data.generator.base_generator import BaseGenerator


class RegistrationGenerator(BaseGenerator):
    def generate_registration_data(self, first_name=None, last_name=None, email=None, password=None, repeat_password=None):
        if password is None and repeat_password is None:
            generated_password = self.generate_password(password)
            password = repeat_password = generated_password
        else:
            password = self.generate_password(password)
            repeat_password = self.generate_password(repeat_password)

        data = RegistrationData(
            first_name=self.generate_first_name(first_name),
            last_name=self.generate_last_name(last_name),
            email=self.generate_email(email),
            password=password,
            repeated_password=repeat_password
        )
        yield data