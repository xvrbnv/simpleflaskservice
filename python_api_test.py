import requests
r = requests.get('http://0.0.0.0:9876/talkingparrot')
print('Python API Test Status Code: ' + str(r.status_code))
print('Python API Test Get Request Response Text: ' + (r.text))
