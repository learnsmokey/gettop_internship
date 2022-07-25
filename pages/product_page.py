from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    CORRECT_PAGE = (By.XPATH, "//h1[@class='product-title product_title entry-title']")

    def correct_product_page(self):
        correct = self.driver.find_element(*self.CORRECT_PAGE)