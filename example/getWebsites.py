from requests import get

websites = (
    "google.com",
    "naver.com",
    "https://twitter.com",
    "facebook.com",
    "https://youtube.com",
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response.status_code)
