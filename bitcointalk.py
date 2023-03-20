import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service('/Users/dianavieirafernandes/Desktop/chromedriver_mac64/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://bitcointalk.org/index.php?board=1.0')

columns = ['Subject', 'Link', 'Started by', 'Replies', 'Views', 'Last post']
df = pd.DataFrame(columns=columns)

page_num = 1
while True:
    wait = WebDriverWait(driver, 20)
    topics_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.bordercolor")))

    topics = driver.find_elements(By.CSS_SELECTOR, "tr:not(.headercolor)")

    for topic in topics:
        try:
            subject = topic.find_element(By.XPATH, ".//td[3]/span/a").text
            link = topic.find_element(By.XPATH, ".//td[3]/span/a").get_attribute("href")
            started_by = topic.find_element(By.XPATH, ".//td[4]/a").text
            replies = topic.find_element(By.XPATH, ".//td[5]").text
            views = topic.find_element(By.XPATH, ".//td[6]").text
            last_post = topic.find_element(By.XPATH, ".//td[7]").text
        except NoSuchElementException:
            # Skip the row if any element is not found
            continue

        new_row = pd.DataFrame({
            'Subject': [subject],
            'Link': [link],
            'Started by': [started_by],
            'Replies': [replies],
            'Views': [views],
            'Last post': [last_post]
        })

        df = pd.concat([df, new_row], ignore_index=True)

        print("Subject:", subject)
        print("Link:", link)
        print("Started by:", started_by)
        print("Replies:", replies)
        print("Views:", views)
        print("Last post:", last_post)
        print("-------------------------")

    time.sleep(5)

    try:
        page_link = driver.find_element(By.XPATH, f"//td[@class='middletext']//a[contains(text(), '{page_num + 1}')]")
        if page_link:
            page_link.click()
            page_num += 1
            print("Navigating to page", page_num)
        else:
            print("No more pages found.")
            break
    except NoSuchElementException:
        print("No more pages found.")
        break

driver.quit()
df.to_csv("bitcointalk_data.csv", index=False)

#use 
#caffeinate -i /Users/dianavieirafernandes/PycharmProjects/pythonProject1 caffeinate command while running this script to prevent your Mac from going to sleep
