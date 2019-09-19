from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.python.org")

# menubar_links = driver.find_elements_by_css_selector("ul[role='menubar'] > li")
menubar_links = driver.find_elements_by_css_selector("ul[role='menubar'] > li > a")
print(len(menubar_links))

for link in menubar_links:
    # print(link.find_element_by_css_selector("a").get_attribute("href"))
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.move_to_element(link)
    actions.click(link)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    actions.reset_actions()
    time.sleep(1)

driver.close()
driver.quit()
