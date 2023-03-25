from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='
serch_term = 'python'

response = get(f'{base_url}{serch_term}')
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    print(len(jobs))
    for job_sections in jobs:
        job_posts = job_sections.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            print(post)
            print('-----------------------------')
