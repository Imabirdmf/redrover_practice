import time

from data.urls import Urls
from pages.tool_tips_page import ToolTipsPage


class TestToolTips:
    url = Urls()

    def test_hover_btn(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_btn()
        # text = page.hover_btn()
        text = page.get_text()
        assert text == 'You hovered over the Button'

    def test_get_cursor(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_btn()
        property_value = page.get_css_property('cursor')
        assert property_value == 'pointer'

    def test_get_color(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        property_value_before = page.get_css_property("background-color")
        page.hover_btn()
        property_value_after = page.get_css_property("background-color")
        assert property_value_before != property_value_after
        assert property_value_after == "rgba(33, 136, 56, 1)"