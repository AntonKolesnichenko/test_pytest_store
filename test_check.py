import pytest
from selenium import webdriver
from pages.poProduct import Goods

driver = webdriver.Chrome()
poProduct = Goods(driver)

expected = {'id': '14', 'name': 'Lenovo yoga', 'price': '30000.0', 'quantity': 'В наличии немного'}

@pytest.fixture
def pre_test(request):
    poProduct.load(expected['id'])

def teardown_module(module):
    driver.close()

def test_goods(pre_test):
    assert expected['name'] in poProduct.title(), "Wrong name"
    assert expected['id']+".png" in poProduct.img(), "Wrong image"
    assert expected['price'] in poProduct.price(), "Wrong price"
    assert expected['quantity'] in poProduct.quantity(), "Wrong quantity"