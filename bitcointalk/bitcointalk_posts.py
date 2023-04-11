import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def extract_post_data(post_element):
    try:
        username_element = post_element.find_element(By.CSS_SELECTOR, "td.poster_info > b > a")
        post_date_element = post_element.find_element(By.CSS_SELECTOR, "td.td_headerandpost > table > tbody > tr > "
                                                                       "td:nth-child(2) > div.smalltext")
        post_content_element = post_element.find_element(By.CSS_SELECTOR, "div.post")
        post_title_element = post_element.find_element(By.CSS_SELECTOR, "div.subject > a")
        post_id_element = post_element.find_element(By.CSS_SELECTOR, "a.message_number")
        post_url = post_id_element.get_attribute("href")

        if username_element and post_date_element and post_content_element and post_title_element and post_id_element:
            return {
                "Username": username_element.text,
                "PostDate": post_date_element.text,
                "PostContent": post_content_element.text,
                "PostTitle": post_title_element.text,
                "PostID": post_id_element.text.strip("#"),
                "PostURL": post_url
            }
        else:
            print("One or more elements not found in post.")
            return None

    except NoSuchElementException as e:
        #print(f"Error extracting data from post element: {e}")
        return None


def extract_posts_from_page(driver):
    table = driver.find_element(By.XPATH, '//*[@id="quickModForm"]/table[1]')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    all_post_data = []
    for post in rows:
        post_data = extract_post_data(post)
        all_post_data.append(post_data)
    return all_post_data

chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service('/Users/dianavieirafernandes/Desktop/chromedriver_mac64/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://bitcointalk.org/index.php?topic=20333.0')

all_data = []

page_num = 0

while True:
    page_data = extract_posts_from_page(driver)
    all_data.extend(page_data)

    try:
        next_page_num = page_num + 1
        next_page_link = driver.find_element(By.XPATH, f"//td[@class='middletext']//a[contains(text(), '{next_page_num}')]")
        if next_page_link:
            next_page_link.click()
            page_num += 1
            print("Navigating to page", page_num)
        else:
            print("No more pages found.")
            break
    except NoSuchElementException:
        print("No more pages found.")
        break

driver.quit()
df = pd.DataFrame([d for d in all_data if d is not None])

print(df)

df.to_csv('bitcointalk_forum_data.csv', index=False)
