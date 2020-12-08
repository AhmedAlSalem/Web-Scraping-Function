#from config import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

'''
                                Web Scraping Function to
                                1-  Disable flash player
                                2-  Disable volume
                                3-  Disable web notifications
                                4-  Disable image loading
                                
                                       Code By BeRLiN
                                     twitter @iAhmedika

'''
try:
    current_path = os.path.dirname(os.path.abspath(__file__))
except:
    current_path = '.'

target_site = "enter url" # web scraping target
geckodriver = r"C:\Users\BeRLiN\Desktop\WebScrapingPython\geckodriver"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'

def init_driver(geckodriver, load_images=True, user_agent='', headGUI=False):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("dom.webnotifications.enabled", False)  # Disable web notifications
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)  # Disable flash player
    firefox_profile.set_preference('media.volume_scale', "0.0")  # Disable volume
    if load_images != True:
        firefox_profile.set_preference('permissions.default.image', 2) # Disable image loading
    if user_agent !='':
        firefox_profile.set_preference("general.useragent.override", user_agent)
    options = Options()
    options.headless = headGUI
    driver = webdriver.Firefox(executable_path=geckodriver, firefox_profile=firefox_profile)
    return driver

driver = init_driver(geckodriver,user_agent=user_agent)
driver.get("https://www.google.com/")
