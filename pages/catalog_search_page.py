import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CatalogSearchPage(BasePage):
    ITEMS_NAME_FIELD = ("xpath", "//span[@class='goods-tile__title']")
    ITEMS_PRICE_FIELD = ("xpath", "//span[@class='goods-tile__price-value']")
    MIN_PRICE_FILTER = ("xpath", '//input[@formcontrolname="min"]')
    MAX_PRICE_FILTER = ("xpath", '//input[@formcontrolname="max"]')
    PRICE_FILTER_BUTTON = ("xpath", '//button[@type="submit" and contains(@class, "slider-filter__button")]')
    PRICE_FILTER_APPLIED = ("xpath", '//button[@type="submit" and contains(@class, "slider-filter__button")]')

    @property
    @allure.step("Get search items name")
    def get_result_items_name(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS_NAME_FIELD))

    @property
    @allure.step("Get search items price")
    def get_result_items_price(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS_PRICE_FIELD))

    @allure.step("Set Price Filter")
    def set_price_filter(self, min_price, max_price):
        min_price_input = self.wait.until(EC.element_to_be_clickable(self.MIN_PRICE_FILTER))
        min_price_input.clear()
        min_price_input.send_keys(min_price)

        max_price_input = self.wait.until(EC.element_to_be_clickable(self.MAX_PRICE_FILTER))
        max_price_input.clear()
        max_price_input.send_keys(max_price)

        self.wait.until(EC.element_to_be_clickable(self.PRICE_FILTER_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(("xpath", f'//button[contains(text(),"{min_price} - {max_price}")]')))
