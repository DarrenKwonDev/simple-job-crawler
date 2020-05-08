import requests
from bs4 import BeautifulSoup

INDEED_URL = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50'


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
