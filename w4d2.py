"""

APIs Part 2
● JSON data parsing
● Extracting specific data from API responses
● Practice: Fetch and display data from public API

"""
import json

data = '{"name": "Ali", "age": 22, "city": "Lahore"}'

parsed_data = json.loads(data)

print(parsed_data["name"])
print(parsed_data["age"])
print(parsed_data["city"])

"""import json
with open("C:\\Users\\Chaudhary Computers\\Desktop\\Daily Task part-4\\data.json","r") as file:
    data = json.load(file)

print(data["product"])
print(data["price"])
print(data["stock"])
"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(user["name"], "-", user["email"])

import json

person = {
    "name": "Sara",
    "age": 25
}
data = json.dumps(person)
print(data)

import json

data = '{"name":"Hassan","skills":["Python","API","JSON"]}'
d = json.loads(data)
print(d["skills"])

import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

for post in data:
    print(post["title"])
    if response.status_code==200:
        data=response.json()
    else:
        print("Failed to Fetch data")

#practice
import requests
# API URL (Free test API)
URL = "https://jsonplaceholder.typicode.com/users"

def fetch_api_data():
    """Fetch data from API"""
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()   # JSON → Python list/dict
    else:
        print("Failed to fetch data")
        return []
def extract_names(data):
    print("\n--- User Names ---")
    for user in data:
      print(user["name"])

api_data = fetch_api_data()
extract_names(api_data)
       


import requests
URL = "https://jsonplaceholder.typicode.com/users"
def fetch_api_data():
    """Fetch data from API"""
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()   # JSON → Python list/dict
    else:
        print("Failed to fetch data")
        return []

def extract_emails(data):
    emails= [user['email'] for user in data]
    print(emails)
def main():
    data = fetch_api_data()

    if not data:
            return
    extract_emails(data)

if __name__ == "__main__":
    main()


import requests
URL = "https://jsonplaceholder.typicode.com/users"
def fetch_api_data():
    """Fetch data from API"""
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()   # JSON → Python list/dict
    else:
        print("Failed to fetch data")
        return []

def extract_nested_city(data):
    """Extract nested city data"""
    print("\n--- Name & City ---")
    for user in data:
        print(user["name"], "-", user["address"]["city"])

def main():
    data = fetch_api_data()

    if not data:
            return
    extract_nested_city(data)

if __name__ == "__main__":
    main()

