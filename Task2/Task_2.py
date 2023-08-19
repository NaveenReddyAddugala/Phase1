
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import datetime
def get_driver():
    options=webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver=webdriver.Chrome(options=options)
    driver.get('https://www.primevideo.com/offers/nonprimehomepage/ref=dvm_pds_amz_in_as_s_gm_21_mkw_sDTaWHMbb-dc?gclid=CjwKCAjwivemBhBhEiwAJxNWN4qeUyxD-H42BaMt4TGJeAA0bueHnxTyp7ODd9_XzzVy4C7Xq9zVxxoCC_8QAvD_BwE&mrntrk=pcrid_657901934582_slid__pgrid_84577172528_pgeo_9154412_x__adext__ptid_kwd-299989972454')
    return driver



def main():
    driver=get_driver()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/form/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys("8790762651")
    driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div/form/div/div/div/input[2]').send_keys("Nand@951")
main()