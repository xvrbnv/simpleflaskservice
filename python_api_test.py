import requests
r = requests.get('http://0.0.0.0:9876/talkingparrot')
print(r.status_code)
print(r.text)
