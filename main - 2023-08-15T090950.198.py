import requests
from bs4 import BeautifulSoup

# Specify the URL of the MLS website's search results page for new homes in Maui
url = "https://example-mls-website.com/search?location=Maui&type=new_home"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the listings on the page
listings = soup.find_all("div", class_="listing")

# Loop through each listing and extract relevant information
for listing in listings:
    address = listing.find("h2", class_="address").text
    price = listing.find("span", class_="price").text
    details = listing.find("p", class_="details").text
    
    print(f"Address: {address}")
    print(f"Price: {price}")
    print(f"Details: {details}")
    print("=" * 40)
