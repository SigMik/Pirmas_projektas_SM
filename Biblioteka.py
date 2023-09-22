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
# print(df.head(5))
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Mėnuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
# print(f'\n', df)
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
#
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








