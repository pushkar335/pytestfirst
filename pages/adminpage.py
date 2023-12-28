from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.support.select import Select


class Admin_page(Base_page):
    admin_but = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    system_user = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
    user_role = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
    employee_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input")
    status = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input")
    search_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    reset_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def search_user(self, user, emp_name):
        self.do_click(self.admin_but)
        self.do_send_keys(self.system_user, user)
        sel = Select(self.user_role)
        sel.select_by_value('Admin')
        self.do_send_keys(self.employee_name, emp_name)
        sel1 =Select(self.status)
        sel1.select_by_value('Enabled')

    

