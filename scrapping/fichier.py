import requests

from bs4 import BeautifulSoup

url = "http://www.abidjanguide.com/AbidjanGuidefr.htm"

response = requests.get(url)

#print(response.status_code)

if response.status_code == 200 : 
    
    #----------------------------RECUPERATION HTML--------------------# 
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    #----------------------------RECUPERATION TITRE--------------------# 
    
    div_title = html_soup.find('div', attrs={ 'class': 'navbar-header'})
    h1_title = div_title.find('h1')
    
    #----------------------------RECUPERATION PRESENTATION--------------------# 
    
    div_presentation = html_soup.find_all('div', attrs={ 'class': 'col-md-2'})
    
    div_col= html_soup.find_all('div', attrs={ 'class': 'col-md-5'})
    
    compt = 0
    for item in div_presentation:
        if compt < 3:
            
            ba = item.find('a')
            url = ba['href']
            img = ba.find('img')
            h3 = ba.find('h3')
            
            image = img['src']
            titre = h3.text
            
            
            #print(compt+1, "\n\n"+"Nom:"+titre ,"\n", "Url:"+url , "\n", "Image:"+image )
            
            
            #print(url)
            
            #print(compt)
            #print(item.text)
            compt += 1
            
    print(div_col)
    varr = 0
    for var in div_col:
        if varr < 6:
            li = var.find('')


    
    #print(div_presentation)
    #print(h1_title.text)

    #print(div_title.text)

else:
    print("Error", response.status_code)
