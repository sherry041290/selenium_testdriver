from selenium import webdriver
import os


class FindingXpathCss():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementbyXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementbyXpath is not None:
            print("Found an element by Xpath")
        elementbyCss = driver.find_element_by_css_selector("#name")
        if elementbyCss is not None:
            print("Found an element by Css")


findnew = FindingXpathCss()
findnew.test()
