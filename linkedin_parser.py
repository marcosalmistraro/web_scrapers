import csv
import requests
from bs4 import BeautifulSoup

def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']

        writer.writerow([
            job_title,
            job_company,
            job_location,
            job_link
            ])
    
    if page_number < 200:
        page_number = page_number + 25
        soup = linkedin_scraper(webpage, page_number)
    else:
        file.close()
        print('File closed')

webpage = "https://www.linkedin.com/jobs/search?keywords=engineer&location=Bruxelles%2C%20Bruxelles-Capitale%2C%20Belgio&geoId=100432943&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start="

file = open('linkedin-jobs.csv', 'a', encoding='utf8')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'Apply'])

linkedin_scraper(webpage, 0)