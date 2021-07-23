import requests
from bs4 import BeautifulSoup
import json
import metadata_parser

raw_urls=[]
u_rl=input("Enter Url : ")
page=requests.get(u_rl)
bSoup=BeautifulSoup(page.content,'html.parser')
links_lists=bSoup.findAll('a')

for link in links_lists:
    if 'href' in link.attrs:
        arr=(str(link.attrs['href']))   
    raw_urls.append(arr)
# print(*raw_urls,sep="\n") 
# prints raw urls as array

#removes dulicates links
newurls = list(dict.fromkeys(raw_urls))
# print(*newurls, sep="\n")

#filtering the urls
for i in newurls[:]:
    if i.startswith('#') or i.startswith('/') or i.startswith(str(u_rl+'page')) or i.startswith('https://www.youtube.com/') or  i.startswith('https://bit.ly/') or i.startswith('https://www.facebook.com/') or i.startswith('https://instagram.com/') or i.startswith('https://twitter.com/'):
        newurls.remove(i)
# del newurls[-1]   
#print(*newurls,sep="\n")

for x in newurls:
    print(x)
    f_url=x
    npage=metadata_parser.MetadataParser(f_url)
    title=(npage.get_metadata('title'))
    desc=(npage.get_metadata('description'))

    # #Data to be written
    def write_json(data,filename="sample.json"):
        with open(filename,'w') as f:
            json.dump(data,f,indent=4)
    with open("sample.json") as json_file:
        data=json.load(json_file)
        temp=data["websites"]
        y={
            "link":f_url,
            "title":title,
            "description":desc
        }
        temp.append(y)
    write_json(data)
