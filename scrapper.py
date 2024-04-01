from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

# Initialize an empty DataFrame to store the scraped data
df = pd.DataFrame(columns=['Accession', 'Name', 'Species', 'Gene'])

# Configure Selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)  # Implicit wait to handle dynamic page elements

# URL of the page
url = 'https://www.ebi.ac.uk/interpro/api//protein/UniProt/entry/pfam/PF00704/?page_size=100'
driver.get(url)

my_variable = driver.find_element(by=By.CLASS_NAME, value="nocode")
my_variable.get_attribute("innerHTML")
print(my_variable.get_attribute("innerHTML"))


# # Function to extract display-start and display-end values from HTML
# def extract_display_values(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     nightingale_sequence = soup.find('nightingale-sequence')
#     if nightingale_sequence:
#         display_start = nightingale_sequence.get('display-start', 'Not Available')
#         display_end = nightingale_sequence.get('display-end', 'Not Available')
#         return f"{display_start} - {display_end}"
#     else:
#         return "Not Available"

# # Function to scrape table data from the current page
# def scrape_table():
#     # Find all rows in the table body
#     rows = driver.find_elements(By.XPATH, "//tbody/tr")
#     for row in rows:
#         # Extract data from each column of the row
#         cells = row.find_elements(By.TAG_NAME, "td")
#         accession = cells[0].text.strip()
#         name = cells[1].text.strip()
#         species = cells[2].text.strip()
#         gene = cells[3].text.strip()
#         # matches_element = cells[4].find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
#         # matches = extract_display_values(matches_element)
#         # Append the row data to the DataFrame
#         df.loc[len(df)] = [accession, name, species, gene]


# ## Function to click on the next page button
# def click_next_page():
#     try:
#         # Wait for overlay to disappear
#         WebDriverWait(driver, 10).until(
#             EC.invisibility_of_element_located((By.XPATH, "//div[@class='overlay']"))
#         )
#         next_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[text()='Next']"))
#         )
#         next_button.click()
#         time.sleep(2)
#     except Exception as e:
#         print(f"Error clicking next page button: {e}")


# # Scrape data from the first page
# scrape_table()

# Check if there is pagination
# while True:
#     try:
#         # Scrape data from the current page
#         click_next_page()
#         scrape_table()
#     except NoSuchElementException:
        # break  # Exit the loop if the "Next" button is not found (no more pages)

# Close the driver
driver.quit()

# Display the scraped data
print(df)
