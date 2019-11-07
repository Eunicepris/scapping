import requests

from bs4 import BeautifulSoup

url = "https://www.lespagesjaunesafrique.com/"

response = requests.get(url)

#print(response.status_code)

if response.status_code == 200 : 
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    div_pays = html_soup.find_all('div', attrs={ 'class': 'col-sm-4 col-xs-6 col-md-4 col-lg-3'})
    
    compt = 0
    for item in div_pays:
        div_pays = html_soup.find_all('div', attrs={ 'class': 'col-sm-4 col-xs-6 col-md-4 col-lg-3'})
        pays = html_soup.find_all('div', attrs={ 'class': 'drapeaux'})

        if compt < 52:
            pays = item.find('div')
            nom = pays
            ba = item.find('a')
            
            url = ba['href']
            print(compt+1, "\n"+"Pays:"+pays.text ,"\n", "Url:"+url  )

            #print(url)
        compt += 1
    


else:
    print("Error", response.status_code)
