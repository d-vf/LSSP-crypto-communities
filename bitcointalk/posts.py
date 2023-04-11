import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def configure_driver():
    service = Service('/Users/dianavieirafernandes/Desktop/chromedriver_mac64/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def extract_rows_from_table(driver):
    table = driver.find_element(By.XPATH, '//*[@id="quickModForm"]/table[1]')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    return rows

def main():
    driver = configure_driver()
    driver.get('https://bitcointalk.org/index.php?topic=5428062.20')

    data = []

    page_num = 1
    while True:
        rows = extract_rows_from_table(driver)

        for i, row in enumerate(rows, start=len(data) + 1):
            data.append((i, row.text))
            print(f"Row {i}: {row.text}")

        try:
            page_num += 1
            page_link = driver.find_element(By.XPATH, f"//td[@class='middletext']//a[contains(text(), '{page_num}')]")
            if page_link:
                page_link.click()
                print("Navigating to page", page_num)
            else:
                print("No more pages found.")
                break
        except NoSuchElementException:
            print("No more pages found.")
            break

    df = pd.DataFrame(data, columns=['index', 'text'])
    df.to_csv("output111.csv", index=False)
    driver.quit()
