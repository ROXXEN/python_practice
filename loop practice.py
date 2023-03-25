from requests import get

websites = [
    'google.com',
    'airbnb.com',
    'https://twitter.com',
    'facebook.com',
    'https://tiktok.com',
    'httpstat.us/101',
    'httpstat.us/200',
    'httpstat.us/300',
    'httpstat.us/400',
    'httpstat.us/500'
]
results = {}

for website in websites:
    if not website.startswith('https://'):
        website = f"https://{website}"
    response = get(website)
    response_number = response.status_code
    if response_number >= 100 and response_number < 200:
        results[website] = 'Server recive'
    elif response_number >= 200 and response_number < 300:
        results[website] = 'OK'
    elif response_number >= 300 and response_number < 400:
        results[website] = 'is Redirection'
    elif response_number >= 400 and response_number < 500:
        results[website] = 'is Bad Request'
    elif response_number >= 500:
        results[website] = 'Server is Down'
print(results)
