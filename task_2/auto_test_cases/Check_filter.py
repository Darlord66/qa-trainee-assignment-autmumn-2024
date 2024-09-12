from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
browser.implicitly_wait(5)

try:
    link = browser.find_element(By.XPATH,('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div'))
    link.click()
    var = browser.find_element(By.XPATH,('/html/body/div[2]/div/div/div[2]/div/div/div/div[4]/div'))
    var.click()
    card = browser.find_element(By.XPATH,('//*[@id="root"]/div/div[5]/div[2]/div/ul/li[1]/div/div/div/div'))
    card.click()
    button = browser.find_element(By.XPATH,('//*[@id="root"]/div/div[3]/div/div/div[5]/div/button'))
    button.click()
    element_value = browser.find_element(By.XPATH,('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div/span[2]'))
    assert element_value == var, "Fail: фильтр выбора категории сбросился после возврата на главную из карточки товара"
finally:
    browser.quit()
    #Тест должен завершиться с ошибкой