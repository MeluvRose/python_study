from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"
