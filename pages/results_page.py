from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResultsPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def assert_results_contains(self, text):
        xpath = f"//ol//li[@class='sku-item']//a[contains(text(),'{text}')]"
        assert len(self.driver.find_elements_by_xpath(xpath))

    def select_product_by_index(self, index):
        xpath = f"//ol//li[@class='sku-item'][{index}]//a[@class='image-link']"
        self.driver.find_elements_by_xpath(xpath).click()
