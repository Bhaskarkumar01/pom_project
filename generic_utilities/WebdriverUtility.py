class Webdriverutility:
    def __init__(self,driver):
        self.driver=driver
    def click(self,var):
        self.driver.find_element(*var).click()


