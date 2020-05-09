from indeed import get_indeed_jobs
from stackoverflow import get_stackoverflow_jobs
from save import save_to_file

indeed_jobs = (get_indeed_jobs())
so_jobs = (get_stackoverflow_jobs())

# put your data
save_to_file(so_jobs)