from selenium import webdriver
import os


class RunWindownEdgeTests():
    def test(self):
        driverLocation = "C:\\Users\\lenovo\\PycharmProjects\\pythontutorial\\venv\\Lib\\site-packages\\selenium\\MicrosoftWebDriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Edge(driverLocation)
        driver.get("https://consumer.hottab.us/")


ff = RunWindownEdgeTests()
ff.test()