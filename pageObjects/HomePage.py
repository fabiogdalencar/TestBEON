from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.JobPage import JobPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    joinus = (By.XPATH, "/html/body/header/nav/div[2]/div/a")

    def searchJob(self):
        #WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(*HomePage.joinus)).click()
        self.driver.find_element(*HomePage.joinus).click()
        jobPage = JobPage(self.driver)
        return jobPage



