import time

import pytest

from data.urls import Urls
# from functions import get_root_path
from pages.upload_page import UploadPage


class TestUpload:
    url = Urls()

    @pytest.mark.parametrize('file_name',  ['screenshot.png', 'test.txt'])
    def test_upload_file(self, driver, file_name):
        #file_path = get_root_path('data/upload/screenshot.png')
        page = UploadPage(driver, f'{self.url.herokuapp_base_url}upload')
        page.open()
        page.upload_file(file_name)
        h3_text, file_name_text = page.check_success_upload_file()
        assert h3_text == 'File Uploaded!'
        assert file_name_text == file_name
        