from bs4 import BeautifulSoup
import requests
x = input("Enter str : ")
url  = "https://www.merriam-webster.com/thesaurus/'{}'".format(x)
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
a = "Essay"
li_tag = doc.find_all("li")
print(li_tag)