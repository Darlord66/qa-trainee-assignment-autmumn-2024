from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
browser.implicitly_wait(5)

try:
    link = browser.find_element(By.XPATH,('//*[@id="root"]/div/div[5]/div[2]/div/ul/li[1]/div/div/div/div'))
    link.click()
    button = browser.find_element(By.XPATH, ('//*[@id="root"]/div/div[3]/div/div/div[5]/div/button'))
    button.click()
    main_page = browser.find_element(By.XPATH, ('//*[@id="root"]/div/div[1]/div/h1'))
    assert main_page, "Fail: main page не обнаружено"
finally:
    browser.quit()