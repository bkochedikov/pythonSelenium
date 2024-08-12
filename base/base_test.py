import pytest
from pages.home_page import HomePage
from pages.catalog_search_page import CatalogSearchPage


class BaseTest:

    home_page: HomePage
    catalog_search_page: CatalogSearchPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver

        request.cls.home_page = HomePage(driver)
        request.cls.catalog_search_page = CatalogSearchPage(driver)
