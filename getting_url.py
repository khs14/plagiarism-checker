import urllib.request 
from bs4 import BeautifulSoup



def read_url(url):
    html = urllib.request.urlopen(url)
    htmlParse = BeautifulSoup(html, 'html.parser')
    url_text = ""
    for para in htmlParse.find_all("p"):
        url_text = url_text + para.get_text()
    url_text = url_text.lower()
    file_list = url_text.split()
    conjunctions = ['after','although','as','because', 'before', 
    "for","if","since","unless",
    "until","when","whenever","where","wherever",'while','is',
    'a','the','an','of','to','that','on','are','but','and','from','also','the','so']
    try:
        for i in (file_list):
            for m in conjunctions:
                if(m==i):
                    file_list.remove(i)
    except Exception:
            pass
    file_string_new = ""
    for j in file_list:
        file_string_new = file_string_new + j + " "
    
    return file_string_new

