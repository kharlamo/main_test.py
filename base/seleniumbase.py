
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.ui import Select
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'id': By.ID,
                    'class_name': By.CLASS_NAME,
                    'name': By.NAME,
                    'xpath': By.XPATH,
                    'link_text': By.LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        try:
            self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)
        except Exception:
            element = self.driver.find_element((self.__get_selenium_by(find_by), locator))
        return element

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def select_el(self, find_by: str, locator: str):
        return Select(self.driver.find_element(self.__get_selenium_by(find_by), locator))

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)
