import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random, time, os, sys
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-plugins-discovery")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user_agent=DN")
    # chrome_options.headless = True
    driver = uc.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    driver.maximize_window()
    return driver


############## PyTest HTML Report #########

# it is hook for adding environment info to HTML report

def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Tester'] = 'Suman'




