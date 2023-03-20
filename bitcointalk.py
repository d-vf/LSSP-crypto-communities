from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver',options=chrome_options)
# Call url through selenium driver
# navigate to Bitcoin Discussion board
driver.get('https://bitcointalk.org/index.php?board=1.0')

# wait for page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bordercolor')))

# initialize empty dataframe to store post data
columns = ['Subject', 'Started by', 'Replies', 'Views', 'Last post']
df = pd.DataFrame(columns=columns)

# loop through pages
page_num = 1
while True:
    # find table element containing post data
    table_element = driver.find_element(By.CSS_SELECTOR, 'table.bordercolor')

    # find all rows in table
    rows = table_element.find_elements(By.TAG_NAME, 'tr')

    # loop through rows and extract data for each post
    for row in rows:
        # skip header row
        if row.get_attribute('class') == 'titlebg':
            continue

        # extract data from columns
        subject_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3) span.subject a')
        started_by_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4) a')
        replies_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)')
        views_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)')
        last_post_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7) span small')

        subject = subject_element.text
        started_by = started_by_element.text
        replies = replies_element.text
        views = views_element.text
        last_post = last_post_element.text

        # add data to dataframe
        data = {'Subject': subject, 'Started by': started_by, 'Replies': replies, 'Views': views, 'Last post': last_post}
        df = df.append(data, ignore_index=True)

    # check if there is a next page
    next_button = driver.find_element(By.CSS_SELECTOR, 'div.pagesection span.next a')
    if 'disabled' in next_button.get_attribute('class'):
        break

    # navigate to next page
    page_num += 1
    driver.get(f'https://bitcointalk.org/index.php?board=1.{20*page_num}')

# close driver
driver.quit()

# print dataframe
print(df)