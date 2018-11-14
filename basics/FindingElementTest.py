from selenium import webdriver
import os


class FindingElement():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementbyid = driver.find_element_by_id("name")
        if elementbyid is not None:
            print("Found an element by id")
        elementbyname = driver.find_element_by_name("show-hide")
        if elementbyname is not None:
            print("Found an element by name")


findnew = FindingElement()
findnew.test()
