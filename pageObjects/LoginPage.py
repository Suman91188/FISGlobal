import time
import time
import random,time,os,sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class LoginPage:

    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    SearchBox = "//div[@id = 'gh-ac-box2']/input[@placeholder='Search for anything']"
    SearchBtn = "#gh-btn"
    FirstBook = "//ul[@class='srp-results srp-list clearfix']/li//div[@class='s-item__info clearfix']/a"
    AddToKartBtn ='atcBtn_btn_1'
    CartBtn = "//li[@id='gh-minicart-hover']/div/a"


    def __init__(self, driver):
        self.driver = driver


    def launch_Ebay_portal(self,setup):
        self.logger.info("************* Verifying Login to Google Finance ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        return self.driver




