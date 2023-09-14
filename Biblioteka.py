# 2023-09-14 Duomenu analitikos pagrindai

import pandas as pd
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

import matplotlib.pyplot as plt

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

data = {'Miestas': ['Alytus', 'Londonas', 'Punskas','Ryga'],
        'Populiacija': [70000,600000,15000, 500000]
        }

data1=pd.DataFrame(data)
# pagal_populiacija = data1[data1['Populiacija'] >200000]
# print(pagal_populiacija)
#
# min_miestas = data1[data1['Populiacija']==data1['Populiacija'].min()]
# print(min_miestas)
#
# data1.loc[data1['Miestas'] =='Alytus', 'Populiacija'] += 21
# print(data1)


# Duomenų grupavimas ir agregavimas:
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma,
# kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.

data1['Salis'] = ['Lietuva', 'Anglija', 'Lenkija', 'Latvija']
print('Atnaujintas sarasas su salimis: ')
print(data1)

bendra_populiacija_saliai = data1.groupby('Salis')['Populiacija'].mean()
print(bendra_populiacija_saliai)

miestai_pagal_populiacija = data1.sort_values('Populiacija', ascending=False)
print(miestai_pagal_populiacija)