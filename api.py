import pip._vendor.requests as requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1"

data = requests.get(url)

response = data.json()

for k in response:
    print(k)



