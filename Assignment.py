import requests
import json

url = "https://en.wikipedia.org/w/api.php?action=opensearch&namespace=0&limit=1&format=json&search="
Search_String = input("Enter the string to be searched : ")
Search_String = Search_String.strip()
url = url + Search_String
url = '_'.join(url.split(' '))
response = requests.request("GET", url,)
outputfile = open("results.txt", "a")
try:
    print("####                   (33%)\r", end = ' ')
    time.sleep(1)
    print("############           (66%)\r", end = ' ')
    time.sleep(1)
    print("##################     (100%)\r")
    outputfile.write(response.json()[3][0]+"\n")
except:
    print("Not found")
    f.write("Not found\n")

outputfile.close()
