# from pages.HomePage import HomePage
# from pages.LoginPage import LoginPage

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, os
from time import sleep
import random
import time
import pytest



def test_google_search(get_visit_result, check):
    driver = webdriver.Chrome(executable_path="/Users/cathy/Documents/Gitrep/google_search_UI_automation/chromedriver")
    driver.get("https://www.google.com/imghp?hl=en")
    time.sleep(2)
    try:
        # cam_button = driver.find_elements_by_xpath("//div[@aria-label='Search by image' and @role='button']")[0]
        cam_button = driver.find_element_by_xpath("//div[@aria-label='Search by image' and @role='button']")
        cam_button.click()

        time.sleep(2)
        # upload_image_tab = driver.find_element_by_xpath("//div[@id='FQt3Wc']//div/div/span")
        upload_image_tab = driver.find_element_by_xpath("//div[@id='dRSWfb']//a")

        upload_image_tab.click()

        choose_file_button = driver.find_element_by_id("awyMjb")
        choose_file_button.send_keys("/Users/cathy/Documents/Gitrep/UI/data/test1.jpeg")

        time.sleep(2)

        results_h3_text = driver.find_elements_by_xpath("//div[@id='rso']/div//h3")
        results_link = driver.find_elements_by_xpath("//div[@id='rso']/div//a")
        for i in results_link:
            print(i.get_attribute("href"))

        visit_result = get_visit_result
        link_2 = results_link[visit_result].get_attribute("href")
        driver.get(link_2)
        time.sleep(2)










    finally:
        driver.quit()
