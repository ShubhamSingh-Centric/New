from base.base_page import BasePage
from selenium.webdriver.common.by import By
from base.base_element import BaseElement
from selenium import webdriver


class GoogleHome(BasePage):

    url = "https://www.google.com"

    @property
    def link_gmail(self):
        return BaseElement(self.driver, By.XPATH, '//a[text()="Gmail"]')


if __name__ == "__main__":
    browser = webdriver.Chrome()
    page = GoogleHome(browser)
    page.go()
    page.link_gmail.click_element()

