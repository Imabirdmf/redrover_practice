from faker import Faker

class BaseGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_first_name(self, first_name):
        if first_name is None:
            return self.fake.first_name()
        return first_name

    def generate_last_name(self, last_name):
        if last_name is None:
            return self.fake.last_name()
        return last_name

    def generate_email(self, email):
        if email is None:
            return self.fake.email()
        return email

    def generate_password(self, password):
        if password is None:
            return self.fake.password()
        return password

    def generate_random_number(self, number):
        if number is None:
            return self.fake.random_int()
        return number

    def generate_random_word(self, word):
        if word is None:
            return self.fake.word()
        return word