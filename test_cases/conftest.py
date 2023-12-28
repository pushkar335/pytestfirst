import pytest
from selenium import webdriver
from utilities.Readconfig import Configparser


@pytest.fixture(autouse=True, scope="class")
def setup(request):
    driver= webdriver.Firefox()
    # driver = webdriver.Chrome(service=Service(executable_path="C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"))
    # driver = webdriver.Edge(service=Service(executable_path="C:\\Users\hp\\Downloads\\edgedriver_win64\\msedgedriver.exe"))
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(Configparser.get_url())
    request.cls.driver = driver
    yield
    driver.close()
