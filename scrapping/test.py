import requests

from bs4 import BeautifulSoup

url = "https://pratik.ci/thematiques/loisirs/confiserie"

response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

#print(html_soup.prettify)

entreprise = html_soup.find('div', attrs={'class': "views-row"})

#print(entreprise.prettify)

titre = entreprise.find('div', attrs={'class': "field field-name-title field-type-ds field-label-hidden"}).get_text()

#print(titre)


tel = entreprise.find('div', attrs={'class': "field field-name-field-telepone-1 field-type-text field-label-hidden color_black_blold"}).get_text()

#print(tel)

phone = entreprise.find('div', attrs={'class': "field field-name-field-cellulaire1 field-type-text field-label-hidden color_black_blold"}).get_text()

localisation = entreprise.find('div', attrs={'class': "field field-name-field-localisation-lieu field-type-taxonomy-term-reference field-label-hidden"}).get_text()

siege = entreprise.find('div', attrs={'class': "field field-name-field-siege field-type-list-boolean field-label-hidden color_siege_agenge"}).get_text()

data = {
    'titre': titre,
    'tel':tel, 
    'phone':phone,
    'localisation': localisation,
    'siege': siege
}
print(data)
