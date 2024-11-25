from pages.base_page import BasePage
from locators.tool_tips_page_locators import ToolTipsPageLocators

class ToolTipsPage(BasePage):

    locators = ToolTipsPageLocators()

    def hover_btn(self):
        elem = self.element_is_visible(self.locators.TOOL_TIPS_BTN)
        self.action_move_to_element(elem)

    def get_text(self):
        text = self.element_is_visible(self.locators.HOVER_MSG).text
        return text

    def get_css_property(self, property_name):
        data = self.element_is_visible(self.locators.TOOL_TIPS_BTN)
        return data.value_of_css_property(property_name)