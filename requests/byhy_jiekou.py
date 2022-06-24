import requests

# proxies = {
#   'http': 'http://127.0.0.1:8888',
#   'https': 'http://127.0.0.1:8888',
# }

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {
    'username': 'byhy',
    'password': '88888888'
}
r = requests.post('http://127.0.0.1/api/mgr/signin',
                  data=payload,
                  headers=headers)
                  #proxies=proxies)
print(r.json())



