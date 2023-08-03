import pytest
from selenium import webdriver
from pages.poCart import StoreCart

driver = webdriver.Chrome()
poCart = StoreCart(driver)

@pytest.fixture
def pre_test():
    poCart.load()

def teardown_module(module):
    driver.close()
    
def check_search(driver):
    header = driver.find_element(*poCart.CART_LENOVO).text
    assert "Lenovo" in header, 'Lenovo ok'
    
def check_cartAdd(driver):
    header = driver.find_element(*poCart.CART_LENOVO).text
    assert "Lenovo" in header, 'Lenovo ok'
    
def check_cart(driver):
    header = driver.find_element(*poCart.DELETE_BUTTON).text
    assert "Удалить" in header, "Удалить ok"

def check_cartCountAdd(driver):
    header = driver.find_element(*poCart.PRICE_LENOVO).text
    assert "60000.0 р" in header, "60000.0 р ok"

def check_cartCountDelete(driver):
    header = driver.find_element(*poCart.PRICE_LENOVO).text
    assert "30000.0 р" in header, "30000.0 р ok"

def check_cartDelete(driver):
    header = driver.find_element(*poCart.CART_NOTICE).text
    assert "Ваша корзина пуста" in header, "Ваша корзина пуста ok" 

def test_search(pre_test):
    poCart.search()
    check_search(driver)

    poCart.cartAdd()
    check_cartAdd(driver)

    poCart.cart()
    check_cart(driver)

    poCart.cartCountAdd()
    check_cartCountAdd(driver)

    poCart.cartCountDelete()
    check_cartCountDelete(driver)

    poCart.cartDelete()
    check_cartDelete(driver)