import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def extract_indeed_pages():
    indeed_results = requests.get(INDEED_URL)

    # 파싱해줍니다.
    soup = BeautifulSoup(indeed_results.text, 'html.parser')

    # 몇 페이지인지 체크한 후 해당 페이지의 url을 얻습니다.
    pagination = soup.find("div", class_="pagination")
    lists = pagination.find_all("a")
    pages = []  # 여기에 각 페이지가 담깁니다.

    for page in lists[:-1]:
        pages.append(int(page.find("span").string))

    max_page = max(pages)  # 가장 높은 숫자의 페이지입니다.

    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{INDEED_URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = (soup.find_all("div", class_="jobsearch-SerpJobCard"))
        print(f"{INDEED_URL}&start={page * LIMIT}")
        # print(results)
        for result in results:
            title = result.find("a", class_="jobtitle")["title"]
            location = result.find("span", class_="location").string
            if result.find("div", class_="sjcl").find("span", class_="company").string is None:
                break
            company = result.find("div", class_="sjcl").find("span", class_="company").string.strip()
            if company is None:
                company = result.find("div", class_="sjcl").find("span", class_="company").find("a").string.strip()
            jobs.append({"title": title, "company": company, "location": location})
            print(jobs)
    return jobs


