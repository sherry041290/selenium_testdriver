from selenium import webdriver


class RunFFTests():
    def testff(self):
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff=RunFFTests()
ff.testff()