from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("file:///Users/jz/Desktop/automated_testing/web.py")
print(driver.body)

tabs = driver.find_element_by_css_selector("#filtertable tr td[style*='display: table-cell']")
tabs = map(lambda x: x.split("tr")[1], tabs)

for index, key in tabs:
    dropdown = driver.find_element_by_css_selector("#filtertable tr ") 


