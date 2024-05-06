# coding=utf-8
import pytest
from pages.results_page import ResultsPage
from pages.site_page import SitePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def test_search(self):
        site_page = SitePage(self.driver, self.wait)
        site_page.go_to_site_page()
        site_page.select_a_site(True)
        search_page = SearchPage(self.driver)
        search_page.make_a_search("hello")
        result_page = ResultsPage(self.driver, self.wait)

        result_page.assert_results_contains("Hello Kitty")
        result_page.select_product_by_index(3)
        product_page = ProductPage(self.driver, self.wait)
        product_page.assert_price()


