from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time

# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=C:\\Users\\jerzhou\\AppData\\Local\\Google\\Chrome\\User Data') #Path to your chrome profile
# options.add_argument('--profile-directory=Default') #Path to your chrome profile

# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
browser = webdriver.Chrome(ChromeDriverManager().install());
browser.get("file:///Users/jz/Desktop/automated_testing/Overview.html")

# EMAILFIELD = (By.ID, "i0116")
# PASSWORDFIELD = (By.ID, "i0118")
# NEXTBUTTON = (By.ID, "idSIButton9")

# DEV_EMAIL = (By.CSS_SELECTOR, ".tile-container:nth-child(2) div:nth-child(3)")
# WebDriverWait(browser,10).until(EC.element_to_be_clickable(DEV_EMAIL)).click()

FILTER_BUTTON = (By.ID, "filterbutton")
WebDriverWait(browser,10).until(EC.element_to_be_clickable(FILTER_BUTTON)).click()

tabs = browser.find_elements(By.CSS_SELECTOR, 'td[style*="display: table-cell;"]')


selectedFilters = []
# [<selenium.webdriver.remote.webelement.WebElement (session="658a9c19355bd7c156bf88813ddb8d35", element="2e554cf2-b7a2-44ac-b842-b6c964abe4af")>]
for element in tabs:
    name = element.get_attribute("id").split("_tab")[0]
    dropDownSelection = browser.find_elements(By.CSS_SELECTOR, '#{} option'.format(name))

    for selection in dropDownSelection:
        print("{} - {}".format(name, selection.get_attribute('innerHTML')))
        selection.click()
        browser.find_element(By.ID, 'apply').click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable(FILTER_BUTTON)).click()
        



def validateGraphs(browser):
    expected_graph_length = len(browser.find_elements(By.CSS_SELECTOR, 'img[alt="Loading"]'))
    for x in range(expected_graph_length):
        WebDriverWait(browser,10).until(EC.element_to_be_clickable(FILTER_BUTTON)).click()


    







        
        

    

    

# tabs = map(lambda x: x.get_property("id"), tabs)

# print(tabs)s

# # wait for email field and enter email
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("jerry.zhou@loblaw.ca")

# # Click Next
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# # wait for password field and enter password
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("New12User!")

# # Click Login - same id?
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()






# -----------------------------------------------
