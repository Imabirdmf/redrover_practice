import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from functions import get_root_path



download_path = get_root_path('data/download')


@pytest.fixture(scope='session')
def driver():
    service = Service(executale_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': download_path
    }

    options.add_experimental_option('prefs', prefs)
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1000,1000')
    # options.add_argument('--incognito')
    # options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

