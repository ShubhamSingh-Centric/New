
from page.google_home import GoogleHome

class TestGoogleTest:

    def test_first(self, chrome_browser):
        chrome_browser.get('https://www.google.com')

# page.go()

page = TestGoogleTest.test_first()
