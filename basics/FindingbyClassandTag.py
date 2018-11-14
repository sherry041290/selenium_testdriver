from selenium import webdriver
import os


class ClassNameandTagName():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementbyClassName = driver.find_element_by_class_name("inputs")
        elementbyClassName.send_keys("Hello Sherry")
        if elementbyClassName is not None:
            print("Found an element by ClassName")
        elementbyTagName = driver.find_element_by_tag_name("h1")
        text = elementbyTagName.text
        if elementbyTagName is not None:
            print("Found an element by TagName, the text: " + text)


findnew = ClassNameandTagName()
findnew.test()
