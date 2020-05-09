import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"


def extract_stackoverflow_pages():
    stackoverflow_result = requests.get(URL)
    soup = BeautifulSoup(stackoverflow_result.text, "html.parser")

    page_list = soup.find("div", class_="s-pagination").find_all("a", class_="s-pagination--item")

    pages = []
    for i in page_list[:-2]:
        page = int(i.find("span").string)
        pages.append(page)

    max_page = pages[-1]

    return max_page


def extract_stackoverflow_jobs(max_page):
    jobs = []

    # 각 페이지마다 crawling을 합니다.
    for i in range(max_page):
        page = i + 1
        print(f"Scrapping stackoverflow page : {page}")
        # print(f"Scrapping stackoverflow page: {page}")
        result = requests.get(f"{URL}&pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")

        job = soup.find_all("div", {"class": "-job"})

        for k in job:

            # 제목 추출
            pre_title = k.find("a", {"class": ["s-link", "stretched-link"]})
            if pre_title is not None:
                title = pre_title.string

            # 로케이션 추출
            pre_location = k.find("h3", {"class": "mb4"}).find("span", {"class": "fc-black-500"})
            if pre_location is not None:
                location = pre_location.string.strip()

            # 회사 추출
            pre_company = k.find("h3", {"class": "mb4"}).find("span")
            if pre_company is not None:
                company = pre_company.string.strip()

            # 링크 추출
            pre_link = k["data-jobid"]
            if pre_link is not None:
                link = "https://stackoverflow.com/jobs/" + pre_link

            jobs.append({"title": title, "location": location, "company": company, "link": link})

    return jobs


def get_stackoverflow_jobs():
    jobs = extract_stackoverflow_jobs(extract_stackoverflow_pages())
    return jobs
