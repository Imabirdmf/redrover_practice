import pytest

from data.urls import Urls
from pages.alert_page import AlertPage


class TestAlert:
    url = Urls()

    def test_alert(self, driver):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        alert_text = page.alert()
        assert alert_text == 'I am a JS Alert'

    def test_alert_text(self, driver):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        page.alert()
        text = page.get_text()
        assert text == 'You successfully clicked an alert'


    @pytest.mark.parametrize('value', [('YES', 'Ok'), ('NO', 'Cancel')])
    def test_alert_confirms(self, driver, value):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        page.alert_confirm(value[0])
        text = page.get_text()
        assert text == f'You clicked: {value[1]}'

    def test_alert_confirms2(self, driver):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        text = page.alert_confirm('YES')
        assert text == 'I am a JS Confirm'

    def test_alert_prompt(self, driver):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        text = page.alert_prompt('Hello')
        assert text == 'I am a JS prompt'

    def test_alert_prompt2(self, driver):
        page = AlertPage(driver, f'{self.url.herokuapp_base_url}javascript_alerts')
        page.open()
        page.alert_prompt('Hello')
        text = page.get_text()
        assert text == 'You entered: Hello'