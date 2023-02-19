from bs4 import BeautifulSoup
import requests
import time


def job_posts(unfamiliar_skill):
    content = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0').text

    soup = BeautifulSoup(content, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").text
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skill = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skill:
                with open(f'Posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skill Required: {skill.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f"File save: {index}")


if __name__ == "__main__":
    while True:
        print("Enter a Skill that you are not familiar with:")
        unfamiliar_skill = input("> ")
        print(f"Filteringout skill {unfamiliar_skill}")
        job_posts(unfamiliar_skill)
        time_wait = 10
        print(f"Wait {time_wait} seconds")
        time.sleep(time_wait * 60)
