from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_result_text(self, verify_text, *locator):
        result = self.driver.find_element(*locator)
        assert result.text == verify_text, f'Got Error. Expected {verify_text}, but got {result.text}'

    def verify_link_count(self, link_count, *locator):
        link = self.driver.find_elements(*locator)
        print(*locator)
        assert len(link) == link_count, f'Error. Expected {link_count}, but got {link}'

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.driver.find_elements(*locator)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

#    def wishlist_verify(self,*locator):
#        self.driver.find_element(*locator)

