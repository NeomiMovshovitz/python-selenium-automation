from pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def make_a_search(self, input_text):
        self.driver.find_elements_by_id("gh-search-input").send_keys(input_text)
        self.driver.find_elements_by_class_name("header-search-button").click()
        assert len(self.driver.find_elements_by_id("main-results"))

