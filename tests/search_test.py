import allure
from base.base_test import BaseTest


@allure.feature("Search Functionality")
class TestSearchFeature(BaseTest):
    SEARCH_INPUT = "iPhone"

    @allure.title("Check Search Functionality")
    @allure.severity("Critical")
    def test_search(self):
        self.home_page.open()
        self.home_page.enter_text_into_search_bar(self.SEARCH_INPUT)
        self.home_page.click_search_button()
        names = self.catalog_search_page.get_result_items_name
        with allure.step(f"Assert all products have '{self.SEARCH_INPUT}' in name"):
            for name in names:
                assert self.SEARCH_INPUT in name.text
        self.catalog_search_page.make_screenshot("Success")
