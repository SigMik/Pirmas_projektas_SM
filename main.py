# temperaturos = [20, 25, 22, 18, 12]
#
# suma = sum(temperaturos)
#
# kiekis = len(temperaturos)
#
# vidutine_temp = suma / kiekis
#
# print("Vidutine temperatura yra: ", vidutine_temp)


# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Jonas',
#     'Amzius': 34,
#     'Miestas': 'Klaipėda'}
# print('Prieš:')
# print('Vardas: ', lietuvos_pilietis['Vardas'])
# print ('Po:')
# lietuvos_pilietis['Vardas']  = 'Giedrius'
# print ('Vardas: ',lietuvos_pilietis['Vardas'])
# print ('Amzius: ',lietuvos_pilietis['Amzius'])
# print ('Gyvenamoji vieta: ',lietuvos_pilietis['Miestas'])
# lietuvos_pilietis['Miestas'] = 'Alytus'
# print ('Gyvenamoji vieta: ', lietuvos_pilietis['Miestas'])

# Uzduotis = {
#     'vardas': 'Sigita'}
#
# print('Sveikinu su kursų pradžia,', Uzduotis['vardas'])
# Uzduotis['vardas'] = 'Jonas'
# print ('Sveikinu su kursų pabaiga,', Uzduotis['vardas'])

# 2. Sukurkite kintamuosius skaicius1 ir skaicius2, ir priskirkite jiems du skaičius. Parašykite programą,
# kuri juos sudeda ir išspausdina sumą.
import random

# Uzduotis 2023-09-05 (1)

# for b in range(5, 0, -1):
#     print(b)

# Uzduotis 2023-09-05 (2)

# skaiciai = [100, 23, 135, 24]
# maziausias_skaicius = skaiciai[3]
# for skaicius in skaiciai:
#     if skaicius < maziausias_skaicius:
#         maziausias_skaicius = skaicius
# print("Maziausias skaicius yra: ", maziausias_skaicius)



# skaicius = int(input("Iveskite skaiciu: "))
# suma = 0
#
# for i in range(1, skaicius +1):
#     suma += i
# print("Skaiciu suma nuo 1 iki", skaicius, "yra", suma)

# Is saraso isfiltruoti lyginius skaicius

# sarasas = [2,5,11,25,9]
# lyginiai_skaiciai = []
#
# for skaicius in sarasas :
#     if skaicius %2 ==0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai ", lyginiai_skaiciai)

# Ispausdinti piramide su zvaigzdutemis

# eiluciu_sk = int(input("iveskite sveika skaiciu"))
# for eilute in  range(1,eiluciu_sk+1):
#     tarpas = eiluciu_sk - eilute
#     luna = 2 * eilute -1
#     print(" " * tarpas + "*" * luna )

# Surasti pirminius skaicius is intervalo tarp 10 ir 50 pirminiai skaiciai

# pradzia = 10
# pabaiga = 50
#
# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range(pradzia, pabaiga +1):
#     if skaicius > 1:
#         for daliklis in range(2,skaicius):
#             if (skaicius % daliklis) ==0:
#                 break
#         else:
#             print(skaicius)

# Patikrinti zodzius is saraso. Rasti ir palikti tuos zodzius, kurie prasideda raide a.

# zodziai_is_a = ["as", "tu", "jis", "ji", "asta", "marius"]
# raide = "a"
# for zodis in zodziai_is_a:
#     if zodis[0].lower()==raide.lower():
#         print(zodis)

# 5. Sudaryti ir isvesti daugybos lentele.

# print("daugybos lentele nuo 1 iki 10")
# for i in range(1,11):
#     for j in range (1,11):
#         rezultatas = i*j
#         print (f"{i} * {j} = {rezultatas}")
#     print()

# 6. Parasyti ir patikrinti, ar skaicius, kuri ivede vartotojas yra teigiamas, neigiamas, nulis. Ir ismesti koks

# skaicius = int(input("iveskite skaiciu_> "))
# if skaicius >0:
#     print("ivestas skaicius teigiamas")
# elif skaicius <0:
#     print("ivestas skaicius neigiamas")
# else:
#     print("ivestas skaicius = 0")

# 7. Sukurti programa, kuri isveda fizz skaiciams, kurie dalinasi is 3, buzz skaiciams, kurie dalinasi is 5, fizzbuzz
# skaiciai, kurie dalinasi ir is 10 ir is 3. Iki 100.

# for skaicius in range(1,101):
#     if skaicius %3 ==0 and skaicius %5 ==0:
#         print("fizzbuzz")
#     elif skaicius %3 ==0:
#         print("fizz")
#     elif skaicius %5 ==0:
#         print("buzz")
#     else:
#         print(skaicius)

# 8. Sukurkite skaiciu atspejimo zaidima


# pasleptas_skaicius = random.randint(1,100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 5
# while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100: "))
#     bandymai += 1
#     if spejimas == pasleptas_skaicius:
#         print(f"Valio! Atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("Bandykite didesni skaiciu")
#     else:
#         print("Bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"Jus pasiekete maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}")

# Sukurti sarasa zodziu, ju ilgi ir isvesti zodzius, kurie ilgesni nei 6 raides

# zodziai = ["uosis", "pipiras", "kibiriukas", "telefonas", "kompiuteris","mama"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")

# from random import randint
#
# # skaicius = random.randint(1,100)
# # print(skaicius)
#
# atsitiktinis = randint(1, 5)
#
# spejimas = int(input('Spekite skaiciu nuo 1 iki 5: '))
#
# if spejimas == atsitiktinis:
#     print('Sveikiname, atspejote skaiciu')
# else:
#     print('Neatspejote')

# vardas = input('Iveskite savo varda: ')
#
# if vardas:
#     print('Labas ' + vardas + '!')
# else:
#     print('Nieko neivedete')

# pazymys = 9
# ivertinimas = 'Puikiai' if pazymys ==10 else 'Galima geriau'
# print(ivertinimas)

# pazymys = 10
# ivertinimas = 'Galima geriau!'
# if pazymys ==10:
#     print('Puikiai')
# else:
#     print(ivertinimas)


# taskai = 90
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(tipas)


# taskai = 110
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(taskai, tipas)
#
# taskai = 50
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(taskai, tipas)


# patikrinimas = True if 10*2 > 0 else False
# print(patikrinimas)


# marke = 'Citroen'
# modelis = 'Xsara'
# metai = 2002
# rida = 702000
#
# # print(f'{marke} {modelis} buvo pagaminta {metai} ir nuvaziavo {rida} km')
#
# sakinys = f"""
# {marke} {modelis}
# buvo pagaminta {metai}
# ir nuvaziavo {rida} km
# """
# print(sakinys)

# print(f'skaiciavimu atsakymas yra: {8*2+5}')

# vardas = input('Iveskite varda: ')
# print(vardas)

# skaicius = input('Iveskite skaiciu:  ')
#
# if skaicius.isdigit():
#     skaicius = int(skaicius)
#
# print('Ivestas skaicius: ', skaicius, type(skaicius))

# skaicius = int(input('Iveskite skaiciu: '))
# skaicius_1 = int(input('Iveskite antra skaiciu: '))
# print(f'{skaicius} + {skaicius_1} = {skaicius + skaicius_1}')

# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą,
# kur n yra vartotojo įvestas skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte,
# ar įvestas skaičius yra sveikasis;

# n = int(input('Iveskite skaiciu: '))
# if n <= 1:
#     print('Ivestas skaicius turi buti sveikasis, bandykite dar')
# else:
#     suma = 0
#     for skaicius in range(2,n + 1):
#         suma +=skaicius
#     print(f'suma nuo 1 iki {n} yra {suma}')

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10).
# Programa turi grąžinti mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai").
# Naudokite "if" sąlygos sakinį;

# pazymys = int(input("Iveskite pazymi nuo 1 iki 10: "))
# ivertinimas = 'Puikiai'
# ivertinimas_1 = 'Gerai'
# ivertinimas_2 = 'Vidutiniskai'
# ivertinimas_3 = 'Silpnai'
# ivertinimas_4 = 'Neuztektinai'
# if pazymys <= 3:
#     print(f'Jusu rezultatas {ivertinimas_4}')
# elif pazymys <=5:
#     print(f'Jusu rezultatas {ivertinimas_3}')
# elif pazymys <=7:
#     print(f'Jusu rezultatas {ivertinimas_2}')
# elif pazymys <=9:
#     print(f'Jusu rezultatas {ivertinimas_1}')
# elif pazymys ==10:
#     print(f'Jusu rezultatas {ivertinimas}')
# elif: pazymys >10:
#     print(f' Pazymys negali buti didenis nei 10')

# Kitas sprendimas 1 uzduoties
# # Vartotojas įveda pažymį
# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
# #
# # Vartotojas įveda pažymį

# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
#
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
#
# print(f"Mokinio vertinimas: {vertinimas}")

# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti, ar įvesti metai yra keliamieji
# (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą

# metai = int(input('Iveskite metus: '))
# if metai %4 == 0:
#     print('Jūsų įvesti metai yra keliamieji')
# else:
#     print('Jūsų įvesti metai yra ne keliamieji')

# 4. Turite žodyną, kuriame yra vardai ir amžius.
# Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras, kuriose amžius yra didesnis arba lygus 18.
# Rezultatus patalpinkite naujame žodyne
#
# asmenys ={
#      'Rasa': 46,
#      'Daiva': 30,
#      'Jurga': 15,
#      'Joana': 18,
#      'Antanas': 32,
#      'Jurgis': 14,
#      'Domas': 45,
#      'Linas': 37
#      }
# asmenys_naujas = {}
# for vardas, amzius in asmenys.items():
#     if amzius >= 18:
#         asmenys_naujas[vardas] = amzius
# print(asmenys_naujas)

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")

# 2023-09-07 pamokos darbai:
#
# 1. Sukurkite sąrašą temperatūros su temperatūromis.
# Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta" (jei temperatūra virš 20) arba "šalta"
# (jei temperatūra 20 ar mažiau)

# temperaturos = [10, -7, 25, 36]
#
# for temperatura in temperaturos:
#      if temperatura >20:
#           print('silta')
#      elif temperatura <20:
#           print('salta')

# 2. Turite žodyną su studentų vardais ir jų pažymiais. Parašykite "for" ciklą,
# kuris išveda kiekvieno studento vardą ir jo pažymį.

# studentai = {
#      'Jonas': 9,
#      'Migle': 6,
#      'Eugenijus': 10,
#      'Tomas' : 4
#  }
#
# studentas = {}
# for vardas, pazymys in studentai.items():
#     studentas [vardas] = pazymys
# print(f'Studentai ir ju pazymiai: {studentai}')

# asmenys_naujas = {}
# for vardas, amzius in asmenys.items():
#     if amzius >= 18:
#         asmenys_naujas[vardas] = amzius

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo. Ciklą nutraukite, kai vartotojas įveda 0.
# NEBAIGTA

# vardai = ['Jonas', 'Petras', 'Marius', 'Laura', 'Laura']
#
# pirmas_vardas = vardai.pop(2)
# print(pirmas_vardas)
# #
# vardai.insert(1,'Giedrius')
# print (vardai)
#
# vardai.append('Onute')
# print (vardai)

# vardai.sort (reverse=True)
# print(vardai)

# vardai.remove('Laura')
# print(vardai)

# vaisiai = ('obuolys', 'kriause', 'bananas', 'braske')

# touple virsuje reiksmes nekeiciamos

# vaisia1 = ['obuolys', 'kriause', 'bananas', 'braske']

# liste virsuje galima keisti reiksmes
#
# vaisiai = {
#     'obuolys',
#     'kriause'
#     'bananas'
#     'braske'
# }
#
# vaisiai2 = vaisiai[0]
# print(vaisiai2)
#
# # sitas leidzia grazinti is saraso 0 reiksme
#
# skaiciai = (3.14, 2.71)
#
# a,b = skaiciai
# print(a)
# print(b)

# vaisiai = ['obuolys', 'kriause', 'bananas', 'braske']
#
# for sarasas, vaisius in enumerate(vaisiai, start=0):
#     print(f"{sarasas}. {vaisius}")

# Zemiau sukuriame nauja faila su tekstu:

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")

# with open("failo_pav.txt", 'a', encoding='utf-8') as file:
#     content = file.write("\nPapildomas tekstas")
#     print (content)

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")

# Zemiau abu pavyzdziai nuskaito sukurta faila

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print (content)
#
# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())

# vaisiai = []
#
# with open("vaisiai.txt", 'w', encoding='utf-8') as file:
#     content = file.write('obuolys, \nkriause, \nbananas, \nbraske')

studentai = {
     'Jonas': 9,
     'Migle': 6,
     'Eugenijus': 10,
     'Tomas' : 4
 }

studentas = {}
for vardas, pazymys in studentai.items():
    studentas [vardas] = pazymys
print(f'Studentai ir ju pazymiai: {studentai}')