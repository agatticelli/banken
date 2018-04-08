from selenium import webdriver

class Bank(object):

    def __init__(self, browserName):

        self.browserName = browserName

        if self.browserName == "firefox":
            self.driver = webdriver.Firefox()

        elif self.browserName == "chrome":
            self.driver = webdriver.Chrome()

        else:
            raise Exception('Browser not supported')


    def close(self):

        if self.driver:
            self.driver.close()