from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def alert_is_visible(self, timeout=10):
        wait(self.driver, timeout=timeout).until(EC.alert_is_present())

    def double_click(self, elem):
        action = ActionChains(self.driver)
        action.double_click(elem)
        action.perform()

    def right_click(self, elem):
        action = ActionChains(self.driver)
        action.context_click(elem)
        action.perform()

    def action_move_to_element(self, elem):
        action = ActionChains(self.driver)
        action.move_to_element(elem)
        # time.sleep(5)
        action.perform()

    def action_drag_and_drop(self, source_elem, target_elem):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_elem, target_elem)
        action.perform()

    def action_drag_and_drop_by_offset(self, elem, xoffset, yoffset):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(elem, xoffset, yoffset)
        action.perform()