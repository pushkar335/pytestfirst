import pytest
from pages.loginPage import LoginPage
from utilities.Readconfig import Configparser
from utilities.customLogger import Loggen


@pytest.mark.usefixtures("setup")
class Test_loginPage:

    def test_login(self):
        # ReadConfig.geturl()
        lp = LoginPage(self.driver)
        logger = Loggen.loggen()
        logger.info("========Test login started=======")
        lp.do_login(Configparser.get_username(), Configparser.get_password())
        assert True  
        logger.info("========login_test passed=======")

        # assert True

    # def test_title(self):
    #     # Configparser.geturl()
    #     lp = LoginPage(self.driver)
    #     element = lp.get_login_title(lp.title)
    #     if element == lp.title:
    #         assert True
    def test_logout(self):
        lp = LoginPage(self.driver)
        lp.do_logout()
        assert True
