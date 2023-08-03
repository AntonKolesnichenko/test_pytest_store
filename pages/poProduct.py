from selenium.webdriver.common.by import By

class Goods:
    URL = "http://testshop.sedtest-school.ru/product/"
    NAME = (By.CSS_SELECTOR, "h5 span")
    IMAGE = (By.CSS_SELECTOR, '.col-md-6 img')
    PRICE = (By.CSS_SELECTOR, ".card-body .row .col-md-6:nth-child(2) span:nth-child(1)")
    QUANTITY = (By.CSS_SELECTOR, ".card-body .row .col-md-6:nth-child(1)")


    def __init__(self, driver):
        self.driver = driver

    def load(self, product_id):
        url = f"http://testshop.sedtest-school.ru/product/{product_id}/"
        self.driver.get(url)

    def title(self):
        return self.driver.find_element(*self.NAME).text

    def img(self):
        return self.driver.find_element(*self.IMAGE).get_attribute("src")

    def price(self):
        return self.driver.find_element(*self.PRICE).text

    def quantity(self):
        return self.driver.find_element(*self.QUANTITY).text
