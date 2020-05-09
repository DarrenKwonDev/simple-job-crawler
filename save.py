import csv

def save_to_file(jobs):
    # 같은 경로에 있는 job.csv를 엽니다. 없으면 job.csv를 만듭니다.
    file = open("job.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    for job in jobs:
        # js처럼 job.title과 같이 직접 빼서 쓸 수 없습니다.
        # list로 하지 않으면 dict_values 라는 자료형으로 나옵니다. list로 변환합시다.
        writer.writerow(list(job.values()))