from selenium import webdriver
from selenium.webdriver.common.by import By


class FindingElement():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementbyid = driver.find_element(By.ID, "name")
        if elementbyid is not None:
            print("Found an element by id")
        elementbyname = driver.find_element(By.NAME, "show-hide")
        if elementbyname is not None:
            print("Found an element by name")
        elementbyXpath = driver.find_element(By.XPATH, "//a[@id='opentab']")
        if elementbyXpath is not None:
            print("Found an element by Xpath")


findnew = FindingElement()
findnew.test()
