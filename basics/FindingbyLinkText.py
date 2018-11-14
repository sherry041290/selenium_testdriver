from selenium import webdriver
import os


class FindingbyLinktext():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementbyLinktext = driver.find_element_by_link_text("Login")
        if elementbyLinktext is not None:
            print("Found an element by Linktext")
        elementbyPartialLinkText= driver.find_element_by_partial_link_text("Pract")
        if elementbyPartialLinkText is not None:
            print("Found an element by Partial Link Text")


findnew = FindingbyLinktext()
findnew.test()
