import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg


path = "C:/Users/Administrator/Desktop/whatsappauto-main/driver/chromedriver.exe"
link = "https://www.airtel.in/business/thanksforbusiness/data/sr/raise/"
browser = webdriver.Chrome(path)
browser.get(link)
browser.maximize_window()
time.sleep(5)

def Call_log():
    issue_details = browser.find_element(by=By.XPATH,value="/html/body/div[2]/div[3]/main/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/input")
    issue_details.click()
    pg.write("123456")
    proceed = browser.find_element(by=By.XPATH,value='//*[@id="root"]/div[3]/main/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[2]/div')
    proceed.click()
    time.sleep(2)
    issue_type = browser.find_element(by=By.XPATH,value='//*[@id="initial"]')
    issue_type.click()
    time.sleep(1)
    Link_down = browser.find_element(by=By.XPATH,value='//*[@id="root"]/div[3]/main/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/ul/li[7]')
    Link_down.click()
    time.sleep(2)
    name = browser.find_element(by=By.XPATH,value='//*[@id="name"]')
    name.click()
    pg.write("Gtpl_Noc")
    time.sleep(1)
    mobile = browser.find_element(by=By.XPATH,value='//*[@id="root"]/div[3]/main/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/input')
    mobile.click()
    pg.write("8240661825")
    time.sleep(1)
    mail = browser.find_element(by=By.XPATH,value='//*[@id="email"]')
    mail.click()
    pg.write("bhaskarhug@gmail.com")
    time.sleep(1)
    comment = browser.find_element(by=By.XPATH,value='//*[@id="description"]')
    comment.click()
    pg.write("We are facing link down issue.")
    time.sleep(2)
    # submit = browser.find_element_by_xpath('//*[@id="root"]/div[3]/main/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/button[2]/div')
    browser.close()
if __name__ == "__main__":
    Call_log()


