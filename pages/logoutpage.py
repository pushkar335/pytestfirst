from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Logout(Base_page):
    logout_button = (By.XPATH,  '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    def get:
    