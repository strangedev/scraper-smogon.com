from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lib.singleton import SingletonMeta


class WebDriver(metaclass=SingletonMeta):
    def __init__(self):
        self._driver = WebDriver.newWebDriver()

    def __del__(self):
        self._driver.close()

    @property
    def d(self) -> webdriver.Chrome:
        return self._driver

    @staticmethod
    def newWebDriver() -> webdriver.Chrome:
        """
        Creates a new WebDriver using selenium and navigates
        to the given url.
        :return: The WebDriver
        """
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        return driver
