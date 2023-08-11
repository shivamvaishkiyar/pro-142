from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list=[]
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

    star_names =[]
    Distance=[]
    Mass=[]
    Redius=[]
    Lum=[]

    for r in range(1,len(temp_list)):
        star_names.append(temp_list[r][1])
        Distance.append(temp_list[r][5])
        Mass.append(temp_list[r][6])
        Lum.append(temp_list[r][7])

    df2 = pd.DataFrame(list(zip(star_names,Distance,Mass,Redius,Lum)),columns=('star_names','Distance','Mass','Redius','Lum'))
    print(df2)
    df2.to_csv('bright_star.csv')