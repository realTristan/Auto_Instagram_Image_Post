import autoit, time, chromedriver_autoinstaller
from selenium import webdriver
from colorama import Fore, Style, init; init(convert=True)
chromedriver_autoinstaller.install()

print(Style.BRIGHT + Fore.BLUE + """
 █████                     █████                                                          
░░███                     ░░███                                                           
 ░███  ████████    █████  ███████    ██████    ███████ ████████   ██████   █████████████  
 ░███ ░░███░░███  ███░░  ░░░███░    ░░░░░███  ███░░███░░███░░███ ░░░░░███ ░░███░░███░░███ 
 ░███  ░███ ░███ ░░█████   ░███      ███████ ░███ ░███ ░███ ░░░   ███████  ░███ ░███ ░███ 
 ░███  ░███ ░███  ░░░░███  ░███ ███ ███░░███ ░███ ░███ ░███      ███░░███  ░███ ░███ ░███ 
 █████ ████ █████ ██████   ░░█████ ░░████████░░███████ █████    ░░████████ █████░███ █████
░░░░░ ░░░░ ░░░░░ ░░░░░░     ░░░░░   ░░░░░░░░  ░░░░░███░░░░░      ░░░░░░░░ ░░░░░ ░░░ ░░░░░ 
                                              ███ ░███                                    
                                             ░░██████                                     
                                              ░░░░░░                                      """)

image_name = "image_1.jpg" # // Change "image_1.jpg" to the name of the picture you want to post
wait_time = 2 # // Make this higher if you have bad internet

opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", { "deviceName": "Pixel 2" }); opts.add_argument('--log-level=3'); opts.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=opts); driver.get("https://www.instagram.com")

def main():
    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//input[@name='username']").send_keys(open("username.txt", "r").readline())
    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//input[@name='password']").send_keys(open("password.txt", "r").readline()).submit()

    try: driver.implicitly_wait(3); driver.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except: driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

    try: driver.implicitly_wait(3); driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
    except: print(Style.BRIGHT + Fore.RED + "[ERROR] FAILED TO LOG IN" + Fore.BLUE)

    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//div[@role='menuitem']").click()
    driver.implicitly_wait(wait_time); autoit.win_active("Open")
    driver.implicitly_wait(wait_time); autoit.control_send("Open","Edit1", image_name)
    driver.implicitly_wait(wait_time); autoit.control_send("Open","Edit1","{ENTER}")

    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']").send_keys(open("caption.txt", "r").readlines())
    driver.implicitly_wait(wait_time); driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()

    time.sleep(10); driver.close()
