from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

#  headless mode を使う:  <15-09-19, yourname> #

URL = "http://www.python.org"
SEARCH_WORD = "GCP"

contents_list = []

# ブラウザを開き、URLにアクセスする
driver = webdriver.Firefox()
driver.get(URL)

# 検索ボックスに検索ワードを入力して検索する
search_box = driver.find_element_by_css_selector("input#id-search-field")
search_box.send_keys(SEARCH_WORD)
search_box.send_keys(Keys.RETURN)

#  Nextボタンが無くなるまでループする:  <15-09-19, yourname> #

# ページのロードを待機する
try:
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "ul.list-recent-events li p")
        )
    )
except Exception as e:
    print(e)
    raise

# 検索結果を取得する
search_result = driver.find_element_by_css_selector("ul.list-recent-events li")
# print(type(search_result), search_result)
# title = search_result.find_element_by_css_selector("h3 a").text()
title = search_result.find_element_by_css_selector("h3 a").text
print(title)
url = urljoin(
    URL, search_result.find_element_by_css_selector("h3 a").get_attribute("href")
)
print(url)
description_text = ""
descriptions = search_result.find_elements_by_css_selector("p")
for description in descriptions:
    description_text += description.text + "\n"

print(description_text)

#  検索結果をlistに格納する:  <15-09-19, yourname> #

# Nextボタンを押す

# 結果を出力する
