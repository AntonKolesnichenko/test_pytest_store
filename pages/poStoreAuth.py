from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class StoreAuth:
    URL_main = "http://testshop.sedtest-school.ru/"
    URL_auth = "http://testshop.sedtest-school.ru/users/auth/"
    TITLE = (By.ID, "TestGym")
    HEADER_auth = (By.CSS_SELECTOR, "h2") ## "Авторизация" на странице авторизации
    WELCOME = (By.CSS_SELECTOR, "h4") ## Каталог
    MAIN = (By.CSS_SELECTOR, '#nav_link_main > a') ##"Главная"
    SEARCH_INPUT = (By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div.col-md-9.mt-2 > form > div > input")  ## Строка поиска
    ENTER_BUTTON = (By.CSS_SELECTOR , "body > div.row.mt-5 > div.container.mt-5.col-md-4 > form > button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#navbarCollapse > div > a.btn.btn-danger")
    PROFILE_ICON = (By.CSS_SELECTOR, "#navbarCollapse > div > a:nth-child(3) > img")
    GOODS_LENOVO = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div:nth-child(2) > div > div > h5 > span")
    PRICE_LENOVO = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div:nth-child(2) > div > div > div > div:nth-child(2) > span:nth-child(1)")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_email")
    INPUT_PASS = (By.CSS_SELECTOR, "#id_password")

    def __init__(self, driver):
        self.driver = driver
        
    def load(self):
        self.driver.get(self.URL_main)
        self.driver.find_element(*self.MAIN).text
        
    def auth_load(self):
        self.driver.get(self.URL_main)
        self.driver.find_element(*self.WELCOME).text
        
        self.driver.find_element(By.CSS_SELECTOR, '#navbarCollapse > div > a.btn.btn-primary').click()
        self.driver.find_element(*self.HEADER_auth).text
        
    def auth(self):
        email = self.driver.find_element(*self.INPUT_EMAIL)
        email.send_keys('kag@synum.ru')
        password = self.driver.find_element(*self.INPUT_PASS)
        password.send_keys('123454321')
        self.driver.find_element(*self.ENTER_BUTTON).send_keys(Keys.ENTER)