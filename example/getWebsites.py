from requests import get

websites = (
    "google.com",
    "naver.com",
    "https://twitter.com",
    "facebook.com",
    "https://youtube.com",
)

result = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    # print(response.status_code)
    status = response.status_code
    if (status / 100) == 2:
        # print(f"{website} is OK")
        result[website] = "OK"
    elif (status / 100) == 3:
        result[website] = "MAYBE REDIRECT"
    else:
        # print(f"{website} is not OK")
        result[website] = "FAILED"

print(result)
