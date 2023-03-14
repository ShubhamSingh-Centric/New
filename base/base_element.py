class BaseElement:

    def __init__(self, driver, locator, locator_value):
        self.driver = driver
        self.locator = locator
        self.locator_value = locator_value

    def element(self):

        return self.driver.find_element(self.locator, self.locator_value)

    def click_element(self):
        self.element().click()
