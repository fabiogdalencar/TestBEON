import pytest
from selenium import webdriver
import time
driver = None
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()

    driver.get("https://beon.studio/")

    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()