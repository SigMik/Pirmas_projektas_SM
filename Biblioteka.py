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
import time()

def create_and_insert_product():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="VarleProducts",
        user="postgres",
        password="Dekingumas123*"
    )
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS varle_products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10,2),
        quantity INT)
    """
    # cursor.execute(create_table_query)
    # print('Table created successfully')


    url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    product_elements = soup.find_all('div', class_='GRID_ITEM')
    # print(product_elements)

    product_data = []

    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip()
        product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
        product_quantity = product_element.find('b').text.strip()[:1]

        # print(f'Adding products to the list: {product_name}')
        time.sleep(2)
        # product_data.append((product_name, product_price, product_quantity))
        # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES(%s, %s, %s)"
        # cursor.execute(insert_query, (product_name, product_price, product_quantity))
        # print(f'Products inserted into list succesfully!')
        connection.commit()

    # df=pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
    # print(df)

    select_query = "SELECT * FROM varle_products"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    df=pd.DataFrame(rows, columns = ['id', 'name', 'price', 'quantity'])
    print(df)

if __name__ =='__main__':
    create_and_insert_product()












