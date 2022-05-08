import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


def main():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()

    driver.get("https://beon.studio/")

    joinus = '/html/body/header/nav/div[2]/div/a'

    WebDriverWait(driver,20).until(ec.presence_of_element_located((By.XPATH,joinus))).click()

    time.sleep(15)

    cb1 = "/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[1]/select"

    dropdown = Select(driver.find_element(By.XPATH,cb1))

    dropdown.select_by_index(2)

    cb2 = '/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[2]/select'

    dropdown2 = Select(driver.find_element(By.XPATH, cb2))

    dropdown2.select_by_index(2)

    cb3 = '/html/body/section[2]/div[1]/div[2]/div/div/div[1]/div[3]/select'

    dropdown3 = Select(driver.find_element(By.XPATH, cb3))

    dropdown3.select_by_index(2)

    result = '/html/body/section[2]/div[1]/div[2]/div/div/div[3]/div[3]'

    r = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, result)))

    print(r.text)

    assert r.text == "There are no results that match your criteria. Don't worry, we have some interesting offers..."

main()