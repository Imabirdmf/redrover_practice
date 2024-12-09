from locators.browser_window_page_locators import BrowserWindowPageLocators
from pages.base_page import BasePage


class BrowserWindow(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_PAGE).text
        return text_title
