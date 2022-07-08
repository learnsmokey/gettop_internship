# This .py file is to open and see the sub menus of Accessories
# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# set the chrome browser
browser = webdriver.Chrome('chromedriver_win32\\chromedriver.exe')
browser.get('https://gettop.us/')

# find the accessories xpath element based on id
accessories = browser.find_element(By.ID,'menu-item-472')

# to identify the mouse over mouseover
action = ActionChains(browser)
action.move_to_element(accessories).perform()