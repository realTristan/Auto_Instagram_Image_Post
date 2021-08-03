import autoit, os, time, random, sys, chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, init, Style, Back
init(convert=True)

# installing dependencies
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
print(Fore.BLACK + Style.DIM)

opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", { "deviceName": "Pixel 2" }); opts.add_argument('--log-level=3'); opts.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=opts); driver.get("https://www.instagram.com")

def main():
    #Logging into the account
    driver.implicitly_wait(3); driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
    driver.implicitly_wait(3); driver.find_element_by_xpath("//input[@name='username']").send_keys(open("username.txt", "r").readline())
    driver.implicitly_wait(3); driver.find_element_by_xpath("//input[@name='password']").send_keys(open("password.txt", "r").readline()).submit()

    try:
        driver.implicitly_wait(2); driver.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except:
        driver.implicitly_wait(2); driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

    try:
        driver.implicitly_wait(5); driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
    except:
        print(Style.BRIGHT + Fore.RED + "[LOG] FAILED TO LOG IN" + Fore.BLUE)


    driver.implicitly_wait(2); driver.find_element_by_xpath("//div[@role='menuitem']").click()
    driver.implicitly_wait(2); autoit.win_active("Open")
    driver.implicitly_wait(2); autoit.control_send("Open","Edit1", "instameme.jpg")
    driver.implicitly_wait(2); autoit.control_send("Open","Edit1","{ENTER}")

    driver.implicitly_wait(2); driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    driver.implicitly_wait(2); driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']").send_keys(open("caption.txt", "r").readlines())

    driver.implicitly_wait(2); driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()


    time.sleep(10); print(Style.BRIGHT + Fore.GREEN + "[LOG] SUCCESSFULLY UPLOADED IMAGE")
    input(); driver.close()





# NOTE: I did some extra cleaning up and changes without fully testing them as I didn't have the time. Therefore if there's any errors or problems,
# PLEASE DM me on discord @ tristan#2230
# CHANGE the image you want to upload to instameme.jpg
# IF your internet is slow, then change the "driver.implicitly_wait(2)" to "driver.implicitly_wait(4)"
