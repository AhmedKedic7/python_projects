from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def grab_links(browser):
    links = []

    rows = browser.find_elements(By.CSS_SELECTOR, "#docsDataTable tbody tr")
    for row in rows:
        link_element = row.find_element(By.TAG_NAME, 'a')
        href_value = link_element.get_attribute('href')
        links.append(href_value)

    return links

# Start the webdriver
browser = webdriver.Firefox()
browser.get('https://juntasupervision.pr.gov/documents/')

# Set display to 100 rows per page
dropdown = browser.find_element(By.CSS_SELECTOR, "#docsDataTable_length select")
dropdown.click()
option_100 = browser.find_element(By.CSS_SELECTOR, "#docsDataTable_length option:nth-child(5)")
option_100.click()

links = []

# Get the last pagination link's text to determine the final page
last_page_element = browser.find_element(By.CSS_SELECTOR, ".paginate_button.last")
last_page_text = last_page_element.text
last_page = int(last_page_text) if last_page_text else 1

# Loop through pages
for _ in range(1, last_page + 1):
    links.extend(grab_links(browser))
    next_button = browser.find_element(By.ID, "docsDataTable_next")
    next_button.click()
    time.sleep(2)  # Adding a delay for the page to load

print(f"Total links collected: {len(links)}")
for link in links:
    print(link)
