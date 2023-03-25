from requests import get, status_codes

websites = [
    'google.com',
    'airbnb.com',
    'https://twitter.com',
    'facebook.com',
    'https://tiktok.com'
]
results = {}

for website in websites:
    if not website.startswith('https://'):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 200 and response.status_code < 300:
        results[website] = 'OK'
    elif response.status_code >= 300 and response.status_code < 400:
        results[website] = 'is Redirection'
    elif response.status_code >= 400 and response.status_code < 500:
        results[website] = 'is Bad Request'
    elif response.status_code >= 500:
        results[website] = 'Server is Down'
print(results)
