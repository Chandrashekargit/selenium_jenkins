import time
from selenium import webdriver


def driver():
    driver = webdriver.Chrome(executable_path="/home/we45-lt24/ASE_UI_Automation/venv/bin/chromedriver_linux64/chromedriver")
    driver.maximize_window()
    driver.get("https:www.google.com")
    time.sleep(5)
    a = 5
    assert a == 6

driver()

