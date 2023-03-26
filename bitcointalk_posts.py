import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

service = Service('/Users/dianavieirafernandes/Desktop/chromedriver_mac64/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://bitcointalk.org/index.php?topic=5428062.20')

# create a list to store the data
data = []

# Find all title_selector elements on the page
table = driver.find_element(By.XPATH, '//*[@id="quickModForm"]/table[1]')
rows = table.find_elements(By.TAG_NAME, 'tr')
# print the rows
for i, row in enumerate(rows, start=1):
    data.append((i, row.text))
    print(f"Row {i}: {row.text}")

page_num = 1
while True:
    try:
        page_num += 1
        page_link = driver.find_element(By.XPATH, f"//td[@class='middletext']//a[contains(text(), '{page_num}')]")
        if page_link:
            page_link.click()
            print("Navigating to page", page_num)
            table = driver.find_element(By.XPATH, '//*[@id="quickModForm"]/table[1]')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for i, row in enumerate(rows, start=i):
                print(f"Row {i+1}: {row.text}")


        else:
            print("No more pages found.")
            break
    except NoSuchElementException:
        print("No more pages found.")
        break

df = pd.DataFrame(data, columns=['index', 'text'])
df.to_csv("output111.csv", index=False)
# Quit the driver
driver.quit()
