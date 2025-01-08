import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random,time,os,sys
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()



    def test_login_ebay(self, setup):
        self.logger.info("************* Verifying ebay test ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.driver.find_element(By.XPATH,self.lp.SearchBox).send_keys("book")
        self.driver.find_element(By.CSS_SELECTOR, self.lp.SearchBtn).click()
        self.driver.find_element(By.XPATH, self.lp.FirstBook).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        print(self.driver.title)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
        self.driver.find_element(By.ID, self.lp.AddToKartBtn).click()
        item_in_kart = self.driver.find_element(By.XPATH, self.lp.CartBtn).get_attribute('aria-label')



        if item_in_kart == "Your shopping cart contains 1 item":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookSearch.png")

            self.logger.error("************* Login Test test_login_ebay Fails ***********")
            self.driver.quit()



