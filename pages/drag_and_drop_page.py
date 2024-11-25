from pages.base_page import BasePage
from locators.drag_and_drop_page_locators import DragAndDropLocators

class DragAndDropPage(BasePage):
    locators = DragAndDropLocators()

    def drag_and_drop_(self):
        source_elem = self.element_is_visible(self.locators.DRAG_ME_LOC)
        target_elem = self.element_is_visible(self.locators.DROP_ME_LOC)
        self.action_drag_and_drop(source_elem, target_elem)

    def get_text(self):
        text = self.element_is_visible(self.locators.DROP_ME_TEXT_LOC).text
        return text

    def draggable(self, xoffset, yoffset):
        elem = self.element_is_visible(self.locators.DRAG_LOC)
        coords_before = elem.location
        self.action_drag_and_drop_by_offset(elem, xoffset, yoffset)
        coords_after = elem.location
        return coords_before, coords_after

    def check_coordinates(self, coords_before, coords_after):
        x = coords_after['x'] - coords_before['x']
        y = coords_after['y'] - coords_before['y']
        return x, y
