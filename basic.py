import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"test": 1234}, json={"query": " HEllo there"})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
