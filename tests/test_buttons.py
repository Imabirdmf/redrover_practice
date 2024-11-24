from data.urls import Urls
from pages.buttons_page import ButtonsPage


class TestButtonsPage:
    url = Urls()

    def test_double_click(self, driver):
        page = ButtonsPage(driver, self.url.demoqa_buttons_url)
        page.open()
        text = page.double_click_btn()
        assert text == 'You have done a double click'

    def test_right_click(self, driver):
        page = ButtonsPage(driver, self.url.demoqa_buttons_url)
        page.open()
        text = page.right_click_btn()
        assert text == 'You have done a right click'

    def test_single_click(self, driver):
        page = ButtonsPage(driver, self.url.demoqa_buttons_url)
        page.open()
        text = page.single_click_btn()
        assert text == 'You have done a dynamic click'
