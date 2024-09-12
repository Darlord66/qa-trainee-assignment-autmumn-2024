from unittest.result import failfast

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
browser.implicitly_wait(5)
try:
    link = browser.find_element(By.XPATH, ('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div'))
    link.click()
    var = browser.find_element(By.XPATH, ('/html/body/div[2]/div/div/div[2]/div/div/div/div[4]/div'))
    var.click()
    link = browser.find_element(By.XPATH, ('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div'))
    link.click()
    not_chosen = browser.find_element(By.XPATH, ("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div"))
    not_chosen.click()
    error = browser.find_element(By.XPATH,('//*[@id="error-page"]'))
    assert not error, "Fail: страница не найдена"
finally:
    browser.quit()
    #Тест должен завершиться с ошибкой