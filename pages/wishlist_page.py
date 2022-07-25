import time

from pages.base_page import Page
from selenium.webdriver.common.by import By


class WishlistPage(Page):
    WISHLIST_VERIFY = (By.CSS_SELECTOR, "td.product-name")
    REMOVE_PRODUCT = (By.XPATH, "//a[@title='Remove this product']")
    #CONFIRMATION_MESSAGE = (By.XPATH, "//td[@class='wishlist-empty']")
    #CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "i.icon-checkmark")
    CONFIRMATION_MESSAGE = (By.XPATH, "//div[@role='alert']")
    WISHLIST_ITEM = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2013/08/ipad-mini-1-300x300.jpg']")
    SOCIAL_LOGO = (By.XPATH, "//div[@class='yith-wcwl-share social-icons share-icons share-row relative']/a")

    def wishlist_verify(self):
        verify = self.driver.find_element(*self.WISHLIST_VERIFY)

    def remove_product(self):
        #time.sleep(2)
        product = self.driver.find_element(*self.REMOVE_PRODUCT)
        product.click()

    def confirmation_message(self):
        time.sleep(5)
        message = self.driver.find_element(*self.CONFIRMATION_MESSAGE)
        #assert message.text == 'No products added to the wishlist', f'Error.Expected No products added to the wishlist , but got{message.text}'

    def wishlist_item(self):
        item = self.driver.find_element(*self.WISHLIST_ITEM)
        item.click()

    def logo_to_share(self):
        time.sleep(2)
        social_links = self.driver.find_elements(*self.SOCIAL_LOGO)
        assert len(social_links) == 4, f'Expected 4 social links to share, but got only {len(social_links)} links'
