class BasePage:

    url = ''

    def __init__(self, driver):
        self.driver = driver;

    def go(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
