from selenium import webdriver
import os
from selenium.webdriver.common.by import By

class ListofElement():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementbyListClassName = driver.find_elements_by_class_name("inputs")
        leng1 = len(elementbyListClassName)
        if elementbyListClassName is not None:
            print("Size of list Class Name is: " + str(leng1))

        elementbyListTagName = driver.find_elements(By.TAG_NAME,"td")
        leng2 = len(elementbyListTagName)
        if elementbyListTagName is not None:
            print("Size of list Tag Name is: " + str(leng2))


findnew = ListofElement()
findnew.test()
