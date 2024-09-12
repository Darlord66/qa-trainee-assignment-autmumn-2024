from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestButtonDisabled(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
        self.browser.implicitly_wait(5)

    def test_button_disabled(self):
        link = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/div[5]/div[1]/ul/li[2]/a')
        link.click()
        button = self.browser.find_element(By.XPATH, "//*[@id='root']/div/div[5]/div[1]/ul/li[1]/button")
        self.assertTrue(button.get_attribute("disabled") is not None), "Кнопка активна"

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
