import re
from urllib.parse import urlparse

print("=" * 50)
print("AI Suspicious URL Detector")
print("=" * 50)

shorteners = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "is.gd"
]

def check_url(url):
    score = 0

    if len(url) > 75:
        score += 1

    if url.count(".") > 3:
        score += 1

    if "@" in url:
        score += 2

    if "-" in url:
        score += 1

    if not url.startswith("https://"):
        score += 1

    for s in shorteners:
        if s in url:
            score += 2

    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        score += 3

    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"

while True:
    url = input("\nEnter URL: ")

    if url.lower() == "exit":
        break

    print("\nRisk Level:", check_url(url))