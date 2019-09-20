from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import time
from pprint import pprint
import json


URL = "http://www.python.org"
SEARCH_WORD = "AWS"

contents_list = []

# ブラウザを開き、URLにアクセスする
driver = webdriver.Firefox()
driver.get(URL)

# 検索ボックスに検索ワードを入力して検索する
search_box = driver.find_element_by_css_selector("input#id-search-field")
search_box.send_keys(SEARCH_WORD)
search_box.send_keys(Keys.RETURN)

#  Nextボタンが無くなるまでループする
while True:
    # ページのロードを待機する
    try:
        search_results = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "ul.list-recent-events li")
            )
        )
    except TimeoutException:
        raise

    # 検索結果を取得する
    for search_result in search_results:
        title = search_result.find_element_by_css_selector("h3 a").text
        url = urljoin(
            URL,
            search_result.find_element_by_css_selector("h3 a").get_attribute("href"),
        )
        description_text = ""
        descriptions = search_result.find_elements_by_css_selector("p")
        for description in descriptions:
            description_text += description.text + "\n"

        item = {"url": url, "title": title, "description": description_text}

        #  検索結果をlistに格納する
        contents_list.append(item)

    # 次のページへ移動する
    try:
        next_elem = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div/a[contains(@href,'page')][contains(text(),'Next')]")
            )
        )
        print("go to next")
        driver.get(next_elem.get_attribute("href"))
        time.sleep(1)
    except TimeoutException:
        print("end of search result")
        break


# 結果を出力する
pprint(contents_list[:5])
print(len(contents_list))
# jsonに保存する
with open("./search_reslut.json", "w") as f:
    json.dump(contents_list, f, indent=2)

driver.close()
