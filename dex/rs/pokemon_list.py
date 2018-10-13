import time
import unittest
from typing import Set

import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from configuration import configuration as projectConfiguration
from lib.webdriver import WebDriver


class PokemonListResource(object):
    url = "https://{}/dex/rs/pokemon/".format(projectConfiguration['smogon.com']['HostName'])
    rowSelector = ".DexTable>div"

    @staticmethod
    def getHtmlDocument() -> str:
        d = WebDriver().d
        d.get(PokemonListResource.url)
        contentfulPaintTimeout = float(projectConfiguration['smogon.com']['ContentfulPaintTimeout'])
        WebDriverWait(d, contentfulPaintTimeout).until(
            lambda driver: driver.find_element_by_tag_name("body")
        )
        return d.page_source

    @staticmethod
    def getListElements() -> Set[WebElement]:
        d = WebDriver().d
        d.get(PokemonListResource.url)
        contentfulPaintTimeout = float(projectConfiguration['smogon.com']['ContentfulPaintTimeout'])

        WebDriverWait(d, contentfulPaintTimeout).until(
            lambda driver: driver.find_element_by_css_selector(PokemonListResource.rowSelector)
        )

        listRowElements = set()
        body = d.find_element_by_tag_name("body")
        for i in range(40):
            time.sleep(0.3)
            listRowElements.update(d.find_elements_by_css_selector(PokemonListResource.rowSelector))
            body.send_keys(Keys.PAGE_DOWN)

        return listRowElements


class TestSiteIsPresent(unittest.TestCase):
    def test_http_get(self):
        httpTimeout = float(projectConfiguration['smogon.com']['HttpTimeout'])
        response = requests.get(PokemonListResource.url, timeout=httpTimeout)
        response.close()
        self.assertEqual(response.status_code, 200,
                         "The server at {} did not respond with 200.".format(PokemonListResource.url))


class TestSiteHasContent(unittest.TestCase):
    def setUp(self):
        WebDriver().d.get(PokemonListResource.url)

    def test_content_not_empty(self):
        url = PokemonListResource.url
        pageSource = PokemonListResource.getHtmlDocument()
        self.assertGreater(len(pageSource), 0, "The page {} has no content.".format(url))

    def test_content_has_one_body(self):
        url = PokemonListResource.url
        time.sleep(int(projectConfiguration['smogon.com']['InitialLoadingTime']))
        elements = WebDriver().d.find_elements_by_tag_name('body')
        self.assertEqual(len(elements), 1, "The page {} has not got a 1 body tag".format(url))


class TestContentSelectors(unittest.TestCase):
    def test_get_list_elements(self):
        elements = PokemonListResource.getListElements()
        allElements = list(elements)
        self.assertNotEqual(allElements, [])
        self.assertEqual(len(allElements), 389)
        for element in allElements:
            self.assertEqual(type(element), WebElement)

