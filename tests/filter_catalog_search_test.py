import allure
from base.base_test import BaseTest
import search_test


@allure.feature("Filter Functionality On Catalog Search")
class TestFilterFeatureOnCatalogSearch(BaseTest):
    MIN_PRICE = 30000
    MAX_PRICE = 40000
    SEARCH_INPUT = "iPhone"

    @allure.title("Check Filter Functionality On Catalog Search")
    @allure.severity("Critical")
    def test_search(self):
        with allure.step("Repeat all test_search steps"):
            search_test.TestSearchFeature.test_search(self)
        self.catalog_search_page.set_price_filter(self.MIN_PRICE, self.MAX_PRICE)
        prices = self.catalog_search_page.get_result_items_price
        with allure.step(f"Assert all products have filtered price"):
            for price in prices:
                assert self.MIN_PRICE <= int(price.text.replace(" ", "").replace("₴", "")) <= self.MAX_PRICE
        self.catalog_search_page.make_screenshot("Success")
