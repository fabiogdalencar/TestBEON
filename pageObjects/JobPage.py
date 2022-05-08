from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class JobPage:

    def __init__(self, driver):
        self.driver = driver

    cb_tech = (By.XPATH, "/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[1]/select")
    cb_business = (By.XPATH, "/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[2]/select")
    cb_role = (By.XPATH, "/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[3]/select")

    def getTechCb(self):
        return self.driver.find_element(*JobPage.cb_tech)


    def getBusinessCb(self):
        return self.driver.find_element(*JobPage.cb_business)

    def getRoleCb(self):
        return self.driver.find_element(*JobPage.cb_role)


