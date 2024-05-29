import time
import asyncio
import requests

url="https://instagram.com/favicon.ico"
response=requests.get(url)
open("instagram.ico","wb").write(response.content)
async def function1():
    url="https://instagram.com/favicon.ico"
    response=requests.get(url)
    open("instagram.ico","wb").write(response.content)
    print("func 1")
    return "kanxu"

async def function2():
    url="https://instagram.com/favicon.ico"
    response=requests.get(url)
    open("instagram.ico","wb").write(response.content)

    print("func 2")
    
    
async def function3():
    url="https://instagram.com/favicon.ico"
    response=requests.get(url)
    open("instagram.ico","wb").write(response.content)
    print("func 2")

async def main():
    l=await asyncio.gahter(function1(),function2(),function3())
    print(l)
    
