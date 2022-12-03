'''webscraping'''
import csv
from bs4 import BeautifulSoup
import requests
filecsv = open('job_posts.csv', 'w', encoding='utf8')
csv_columns = ['company name', 'skills', 'job link', 'published_date']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
# import html from the website
URL = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence='
for page in range(1, 51, 1):
    html_text = requests.get(URL + str(page), timeout=10).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(f'scraping page number {page}')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').text.strip()
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href'].strip()
        writer.writerow({'company name': company_name, 'skills': skills,
                        'job link': more_info, 'published_date': published_date})
print('file saved')
