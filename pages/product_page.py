from selenium.webdriver.common.by import By
from pages.results_page import ResultsPage


class ProductPage(ResultsPage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def assert_price(self):
        price = self.driver.find_element_by_class_name("priceView-hero-price")
        price_size = price.getCssValue("font-size")
        assert price_size == "30px"

