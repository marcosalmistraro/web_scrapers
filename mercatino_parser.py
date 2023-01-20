import csv
import requests
from bs4 import BeautifulSoup

file = open("mercatino.csv", "w", encoding='utf8')
writer = csv.writer(file)
writer.writerow(['Instrument', 'Price', 'Location', 'Time', 'Description'])

page_number = 1
url = "https://www.mercatinomusicale.com/mm/s_synth-a-tastiera-modulari_rp1-ct1-pg" + str(page_number) + ".html"

# range of page numbes set to url's standard
for page_number in range(26):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id='search_list')

    instruments = results.find_all('div', class_='ann')
    infos = results.find_all('div', class_='inf')
    users = results.find_all('div', class_='usr')
    others = results.find_all('div', class_='item pri')

    names = []
    descriptions = []
    prices = []
    locations = []
    times = []
    links = []

    for instrument in instruments:
        name = instrument.find('a').text
        description = instrument.find('p').text
        names.append(name)
        descriptions.append(description)

    for info in infos:
        price = info.find('span', class_="prz").text
        prices.append(price)

    for user in users:
        location = user.find('span', class_="prv")
        if location != None:
            locations.append(location.text)
        else:
            locations.append("")
        time = user.find('span', class_="data").text
        times.append(time)

    for item in others:
        link = "mercatinomusicale.com" + item.find('a', href=True)['href']
        links.append(link)

    for i in range(len(names)):
        writer.writerow([names[i],
                        prices[i],
                        times[i],
                        locations[i],
                        descriptions[i]])
    
    page_number += 1
    
file.close()
print("File closed")