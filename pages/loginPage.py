from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class LoginPage(Base_page):
    Text_username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME, "password")
    Click_Login_Xpath = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")
    title = "OrangeHRM"
    logout_button = (By.XPATH,  '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
    user_logo = (By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_login_title(self, title):
        title = self.get_title(title)
        return title

    def do_login(self, username, password):
        self.do_send_keys(self.Text_username_Name, username)
        self.do_send_keys(self.Text_Password_Name, password)
        self.do_click(self.Click_Login_Xpath)

    def do_logout(self):
        self.do_click(self.user_logo)
        self.do_click(self.logout_button)