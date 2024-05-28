#First of all install request module
#by giving command in command promt as, pip install request
import requests
response= requests.get("https://www.google.com")
print(response.text)#In response we get code of google

url="https://jsonplaceholder.typicode.com/posts"
data={
    "title": 'Kanchan',
    "body": 'sis',
    "userId": 3,
  }
headers= {
    'Content-type': 'application/json; charset=UTF-8',
  }

response=requests.post(url,headers=headers,json=data)

print(response.text)