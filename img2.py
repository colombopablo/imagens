import bs4
import requests
import shutil
import os

fortnite_imagenes = \
    'https://universofortnite.com/tienda-de-hoy-en-fortnite/'


def extract():
    URL_input = fortnite_imagenes 
    print('Fetching from url =', URL_input)
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "lxml")
    ImgTags = soup.find_all('img')
    quantity= len(ImgTags)
    i = 0
    print('Please wait..')
    while i < quantity:

        for link in ImgTags:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                # elif ext.startswith('.com'):
                #     ext = '.jpg'
                # elif ext.startswith('.svg'):
                #     ext = '.svg'
                data = requests.get(images, stream=True)
                filename = str(i) + ext
                with open(filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
            except:
                pass
    print('\t\t\t Downloaded Successfully..\t\t ')


extract()
