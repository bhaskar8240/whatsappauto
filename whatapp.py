import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pg


path = "C:/Users/Administrator/Desktop/whatsappauto-main/driver/chromedriver.exe"
link = "https://web.whatsapp.com/"
chrome_option = Options()
chrome_option.add_argument("--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
browser = webdriver.Chrome(path,options=chrome_option)
browser.get(link)
time.sleep(10)
tab = pg.press(["tab","tab","tab"])

# Run function For send sms .

def send_sms(data):
    tab
    serch_bar = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
    serch_bar.click()
    browser.execute_script("""
    document.querySelector("#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text").innerText= "";
    """)
    pg.write("bapi")
    time.sleep(3)
    user = browser.find_element_by_xpath(
        '//span[@title = "{}"]'.format("bapi"))
    user.click() 
    time.sleep(3) 
    massage = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
    massage.click()
    pg.write(data)
    button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
    time.sleep(1)
    button.click()
    time.sleep(3)   
    browser.close()

#Run the Funtion 
    
send_sms("x")    


