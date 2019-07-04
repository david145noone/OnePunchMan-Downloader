import os
import requests
import shutil
import urllib.request
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    Prints any log errors which occur
    """
    print(e)


def main():

    for j in range(1, 22):

        if (not os.path.exists("Volume "+str(j))):
            os.makedirs("Volume "+str(j))
            #populatechapter(j):
            if j is 1:
                #chapter's 1->8.5 of Volume 1
                for i in range(1,10):              
                    if i is 9:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-0.5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1

            if j is 2:
                 #chapter's 9 -> 15.5 of Volume 2
                for i in range(9,17):
                    if i is 16:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-0.5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1

            if j is 3:
                 #chapter's 16 -> 22.6 of Volume 3
                for i in range(16,23):
                    if i is 21:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 22:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-2)+"-"+str(6)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-2)+"ZBonus2_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 4:
                 #chapter's 21 -> 24.5 of Volume 4
                for i in range(21,26):
                    if i is 25:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 5:
                 #chapter's 25 -> 29.5 of Volume 5
                for i in range(25,31):
                    if i is 30:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 6:
                 #chapter's 30 -> 34.5 of Volume 6
                for i in range(30,36):
                    if i is 35:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 7:
                 #chapter's 35 -> 37.7 of Volume 7
                for i in range(35, 41):
                    if i is 38:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 39:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-2)+"-"+str(6)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-2)+"ZBonus2_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 40:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-3)+"-"+str(7)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-3)+"ZBonus3_Part_"+str(counter)+".png")
                                counter+=1           
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 8:
                 #chapter's 38 -> 40.6 of Volume 8
                for i in range(38, 43):
                    if i is 41:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 42:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-2)+"-"+str(6)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-2)+"ZBonus2_Part_"+str(counter)+".png")
                                counter+=1
                                
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 9:
                 #chapter's 41 -> 47.5 of Volume 9
                for i in range(41, 49):
                    if i is 42:
                        y=True
                        #Sadly chapter 42 is off the site for some reason... 
                    elif i is 48:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1           
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 10:
                #chapter's 48 -> 55.7 of Volume 10
                for i in range(48, 59):
                    if i is 56:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 57:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-2)+"-"+str(6)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-2)+"ZBonus2_Part_"+str(counter)+".png")
                                counter+=1
                    elif i is 58:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-3)+"-"+str(7)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-3)+"ZBonus3_Part_"+str(counter)+".png")
                                counter+=1 
                    elif i is 50:
                        y = True
                    else:

                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 11:
                 #chapter's 56 -> 61.5 of Volume 11
                for i in range(56, 63):
                    if i is 62:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1         
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 12:
                 #chapter's 62 -> 67.5 of Volume 12
                for i in range(62, 69):
                    if i is 68:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1         
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1

            if j is 13:
                 #chapter's 68 -> 71.5 of Volume 13
                for i in range(68, 73):
                    if i is 72:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i-1)+"-"+str(5)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')   
                        counter = 1                     
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i-1)+"ZBonus_Part_"+str(counter)+".png")
                                counter+=1         
                    else:
                        raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                        html = BeautifulSoup(raw_html, 'html.parser')
                        counter = 1
                        for item in html.find_all('center'):
                            if item.img:
                                str_url = item.img['src'].split('.png?')
                                a_url = str_url[0] + ".png"
                                
                                urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                                counter+=1
            if j is 14:
                #chapter's 72 -> 75 of Volume 14
                for i in range(72, 76):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 15:
                #chapter's 76 -> 80 of Volume 15
                for i in range(76, 81):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 16:
                #chapter's 81 -> 84 of Volume 16
                for i in range(81, 85):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 17:
                #chapter's 85 -> 87 of Volume 17
                for i in range(85, 88):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 18:
                #chapter's 88 -> 90 of Volume 18
                for i in range(88, 91):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 19:
                #chapter's 91 -> 94 of Volume 19
                for i in range(91, 95):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 20:
                #chapter's 95 -> 99 of Volume 20
                for i in range(95, 100):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
            if j is 21:
                #chapter's 95 -> 99 of Volume 21
                for i in range(101, 108):
                    
                    raw_html = simple_get("http://readonepunchman.net/manga/onepunch-man-chapter-"+str(i)+"/")
                    html = BeautifulSoup(raw_html, 'html.parser')
                    counter = 1
                    for item in html.find_all('center'):
                        if item.img:
                            str_url = item.img['src'].split('.png?')
                            a_url = str_url[0] + ".png"
                            
                            urllib.request.urlretrieve(a_url, "Volume " + str(j) + "\\" + "Ch_"+str(i)+"Part_"+str(counter)+".png")
                            counter+=1
        else:
            if j > 21:
                shutil.rmtree("Volume "+str(j))
    #print(volume_list)
    


main()


