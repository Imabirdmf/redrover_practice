from data.urls import Urls
from pages.frame_page import FramePage


class TestFramePage():
    urls = Urls()

    def test_big_frame(self, driver):
        page = FramePage(driver, self.urls.demoqa_frames_url)
        page.open()
        test_result = page.check_frame('BIG_FRAME')
        assert test_result == ('500px', '350px', 'This is a sample page')

    def test_small_frame(self, driver):
        page = FramePage(driver, self.urls.demoqa_frames_url)
        page.open()
        test_result = page.check_frame('SMALL_FRAME')
        assert test_result == ('100px', '100px', 'This is a sample page')
