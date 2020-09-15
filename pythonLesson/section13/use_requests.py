import requests

payload = {"key1": "value1", "key2": "value2"}


url = "http://httpbin.org"


# get
r = requests.get(url + "/get", params=payload)

print(r.status_code)
print(r.text)
print(r.json())

# post
r = requests.post(url + "/post", data=payload)

print(r.status_code)
print(r.text)
print(r.json())


# put
r = requests.put(url + "/put", data=payload)

print(r.status_code)
print(r.text)
print(r.json())


# delete
r = requests.delete(url + "/delete", data=payload)

print(r.status_code)
print(r.text)
print(r.json())


# timeout
r = requests.get(url + "/get", data=payload, timeout=0.0001)  # second

print(r.status_code)
print(r.text)
print(r.json())

