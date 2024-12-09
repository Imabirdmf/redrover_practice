from data.urls import Urls
from pages.browser_window_page import BrowserWindow


class TestWindowPage():
    url = Urls()

    def test_window_new_tab(self, driver):
        page = BrowserWindow(driver, self.url.demoqa_window_url)
        page.open()
        text_result = page.check_opened_new_tab()
        assert text_result == "This is a sample page", "The new tab is not find"

    def test_window_new_window(self, driver):
        page = BrowserWindow(driver, self.url.demoqa_window_url)
        page.open()
        text_result = page.check_opened_new_window()
        assert text_result == "This is a sample page", "The new tab is not find"