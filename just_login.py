from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get("https://int.keellssuper.net/login")


def login():
    sleep(1)
    driver.find_element_by_xpath(
        "//select[@name='ctl00$BodyContent$ddlDeliveryCity']/option[text()='Thalahena']").click()
    sleep(1)
    driver.find_element_by_xpath("//select[@name='ctl00$BodyContent$ddlSuburb']/option[text()='Thalahena']").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$UserName\"]").send_keys("fb.uwin@gmail.com")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$LoginPassword\"]").send_keys("^1LoK^3hktG!^gUD")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$BtnLogin\"]").click()
    sleep(1)


def loop(driver):
    try:
        login()
    except:
        sleep(1)
        driver.refresh()
        loop(driver)


loop(driver)
