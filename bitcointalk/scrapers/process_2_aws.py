import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import os


def extract_post_data(post_element, url):
    try:
        username_element = post_element.find_element(By.CSS_SELECTOR, "td.poster_info > b > a")
        post_date_element = post_element.find_element(By.CSS_SELECTOR, "td.td_headerandpost > table > tbody > tr > "
                                                                       "td:nth-child(2) > div.smalltext")
        post_content_element = post_element.find_element(By.CSS_SELECTOR, "div.post")
        post_title_element = post_element.find_element(By.CSS_SELECTOR, "div.subject > a")
        post_id_element = post_element.find_element(By.CSS_SELECTOR, "a.message_number")
        post_url = post_id_element.get_attribute("href")

        if username_element and post_date_element and post_content_element and post_title_element and post_id_element:
            post_id = url + "#" + post_id_element.text.strip("#")
            return {
                "PostID": post_id,
                "Username": username_element.text,
                "PostDate": post_date_element.text,
                "PostContent": post_content_element.text,
                "PostTitle": post_title_element.text,
                "PostURL": post_url
            }
        else:
            print("One or more elements not found in post.")
            return None

    except NoSuchElementException as e:
        # print(f"Error extracting data from post element: {e}")
        return None


def extract_posts_from_page(driver, url):
    table = driver.find_element(By.XPATH, '//*[@id="quickModForm"]/table[1]')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    all_post_data = []
    for post in rows:
        post_data = extract_post_data(post, url) # pass url parameter here
        if post_data:
            post_data['URL_Source'] = url
        all_post_data.append(post_data)
    return all_post_data



chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service('/usr/local/bin/chromedriver')


list_posts = pd.read_csv('/home/ec2-user/bitcointalk_data.csv')

# Extract the links from 10,000 to 20,000 from the DataFrame
url_list = list_posts['Link'].iloc[30001:40000].tolist()

for url in url_list:
    all_data = []
    start_time = time.time()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    page_num = 0

    while True:
        page_data = extract_posts_from_page(driver, url)
        all_data.extend(page_data)

        try:
            next_page_num = page_num + 1
            next_page_link = driver.find_element(By.XPATH,
                                                 f"//td[@class='middletext']//a[contains(text(), '{next_page_num}')]")
            if next_page_link:
                next_page_link.click()
                page_num += 1
                print(f"Navigating to page {page_num} of {url}")
        except NoSuchElementException:
            break

    driver.quit()

    df = pd.DataFrame([d for d in all_data if d is not None])
    df.drop_duplicates(subset=['PostID'], keep='first', inplace=True)

    # replace '.' with '_' in file name
    #output_file_name = url.split('=')[1].replace('.', '_')

    output_folder = "/home/ec2-user/output_data/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder,exist_ok=True)

    # replace '.' with '_' in file name and add folder path
    output_file_name = output_folder + url.split('=')[1].replace('.', '_') + ".csv"

    # write DataFrame to CSV file in the output folder
    df.to_csv(output_file_name, index=False)

    # write DataFrame to CSV file
    #df.to_csv(f"{output_file_name}.csv", index=False)

    elapsed_time = time.time() - start_time
    print(f"Processed {len(all_data)} posts from {url} in {elapsed_time:.2f} seconds.")

