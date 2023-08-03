import pytest
from selenium import webdriver
from pages.poStoreAuth import StoreAuth

driver = webdriver.Chrome()
poStoreAuth = StoreAuth(driver)

@pytest.fixture
def pre_test(request):
    poStoreAuth.auth_load()

def teardown_module(module):
    driver.close()

def verify_auth():
    logout = driver.find_element(*poStoreAuth.LOGOUT_BUTTON).text
    assert 'Выйти' in logout, 'Выйти ok'

def test_auth(pre_test):
    poStoreAuth.auth_load()
    verify_auth()

def test_auth(pre_test):
    poStoreAuth.auth()
    verify_auth()