
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()

options.add_experimental_option("detach", True)  # Chorme Browser 자동 종료 방지
browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    browser.get(f'{base_url}{keyword}')
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagenation = soup.find("nav", class_="ecydgvn0")
    pages = pagenation.find_all("div", class_="ecydgvn1", recursive=False)

    if len(pages) == 0:
        return 1
    elif len(pages) < 5:
        count = len(pages)
        return count
    elif len(pages) >= 5:
        count = 0
        page_list = 5
        while page_list >= 5 and count <= 9:
            base_url = 'https://kr.indeed.com/jobs?'
            final_url = (f'{base_url}q={keyword}&start={count*10}')
            browser.get(final_url)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            pagenation = soup.find("nav", class_="ecydgvn0")
            pages = pagenation.find_all(
                "div", class_="ecydgvn1", recursive=False)
            page_list = len(pages)
            count += 1
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        base_url = 'https://kr.indeed.com/jobs?'
        final_url = (f'{base_url}q={keyword}&start={page*10}')
        print(f"Request to {final_url}")
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            zone = job.find('div', class_="mosaic-zone")
            if zone == None:
                h2 = job.find("h2", class_="jobTitle")
                anchor = job.select_one("h2 a")
                position = anchor['aria-label'].replace(",", " ")
                link = f"https://kr.indeed.com{anchor['href']}".replace(
                    ",", " ")
                company = job.find(
                    "span", class_="companyName").text.replace(",", " ")
                location = job.find(
                    "div", class_="companyLocation").text.replace(",", " ")
                job_data = {
                    "link": link,
                    "company": company,
                    "position": position,
                    "location": location,
                }
                results.append(job_data)
    return results
