from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(executable_path="geckodriver", options=options)
driver.get("https://www.python.org")
print(driver.title)
driver.quit()
