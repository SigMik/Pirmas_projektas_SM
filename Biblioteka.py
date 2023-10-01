# 2023-09-14 Duomenu analitikos pagrindai

import pandas as pd
import matplotlib.pyplot as plt

# # sukuriame sarasa su duomenimis
#
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# # sukuriame DataFrame is saraso
# df = pd.DataFrame(duomenys)
#
# # filtruoti duomenis pgl. amziu
#
# jaunesni = df[df['Amzius'] <25]
# # print(jaunesni)
#
# # skaiciuokime vid.amziu
# vidutinis_amzius = df['Amzius'].mean()
# print(f'Vidutinis amzius: {vidutinis_amzius}')

# temperaturos = [24.5, 25.2,23.8, 22.5]
# sr =pd.Series(temperaturos)
# print(sr)
#
# serija_rikiavimas = sr.sort_values(ascending=False)
# print(f'pirmas elementas: {sr[0]}')

# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# # vardai = df['Vardas']
# # jeigu nori list
# vardai = df['Vardas'].to_list()
# # print('Vardai: ')
# # print(vardai)
#
# # pridedame nauja stulpeli i Data Frame (zemiau)
#
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas datarframe su nauju stulpeliu:')
# print(df)



# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardauskai')
# plt.ylabel('Amziauskai')
# plt.title('Mano pavyko Amzius pagal vardus')
# plt.show()
#
#
# df.tail(2)
# df.head()


# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25,25,22,30]
#         }
# data1 = pd.DataFrame(data)
# vidutinis_amzius_pagal_miesta = data1.groupby('Miestas')['Amzius'].mean()
# print(vidutinis_amzius_pagal_miesta)

# Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
# Filtravimas ir paieška:
# a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
# b. Raskite miestą, turintį mažiausią populiaciją.
#
# data = {'Miestas': ['Alytus', 'Londonas', 'Punskas','Ryga'],
#         'Populiacija': [70000,600000,15000, 500000]
#         }
#
# data1=pd.DataFrame(data)
# print(data1)
# pagal_populiacija = data1[data1['Populiacija'] >200000]
# print(pagal_populiacija)
#
# min_miestas = data1[data1['Populiacija']==data1['Populiacija'].min()]
# print(min_miestas)

# data1.loc[data1['Miestas'] =='Alytus', 'Populiacija'] += 21
# print(data1)

#bandome is naujo kita reiksme prideti
# data1.loc[data1['Populiacija'] == 500000, 'Miestas'] = 'Minskas'
# bandome is naujo iloc




# Duomenų grupavimas ir agregavimas:
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma,
# kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.
# #
# data1['Salis'] = ['Lietuva', 'Anglija', 'Lenkija', 'Latvija']
# print('Atnaujintas sarasas su salimis: ')
# print(data1)
# #
# bendra_populiacija_saliai = data1.groupby('Salis')['Populiacija'].mean()
# print(bendra_populiacija_saliai)

# miestai_pagal_populiacija = data1.sort_values('Populiacija', ascending=False)
# print(miestai_pagal_populiacija)

## 2023-09-15
## *Sukurkite Pandas duomenų lentelę su 5 eilutėmis ir 3 stulpeliais. OK
## *Pavadinkite stulpelius "Vardas", "Amžius" ir "Miestas". OK
## *Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
## *Išspausdinkite pirmas 3 eilutes iš lentelės.
##
## *Išspausdinkite stulpelį "Amžius" visų eilučių atveju.
## *Atrinkite visus žmones, kurių amžius yra mažesnis nei 25.
## *Sukurkite naują stulpelį "Gimimo metai" pagal esamą stulpelį "Amžius".Paskaičiuokite gimimo metus pagal 2023 metus.
## *Ištrinkite eilutę su "Jonas" iš lentelės.
## *Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".
##
## *Nuskaitykite duomenis iš "duomenys.csv" failo į naują Pandas lentelę.
## *Atrinkite visus žmones, gyvenančius Vilniuje.

# data = {'Vardas': ['Jonas', 'Augustas', 'Ramune', 'Daiva', 'Tomas'],
#         'Amzius': [35,52, 23,43, 18],
#         'Miestas': ['Alytus', 'Kaunas', 'Panevezys', 'Vilnius', 'Klaipeda']
#         }
# df = pd.DataFrame(data)
# # print(df)

# df['Gimimo metai'] = 2023 - df['Amzius']
# print('Atnaujintas datarframe su nauju stulpeliu:')
# print(df)

# *Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
# df.loc[len(df.index)] = ['Jonas', 30, 'vilnius', 1958]
# print(f'\n ', df)

# *Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".
# df.to_csv('duomenys.csv')

# * Atrinkite visus žmones, gyvenančius Vilniuje.
# Vilniaus_gyventojai = df[df['Miestas']=='Vilnius']
# print(Vilniaus_gyventojai)

# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [35,65,23,41]
#             }
# df = pd.DataFrame(duomenys)
# jaunesni = df [df['Amzius'] < 25]
# # print(jaunesni)
#
# vidutinis_amzius = df['Amzius'].mean()
# print(f'Vidutinis amzius: {vidutinis_amzius}')

# temperaturos = [24.5, 26.5, 23.5, 22.9]
# sr=pd.Series(temperaturos)
# print(sr)
# serija_rikiavimas = sr.sort_values()
# print(serija_rikiavimas)

# amzius = [12,56,81,15,32,56,18]
#
# a=pd.Series(amzius)
# # print(a[0])
# rikiavimas=a.sort_values(ascending=False)
# # print(rikiavimas)

# temperaturos = [24.5, 26.5, 23.5, 22.9]
#
# sr=pd.Series(temperaturos)
# # print (f'Pirmas elementas: {sr[0]}')
#
# vidurkis = sr.mean()
# print(f'Temperaturu vidurkis: {vidurkis}')


# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [35,65,23,41]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df['Vardas']
#
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas sarasas su nauju stulpeliu: ')
# # print(df)

# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='black')
# plt.xlabel('Vardas')
# plt.ylabel('Amzius')
# plt.title('Amzius pagal vardus')
# plt.show()

# df.head(2)
# df.tail(2)

# data = { 'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius', 'Vilnius'],
#          'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Moteris', 'Moteris'],
#          'Amzius': [35,29,51,25,19]
#          }
# data1=pd.DataFrame(data)
#
# vidutinis_amzius_pagal_miesta=data1.groupby('Miestas')['Amzius'].mean()
# print(vidutinis_amzius_pagal_miesta)

# 2023-09-15 1 uzduotis: NEBAIGTA

# csv_failo_pavadinimas = 'data-table.csv'
# df=pd.read_csv(csv_failo_pavadinimas)
#
# savivaldybes =df.loc[df['Administracinė teritorija'].str.endswith("sav."), ['Administracinė teritorija','Reikšmė']]
# print(f'Miesto ir rajono savivaldybės su gyventojų skaičiumi: {savivaldybes}')

# Gyventoju_kiekis_pagal_savivaldybes = savivaldybes.groupby('Administracinė teritorija')['Reikšmė'].sum()
# print(f'Savivaldybės su bendru gyventojų skaičiumi pagal administracines teritorijas:'
#       f' {Gyventoju_kiekis_pagal_savivaldybes}')

# 2023-09-15 namu darbu 2 uzduotis:
# Sukurkite DataFrame su mokinių pažymiais, kuriame yra stulpeliai "Vardas", "Pavardė" ir "Pažymys" (nuo 1 iki 10).
# Atvaizduokite tik tuos mokinius, kurių pažymys yra didesnis nei 7.
# Apskaičiuokite vidutinį pažymį visiems mokiniams:

# mokiniai ={ 'Vardas': ['Jonas', 'Petras', 'Ona', 'Jurgis'],
#             'Pavarde': ['Jonaitis', 'Petraitis', 'Onaite', 'Jurgaitis'],
#             'Pazymys': [9, 10, 7, 6]
#             }
# mokinys=pd.DataFrame(mokiniai)
# su_didesniu_nei_7_pazymiu = mokinys[mokinys['Pazymys'] > 7]
# print(f'Mokiniu sarasas, kuriu pazymus didesnis nei 7: {su_didesniu_nei_7_pazymiu}')
#
# vidurkis=mokinys['Pazymys'].mean()
# print(f'Klases mokiniui tenkantis pazymiu vidurkis:')
# print(vidurkis)

## 2023-09-15 namu darbu 3 uzduotis:
## Sukurkite Pandas DataFrame iš sąrašo žmonių duomenų su stulpeliais "Vardas", "Amžius" ir "Miestas".
## Atspausdinkite šį DataFrame.
# Filtruokite žmones, kurių amžius yra didesnis nei 25 metai ir kurie gyvena Vilniuje.
# Surūšiuokite žmones pagal amžių didėjimo tvarka.
# Pridėkite stulpelį "Lytis" prie DataFrame ir nurodykite lytis (pvz., "Vyras" arba "Moteris").
# Grupuokite duomenis pagal "Lytis" stulpelį ir apskaičiuokite vidutinį amžių kiekvienai lyčiai.
# Pridėkite naują žmogų į DataFrame su vardu "Laura", amžiumi 24 metai ir gyvenančią Kaune.
# Redaguokite žmogų ir amžių padidinkite jį iki n metų.
# Pašalinkite žmogų iš DataFrame.
# Išsaugokite galutinį DataFrame į CSV failą su pavadinimu "zmones.csv".

## Sukurkite Pandas DataFrame iš sąrašo žmonių duomenų su stulpeliais "Vardas", "Amžius" ir "Miestas".
# sarasas = { 'Vardas': ['Algirdas', 'Jonas', 'Ona', 'Marija', 'Jurgita', 'Dovile'],
#             'Amzius': [35, 25, 65, 45, 16, 74],
#             'Miestas': ['Akmene', 'Alytus', 'Kaunas', 'Silute', 'Kaunas', 'Vilnius']
#             }
### Atspausdinkite šį DataFrame.
# sr=pd.DataFrame(sarasas)
# print(sr)

## Filtruokite žmones, kurių amžius yra didesnis nei 25 metai ir kurie gyvena Vilniuje. NEBAIGTA.
# x = sr[sr['Miestas'] == 'Vilnius' & ['Amzius']>25]
# print(x) NEBAIGTA

## Surūšiuokite žmones pagal amžių didėjimo tvarka.
# y = sr.sort_values(['Amzius', 'Vardas'], ascending=[True,False])
# print(y)

## Pridėkite stulpelį "Lytis" prie DataFrame ir nurodykite lytis (pvz., "Vyras" arba "Moteris").
# sr['Lytis'] = ['Vyras', 'Vyras', 'Moteris', 'Moteris', 'Moteris', 'Moteris']
# print(f'Atnaujintas sarasas: {sr}')

## Grupuokite duomenis pagal "Lytis" stulpelį ir apskaičiuokite vidutinį amžių kiekvienai lyčiai.
# y=sr.groupby('Lytis')['Amzius'].mean()
# print(y)

## Pridėkite naują žmogų į DataFrame su vardu "Laura", amžiumi 24 metai ir gyvenančią Kaune.
# sr.loc[len(sr.index)] = ['Janina', 25, 'Klaipeda', 'Vyras']
# print(f'\n ', sr)

## Redaguokite žmogų ir amžių padidinkite jį iki n metų. NEBAIGTA.

## Pašalinkite žmogų iš DataFrame.
# sr.drop(sr.index[0], axis=0, inplace=True)
# print(sr)
#
# sr.to_csv('zmones.csv')

from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
# import time()

# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="VarleProducts",
#         user="postgres",
#         password="Dekingumas123*"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS varle_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2),
#         quantity INT)
#     """
#     # cursor.execute(create_table_query)
#     # print('Table created successfully')
#
#
#     url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     product_elements = soup.find_all('div', class_='GRID_ITEM')
#     # print(product_elements)
#
#     product_data = []
#
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='product-title').text.strip()
#         product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
#         product_quantity = product_element.find('b').text.strip()[:1]
#
#         # print(f'Adding products to the list: {product_name}')
#         # time.sleep(2)
#         # product_data.append((product_name, product_price, product_quantity))
#         # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES(%s, %s, %s)"
#         # cursor.execute(insert_query, (product_name, product_price, product_quantity))
#         # print(f'Products inserted into list succesfully!')
#         connection.commit()
#
#     # df=pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#     # print(df)
#
#     select_query = "SELECT * FROM varle_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df=pd.DataFrame(rows, columns = ['id', 'name', 'price', 'quantity'])
#     print(df)
#
# if __name__ =='__main__':
#     create_and_insert_product()

# 2023-09-18 namų darbas: MODESTO ATSIŲSTAS, BET NESUSIKURIA PREKES:

import psycopg2
import requests
from bs4 import BeautifulSoup
import pandas as pd
#
#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ZaislaiProducts",
#         user="postgres",
#         password="Dekingumas123*"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS zaislai_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#     connection.commit()
#     url = 'https://www.1a.lt/c/zaislu-pasaulis-20-zaislams-su-kodu/87w'
#     response = requests.get(url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='catalog-taxons-product catalog-taxons-product--grid-view')
#
#     print(f"Number of product elements found: {len(product_elements)}")
#     product_data = []
#
#     for product_element in product_elements:
#         try:
#             product_name = product_element.select_one('.catalog-taxons-product a').text.strip()
#             print(f'Product Name: {product_name}')
#
#             product_price_text = product_element.find('span', class_='catalog-taxons-product-price__item-price').text.strip()
#             # Remove unwanted characters and convert to float
#             product_price = float(
#                 product_price_text.replace('€', '').replace('vnt.', '').replace('\n\n/', '').replace(' ', '').replace(
#                     ',', '.'))
#             print(f'Product Price: €{product_price:.2f}')
#
#             product_data.append((product_name, product_price))
#             print(f'Product inserted into the list successfully!\n')
#
#         except AttributeError as e:
#             print(f'Error: {e}')
#         except ValueError as e:
#             print(f'Error converting price to float: {e}')
#
#     print(product_data)
#     # df=pd.DataFrame(product_data, columns=['name', 'price'])
#     # print(df)
#     # select_query = "SELECT * FROM zaislai_products"
#     # cursor.execute(select_query)
#     # rows = cursor.fetchall()
#     # df=pd.DataFrame(rows, columns = ['id', 'name', 'price'])
#
#     # print(df)
#
#
# if __name__ == '__main__':
#     create_and_insert_product()


# 2023-09-19 klases darbai:

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import psycopg2
#
# url = 'http://www.meteo.lt/en/miestas?placeCode=Vilnius'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# forecast = soup.find_all('div', class_='forecast-day')
# week_days = soup.find_all('span', class_='date')
# day_temperature = soup.find_all('span', class_='big up-from-zero')[1::2]
# ##1::2 ima kas antra reiksme
# # print(week_days)
# # print(day_temperature)
#
# ##dabar filtruojam tik savaites dienas
# filtered_week_days=[week_day.get_text().split(',')[0] for week_day in week_days]
# day_temperatures= []
# for temperature in day_temperature:
#     temp_text = temperature.get_text().replace('°C', '')
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# print(day_temperatures)
#
# data={'weekday': filtered_week_days, 'temperature': day_temperatures}
# df=pd.DataFrame(data)
# print(df)
# max_temperature = df['temperature'].max()
# min_temperature = df['temperature'].min()
#
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(8,6))
# plt.bar ('Aukščiausia temperatūra', max_temperature, color = 'green')
# plt.bar ('Žemiausia temperatūra', min_temperature, color = 'red')
# plt.ylabel ('Temperatūra:  °C')
# plt.title ('Aukšciausia ir žemiausia temperatūra Vilniuje')
# plt.show()

###Sukurti DataFrame su procentais ir pavadinimais

# import matplotlib.pyplot as pl
# proc = [90, 10, 145,32,69]
# pasiekimai = ['matematika', 'istorija', 'fizika', 'anglu', 'biologija']
# spalvos = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen','deeppink']
# ex = (0.1, 0, 0, 0, 0)
#
#
# pl.pie(proc, explode=ex, labels=pasiekimai, colors=spalvos, autopct='%1.1f%%',startangle=50)
# pl.title('Pasiekimų diagrama')
# pl.axis('equal')
# pl.show()

# 2023-09-20 pamoka:
# 1 uzduotis

# x = [1,6,5,4,9]
# y = [4,5,7,1,3]
# z = [6,5,2,1,3]

import matplotlib.pyplot as plt

# plt.plot(x,y, label = "linija", color="blue", linestyle= "--", marker="o")
# plt.plot(x,z, label = "linija2", color="red", linestyle= "--", marker="o")
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafinė vizualizacija')
# plt.show()

# 2 uzduotis

# x = [1,6,5,4,9]
# y = [4,5,7,1,3]
# z = [6,5,2,1,3]
#
# import matplotlib.pyplot as plt
#
# plt.scatter(x,y, label='taskai', color = 'red', marker = 's' )
# plt.scatter(x,z, label='taskai', color = 'blue', marker = 'o' )
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafinė vizualizacija')
# plt.show()

# 3 uzduotis

# x = [1,2,3,4,3,2,1,0]
# y = [4,5,7,1,3]
# z = [6,5,2,1,3]
#
# import matplotlib.pyplot as plt
#
# plt.hist(x, bins = 5, color = 'purple', alpha = 0.2, edgecolor='black')
# plt.legend()
# plt.xlabel('x')
# plt.title('Grafinė vizualizacija')
# plt.show()

# 4 uzduotis:

# y = [4,5,7,1,3]
# z = [6,5,2,1,3]
#
# plt.step(y, z, label = 'pakopos', color = 'purple', where='mid')
# plt.fill_between(y,z, color='grey', alpha=0.5)
# plt.text(4,6, 'Svarbus taskas', fontsize = 12, color='blue')
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.title('Grafinė vizualizacija')
# plt.show()

# 5 uzduotis
#
# y = [4,5,7,1,3]
# z = [6,5,2,1,3]
#
# plt.step(y, z, label = 'pakopos', color = 'purple', where='mid')
# plt.fill_between(y,z, color='grey', alpha=0.5)
# plt.text(4,6, 'Svarbus taskas', fontsize = 12, color='blue')
# plt.axhline(y=4, color='green', linestyle = '--', label = 'horizontali')
# plt.axvline(x=4, color='red', linestyle = '--', label = 'vertikali')
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.title('Grafinė vizualizacija')
# plt.show()

# 6 uzduotis

# x = [1,2,3,4,5]
# y = [10,15,7,12,9]
# z = [6,5,2,1,3]
#
#
# plt.subplot(2,1,1)
# plt.plot(x,y, label = 'linija1')
# plt.title('Grafinė vizualizacija')
#
# plt.legend()
# plt.subplot(2,1,2)
# plt.plot(x, [i**2 for i in y], label = 'linija2', color ='green')
#
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.savefig('Grafikas.png')
#
# plt.show()

# Pamokos uzduotys:
# a. Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# b. Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
# c. Apskaičiuokite vidutinę prekių kainą ir vidutinį pardavimų kiekį.

import pandas as pd
# data = pd.read_csv('sales_data.csv.',encoding='iso-8859-1')
# df = pd.DataFrame(data)
# print(df.head(5))
#
# vidutine_pr_kaina = df['PRICEEACH'].mean().round(2)
#
# vidutinis_pardavimas = df['QUANTITYORDERED'].mean()
# print(vidutine_pr_kaina)
# print(vidutinis_pardavimas)
#
# # d. Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.
#
import matplotlib.pyplot as plt
# # Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.

# df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# df['Metai'] = df['ORDERDATE'].dt.year
# df['Mėnuo'] = df['ORDERDATE'].dt.month
# df['Diena'] = df['ORDERDATE'].dt.day
# print(f'\n', df)
# Mėn_suma = df.groupby(['Metai', 'Mėnuo', 'Diena'])['QUANTITYORDERED'].sum()
# Mėn_suma.plot(kind= 'line', color='skyblue')
# plt.xticks(rotation = 90)
# plt.xlabel('Data')
# plt.ylabel('Pardavimai')
# plt.title('pardavimų skaičius laiko atžvilgiu')
# plt.show()


# būdas kaip susikurti su random nauja duomenu lentele Atlyginimai.csv.LABAI GERAS PAVYZDYS.
import random
# data ={ 'Stupelisid': [i+1 for i in range(50)],
#         'Vardas': [random.choice(['Jonas', 'Petras', 'Zemyna'] ) for _ in range(50)],
#         'Alga': [random.randint(1000, 1500) for _ in range(50)]
#
# }
# df=pd.DataFrame(data)
# df.to_csv('Atlyginimai.csv', index=False)

##budas kaip susikurti su random datas ir pardavo kiekius

import random
from datetime import datetime, timedelta
#
# data = {'Stulpelis_id': [i+1 for i in range (10)],
#         'Data': [(datetime(2023, 1, 1) + timedelta(days=random.randint(0,364))).strftime('%Y-%m-%d') for _ in range (10)],
#         'Pardavimai': [random.randint(5, 150) for _ in range (10)]
# }
# df = pd.DataFrame(data)
# print(df)

# 2023-09-20 pamokos uzduotis:

# a. Sukurkite du sąrašus: vienas su laiko žymėmis (mėnesiais nuo sausio iki gruodžio) ir kitas su kas mėnesį
# parduotų prekių kiekiu.
#
# b. Pavaizduokite šiuos duomenis linijiniame grafike. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
#
# c. Pridėkite legenda, kurioje būtų nurodyta, ką reiškia ši linija.

import matplotlib.pyplot as plt
import pandas as pd

# menesiai = [1,2,3,4,5,6,7,8,9,10,11,12]
# pardavimu_suma = [1025, 2563, 5687, 2654, 6254, 3200, 10, 2561, 2541, 2564, 2541, 1256]
#
#
# plt.plot(menesiai, pardavimu_suma, label = "Pardavimai pagal mėnesius", color="purple", linestyle= "--", marker="o")
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('Pardavimų suma ')
# plt.title('Pardavimai pagal mėnesius')
# plt.show()

# 2023-09-21 pamokos darbai:

# df = pd.read_csv('prekybos_duomenys.csv')
# # print(df.head(5))
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Mėnuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
# # print(f'\n', df)
# pagal_produkta = df.groupby(['Mėnuo','Produktas']) ['Pardavimai'].sum()
# products = df['Produktas']
# result = pd.DataFrame(columns=['Produktas', 'Metai', 'Mėnuo', 'Sumazejimas'])
# for product in products:
#     product_df=df[df['Produktas']== product]
#     for year in product_df['Metai'].unique():
#         for month in range(1,13):
#             if product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)].shape[0]>0:
#                 sales = product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)]['Pardavimai'].sum()
#                 if month >1:
#                     praeje_metai=year
#                     peaejes_men=month-1
#                 else:
#                     praeje_metai = year-1
#                     peaejes_men = 12
#                 pr_sales=\
#                 product_df[(product_df['Metai']==praeje_metai) & (product_df['Mėnuo']== peaejes_men)]['Pardavimai'].sum()
#                 decrease = pr_sales-sales
#                 result = pd.concat([result,pd.DataFrame([[product,year,month,decrease]],columns=result.columns)],ignore_index=True)
# print(result)
# plt.plot(result['Produktas'], result['Sumazejimas'], label='linija', color='blue', linestyle ='--', marker = 'o')
# plt.xticks(rotation=90)
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('sumažėjimas')
# plt.title('Pardavimų mažėjimas')
# plt.show()

# Išspausdinkite pirmas 5 eilutes;
# Filtruokite automobilius pagal jų kainą (pvz., kaina mažesnė nei 10 000). Išspausdinkite šiuos automobilius;
# Suskirstykite automobilius pagal gamintoją ir susumuokite kiekvieno gamintojo automobilių kiekius.
# Atvaizduokite stulpelinėje diagramoje automobilių kiekius;


# df=pd.read_csv('automobiliai.csv')
# print(df.head(5))
#
#
# auto_uz_maziau_nei_10000=df[df['Kaina']<10000]
# print(auto_uz_maziau_nei_10000)
#
# auto_pgl_gamintoja = df['Markė'].value_counts()
#
# print(auto_pgl_gamintoja)
# #
# # plt.plot(auto_pgl_gamintoja, label='linija', color='blue', linestyle ='--', marker = 'o')
# # plt.xlabel('Markė')
# # plt.ylabel('Pagaminti automobiliai')
# # plt.title('Automobilių kiekiai pagal markę')
# # plt.show()
#
# auto_pgl_gamintoja.plot(kind='bar', color='green')
# plt.xlabel('Markė')
# plt.xticks(rotation=20)
# plt.ylabel('Pagamintas kiekis')
# plt.title('Pagaminti kiekiai pagal markę')
# plt.show()



# 2023-09-22 pamokos medziaga numpy biblioteka:

import numpy as np
import random
# masyvas =np.array([1,2,3,4,5,])
# masyvas2=np.array([6,2,9,4,7])
#
# suma=np.sum(masyvas)
# vidurkis=np.mean(masyvas)
#
# mediana=np.median(masyvas)
# st_dev = np.std(masyvas)
# min=np.min(masyvas)
#
# print(f'Suma: {suma}')
# print(f'Vidurkis: {vidurkis}')
# print(f'Mediana: {mediana}')
# print(f'Nuokrypis: {st_dev}')
# print(f'Minimumas: {min}')
#
# suma2 = masyvas+masyvas2
# print(suma2)

# Matricos sukūrimas:

# matrica =np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(matrica)
# suma = np.sum(matrica)
# print(f'Matricos suma: {suma}')

# matrica = np.random.randint(1,11,(4,4))
# print(matrica)
# vidurkis=np.mean(matrica)
# print(vidurkis)
# vidurkis_pagal_stulpelius = np.mean(matrica, axis=0) #axis 0 yra stulpelis, 1 -eilute
# print(vidurkis_pagal_stulpelius)

# studentų_pazymiai = np.array([[7, 8, 9], [6, 4, 10], [10, 9, 10], [8, 8, 7]])
# student7_vidurkiai = np.mean(studentų_pazymiai, axis = 1).round(2)
# medianos = np.median(studentų_pazymiai, axis=1)
# print(student7_vidurkiai, medianos)
# for i in range(len(student7_vidurkiai)):
#     print(f'studentas {i+1}: vidurkis {student7_vidurkiai[i]}, mediana {medianos[i]}')


# print(f'Studentu vidurkis: {vidurkis}')
# print(f'Studentu medianos: {medianos}')

# masyvas33 = np.random.randint(1,51,(1,1))
# maksis = np.argmax(masyvas33)
# min=np.argmin(masyvas33)
# # print(maksis)
# print(masyvas33, '\n', min)

# masyvas = np.array([1, 2, 3, 4, 5])
# daugiau_uz_tris = masyvas[masyvas > 3]
# print(daugiau_uz_tris)

# for i in range(1,11):
#     print(i)

# 2023-09-22 Bandymas istraukti duomenis is kripto tinklapio.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
# import time()

#
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
# table=soup.find("table", class_='sc-b28ea1c6-3 izgIsg cmc-table')
#
# antrastes = table.find_all('th')
#
# antrasciu_pavadinimai =[]
#
# for i in antrastes:
#     pavadinimas = i.text
#     antrasciu_pavadinimai.append(pavadinimas)
#     # print(antrasciu_pavadinimai)
# # print(antrastes)
#
# df=pd.DataFrame(columns=antrasciu_pavadinimai[2:7])
# df=pd.DataFrame(columns=['Name', 'Price', '1h%', '7h%', '7d%'])
# print(df)
#
# rows = table.find_all('tr')
# # print(row)
# for i in rows[1:11]:
#     data=i.find_all('td')
#     # print(data)
#     row=[tr.text for tr in data]
#     # print(row[2:7])
#     l=len(df)
#     df.loc[l]=row[2:7]
# print(df)
# df.to_csv('criptocurrency.csv')

# Paskaičiuokite vidutines, minimalias ir maksimalias kainas, taip pat kitas statistikos vertes.

# df=pd.read_csv('criptocurrency.csv')
# data=pd.DataFrame(df)
# print(data)
# min_cripto_kaina=data['Price'].min()
# print(f'Žemiausia cripto kaina: {min_cripto_kaina}')
#
# max_cripto_kaina=data['Price'].max()
# print(f'Didžiausia cripto kaina: {max_cripto_kaina}')

# data['Price'] =data['Price'].str.replace('$', '').str.replace(',', '').astype(float)
# print(data)

# vid_cripto_kaina = data['Price'].mean().round(2)
# print(f'Vidutinė cripto kaina $ valiuta: {vid_cripto_kaina}')


# # Sukurkite linijinį grafiką, kuris atvaizduoja kriptovaliutos kainos kitimą laike (x ašis - laikas, y ašis - kaina).
# # NEPAVYKSTA.
#
# x = data['Name']
# y = data['Price']
# z = data['1h%']
# f = data['7h%']
# g = data['7d%']
#
# print(data)
# cripto_valiutos = df['Name']
# cripto_kainos = df['Price']
# # for valiuta in cripto_valiutos:
# #     df['Name']=valiuta
# #     for kaina in cripto_kainos:
# #         df['Price']=kaina
# #     result=valiuta+kaina
# #     print(result)
# for valiuta, kaina in zip(cripto_valiutos,cripto_kainos):
#     result = valiuta+kaina
#     print(result)
# plt.plot(result['Produktas'], result['Sumazejimas'], label='linija', color='blue', linestyle ='--', marker = 'o')
# plt.xticks(rotation=90)
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('sumažėjimas')
# plt.title('Pardavimų mažėjimas')
# plt.show()

# 2023-09-25 pamoka. Biblioteka numpy tęsinys:

# masyvas = np.arange(1,11)
# print(masyvas)
#
# sum=np.sum(masyvas)
# # print(sum)
#
# dvimatis_masyvas=masyvas.reshape(5,2)
# print(dvimatis_masyvas)
#
# # lyginius skaicius pavesrti i nuli
# masyvas[masyvas%2==0]==0
# # print(masyvas)
#
# x_masyvas=masyvas[masyvas>5]
# print(x_masyvas)

# masyvas = np.random.randint(1,101,(5,5))
# print(masyvas)

# max_masyvas = np.max(masyvas)
# print(max_masyvas)

# min_masyvas=np.min(masyvas)
# print(min_masyvas)

# apsukti eilutes reiksmes nuo galo
# kintamasis=np.flipud(masyvas)
# print(kintamasis)

# stulpelis = masyvas[:,::-1]
# print(stulpelis)

# apsuka is left i right
# stulpelis = np.fliplr(masyvas)
# print(stulpelis)

# sujungti du masyvus i viena horizontaliai

# masyvas = np.random.randint(1,10,10)
# masyvas2 = np.arange(1,50,5)
# print(masyvas, '\n', masyvas2)
# print(masyvas)
# print(masyvas2)

# masyvas_isskirtas = np.split(masyvas,5)
# print(masyvas_isskirtas)
#
# masyvas3=np.hstack((masyvas,masyvas2))
# print(masyvas3)
#
# masyvas4=np.split(masyvas3, 4)
# print(masyvas4)

# 2023-09-25 pamokos uzduotys:
# [!] Sukurkite masyvą nuo 0 iki 9 ir jį pertvarkykite į 3x3 masyvą;

# masyvas = np.arange(1,10)
# print(masyvas)
#
# trimatis_masyvas=masyvas.reshape(3,3)
# print(trimatis_masyvas)

# [!] Sukurkite 5x5 masyvą su atsitiktinėmis reikšmėmis ir raskite vidurkį kiekvieno stulpelio;

# masyvas = np.random.randint(1,256,(5,5))
# print(masyvas)
# vidurkis_pagal_stulpelius = np.mean(masyvas, axis=0)
# print(vidurkis_pagal_stulpelius)

# [!] Sukurkite 6x6 masyvą su skaičiais nuo 1 iki 36 ir transformuokite jį į 2D masyvą (matricą) 3x12;
# masyvas=np.arange(1,37)
# print(masyvas)
# masyvas6_6=masyvas.reshape(6,6)
# print(masyvas6_6)
# masyvas_transformuotas = np.reshape(masyvas, (3,12))
# print(f'Transformuotas masyvas:')
# print(masyvas_transformuotas)

# [!] Sukurkite masyvą su atsitiktinėmis reikšmėmis nuo 0 iki 1 ir raskite jo visų elementų vidurkį.
# Toliau paverskite mažesnes reikšmes į 0 ir didesnes į 1.
#
# masyvas = np.random.randint(0,2,(4,4))
# print(masyvas)
# vidurkis_pagal_elementus = np.mean(masyvas, axis=1)
# print(vidurkis_pagal_elementus)
# naujas_masyvas=vidurkis_pagal_elementus

# naujas_masyvas[naujas_masyvas>=0.5]=1,[naujas_masyvas<0.5]=0
# print(naujas_masyvas)

# [!] Sukurkite du masyvus pirmas_masyvas ir antras_masyvas,
# kiekvieną su 5 atsitiktinėmis reikšmėmis nuo 1 iki 10, ir sudėkite juos taip,
# kad naujas masyvas turėtų visų reikšmių kvadratus.

# masyvas = np.random.randint(1,11,5)
# masyvas1 = np.random.randint(1,11,5)
# print(masyvas)
# print(masyvas1)
# abu_masyvai = np.hstack((masyvas,masyvas1))
# print(abu_masyvai)
# abu_masyvai = abu_masyvai**2
# print(abu_masyvai)

# [!] Sukurkite 2D masyvą (matricą) 5x5 su atsitiktinėmis reikšmėmis nuo 1 iki 10. Raskite eilutes, kuriose yra bent du skaičiai didesni nei 5.

# masyvas11 = np.random.randint(1, 11, (5, 5))
# print('\n ', masyvas11)
# eilute = masyvas11[(masyvas11 > 5).sum(axis = 1) >=2]
# print('\n ', eilute)

# 2023-09-26 pamoka:
# seaborn biblioteka
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# stulpeline i virsu
# df = pd.DataFrame({'category':['a', 'b', 'a', 'b'], 'reiksme':[1,2,3,4,]})
# sns.barplot(data=df, x='category', y = 'reiksme')
# plt.show()

# linijine
# df = pd.DataFrame({'category':['a', 'b', 'a', 'b'], 'reiksme':[1,2,3,4,]})
# sns.lineplot(data=df, x='category', y = 'reiksme')
# plt.show()

# stupeline pagal reiksmes
# df = pd.DataFrame({'category':['a', 'b', 'a', 'b'], 'reiksme':[1,2,3,4,]})
# sns.countplot(data=df, x='category')
# sns.countplot(data=df, y='reiksme')
# plt.show()

# juostine
# df = pd.DataFrame({'category':['a', 'b', 'a', 'b'], 'reiksme':[1,2,3,4,]})
# sns.boxplot(data=df, x='category', y = 'reiksme')
# plt.show()

# daugialype diagrama
# df = pd.DataFrame({'category':[2,4,6,8], 'reiksme':[1,2,3,4,]})
# sns.pairplot(df)
# plt.show()

# regresijos diagrama
# df = pd.DataFrame({'category':[2,4,6,8], 'reiksme':[1,2,3,4,]})
# sns.lmplot(data=df, x='category', y='reiksme')
# plt.show()

# silumine diagrama
# df2 = np.random.rand(5,5)
# sns.heatmap(df2)
# plt.show()

# silumine diagrama (yra 'tips, 'diamond', 'car_crashes')
# df2 = np.random.rand(5,5)
# data=sns.load_dataset('tips')
# sns.histplot(data=data, x='total_bill',kde=True)
# data=data.columns
# print(data)
# plt.show()

# sekantis pavyzdys su car crashe

# data2=sns.load_dataset('car_crashes')
# spederiai=data2['total'].mean()
# print(spederiai)
#
# plt.figure(figsize=(8,6))
# sns.boxenplot(data2, x='total')
# plt.show()

# sekantis su dataset 'exercise'

# data3=sns.load_dataset('exercise')
# print(data3.head())
# # pagal dieta
# sns.pairplot(data=data3,hue='diet')
# plt.show()

# linijini plot piesiam
# data4=sns.load_dataset('flights')
# sns.lineplot(data=data4, x='year', y='passengers', hue='month')
# plt.show()

# 2023-09-26 pamokos uzduotys:
# [!] Naudojant "tips" duomenų rinkinį iš Seaborn, apskaičiuokite vidutinį sąskaitos sumos (total_bill) dydį
# ir vidutinį gauto mėnesinio mokesčio (tip) dydį;

# data5=sns.load_dataset('tips')
# # print(data5)
# vid_saskaitos_suma=data5['total_bill'].mean()
# print(vid_saskaitos_suma)
# vid_tip_dydis = data5['tip'].mean()
# print(vid_tip_dydis)
# sns.lineplot(data=data5, x='total_bill', y='tip')
# plt.show()

# [!] Naudojant "diamonds" duomenų rinkinį iš Seaborn, suskaičiuokite
# ir atvaizduokite vidutinį kainos (price) dydį pagal kiekvieną pjovimo (cut) grupę;

# data6=sns.load_dataset('diamonds')
# # print(data6)
# vid_kaina = data6['price'].mean()
# print(vid_kaina)
# pjovimo_grupes=data6['cut']
# print(pjovimo_grupes)
# #
# sns.barplot(data=data6, x='cut', y = 'price')
# plt.title('Vidutinės kainos pagal deimantų grupę')
# plt.xlabel('Pjovimo grupė')
# plt.ylabel('Vidutinė kaina')
# plt.show()

# [!] Panaudokite "tips" duomenų rinkinį, grupuokite duomenis pagal dienos dalį (time),
# apskaičiuokite vidutinį sąskaitos sumos (total_bill) dydį kiekvienoje dienos dalyje
# ir sukurkite kreivės grafiką, kuri vaizduoja vidutines sąskaitos sumas pagal dienos dalį;

# data7=sns.load_dataset('tips')
# datatime = data7['time']
# print(datatime)
# vid_sask_suma=data7['total_bill'].mean()
# print(vid_sask_suma)
#
# sns.lmplot(data=data7, x='time', y='total_bill')
# plt.title('Vidutinė sąskaitos suma pagal dienos dalį')
# plt.xlabel('Laiko grupė')
# plt.ylabel('Vidutinė suma')
# plt.show()


# [!] Įkelkite "titanic" duomenų rinkinį iš Seaborn. Grupuokite duomenis pagal lytį (sex) ir klasę (class),
# tada suskaičiuokite kiekvienos grupės išgyvenusiųjų skaičių.
# Tada sukurkite stulpelinę diagramą, kuri vaizduoja išgyvenusiųjų skaičių pagal lytį ir klasę;
# duomenys = sns.load_dataset("titanic")

# Grupuojame duomenis pagal lytį ir klasę ir suskaičiuojame išgyvenusiųjų skaičių
# duomenys=sns.load_dataset('titanic')
# grupuoti_duomenys = duomenys.groupby(["sex", "class"])["survived"].sum().reset_index()
#
# # Sukuriame stulpelinę diagramą
# plt.figure(figsize=(10, 6))
# sns.barplot(data=grupuoti_duomenys, x="class", y="survived", hue="sex")
# plt.title("Išgyvenusiųjų skaičius pagal lytį ir klasę")
# plt.xlabel("Klasė")
# plt.ylabel("Išgyvenusiųjų skaičius")
# plt.show()

# data_1 = sns.load_dataset('diamonds')
# print(data_1)
# df = pd.DataFrame(data_1)
# vidutinis_pagal_cut = df.groupby('cut')['price'].mean()
# print(vidutinis_pagal_cut)
# plt.figure(figsize=(12,5))
# sns.barplot(x=vidutinis_pagal_cut.values, y=vidutinis_pagal_cut.index
#             )
# plt.title('Vidutins kainos dydis pagal pjovimo grupe')
# plt.xlabel('Diamonds cut')
# plt.ylabel('Vidutine kaina')
# plt.show()

# 2023-09-27 pamoka: PANASIAI KAIP BAIGIAMASIS DARBAS

# url = 'https://vaga.lt/grozine-literatura'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
# # print(soup)
#
# conteineris = soup.find_all('div', class_='product-item-container')
# # print(conteineris)
#
# knygu_sarasas = []
#
# for knygos in conteineris:
#     pavadinimas = knygos.find('p', class_='name').text.strip()
#     kaina=float(knygos.find('div', class_='price price-align-wrapper'). text.strip('€').replace(',', '.'))
#     autorius = knygos.find('p', class_='Autorius').text.strip()
#     knygu_sarasas.append((pavadinimas, kaina, autorius))
#
# df=pd.DataFrame(knygu_sarasas, columns=['Pavadinimas', 'Kaina', 'Autorius'])
# # print(df)
#
# max = np.max(df['Kaina'])
# min = np.min(df['Kaina'])
# vidurkis = np.mean(df['Kaina'])
# mediana = np.median(df['Kaina'])
# print(f' Kainų Statistika: \n Max kaina: {max},\n Minimumas: {min}, \n Vidurkis: {vidurkis}, \n Mediana:{mediana}')
#
# sns.set(style='darkgrid')
# sns.histplot(data=df, x='Kaina', kde=True)
# plt.ylabel('Knygu skaicius')
# plt.show()

# Savarankiska uzduotis:
# filmu_sarasas = []
# #
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
# }
# for i in range(1,4):
#     url = f'https://www.metacritic.com/browse/movie/?releaseYearMin=1910&releaseYearMax=2023&page={i}'
#     page = requests.get(url, headers=headers)
#     # print(page.status_code)
#
#     soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup)
#
#     filmu_konteineris = soup.find_all('div', class_='c-finderProductCard')
# # print(filmu_konteineris)
#
#     for filmai in filmu_konteineris:
#         pavadinimas = filmai.find('div', class_='c-finderProductCard_title').text.strip().replace('(re-release)', ' ')
#         metascore = filmai.find('div', class_='c-siteReviewScore_background c-finderProductCard_metascoreValue u-flexbox-alignCenter g-height-100 g-outer-spacing-right-xsmall c-siteReviewScore_background-critic_xsmall').text.strip()
#         filmu_sarasas.append((pavadinimas, metascore))
#
# df=pd.DataFrame(filmu_sarasas, columns=['Pavadinimas', 'Metascore'])
# print(df)
#
# df.to_csv('filmai_su_metascore.csv')
#
# sns.set(style='darkgrid')
# sns.histplot(data=df, x='Metascore', kde=True)
# plt.xlabel('Metascore rezultatas')
# plt.ylabel('Filmų skaičius pagal Metascore')
# plt.title('Filmų kiekis pagal Metascore įvertinimą')
# plt.show()

# 2023-09-28 pamoka:

import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
#
#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ButaiProducts",
#         user="postgres",
#         password="Dekingumas123*"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#                 CREATE TABLE IF NOT EXISTS butai (
#                 id SERIAL PRIMARY KEY,
#                 Adresas VARCHAR(255),
#                 Kambariu_sk INT,
#                 Plotas DECIMAL(10,2),
#                 Aukstas VARCHAR(255),
#                 Kaina INT,
#                 Kv_kaina DECIMAL(10,2)
#                 )
#                 """
#
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#
#     Butu_sarasas = []

#     for i in range(1, 6):
#         url = f'https://www.aruodas.lt/atviru-duru-dienos/puslapis/{i}/'
#         response = requests.get(url)
#         # print(response.content)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         blokas = soup.find_all('div', class_='list-row-v2 object-row opendoor advert')
#
#         for butas in blokas:
#             Adresas = soup.select_one('div.list-adress-v2 h3').text.strip()
#             Kambariu_sk = butas.find('div', class_='list-RoomNum-v2 list-detail-v2').text.strip()
#             Plotas = butas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
#             Aukstas = butas.find('div', class_='list-Floors-v2 list-detail-v2').text.strip()
#             Kaina = butas.find('span', class_='list-item-price-v2').text.strip('€').replace(' ', '')
#             Kv_kaina = butas.find('span', class_='price-pm-v2').text.strip().replace('€/m²', '').replace(' ',
#                                                                                                          '').replace(
#                 ',', '.')
#             if Kambariu_sk == '' or Plotas == '' or Kaina == '' or Kv_kaina == '':
#                 continue
#             Kambariu_sk = int(Kambariu_sk)
#             Plotas = float(Plotas)
#             Kaina = int(Kaina)
#             Kv_kaina = float(Kv_kaina)
#
#             Butu_sarasas.append((Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina))
#             # print(Butu_sarasas)
#     df = pd.DataFrame(Butu_sarasas, columns=['Adresas', 'Kambarius_sk', 'Plotas', 'Aukstas', 'Kaina', 'Kv_kaina'])
#     print(df)
#     df.to_csv('Butai.csv')
#
#     insert_query = "INSERT INTO butai (Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina) VALUES(%s, %s,%s,%s,%s,%s)"
#
#     cursor.executemany(insert_query, Butu_sarasas)
#     print(f'Products inserted into list succesfully!')
#     connection.commit()
#
#     cursor.close()
#     # connection.close()
#
#
# if __name__ == '__main__':
#     create_and_insert_product()


# 2023-09-29 pamoka:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1 uzduotis:

# iris = load_iris()
# data=pd.DataFrame(data=iris.data,columns=iris.feature_names)
# data=data.columns
# # print(data)
#
# # seed atlieka, kad random duomenys nesikeistu
# np.random.seed(0)
# X=np.random.randn(200,2)
# y=(X[:,0]+X[:,1]>0).astype(int)
# X_train, X_test = X[:150], X[150:]
# y_train, y_test = y[:150], y[150:]
#
# svm_classifier=SVC(kernel='linear', C = 1)
#
# svm_classifier.fit(X_train, y_train)
# y_pred = svm_classifier.predict(X_test)
# accuracy=accuracy_score(y_test,y_pred)
# print(f'accurancy {accuracy:.2f}')
# # .2f yra tas pats, kas round(2), t.y. du skaiciai po kablelio
#
# xx,yy=np.meshgrid(np.linspace(X[:,0].min() -1, X[:,0].max() +1,100 ),
#                               np.linspace(X[:,0].min() -1, X[:,0].max()+1,100 ))
# Z = svm_classifier.decision_function(np.c_[xx.ravel(),yy.ravel()])
# Z=Z.reshape(xx.shape)
#
# plt.contourf(xx,yy,Z, levels=[-1,0,1],alpha = 0.6, colors = ['red','blue'])
# plt.scatter(X[:,0], X[:,1],c=y, cmap=plt.cm.brg, edgecolors='k')
# plt.xlabel('feature1')
# plt.ylabel('feature2')
# plt.title('Sprendimų ribos vizualizacija')
# plt.show()

# 2 uzduotis:

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# X=np.random.rand(100,1)*10
# y=3*X+np.random.randn(100,1)
# X_train, X_test,y_train, y_test= train_test_split(X,y, test_size=0.2, random_state=42)
# regresor = LinearRegression()
# regresor.fit(X_train,y_train)
# forcast = regresor.predict(X_test)
# Vid_kv_nuokrypis=mean_squared_error(y_test, forcast)
# print(Vid_kv_nuokrypis)
# plt.scatter(X_test,y_test, color='blue', label='actual')
# plt.plot(X_test, forcast, color='red', label = 'predicted')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.title('Linijinė regresija(actual vs predicted)')
# plt.legend()
# plt.show()






















