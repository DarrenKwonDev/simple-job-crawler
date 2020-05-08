from indeed import extract_indeed_pages, extract_indeed_jobs

max_indeed_pages = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(max_indeed_pages)

print(indeed_jobs)