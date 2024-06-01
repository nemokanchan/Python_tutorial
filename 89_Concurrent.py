import concurrent.futures
import requests

def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")
    

url="https://picsum.photos/id/1/2000/3000"

with concurrent.futures.ProcessPoolExecuter() as executor:
    l1=[url for i in range(13)]
    l2=[i for i in range(13)]
    results=executor.map(downloadFile, l1, l2)
    for r in results:
        print(r)