
from pages.base_page import BasePage

'''
    US_SITE = By.CLASS_NAME("us-link")
   CANADA_SITE = By.CLASS_NAME("canada-link")
'''


class SitePage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://www.bestbuy.com/"
        super().__init__(driver, wait)

    def go_to_site_page(self):
        self.go_to_page(self.url)

    def select_a_site(self, us_site=True):
        if us_site:
            self.driver.find_elements_by_class_name("us-link").click()
        else:
            self.driver.find_elements_by_class_name("canada-link").click()
