from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from pageObjects.HomePage import HomePage
from pageObjects.JobPage import JobPage

import logging
import pytest

@pytest.mark.usefixtures("setup")
class TestSearchPage():

    def test_missing_job(self):
        homepage = HomePage(self.driver)
        log = logging.getLogger()
        log.info("getting to the job page")
        jobpage = homepage.searchJob()

        log.info("selecting the comboboxes")
        s = Select(jobpage.getTechCb())
        s.select_by_index(2)
        s = Select(jobpage.getBusinessCb())
        s.select_by_index(2)
        s = Select(jobpage.getRoleCb())
        s.select_by_index(2)

        result = '/html/body/section[2]/div[1]/div[2]/div/div/div[3]/div[3]'

        r = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, result)))

        log.info("Text received from application is " + r.text)

        assert ("There are no results that match your criteria. Don't worry, we have some interesting offers..." in r.text)


