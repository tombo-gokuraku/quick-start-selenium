from selenium import webdriver

URL = "http://www.python.org"
SEARCH_WORD = "AWS"

# ブラウザを開き、URLにアクセスする
driver = webdriver.Firefox()
driver.get(URL)
input_js = f"""
let search_box = document.getElementById('id-search-field');
search_box.value = '{SEARCH_WORD}';
search_box.dispatchEvent(new Event('change'));
"""
driver.execute_script(input_js)
# search_box = driver.find_element_by_css_selector("input#id-search-field")
# search_box.send_keys(SEARCH_WORD)
