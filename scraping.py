from bs4 import BeautifulSoup
import requests
import json

url = "https://www.home.ge/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="new_listing_status")

for listing in lists:
    title = listing.find('li', class_="title").text
    price = listing.find('li', class_="two-inline price_tag").text
    location = listing.find('span', {'id': 'flf_277414_mdebareoba'}).text
    area = listing.find('span', class_="square_feet").text
    bedroom = listing.find('span', class_="badrooms").text
    bathroom = listing.find('span', class_="bathrooms").text
    img = listing.find('a', href="https://www.home.ge/saxlebi-agarakebi/qiravdeba-saxlebi-agarakebi/qiravdeba-sakhli-natakhtari-277414.html").find('img')['src']
    info = [title, price, location, area, bedroom, bathroom, img]
    print(info)
    break

property_info = {
    'title': title,
    'two-inline price_tag': price,
    'flf_277414_mdebareoba': location,
    'square_feet': area,
    'badrooms': bedroom,
    'bathrooms': bathroom
}

with open('property_info.json', 'w') as file:
    json.dump(property_info, file, indent=6)





   