from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver


class Base_page:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence_of_all_web_element(self, locator):
        list_of_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return list_of_elements

    def wait_for_element_tobe_clickable(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return element

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def get_title(self, title):
        title = WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return title
