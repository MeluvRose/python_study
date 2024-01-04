from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=options)
base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"


results = []
response = browser.get(f"{base_url}{search_term}&limit=50")
soup = BeautifulSoup(browser.page_source, "html.parser")
# job_list = soup.find("ul", class_="jobsearch-ResultsList")
job_list = soup.find("ul", class_="eu4oa1w0")
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        # h2 = job.find("h2", class_="jobTitle")
        # anchor = h2.find("a")
        anchor = job.select_one("h2 a")
        title = anchor["aria-label"][:-10]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "link": f"https://kr.indeed.com{link}",
            "company": company.string,
            "location": location.string,
            "position": title,
        }
        results.append(job_data)

for result in results:
    print(result, "\n//////\n///////")
