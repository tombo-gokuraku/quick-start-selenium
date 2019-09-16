from selenium import webdriver

# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import time
from pprint import pprint

#  headless mode を使う:  <15-09-19, yourname> #

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

#  Nextボタンが無くなるまでループする:  <15-09-19, yourname> #
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

    # search_results = driver.find_elements_by_css_selector("ul.list-recent-events li")
    # 検索結果を取得する
    for search_result in search_results:
        # search_result = driver.find_element_by_css_selector("ul.list-recent-events li")
        # print(type(search_result), search_result)
        # title = search_result.find_element_by_css_selector("h3 a").text()
        title = search_result.find_element_by_css_selector("h3 a").text
        # print(title)
        url = urljoin(
            URL,
            search_result.find_element_by_css_selector("h3 a").get_attribute("href"),
        )
        # print(url)
        description_text = ""
        descriptions = search_result.find_elements_by_css_selector("p")
        for description in descriptions:
            description_text += description.text + "\n"

        # print(description_text)

        item = {"url": url, "title": title, "description": description_text}
        # print(item)

        #  検索結果をlistに格納する:  <15-09-19, yourname> #
        contents_list.append(item)

    # Nextボタンを押す
    try:
        next_elem = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    # "//div[a[contains(@href,'page')]][a[contains(text(),'Next')]]",
                    "//div/a[contains(@href,'page')][contains(text(),'Next')]",
                )
            )
        )
        print("go to next")
        # next_elem.click()
        driver.get(next_elem.get_attribute("href"))
        time.sleep(1)
    except TimeoutException:
        print("end of search result")
        break


# 結果を出力する
pprint(contents_list[:5])
print(len(contents_list))

driver.close()
