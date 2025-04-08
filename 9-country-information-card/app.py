import requests
response = requests.get("https://restcountries.com/v3/all")
print(response)

response = requests.get("https://restcountries.com/v3/name/turkey")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)