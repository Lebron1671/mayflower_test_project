import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def get_driver(request):
    if "DOCKER_ENV" in os.environ and os.environ["DOCKER_ENV"] == "true":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=chrome_options, service=Service(executable_path='/usr/bin/chromedriver'))
    else:
        chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_binary_path
        chrome_options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=chrome_options, service=Service(executable_path='chromedriver'))
        driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
