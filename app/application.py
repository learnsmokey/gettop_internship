from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)
        self.product_page = ProductPage(self.driver)

