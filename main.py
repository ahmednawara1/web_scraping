#webscraping

from bs4 import BeautifulSoup
import requests
import time

# import html from a website

print('put some skills u r not familiar with')
unfamiliar_skill = input('>')
print(f'filtring out {unfamiliar_skill}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/ {index}.txt', 'w') as f:
                    f.write(f'company name: {company_name.strip()} \n')
                    f.write(f'skills: {skills.strip()} \n')
                    f.write(f'more_info: {more_info} \n')
                print(f'file saved {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
