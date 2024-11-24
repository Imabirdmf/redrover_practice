from functions import get_root_path
from locators.upload_page_locators_hero import UploadPageLocators
from pages.base_page import BasePage


class UploadPage(BasePage):
    locators = UploadPageLocators()

    def upload_file(self, file_path):
        file_path = get_root_path(f'data/upload/{file_path}')
        self.element_is_visible(self.locators.UPLOAD_FILE_LOCATOR).send_keys(file_path)
        self.element_is_clickable(self.locators.UPLOAD_BTN_LOCATOR).click()

    def check_success_upload_file(self):
        h3_text = self.element_is_visible(self.locators.SUCCESS_UPLOAD_HEADER_LOCATOR).text
        file_name = self.element_is_visible(self.locators.SUCCESS_UPLOAD_FILE_NAME_LOCATOR).text
        return h3_text, file_name
