from pages.adminpage import Admin_page
import pytest


@pytest.mark.usefixtures("setup")
class Test_Admin:

    def test_search_user(self):
        ad = Admin_page()
        ad.search_user()