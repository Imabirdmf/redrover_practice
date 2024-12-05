from data.urls import Urls
from pages.select_page import SelectPage
import time


class TestSelectPage:
    url = Urls()

    def test_select(self, driver):
        page = SelectPage(driver, self.url.demoqa_select_url)
        page.open()
        page.select('Indigo')
        time.sleep(10)