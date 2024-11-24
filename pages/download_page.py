from pages.base_page import BasePage
from locators.download_page_locators_hero import DownloadPageLocators

class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_LOC).click()