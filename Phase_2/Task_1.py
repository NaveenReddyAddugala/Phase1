#Requirements:
#use one common get driver function
###### This program is to ge t the dynamic value from pythonanywhere.com
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# def get_driver():
    # options=webdriver.ChromeOptions()
    # options.add_argument("disable-infobars")
    # options.add_argument("start-maximized")
    # options.add_argument("disable-dev-shm-usage")
    # options.add_argument("no-sandbox")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("disable-blink-features=AutomationControlled")
    
    # driver=webdriver.Chrome(options=options)
    # driver.get('https://automated.pythonanywhere.com/')
    # return driver
# def get_value(text):
    # print(text[-2:])
# def main():
    # driver=get_driver()
    # time.sleep(5)
    # element=driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[2]')
    # get_value(element.text)
    # return element.text


# print(main())

#This Program is for Automate login and Password

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
    driver.get('https://automated.pythonanywhere.com/')
    return driver


def store_in_file(value):
    fetch_datetime=datetime.datetime.now()
    final=f"D:\Python_Automation\Task1\{fetch_datetime.date().isoformat()}-{fetch_datetime.strftime('%X').replace(':','-')}.txt"
    print(final)
    with open(final,'w') as f:
        f.write(value)


# def get_value(text):
    # #print(text)
    # text_value=text.split(': ')[1]
    # store_in_file(text_value)
    # return text_value



def main():
    driver=get_driver()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="basicExampleNav"]/div/a').click()
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys("automated")
    driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys("automatedautomated" + Keys.RETURN)
   # driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/form/button').click()
    time.sleep(5)
    print(driver.current_url)
    button=driver.find_element(By.XPATH,'/html/body/nav/div/a')
    button.click()
    time.sleep(5)
    i=1
    for i in range(5):
        element=driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[2]')
        text=element.text
        text_value=text.split(': ')[1]
        time.sleep(2)
        store_in_file(text_value)
main()




# print("Do it ")
# print("Hi World")
# print("Scrapping the text")
# from selenium import webdriver
# #from selenium.webdriver.common.keys import Keys
# #driver = webdriver.Firefox(
# #executable_path='D:\Python_Automation\geckodriver.exe')
# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com")


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://automated.pythonanywhere.com/')
# d=driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[1]')
# print(d.text)