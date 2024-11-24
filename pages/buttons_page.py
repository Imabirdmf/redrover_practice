from pages.base_page import BasePage
from locators.buttons_page_locators import ButtonsPageLocators


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_btn(self):
        elem = self.element_is_clickable(self.locators.DOUBLE_CLICK_BTN_LOC)
        self.double_click(elem)
        text = self.element_is_visible(self.locators.DOUBLE_CLICK_TEXT_LOC).text
        return text
    def right_click_btn(self):
        elem = self.element_is_clickable(self.locators.RIGHT_CLICK_BTN_LOC)
        self.right_click(elem)
        text = self.element_is_visible(self.locators.RIGHT_CLICK_TEXT_LOC).text
        return text

    def single_click_btn(self):
        elem = self.element_is_clickable(self.locators.CLICK_BTN_LOC)
        elem.click()
        text = self.element_is_visible(self.locators.CLICK_TEXT_LOC).text
        return text