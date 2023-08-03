
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class StoreSearch:
    URL_main = "http://testshop.sedtest-school.ru/"
    HEADER = (By.CSS_SELECTOR, '#nav_link_main > a') ##"Главная"
    SEARCH_INPUT = (By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div.col-md-9.mt-2 > form > div > input")  ## Строка поиска
    GOODS_LENOVO = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div > div > div > h5 > a")
    GOODS_HERO = (By.CSS_SELECTOR, 'body > div.container > div:nth-child(3) > div > div > div > h5 > a')
    
    def __init__(self, driver):
        self.driver = driver
            
    def load(self):
        self.driver.get(self.URL_main)
        header = self.driver.find_element(*self.HEADER).text
        assert "Главная" in header, 'Главная ok'
        
    def search(self, phrase):
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.send_keys('Lenovo')
        search.send_keys(Keys.ENTER)

    def search_fromCatalog(self, phrase):
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.send_keys('Hero')
        search.send_keys(Keys.ENTER)