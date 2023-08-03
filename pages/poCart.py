from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class StoreCart:
    URL_main = "http://testshop.sedtest-school.ru/"
    URL_LENOVO = "http://testshop.sedtest-school.ru/product/14/"
    URL_CART = ("http://testshop.sedtest-school.ru/mycart/")
    TITLE = (By.ID, "TestGym")
    HEADER = (By.CSS_SELECTOR, '#nav_link_main > a') ##"Главная"
    CART_HEADER = (By.CSS_SELECTOR, "body > div.container > h3")
    ADD_TO_CART = (By.CSS_SELECTOR, "#in_cart_link_14") 
    SEARCH_INPUT = (By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div.col-md-9.mt-2 > form > div > input")  ## Строка поиска
    COUNT_INPUT = (By.CSS_SELECTOR, "input.form-control")
    DELETE_BUTTON = (By.CSS_SELECTOR, "body > div.container > div > div.col-md-10 > div > div > div > div > div:nth-child(4) > a")
    CART_ICON = (By.CSS_SELECTOR, '#navbarCollapse > div > a:nth-child(1) > img')
    GOODS_LENOVO = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div > div > div > h5 > a")
    CART_LENOVO = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div:nth-child(2) > div > div > h5 > span")
    PRICE_LENOVO = (By.XPATH, "/html/body/div[1]/div/div[2]/span[1]")
    CART_NOTICE = (By.CSS_SELECTOR, "body > div.container > div > div > h1") ## Ваша корзина пуста
    
    def __init__(self, driver):
        self.driver = driver
            
    def load(self):
        self.driver.get(self.URL_main)
        
    def search(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("Lenovo", Keys.ENTER)

        self.driver.find_element(*self.GOODS_LENOVO).send_keys(Keys.ENTER)
                
    def cartAdd(self):
        self.driver.find_element(*self.ADD_TO_CART).send_keys(Keys.ENTER)
        
    def cart(self):
        self.driver.get(self.URL_CART)
        header = self.driver.find_element(*self.CART_HEADER).text
        assert "Ваша корзина" in header, 'Ваша корзина ok'

    def cartCountAdd(self):
        count_input = self.driver.find_element(*self.COUNT_INPUT)
        self.driver.execute_script("arguments[0].value = '';", count_input)
        count_input.send_keys('2', Keys.ENTER)
        self.driver.implicitly_wait(5000)
    
    def cartCountDelete(self):
        self.driver.find_element(*self.COUNT_INPUT).send_keys(Keys.DELETE, "1", Keys.ENTER)
    
    def cartDelete(self):
        self.driver.find_element(*self.DELETE_BUTTON).send_keys(Keys.ENTER)