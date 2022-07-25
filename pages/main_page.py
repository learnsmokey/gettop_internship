import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import Page


class MainPage(Page):

    WISHLIST_ICON = (By.XPATH, "//div[@class='wishlist-icon']/button")
    WISHLIST_BUTTON = (By.XPATH, "//a[@data-title='Browse wishlist']")

    def open_gettop_website(self):
        self.open_page(url="https://gettop.us/")

    def add_product_to_wishlist(self):
        time.sleep(2)
        action = ActionChains(self.driver)
        prod = self.wait_for_element_appear(*self.WISHLIST_ICON)
        products = self.driver.find_elements(*self.WISHLIST_ICON)
        action.move_to_element(products[2]).click().perform()

    def wishlist_button(self):
        button = self.driver.find_element(*self.WISHLIST_BUTTON)
        button.click()

#    def verify_product(self):
#       pass


