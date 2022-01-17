import time
import pytest

from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)
        print("User logged out Successfully")
