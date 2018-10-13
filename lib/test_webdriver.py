import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWebdriver(unittest.TestCase):
    def test_launch_webdriver(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.close()
