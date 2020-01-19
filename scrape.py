import requests
from bs4 import BeautifulSoup
import urllib.request

def makesoup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup

def dl_img(url,file_name):
    full_path = file_name + '.png'
    urllib.request.urlretrieve(url,full_path)

#designed to take only one author as input


filename=input("Enter input text file : ")
file1 = open(filename,"r")
stri = file1.read()
str1 = stri.split()
print(str1)
start_year=int(str1[1])
start_month=int(str1[0])
end_year=int(str1[3])
end_month=int(str1[2])
i=1

while start_year<=end_year:
    year = start_year
    month = start_month
    author=str1[4]
    url="http://explosm.net/comics/archive/" + str(year) +"/" + str(month) +"/" +str(author)

    soup = makesoup(url)

    table = soup.find('div', attrs={'class': 'small-7 medium-8 large-8 columns'})

    for row in table.findAll('div', attrs={'class': 'small-3 medium-3 large-3 columns'}):
        new_url = row.a['href']
        new_url = "http://explosm.net" + new_url
        new_soup = makesoup(new_url)
        img_src = new_soup.find('img',attrs={'id': 'main-comic',}).get('src')
        img_src = "http:"+img_src
        dl_img(img_src, str(i)) #images are saved as numbers(1,2,...) in the home directory
        i=i+1

    start_month = start_month+1
    if start_year == end_year and start_month==end_year:
        break
    if start_month == 12:
        start_year = start_year + 1
