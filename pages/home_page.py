import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    PAGE_URL = Links.HOME_PAGE

    SEARCH_FIELD = ("xpath", "//input[@name='search']")
    SUBMIT_BUTTON = ("xpath", "//button[contains(@class, 'search-form__submit')]")

    @allure.step("Enter text in search bar")
    def enter_text_into_search_bar(self, text):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD)).send_keys(text)

    @allure.step("Click search button")
    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
