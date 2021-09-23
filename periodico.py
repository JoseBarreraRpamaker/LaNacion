from re import T
import requests
import lxml.html as html
from requests import status_codes
import os
import datetime

from requests.models import Response

URL = 'https://www.larepublica.co/'

XPAHTS_ARICULE = '//div[@class="V_Title"]/h2/a/@href'

XPAHTS_TITLE = '//div[@class="row OpeningPostNormal"]/div/div/h2/span/text()'

#XPAHTS_BODY = '//div[@class="cuerpo intro_ mb-3"]/p/text()'

def parse_notice(links , today):
    try:
        response = requests.get(links)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parced = html.fromstring(notice)

            try:
                title = parced.xpath(XPAHTS_ARICULE)[0]
                title = title.replace('\"','')
                body = parced.xpath(XPAHTS_TITLE)[0]
                articule = parced.xpath(XPAHTS_ARICULE)[0]
            except IndexError:
                return
           
           


            with open(f'{today}/{title}.txt','w',encoding='utf-8') as archivo:
                archivo.write("hola Mi nombre es jose")
                archivo.write(articule)
                archivo.write('\n\n')
                archivo.write(body)
                archivo.write('\n\n')
                for f in body:
                    archivo.write(title)
                    archivo.write('\n')

        else:
            raise ValueError(f'Error:{response.status_codes}')
    except ValueError as error:
        print(error)
        



def parce_home():
    try:
       response = requests.get(URL)
       if response.status_code == 200:
           home = response.content.decode('utf-8')
           parsed = html.fromstring(URL)
           links = parsed.xpath(XPAHTS_ARICULE)
           today = datetime.date.today().strftime('%d-%m-%Y')
           if not os.path.isdir(today):
               os.mkdir(today)
               
               
               for x in links:
                   parse_notice(links,today)
           
       else:                      
            raise ValueError(f'Error:{status_codes}')
            print("error")    
            
   
    except ValueError as error:
        print(error)        

   
parce_home()

    


     