"""

APIs Part 1
● HTTP requests concept
● Install requests library (pip install requests)
● GET requests to free APIs

"""

import requests
response=requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()
print(data)
print(response.text)
print(response.status_code)




import requests
response=requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()
print(data)




import requests
response=requests.get("https://official-joke-api.appspot.com/random_joke")
print(response.status_code)




import requests
response=requests.get("https://official-joke-api.appspot.com/random_joke")
print(response.text)





import requests
url= "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)
users=r.json()
for user in users:
    print(user["name"],"-",user["email"])



import requests
url="https://jsonplaceholder.typicode.com/users"
a= requests.get(url)
users = a.json()



for user in  users :
    print(user["name"],"-", user["email"])
    print(a.status_code)
    import requests

url = "https://api.github.com/users/octocat"

respond = requests.get(url)

print(respond.status_code)
print("data in text form")
print(respond.text,"\n")


print()
print("-"*40)



if respond.status_code ==200:
    data =  respond.json()
else:
    print("Request failed!")


print("Data after using json format")
print(data,"\n")

print("Accessing specific data from whole data")
print("login ",data["login"])

print("name ",data["name"])

print("email ",data["email"])

print("followers ",data["followers"],"\n")


print()
print("-"*40)




url =  "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code==200:
    data = response.json()
else:
    print("Request failed!")


print("Post with id : 1")

post_id_1 = [post for post in data if post['id']==1]
print(post_id_1,"\n")

print("print all posts one by one ")
for post in data:
    print(post)


print()
print("-"*40)



url =   "https://www.google.com"

response = requests.get(url)

if response.status_code==200:
    print(response.text)
else:
    print("Request failed!")

print()
print("-"*40)



url = "https://www.codewithharry.com/courses"

try:
    response = requests.get(url, timeout=5)
    data = response.text
    print(data)   
    
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)


import requests
url = "https://www.codewithharry.com/courses"
r = requests.get("https://www.codewithharry.com/courses")
print(r.text)

