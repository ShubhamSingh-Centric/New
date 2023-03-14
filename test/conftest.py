from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome("C:\\Users\\shubham.singh\\chromedriver_win32\\chromedriver.exe")
    return browser


@fixture(params=[{"brand": "Sony", "size": "50 inch"},
                 {"brand": "Samsung", "size": "65 inch"},
                 {"brand": "Panasonic", "size": "32 inch"}])
def tv_brand(request):
    brand = request.param
    return brand
