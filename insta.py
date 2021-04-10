import autoit
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import colorama
from colorama import Fore, init, Style, Back
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
import os
import time
import random
import sys
init(convert=True)




print(Style.BRIGHT + Fore.BLUE + """
██╗███╗   ██╗███████╗████████╗ █████╗     ███╗   ███╗███████╗███╗   ███╗███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗    ████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║    ██╔████╔██║█████╗  ██╔████╔██║█████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║    ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║    ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                        """)
print(Style.BRIGHT + Fore.WHITE + "[+] CODED BY tristan#2230")
print()
print(Style.BRIGHT + Fore.BLUE + "[+] INSTALLING REQUIRED MATERIALS")
print(Style.DIM + Fore.BLACK)
os.system('pip install chromedriver-autoinstaller')
os.system('pip install selenium')
os.system('cls' if os.name == 'nt' else "printf '\033c'")

chromedriver_autoinstaller.install()

print(Style.BRIGHT + Fore.BLUE + """
██╗███╗   ██╗███████╗████████╗ █████╗     ███╗   ███╗███████╗███╗   ███╗███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗    ████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║    ██╔████╔██║█████╗  ██╔████╔██║█████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║    ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║    ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                        """)
print(Style.BRIGHT + Fore.WHITE + '[+] CREATE A FOLDER NAMED "instameme" ON YOUR DESKTOP')
print()
print('[+] RENAME EACH IMAGE TO "image.jpg"')
username = open("username.txt", "r")
username.readlines()
password = open("password.txt", "r")
password.readlines()
caption = open("caption.txt", "r")
caption.readlines()
image_path = r"instameme.jpg" #The written path is just an example, Delete the path and Enter the Path of your image. #1. path should not start with a back slash
print(Fore.BLACK + Style.DIM)
mobile_emulation = { "deviceName": "Pixel 2" }
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)
#opts.add_argument("--headless")
opts.add_argument('--log-level=3')

driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=opts)

main_url = "https://www.instagram.com"
driver.get(main_url)

sleep(1.5)

def login():
    login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
    login_button.click()
    sleep(2)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()

login()
sleep(1)

def close_reactivated():
    try:
        sleep(1.5)
        not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
        not_now_btn.click()
        
    except:
        pass

close_reactivated()

def close_notification():
    try: 
        sleep(1)
        close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
        close_noti_btn.click()
    except:
        pass

close_notification()

def close_add_to_home():
    try:
        sleep(1) 
        close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
        close_addHome_btn.click()
        sleep(1)
    except NoSuchElementException: 
        print() 
        print(Style.BRIGHT + Fore.RED + "[ERROR] FAILED TO LOGIN")
        print()
        print(Fore.RED + "[-] CLOSING PROGRAM", end = "")
        time.sleep(0.4)
        print(".", end = "")
        time.sleep(0.4)
        print(".", end = "")
        time.sleep(0.4)
        print(".", end = "")
        time.sleep(0.4)
        sys.exit()
    else:
        print(Style.BRIGHT + Fore.GREEN + "[LOG] SUCCESSFULLY LOGGED IN")
        print(Style.BRIGHT + Fore.BLUE) 

close_add_to_home()

sleep(2)

close_notification()

new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
sleep(1.5)
autoit.win_active("Open") 
sleep(2)
autoit.control_send("Open","Edit1",image_path) 
sleep(1.5)
autoit.control_send("Open","Edit1","{ENTER}")

sleep(2)


next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

sleep(1.5)

caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
caption_field.send_keys(caption)



share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()


sleep(10)

print(Style.BRIGHT + Fore.GREEN + "[LOG] SUCCESSFULLY UPLOADED IMAGE")

print(Style.BRIGHT + Fore.BLUE)
input("[+] PRESS ENTER TO CLOSE THE PROGRAM: ")

driver.close()