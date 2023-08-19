#Requirements:
#use one common get driver function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
def main():
    driver=get_driver()
    element=driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[1]")
    return element.text


print(main())






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