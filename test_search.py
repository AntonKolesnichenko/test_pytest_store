import pytest
from selenium import webdriver
from pages.poSearch import StoreSearch

driver = webdriver.Chrome()
poSearch = StoreSearch(driver)

@pytest.fixture
def pre_test():
    poSearch.load()

def teardown_module(module):
    driver.close()

def check_search(driver):
    header = driver.find_element(*poSearch.GOODS_LENOVO).text
    assert "Lenovo" in header, 'Lenovo ok'
    
def check_search_fromCatalog(driver):
    header = driver.find_element(*poSearch.GOODS_HERO).text
    assert "Hero" in header, 'Hero ok'

def test_search(pre_test):
    poSearch.search('Lenovo')
    check_search(driver)
    
    poSearch.search_fromCatalog('Hero')
    check_search_fromCatalog(driver)