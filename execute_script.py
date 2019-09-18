from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result = driver.execute_script("return document.getElementById('about').innerHTML;")
print(result)

