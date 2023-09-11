import requests
from bs4 import BeautifulSoup
import csv

# List of URLs to visit
urls = ["example.com/link1, example.com/link2, example.com/link3"]


# Function to extract the "About" field and full HTML contents from a single webpage
def extract_data_from_page(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Extract the "About" field from the webpage using BeautifulSoup
  about = soup.find(string="About:").find_next().text
  # html_content = str(soup)

  # return {"About": about, "HTML Content": html_content}
  return {"About": about, "URL": url}


# Create a new CSV file at the root with column names
with open("output.csv", "w", newline='') as csvfile:
  # fieldnames = ["About", "HTML Content"]
  fieldnames = ["About", "URL"]
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  # Crawl the list of webpages and extract the data
  for url in urls:
    try:
      data = extract_data_from_page(url)
      writer.writerow(data)
    except Exception as e:
      print(f"Error processing {url}: {e}")
